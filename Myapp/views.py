import uuid
import json
import requests
import urllib.parse
import io
from PIL import Image
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.http import require_http_methods
from django.core.files.base import ContentFile
from .models import ImageGeneration
import os

def call_ai_api(prompt):
    try:
        encoded_prompt = urllib.parse.quote(prompt)
        # ใช้ Pollinations AI ที่ทำงานได้แน่นอนและฟรี
        API_URL = f"https://image.pollinations.ai/prompt/{encoded_prompt}?width=768&height=768&nologo=true"
        
        response = requests.get(API_URL, timeout=60) 
        if response.status_code == 200:
            return response.content, None
        else:
            return None, f"API Error: {response.status_code}"
    except Exception as e:
        return None, str(e)

def index(request):
    # ดึงข้อมูลการสร้างรูปภาพทั้งหมด เรียงจากใหม่ไปเก่า
    history = ImageGeneration.objects.all().order_by('-created_at')
    return render(request, 'Myapp/index.html', {'history': history})

@require_http_methods(["POST"])
def generate_image(request):
    try:
        data = json.loads(request.body)
        prompt = data.get('prompt', '')
        
        if not prompt:
            return JsonResponse({'error': 'No prompt provided'}, status=400)

        image_data, error_info = call_ai_api(prompt)
        
        if not image_data:
             return JsonResponse({'error': f'Failed to generate image: {error_info}'}, status=500)

        # --- IMAGE OPTIMIZATION LOGIC ---
        # 1. เปิดรูปภาพด้วย Pillow
        img = Image.open(io.BytesIO(image_data))
        
        # 2. แปลงเป็น WebP (Original)
        output_webp = io.BytesIO()
        img.save(output_webp, format='WEBP', quality=85)
        webp_data = output_webp.getvalue()
        
        # 3. สร้าง Thumbnail (ขนาดเล็ก)
        thumb_img = img.copy()
        thumb_img.thumbnail((300, 300)) # ปรับขนาดให้เล็กลงสำหรับแสดงใน Grid
        output_thumb = io.BytesIO()
        thumb_img.save(output_thumb, format='WEBP', quality=70)
        thumb_data = output_thumb.getvalue()
        # -------------------------------

        unique_id = uuid.uuid4().hex[:8]
        clean_prompt = "".join(x for x in prompt[:15] if x.isalnum() or x in "._- ")
        base_name = f"gen_{unique_id}_{clean_prompt.replace(' ', '_')}"

        instance = ImageGeneration(prompt=prompt)
        
        # เซฟรูปหลักเป็น .webp
        instance.image.save(f"{base_name}.webp", ContentFile(webp_data), save=False)
        # เซฟรูป Thumbnail
        instance.thumbnail.save(f"{base_name}_thumb.webp", ContentFile(thumb_data), save=False)
        
        instance.save() # บันทึกทั้งคู่

        return JsonResponse({
            'success': True,
            'image_url': instance.image.url,
            'thumbnail_url': instance.thumbnail.url if instance.thumbnail else instance.image.url,
            'prompt': instance.prompt,
            'image_id': instance.id
        })

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON format'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f"Internal Error: {str(e)}"}, status=500)

@require_http_methods(["POST"])
def delete_image(request):
    try:
        data = json.loads(request.body)
        image_id = data.get('id')
        instance = ImageGeneration.objects.get(id=image_id)
        # ✅ เก็บ ID ไว้ที่ตัวแปร Global เพื่อให้ปุ่มลบรูปใหญ่ทำงานได้
        if instance.image and os.path.isfile(instance.image.path):
            os.remove(instance.image.path)
        if instance.thumbnail and os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)
            
        instance.delete()
        return JsonResponse({'success': True})
    except Exception as e:
        return JsonResponse({'success': False, 'error': str(e)}, status=500)

# คลังคำศัพท์สำหรับการทำ Autocomplete (Prompt Engineering)
PROMPT_KEYWORDS = [
    "cinematic lighting", "hyper-realistic", "highly detailed", "4k resolution", "8k wallpaper",
    "masterpiece", "unreal engine 5", "cyberpunk style", "vaporwave aesthetic", "minimalist",
    "oil painting", "digital art", "pencil sketch", "anime style", "studio Ghibli",
    "dreamy atmosphere", "soft bokeh", "golden hour", "neon lights", "dark moody",
    "futuristic city", "fantasy landscape", "mythical creature", "steampunk", "galaxy space",
    "close-up portrait", "wide angle lens", "macro photography", "top-down view",
    "vibrant colors", "pastel palette", "black and white", "monochrome", "sepia",
    "intricate patterns", "surrealism", "pop art", "3d render", "isometric view"
]

def get_suggestions(request):
    query = request.GET.get('q', '').lower()
    if not query:
        return JsonResponse([], safe=False)
    
    # ค้นหาคำที่ขึ้นต้นด้วยหรือมีคำที่ผู้ใช้พิมพ์
    matches = [word for word in PROMPT_KEYWORDS if query in word.lower()]
    return JsonResponse(matches[:8], safe=False) # ส่งกลับไปสูงสุด 8 คำ
