from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .serializers import *
import datetime, jwt
from django.contrib.auth import authenticate
# Create your views here.


def index(request):
    return HttpResponse("<h1>Hello World</h1>")


class UserView():

    # Đăng nhập thông tin người dùng
    @api_view(['POST'])
    def login(request):
        username = request.data['username']
        password = request.data['password']

        user = User.objects.filter(username=username).first()

        if user is None:
            raise AuthenticationFailed("User not found!")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect password!")
        
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.now()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')
        response = Response()
        response.set_cookie(key='jwt', value=token, httponly=True)

        cursor = User.objects.raw("SELECT * FROM main_user u WHERE u.username = %s", [request.data["username"]])
        user = UserSerializer(cursor, many=True).data

        response.data = {
            'jwt': token,
            'user': user
        }

        return response
    
class UploadFileView():
    # Upload file mới
    @api_view(['POST'])
    def upload_file(request):
        serializer = UploadFileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
    # Hiển thị ra danh sách file theo id
    @api_view(['GET'])
    def list_file(request, pk):
        file = UploadFile.objects.raw("SELECT uf.*, u.username FROM main_uploadfile AS uf" + 
                                    " JOIN main_user AS u ON uf.user_id = u.id WHERE u.id = %s", [pk])

        data = UploadFileSerializer(file, many=True).data
        return Response(data)
    
    # Xóa file đã có 
    @api_view(['DELETE'])
    def delete_file(request, pk):
        try:
            file = UploadFile.objects.get(pk=pk)
            file.delete()

            return Response({"Message": "success"})

        except Exception as e:
            return Response({"Message": "Error", "Error": str(e)})