from django.urls import path

from . import views

app_name = "input_data"

urlpatterns = [
    path('', views.index , name='index'),
    path('input/', views.create , name='input'),
    path('delete/<int:delete_id>', views.delete, name='delete'),
        path('update/<int:update_id>', views.update, name='update'),

]
