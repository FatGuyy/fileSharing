from django import forms
from .models import FileUpload

class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = ['file_name', 'uploader_name', 'file']

# from django import forms

# class VideoUploadForm(forms.Form):
#     video_name = forms.CharField(max_length=100)
#     uploader_name = forms.CharField(max_length=100)
#     video_file = forms.FileField()
