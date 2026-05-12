from django.db import models

class ImageGeneration(models.Model):
    prompt = models.TextField()
    image = models.ImageField(upload_to='generated_images/')
    thumbnail = models.ImageField(upload_to='generated_thumbnails/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prompt[:50]}..."
