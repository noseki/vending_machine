from django.shortcuts import render
from .models import Items

def get_post_value(request, key):
    try:
        value = request.POST.get(key)
        return int(value)
    except:
        return 0

def index_view(request):
    return render(request, 'index.html')

def top_view(request):
    deposit = 0

    context = {
        "deposit":deposit
            }
    return render(request, 'machine.html', context)

def charge(request):

    old_deposit = get_post_value(request, 'deposit')
    charge_value = get_post_value(request, 'charge')

    new_deposit = old_deposit + charge_value

    item_list = Items.objects.filter(cost__lt=new_deposit)

    context = {
        "deposit":new_deposit,
        "item_list":item_list,
    }
    return render(request, 'machine.html', context)

def purchase(request):

    old_deposit = get_post_value(request, 'deposit')
    charge_value = get_post_value(request, 'charge')

    new_deposit = old_deposit + charge_value

    flagrant_deposit = new_deposit - Items.cost
    item_list = Items.objects.filter(cost__lt=new_deposit)

    context = {
        "deposit":flagrant_deposit,
        "item_list":item_list,
    }


    return render(request, 'machine.html')

def change(request):

    change = 0

    context = {
        "deposit":change,
    }

    return render(request, 'machine.html', context)


