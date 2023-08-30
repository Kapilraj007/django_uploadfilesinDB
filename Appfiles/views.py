from django.shortcuts import render,redirect
from .forms import MyFileForm
from .models import MyFileUpload
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import os
# Create your views here.
@csrf_exempt
def home(request):
    mydata=MyFileUpload.objects.all()
    form=MyFileForm()
    if mydata!='':
         context={
        'form':form,
        'mydata':mydata
         }
         return render(request, "base.html",context)
    
    else:
        context={
            'form':form
        }
        return render(request, "base.html",context)

    
    
@csrf_exempt
def myuploadfile(request):
    if request.method=='POST':
        form=MyFileForm(request.POST,request.FILES)
        if form.is_valid():
            file_name=request.POST.get('file_name')
            file=request.FILES.get('file')
            # to check the file is already upload or not
            exists=MyFileUpload.objects.filter(file=file).exists()
            if exists:
                messages.error(request,"This file %s is already exists...!!!" %file)
            else:
                MyFileUpload.objects.create(file_name=file_name,file=file).save()

                messages.success(request, 'Files uploaded successfully.')
                
        return redirect('Home')
    
def deletefile(request,id):
    file=MyFileUpload.objects.get(id=id)
    file.delete()
    # to remove the file in local storage
    os.remove(file.file.path)
    messages.success(request,"File deleted successfully!!")
    return redirect('Home')