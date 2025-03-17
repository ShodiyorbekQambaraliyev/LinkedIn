from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='media/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __sts__(self):
        return f"Post {self.id}"
