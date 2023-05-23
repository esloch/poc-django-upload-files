# models.py
from django.db import models
from django.contrib.auth.models import User

class UPFile(models.Model):
    file = models.FileField(upload_to='uploader/data_uploaded/')
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
