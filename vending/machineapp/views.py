from django.shortcuts import render
from .models import Items

purchase_list = []

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

    item_list = Items.objects.filter(cost__lte=new_deposit)

    context = {
        "deposit":new_deposit,
        "item_list":item_list,
    }
    return render(request, 'machine.html', context)

def purchase(request):

    before_deposit = get_post_value(request, 'deposit')
    purchase_cost = get_post_value(request, 'cost')

    now_deposit = before_deposit - purchase_cost

    item_list = Items.objects.filter(cost__lte=now_deposit)

    purchase = Items.objects.filter(id=request.POST.get("id"))

    #purchase_list.append(purchase)

    context = {
        "deposit":now_deposit,
        "item_list":item_list,
        "purchase_list":purchase,
    }


    return render(request, 'machine.html', context)

def change(request):

    change = 0

    context = {
        "deposit":change,
    }

    return render(request, 'machine.html', context)


