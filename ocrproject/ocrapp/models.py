from django.db import models
from datetime import datetime
from django.utils.timezone import now

class UploadImage(models.Model):
    image = models.ImageField(upload_to='media/images/')
    uploaded_at = models.DateTimeField(default=datetime.now, editable=False)
