from django.urls import path, include
from .views import index, resultForecasting

app_name = "forecasting"

urlpatterns = [
    path('', index , name='index'),
    # path('api/data/', ListForecasting.as_view()),
    path('resultforecasting', resultForecasting, name ='resultforecasting' ),
]