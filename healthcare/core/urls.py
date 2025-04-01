from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user, PatientViewSet, DoctorViewSet, PatientDoctorMappingViewSet

# Create a router for ViewSets
router = DefaultRouter()
# Register viewsets with the router
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'mappings', PatientDoctorMappingViewSet, basename='mapping')

# Define URL patterns
urlpatterns = [
    # Authentication endpoints
    path('auth/register/', register_user, name='register'),  # For registering new users
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # For login
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # For refreshing tokens
    
    # Include all the routes from the router
    path('', include(router.urls)),
]