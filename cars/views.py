from django.shortcuts import render
from cars.models import Car
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cars.forms import CarModelForm

# Create your views here.


def CarsIndex(request):  #To get all cars
    allc = Car.get_all_cars()
    return render(request, "cars/index.html", context={"cars":allc})


class CarDetails(DetailView):
    model = Car
    template_name = "cars/show.html"

class CreateCarView(CreateView):
    template_name = "cars/create.html"
    form_class = CarModelForm
    success_url = '/cars/index'

class EditCarView(UpdateView):
    model = Car
    template_name = "cars/edit.html"
    success_url = '/cars/index'
    form_class = CarModelForm

class DeleteCarView(DeleteView):
    model = Car
    template_name = "cars/delete.html"
    success_url = '/cars/index'
    # form_class = CarModelForm