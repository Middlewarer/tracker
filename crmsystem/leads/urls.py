from django.urls import path
from .views import LeadListView, lead_detail, lead_create, lead_update, lead_delete

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name='home'),
    path('create/', lead_create, name='create'),
    path('<int:pk>/', lead_detail, name='detail'),
    path('<int:pk>/update/', lead_update, name='update'),
    path('<int:pk>/delete/', lead_delete, name='delete'),
]