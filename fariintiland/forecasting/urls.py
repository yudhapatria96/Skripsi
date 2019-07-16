from django.urls import path, include
from .views import index, resultForecasting, resultForecastingTahun, indexitem, resultForecastingItem, resultForecastingTahunItem

app_name = "forecasting"

urlpatterns = [
    path('', index , name='index'),
    path('indextahun', indexitem , name='indextahun'),

    # path('api/data/', ListForecasting.as_view()),
    path('resultforecasting', resultForecasting, name ='resultforecasting' ),
    path('resultForecastingItem', resultForecastingItem, name ='resultForecastingItem' ),
    path('resultforecastingtahun', resultForecastingTahun, name ='resultforecastingtahun' ),
    path('resultforecastingtahunitem', resultForecastingTahunItem, name ='resultforecastingtahunitem' ),


]