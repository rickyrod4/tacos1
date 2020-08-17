from django.shortcuts import render, redirect
from .models import User, Taco, Order
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def register(request):
    errors = User.objects.validations(request.POST)
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
            return redirect('/')
    User.objects.register(request.POST)
    user = User.objects.get(email = request.POST['email'])
    request.session['user_id'] = user.id
    return redirect('/dashboard')


def login(request):
    result = User.objects.authenticate(request.POST['email'], request.POST['password'])
    if result == False:
        messages.error(request, "Invalid email/password")
    else:
        user = User.objects.get(email = request.POST['email'])
        request.session['user_id'] = user.id
        return redirect('/dashboard')
    return redirect('/')
def logout(request):
    request.session.clear()
    return redirect('/')

def dashboard(request):
    context = {
        'user' : User.objects.get(id = request.session['user_id']),
        'tacos': Taco.objects.all()
    }
    return render(request, 'dashboard.html', context)


def myAccount(request):
    context = {
        'user' : User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'updateAccount.html', context)

def orderHistory(request):
    context = {
        'user' : User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'orderHistory.html', context)

def favorites(request):
    context = {
        'user' : User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'favorites.html', context)

def checkout(request):
    context = {
        'user' : User.objects.get(id = request.session['user_id']),
    }
    return render(request, 'checkout.html', context)

def updateInfo (request):
    errors = User.objects.update(request.POST, request.session['user_id'])
    if errors:
        for field, value in errors.items():
            messages.error(request, value)
            return redirect('/myAccount')
    return redirect('/myAccount') 

def taco(request):
    user = User.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        this_taco = Taco.objects.filter(id=request.POST['id'])

        if not this_taco:
            return redirect('/dashboard')
        else:
            quantity = request.POST['quantity']
            total_cost = quantity*this_taco[0].price
            Order.objects.create(quantity_ordered = quantity, total_price =total_cost,ordered_by = user)
            return redirect('/checkout')
    else: 
        return redirect('/')