from django.db import models


class Posts(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
