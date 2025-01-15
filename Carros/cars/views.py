from django.shortcuts import render
from cars.models import Car


# Create your views here.
def cars_view(request):

    search = request.GET.get('search')

    cars = Car.objects.all().order_by('model')
    # cars = Car.objects.filter(brand__name='Chevrolet')
    # cars = Car.objects.filter(model='Chevette Tubarão')
    # cars = Car.objects.filter(model__contains='Chevette')
    if search:
        cars = Car.objects.filter(model__icontains=search).order_by('model')

    return render(
        request, 
        'cars.html', 
        {'cars': cars }
    )
