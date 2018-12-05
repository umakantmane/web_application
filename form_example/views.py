from django.shortcuts import render
from form_example.forms import UserForm

def userForm(request):

    formObj = UserForm()
    if request.method == 'POST':
        formObj = UserForm(request.POST)

        if formObj.is_valid():
            pass
    return  render(request, 'user_form.html', {'form':formObj})


def staticExample(request):

    return render(request, 'static_examples.html')