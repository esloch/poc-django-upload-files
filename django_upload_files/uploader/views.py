from django.shortcuts import render, redirect 
from django.contrib.auth.decorators import login_required 
from django.contrib import messages
from .forms import FileUploadForm 
from .models import UPFile 
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    pass

@login_required 
def accounts_view(request): 
    # Your view logic goes here 
    # You can render a template or perform any other operations 
    return render(request, 'accounts.html') 

@login_required 
def upload_file(request): 
    if request.method == 'POST': 
        form = FileUploadForm(request.POST, request.FILES) 
        if form.is_valid(): 
            file = form.cleaned_data['file'] 
            # Save the file to the file system 
            up_file = UPFile(file=file, uploaded_by=request.user) 
            up_file.save() 
            # Process the file or perform any required operations 
            # ... 
            messages.success(request, 'File uploaded successfully.')
            return redirect('success') 
        else:
            messages.error(request, 'Error uploading file. Please try again.')
    else: 
        form = FileUploadForm() 
    return render(request, 'upload.html', {'form': form}) 

@login_required 
def upload_success(request): 
    return render(request, 'success.html')

def error_404_view(request, exception):
    return render(request,'uploader/templates/error_404.html')

