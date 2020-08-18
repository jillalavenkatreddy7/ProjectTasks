from django.db import models
class UserRegistration(models.Model):
    idno=models.AutoField(primary_key=True)
    email=models.EmailField(unique=True)
    phone_number=models.IntegerField()
    password=models.CharField(max_length=100)
class UserRequests(models.Model):
    idno=models.AutoField(primary_key=True)
    requested_user_name=models.CharField(max_length=100)
    request_type=models.CharField(max_length=100)
    request_discription=models.TextField()
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    pincode=models.IntegerField()
    alternate_ph_number=models.IntegerField()
    status=models.CharField(max_length=100)
    remarks=models.TextField()