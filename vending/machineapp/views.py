from django.shortcuts import render
from .models import Items

def index_view(request):
    return render(request, 'index.html')

def top_view(request):
    return render(request, 'machine.html')

def vending_machine(request):

    _deposit = 0

    if (request.POST.get('deposit') != ""):
        tmp = request.POST.get('deposit')
        _deposit = int(tmp)

    _items = Items.objects.all()

    context = {
        "deposit":_deposit,
        "items":_items,
    }

    return render(request, 'machine.html', context)

def charge(request):

    tmp1 = request.POST.get('deposit')
    _deposit = int(tmp1)

    if (request.POST.get('charge') != ""):
        tmp2 = request.POST.get('charge')
        _deposit += int(tmp2)

    _items = Items.objects.all()

    context = {
        "deposit":_deposit,
        "items":_items,
    }
    return render(request, 'machine.html')

def purchase(request):
    return render(request, 'machine.html')

def change(request):


    return render(request, 'machine.html')

