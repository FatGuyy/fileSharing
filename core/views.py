from .forms import VideoUploadForm
from django.shortcuts import render
# from django.contrib import messages
from django.views.decorators.csrf import csrf_protect


# Create your views here.
@csrf_protect
def upload(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # messages.info(request, 'Got the video!')
        else:
            pass
    else:
        form = VideoUploadForm()
    return render(request, 'index.html', {'form': form})
