from django.urls import path
from mainly.api.views import MainSearchAPIView

app_name = 'api_main'

urlpatterns = [
    path('objects/',MainSearchAPIView.as_view(),name='objects')

]