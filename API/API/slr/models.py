import os
from django.db import models
from django.utils import timezone
def user_directory_path(instance, filename):
    base_dir = 'csv_files'
    username = instance.user.username
    user_dir = os.path.join(base_dir, username)
    return os.path.join(user_dir, filename)

class CSVFile(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, default=None)
    file = models.FileField(upload_to=user_directory_path)

    def __str__(self):
        return self.file.name.split("/")[-2]+"/"+self.file.name.split("/")[-1]