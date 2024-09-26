from django.urls import path
from .views import LeadListView, lead_detail, lead_create, lead_update

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='home'),
    path('create/', lead_create, name='create'),
    path('<int:pk>/', lead_detail, name='detail'),
    path('<int:pk>/update/', lead_update, name='update')
]