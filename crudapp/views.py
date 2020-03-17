from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def index(request):
    data = CrudData.objects.all()
    form = CrudForm()
    if request.method == 'POST':
        form = CrudForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'data' : data, 'form' : form }
    return render(request, 'list.html', context)


# this usrl is for delete
def delete(request):
    return render(request, 'delete.html')

# this url is for update
def update(request, pk):
    data = CrudData.objects.get(id = pk)
    form = CrudForm(instance = data)
    if request.method == 'POST':
        form = CrudForm(request.POST, instance= data)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {'form' : form}
    return render(request, 'update.html', context)