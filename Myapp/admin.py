from django.contrib import admin
from .models import ImageGeneration 

@admin.register(ImageGeneration)
class ImageGenerationAdmin(admin.ModelAdmin):
    list_display = ('id', 'prompt', 'created_at') 
    # เพิ่มตัวกรอง (Filter)
    list_filter = ('created_at',)
    # เพิ่มช่องค้นหา
    search_fields = ('prompt',)