from django.db import models
from datetime import datetime
# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=100)
    image=models.ImageField(upload_to="images/")
    description=models.TextField()
    author=models.CharField(max_length=100)
    created_at=models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title
    
