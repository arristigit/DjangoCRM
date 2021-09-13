from leads.views import *
from django.urls import path

app_name = 'leads'

urlpatterns = [
    path('', LeadListView.as_view(), name="lead-list"),  
    path('<int:pk>/', LeadDetailView.as_view(), name="lead-details"),  
    path('<int:pk>/update/', LeadUpdateView.as_view(), name="lead-update"),  
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name="lead-delete"),
    path('create/', LeadCreateView.as_view(), name="lead-create"),  
    # path('<int:pk>/update/', lead_update, name="lead-update"),  
    # path('<int:pk>/delete/', lead_delete, name="lead-delete"),  
    # path('', lead_list, name="lead-list"),  
    # path('<int:pk>/', lead_details, name="lead-details"),  
    # path('create/', create_lead, name="lead-create"),  
]
