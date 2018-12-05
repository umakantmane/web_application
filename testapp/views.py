from django.shortcuts import render


def helloDjango(request):

    d1 = {
        'name':'Manas',
        'email':'manas@gmail.com',
        'l1':[1,2,3,4,5,'xyz'],
        'd2':{'city':'Bangalore', 'address':'BTM'}
    }
    return render(request, 'hello.html', d1)


def helloPython(request):

    return render(request, 'hello_python.html')