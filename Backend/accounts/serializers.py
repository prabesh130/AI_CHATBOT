from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name']

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)
    email=serializers.EmailField(required=True)


    class Meta:
        model=User
        fields=['username','email','password','password2']
    def validate(self,attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidateError({'passowrd': "passowrd field didn't match"})
        if User.objects.filter(email=attrs['email']).exist():
            raise serializers.ValidationError({'email':"Email already exist!"})
        return attrs
    

    def create(self,valdiate_data,validated_data:dict):
        valdiate_data.pop("password2")
        user=User.objects.create_user(
            username=validated_data['username'],
            emaild=validated_data['email'],
            password=validated_data['password']

        )
        return user 