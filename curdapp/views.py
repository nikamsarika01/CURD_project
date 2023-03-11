from django.shortcuts import render,redirect
from .forms import ProductForm
from .models import Product
# Create your views here.
def create(r):
    form = ProductForm()
    if r.method=='POST':
        form = ProductForm(r.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(r,'curdapp/emp.html',{'form':form})

def read(r):
    obj = Product.objects.all()
    return render(r,'curdapp/empdatafetch.html',{'obj':obj})

def delete(r,id):
    obj = Product.objects.get(id=id)
    obj.delete()
    return redirect('/')


def update(r,id):
    obj = Product.objects.get(id=id)
    if r.method=='POST':
        form = ProductForm(r.POST,instance=obj)

        if form.is_valid():
            form.save()
            return redirect('/')
    return render(r,'curdapp/update.html',{'obj':obj})


