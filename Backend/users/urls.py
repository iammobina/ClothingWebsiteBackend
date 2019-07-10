from django.urls import path
from .views import *

urlpatterns = [
    path('createuser/', CreateUser.as_view()),
    path('uploaddesign/', UploadDesign.as_view()),
   # path('deletedesign/',DesignDetail.as_view()),

]