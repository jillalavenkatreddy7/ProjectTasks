from django.core.validators import RegexValidator
from rest_framework import serializers
from app.models import UserRegistration,UserRequests
import re

def check_email(email):
    if str(email).endswith("@gmail.com") or str(email).endswith("@yahoo.com"):
        return email
    else:
        raise serializers.ValidationError("email should ended with @gmail.com or @yahoo.com")

def check_phone_number(phone_number):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    m=Pattern.match(str(phone_number))
    if m!= None:
        return phone_number
    else:
        raise  serializers.ValidationError("Phone number must be 10 digits and starts with 7 or 8 or 9")


def check_phone_number1(alternate_ph_number):
    Pattern = re.compile("(0/91)?[7-9][0-9]{9}")
    m=Pattern.match(str(alternate_ph_number))
    if m!= None:
        return alternate_ph_number
    else:
        raise  serializers.ValidationError("Phone number must be 10 digits and starts with 7 or 8 or 9")

class UserRegisterSerializer(serializers.Serializer):
    idno=serializers.IntegerField()
    email=serializers.EmailField(validators=[check_email],max_length=100)
    phone_number=serializers.IntegerField(validators=[check_phone_number])
    password=serializers.CharField(validators=[RegexValidator('^(?=.*[A-Za-z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]{8,}$',message="password should be combinations of numbers and charecters")])

    def create(self, validated_data):
        return UserRegistration.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get("email", instance.email)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.password = validated_data.get("password", instance.password)
        instance.save()
        return instance

class UserRequestsSerializer(serializers.ModelSerializer):
    alternate_ph_number = serializers.IntegerField(validators=[check_phone_number1])
    class Meta:
        model=UserRequests
        fields="__all__"