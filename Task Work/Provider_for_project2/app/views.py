from django.shortcuts import render
from rest_framework.views import APIView
from app.models import UserRegistration,UserRequests
from app.serializers import UserRegisterSerializer,UserRequestsSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

class UserRegister(APIView):
    def post(self,request):
        bytes_data=request.body
        stream_data=io.BytesIO(bytes_data)
        python_dict=JSONParser().parse(stream_data)
        try:
            UserRegistration.objects.get(email=python_dict['email'])
        except:
            es=UserRegisterSerializer(data=python_dict,partial=True)
            if es.is_valid():
                es.save()
                msg={"msg":"data saved"}
                return Response(msg)
            else:
                msg={"msg":es.errors}
                return Response(msg)
        else:
            msg = {"msg": "Email Already Used"}
            return Response(msg)


class Login_check(APIView):
    def post(self,request):
        bytes_data=request.body
        stream_data=io.BytesIO(bytes_data)
        python_dict=JSONParser().parse(stream_data)
        try:
            udata=UserRegistration.objects.get(email=python_dict['email'],password=python_dict["password"])
        except:
            msg={"code":500}
        else:
            msg={"code":200,"udata":udata.email}
        return Response(msg)


class User_req_save(APIView):
    def post(self,request):
        bytes_data=request.body
        stream_data=io.BytesIO(bytes_data)
        python_dict=JSONParser().parse(stream_data)
        python_dict["status"]="pending"
        python_dict["remarks"]="Not given till now"
        ur=UserRequestsSerializer(data=python_dict,partial=True)
        if ur.is_valid():
            ur.save()
            msg = {"msg": "data saved"}
            return Response(msg)
        else:
            msg = {"msg": ur.errors}
            return Response(msg)


class My_requests(APIView):
    def get(self,req,email):
        data=UserRequests.objects.filter(requested_user_name=str(email))
        ur=UserRequestsSerializer(data,many=True)
        return Response(ur.data)

class Forgot_save(APIView):
    def put(self,request):
        bytes_data=request.body
        streamed_data=io.BytesIO(bytes_data)
        python_dict=JSONParser().parse(streamed_data)
        qs=UserRegistration.objects.get(email=python_dict["email"])
        ur=UserRegisterSerializer(qs,data=python_dict,partial=True)
        if ur.is_valid():
            ur.save()
            msg={"msg":"updated"}
        else:
            msg={"msg":ur.errors}
        return Response(msg)
