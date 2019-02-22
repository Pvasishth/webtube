from django.db import models

# Create your models here.
class Video(models.Model):

    emd_code = models.TextField()
    title = models.CharField(max_length=50, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title