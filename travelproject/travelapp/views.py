from django.shortcuts import render
from .models import place
from .models import Destination

# from .models import explore


# Create your views here.

def home(request):
    obj = place.objects.all()
    obj_2 = Destination.objects.all()
    context = {
        'place': obj,
        'Dest':obj_2,
    }
    return render(request, 'index.html', context)




    


