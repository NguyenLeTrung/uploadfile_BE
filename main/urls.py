from django.urls import path
from .views import *

urlpatterns = [
    path("", index),
    path("login", UserView.login),
    path("upload", UploadFileView.upload_file),
    path("delete-file/<pk>", UploadFileView.delete_file),
    path("list-file/<pk>", UploadFileView.list_file),
]