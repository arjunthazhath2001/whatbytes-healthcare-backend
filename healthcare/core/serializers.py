from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping

# Below serializer is for user registration

class UserSerializer(serializers.ModelSerializer):
    password= serializers.CharField(write_only=True)

    class Meta:
        model= User
        fields=('id', 'username', 'email', 'password','first_name','last_name')
    
    def create(self,validated_data):
        user= User.objects.create_user(
            username= validated_data['username'],
            password= validated_data['password'],
            email= validated_data.get('email',''),
            first_name= validated_data.get('first_name',''),
            last_name= validated_data.get('last_name',''),
        )
        return user

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields= '__all__'
        read_only_fields= ('user',) #Users can't create patients that belong to other users
    
    def create(self, validated_data):
        validated_data['user']= self.context['request'].user
        return super().create(validated_data)
    #Every patient is tied to the user who created it

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields= '__all__'

class PatientDoctorMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model= PatientDoctorMapping
        fields='__all__'