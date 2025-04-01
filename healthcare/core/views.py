from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import UserSerializer, PatientSerializer, DoctorSerializer, PatientDoctorMappingSerializer
from rest_framework.decorators import api_view, permission_classes

# This function handles user registration
@api_view(['POST'])  # Only accept POST requests
def register_user(request):
    # Create a serializer with the data from the request
    serializer = UserSerializer(data=request.data)
    
    # Check if the data is valid
    if serializer.is_valid():
        # Save the user
        user = serializer.save()
        
        # Create JWT tokens for the new user
        refresh = RefreshToken.for_user(user)
        
        # Return the tokens and user data
        return Response({
            'refresh': str(refresh),  # Refresh token for getting new access tokens
            'access': str(refresh.access_token),  # Access token for authentication
            'user': serializer.data  # The user data (except password)
        }, status=status.HTTP_201_CREATED)
    
    # If data is invalid, return the errors
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ViewSet for Patient model - handles CRUD operations
class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer  # Use PatientSerializer
    permission_classes = [permissions.IsAuthenticated]  # User must be logged in
    
    def get_queryset(self):
        # Only show patients created by the current user
        return Patient.objects.filter(user=self.request.user)

# ViewSet for Doctor model - handles CRUD operations
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()  # Show all doctors
    serializer_class = DoctorSerializer  # Use DoctorSerializer
    permission_classes = [permissions.IsAuthenticated]  # User must be logged in

# ViewSet for PatientDoctorMapping model - handles CRUD operations
class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    serializer_class = PatientDoctorMappingSerializer  # Use PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]  # User must be logged in
    
    def get_queryset(self):
        # Get patient_id from the URL parameters (if provided)
        patient_id = self.request.query_params.get('patient_id')
        
        # If patient_id is provided, filter mappings by patient
        if patient_id:
            return PatientDoctorMapping.objects.filter(patient_id=patient_id)
        
        # Otherwise, return all mappings
        return PatientDoctorMapping.objects.all()