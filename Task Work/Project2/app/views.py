from django.shortcuts import render,HttpResponse
import requests
import json
def login(request):
    return render(request,"login.html")

def register_save(request):
    email=request.POST.get("email")
    num=request.POST.get("num")
    pword=request.POST.get("pword")
    python_dict={"email":email,"phone_number":num,"password":pword}
    json_data=json.dumps(python_dict)
    try:
        res=requests.post("http://127.0.0.1:8000/user_registration/",data=json_data)
        return render(request,"register.html",{"data":res.json()})
    except:
        return HttpResponse("du to internet connection or provider server problem we are unable to process")

def login_check(request):
    email=request.POST.get("email")
    pword=request.POST.get("pword")
    python_dict={"email":email,"password":pword}
    json_data=json.dumps(python_dict)
    try:
        res=requests.post("http://127.0.0.1:8000/login_check/",data=json_data)
        data=res.json()

    except:
        return HttpResponse("du to internet connection or provider server problem we are unable to process")
    else:
        if data["code"]==500:
            return render(request,"login.html",{"data1":"Invalid details"})
        if data["code"]==200:
            return render(request,"userhome.html",{"data":data["udata"]})

def req(request):
    email=request.GET.get("email")
    return render(request,"userreq.html",{"email":email})

def req_save(request):
    email=request.POST.get("rname")
    rtype=request.POST.getlist("rtype")
    rdis=request.POST.get("dis")
    city=request.POST.get("city")
    state=request.POST.get("state")
    pincode=request.POST.get("pincode")
    num=request.POST.get("num")
    str=''
    for x in rtype:
        str=str+","+x
    python_dict={ "requested_user_name":email,"request_type":str,"request_discription":rdis,"city":city,"state":state,"pincode":pincode,"alternate_ph_number":num}
    json_data = json.dumps(python_dict)
    try:
        res = requests.post("http://127.0.0.1:8000/user_req_save/", data=json_data)
        return render(request, "userreq.html", {"data": res.json()})
    except:
        return HttpResponse("du to internet connection or provider server problem we are unable to process")

def myreq(request):
    email=request.GET.get("email")
    try:
        res=requests.get("http://127.0.0.1:8000/my_requests/"+email+"/")
        return render(request,"my_req.html",{"data":res.json()})
    except:
        return HttpResponse("du to internet connection or provider server problem we are unable to process")

def forgot(request):
    return render(request,"forgot.html")

def forgot_save(request):
    email=request.POST.get("email")
    password=request.POST.get("pword")
    python_dict = {"email": email, "password":password}
    json_data = json.dumps(python_dict)
    try:
        res = requests.put("http://127.0.0.1:8000/forgot_save/", data=json_data)
        return render(request, "login.html", {"data": res.json()})
    except:
        return HttpResponse("du to internet connection or provider server problem we are unable to process")
