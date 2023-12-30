from django.db import models

# Create your models here.
class basic_info(models.Model):
        name = models.CharField(max_length=255, default="Patrick A. Noblet")
        endpoint_url = models.URLField(default="https://backend-ninja-tutorials.onrender.com/post")
        github_url = models.URLField(default="https://github.com/thenoblet/backend_ninja")