from django.urls import path

from .views import SahifaPageView

urlpatterns =[
    path('', SahifaPageView.as_view(), name='sahifa')
]