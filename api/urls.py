from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import register_user, home, patient_list_create, PatientDetailView
from .views import AppointmentListCreateView, AppointmentDetailView
from .views import DoctorListCreateView, DoctorDetailView




urlpatterns = [
    path('', home),  # Home page
    
    # Authentication endpoints
    path('auth/register/', register_user),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Patient endpoints
    path('patients/', patient_list_create, name='patients'),  # GET (list), POST (create)
    path('patients/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),  # GET, PUT, DELETE

    # Appointment endpoints
    path('appointments/', AppointmentListCreateView.as_view(), name='appointment-list-create'),
    path('appointments/<int:pk>/', AppointmentDetailView.as_view(), name='appointment-detail'),

    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorDetailView.as_view(), name='doctor-detail'),


]
