from django.shortcuts import render,redirect
from django.core.files.storage import FileSystemStorage
from .models import UploadImage
import pytesseract 
from PIL import Image
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
import os


def upload_image(request):
    if request.method == 'POST' and request.FILES['image']:
        uploaded_file = request.FILES['image']
        language=request.POST.get('language')
        if UploadImage.objects.filter(image=uploaded_file.name).exists():
            previous_image = UploadImage.objects.get(image=uploaded_file.name)
            file_path='D:/OCR/ocrproject/media/images/'+str(previous_image.image)
            if os.path.exists(file_path):
                os.remove(file_path)
                previous_image.delete()         
        fs = FileSystemStorage(location='media/images/')
        filename = fs.save(uploaded_file.name, uploaded_file)
        uploaded_image = UploadImage.objects.create(image=filename)
        upload_image = UploadImage.objects.last()
        image_path="D:/OCR/ocrproject/media/images/"+str(upload_image.image)
        extracted_text = pytesseract.image_to_string(Image.open(image_path),lang=language)
        return render(request, 'index.html',{'image_path': upload_image,'extracted_text': extracted_text})
    return render(request, 'index.html')
    