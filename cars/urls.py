from django.urls import path
from cars.views import CarsIndex, CarDetails, CreateCarView, DeleteCarView, EditCarView

urlpatterns=[
    path('index', CarsIndex),
    path('<int:pk>', CarDetails.as_view(), name='cars.show'),
    path('create', CreateCarView.as_view()),
    path('edit/<int:pk>', EditCarView.as_view(), name='cars.edit'),
    path('delete/<int:pk>', DeleteCarView.as_view(), name='cars.delete')

]