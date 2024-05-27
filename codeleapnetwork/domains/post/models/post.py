from django.db import models


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, null=False, blank=False)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created_date_time']