from django.urls import path 
from . import views

urlpatterns = [

    path('notes/',views.note,name='notes'),
    path('addnote/',views.addnote,name='addnote'),
    path('updatenote/<int:id>/',views.updatenote,name='updatenote'),
    path('deletenote/<int:id>',views.deletenote,name='deletenote')

]



