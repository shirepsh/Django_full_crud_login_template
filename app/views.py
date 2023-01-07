from django.shortcuts import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .models import *

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
 
        # Add custom claims
        token['username'] = user.username

        return token
 
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(["GET","POST","DELETE","PUT"])
@permission_classes([IsAuthenticated])
def teacher(request,_id=-1):
    # give all or one teacher
    if request.method == "GET":
        if _id == -1:
            serializer = TeacherSerializer(Teacher.objects.all(), many=True)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            try:
                teacher = Teacher.objects.get(id=_id)
                serializer = TeacherSerializer(Teacher.objects.get(id=_id))
            except:
                 return Response(status=status.HTTP_400_BAD_REQUEST, data="teacher nor found")
            return Response(status=status.HTTP_200_OK, data=serializer.data)

    # create a teacher
    elif request.method == "POST":
        # create varabile with the serialixation type , if it valid we save it to the DB 
        new_teacher = TeacherSerializer(data=request.data)
        if new_teacher.is_valid():
            new_teacher.save()
        return Response (status=status.HTTP_201_CREATED, data=new_teacher.data)

    # delete by id
    elif request.method == "DELETE":
        id_2_del = _id
        try:
            teacher = Teacher.objects.get(id=id_2_del)
            teacher.delete()
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="teacher nor found")
        return Response(status=status.HTTP_200_OK, data="teacher delete")

    # update by id
    elif request.method == "PUT":
        id_2_upd = _id
        try:
            ser = TeacherSerializer(data=request.data)
            old_teacher = Teacher.objects.get(id=id_2_upd)
            res = ser.update(old_teacher, request.data)
            return HttpResponse(res, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST, data="teacher nor found")
            


    