from django.shortcuts import render, redirect
from .models import add_new_menu, menuorder
import easygui


# THE MODULE IS FOR ADMINISTRATORS ONLY.
# Create your views here.
# ADD NEW MENU ADMINISTRATOR PRIVILEGE
def index(request):
    if request.method == "POST":
        if request.POST.get('Pizzaname'):
            form = add_new_menu()
            form.Pizzaname = request.POST.get('Pizzaname')
            form.save()
            easygui.msgbox("Added new menu!")
            return redirect('/')
    else:
        return render(request, 'index.html')


# DISPLAY MENU ADMINISTRATOR AND USER PRIVILEGE
def menu(request):
    menu_item = add_new_menu.objects.all()
    if request.method == "POST":
        if request.POST.get('Pizzaorder') and request.POST.get('Foodtype') and request.POST.get('Foodsize') \
                and request.POST.get('Toppings'):
            order = menuorder()
            order.Pizzaorder = request.POST.get('Pizzaorder')
            order.Foodtype = request.POST.get('Foodtype')
            order.Foodsize = request.POST.get('Foodsize')
            order.Toppings = request.POST.getlist('Toppings')
            order.save()
            easygui.msgbox("ORDER PLACED")
            return redirect('/')
    else:
        return render(request, 'menu.html', {'menu_item': menu_item})


# DISPLAY ORDER LIST ADMINISTRATOR PRIVILEGE
def admin(request):
    order2 = menuorder.objects.all()
    return render(request, 'admin.html', {'order2': order2})


# DELETE ORDER ADMINISTRATOR PRIVILEGE
def deleteorder(request, id):
    deleteitem = menuorder.objects.get(id=id)
    deleteitem.delete()
    return redirect('/adminpage')


# LANDING PAGE
def landing(request):
    return render(request, 'landing.html')


# REGISTERING ADMIN
