from django.urls import path
from . import views

urlpatterns=[
    #path('',views.home,name='home'),
    path('',views.index_audio_video,name='list'),
    path('view/',views.show_file,name='view'),
    #path('viewdoc/',views.show_filed,name='view1')
]