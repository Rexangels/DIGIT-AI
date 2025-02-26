from django.urls import path
from .views import AgentListCreateView, AgentDetailView

app_name = 'agents'

urlpatterns = [
    path('', AgentListCreateView.as_view(), name='list'),
    path('<int:pk>/', AgentDetailView.as_view(), name='detail'),
]
