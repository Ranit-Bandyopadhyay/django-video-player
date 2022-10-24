from django import forms

class uploadFileForm_ad(forms.Form):
    file_audio_video=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    files_audio_video=forms.FileField(widget=forms.FileInput(attrs={'class':"form-control"}))

class uploadFileForm_doc(forms.Form):
    file_d=forms.CharField(widget=forms.TextInput(attrs={'class':"form-control"}))
    files_d=forms.FileField(widget=forms.FileInput(attrs={'class':"form-control"}))