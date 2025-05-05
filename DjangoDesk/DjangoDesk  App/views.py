from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .forms import ReservationForm

def hello_world(request):
    return HttpResponse("Hello world")

class HelloEthiopia(View):
    def get(self, request):
        return HttpResponse("Hello Ethiopia")
    
def home(request):
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Reservation saved successfully!")
    return render(request, 'index.html', {'form': form})