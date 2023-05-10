from servers.views import IndexTemplateView
from django.urls import path, include

urlpatterns = [
    path('', IndexTemplateView.as_view(), name='index')
]