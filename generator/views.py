from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def band_name_generator(request):
    band_name = None
    if request.method == "POST":
        city = request.POST.get("city")
        pet = request.POST.get("pet")
        band_name = f"{city}_{pet}"
    return render(request, "generator/band_name.html", {"band_name": band_name})
    
