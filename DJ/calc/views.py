from fileinput import filename
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from .models import video_audio_file_upload,document_file_upload
from .forms import uploadFileForm_ad,uploadFileForm_doc

def home(request):
    return render(request,"home.html")

# Create your views here.
'------------------------------------------------------------------------------------------'

def index_audio_video(request):
    if(request.method=='POST'):
        c_form = uploadFileForm_ad(request.POST, request.FILES)
        c_formd = uploadFileForm_doc(request.POST, request.FILES)
        
        if(c_form.is_valid()):
            name = c_form.cleaned_data['file_audio_video']
            the_files = c_form.cleaned_data['files_audio_video']
            x=str(the_files).split('.')
            y=x[-1]
            if(y not in ["mp3","mp4","aiff","aac","dsd"]):
                return HttpResponse('Select proper video/audio files')
            video_audio_file_upload(file_name=name, my_file=the_files).save()           #from .models
            return HttpResponse("file upload")
        
        elif(c_formd.is_valid()):
                
            name_d = c_formd.cleaned_data['file_d']
            the_files_d = c_formd.cleaned_data['files_d']
            x1=str(the_files_d).split('.')
            y1=x1[-1]
            if(y1 not in ["pdf","doc"]):
                return HttpResponse('Select proper text files')
            document_file_upload(file_named=name_d, my_filed=the_files_d).save()           #from .models
            return HttpResponse("file upload")
        
        else:
            return HttpResponse('error')

    else:
        context = {'form':uploadFileForm_ad(request.POST, request.FILES or None),
               'form1': uploadFileForm_doc(request.POST, request.FILES or None)}  
        
        return render(request, 'home.html', context)
'----------------------------------------------------------------------------------------'

def show_file(request):
    # this for testing 
    all_data = video_audio_file_upload.objects.all()
    all_datad = document_file_upload.objects.all()

    context = {
        'data':all_data ,
        'datad':all_datad
        }

    return render(request, 'view.html', context)

'----------------------------------------------------------------------------------------'
