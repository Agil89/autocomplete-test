from django.urls import path
from mainly.views import MainClassView

app_name = 'main'

urlpatterns = [
    path('',MainClassView.as_view(),name='home'),
]
