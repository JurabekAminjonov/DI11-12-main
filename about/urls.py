from django.urls import path
from .views import AboutPageView  # `AboutView` ni mos ravishda import qiling

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
]