from django.shortcuts import render, redirect
from crud.forms import CollageForm
from form_example.models import Collage
from django.contrib.auth.decorators import login_required

def create(request):

    form = CollageForm()
    if request.method  == 'POST':

        form = CollageForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect(index)

    return  render(request, 'crud/create.html', {'form':form})

@login_required(login_url='/login')
def index(request):

    data = Collage.objects.raw('select * from collage')

    return render(request, 'crud/index.html', {'data':data})

def update(request):

    data = Collage.objects.get(id=request.GET['id'])
    form = CollageForm(instance=data)
    if request.method == 'POST':

        form = CollageForm(request.POST, instance=data)

        if form.is_valid():
            form.save()
            return redirect(index)

    return render(request, 'crud/update.html', {'form': form})


def delete(request):

    data = Collage.objects.get(id=request.GET['id'])
    data.delete()
    return redirect(index)

def view(request):
    data = Collage.objects.get(id=request.GET['id'])

    return render(request, 'crud/view.html', {'data':data})
