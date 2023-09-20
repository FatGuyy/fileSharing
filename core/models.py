# import uuid
from django.db import models

def dynamic_upload_path(instance, filename):
    return f'uploads/{instance.uploader_name}/{filename}'

# Create your models here.
class FileUpload(models.Model):
    # id = models.UUIDField(primary_key=True, default= uuid.uuid4)
    file_name = models.TextField()
    uploader_name = models.TextField()
    file = models.FileField(upload_to=dynamic_upload_path)

    def __str__(self) -> str:
        return str(self.file_name)
