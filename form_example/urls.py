from django.conf.urls import url
from form_example import views

urlpatterns = [

    url(r'^user_form$', views.userForm),
    url(r'^static_example$', views.staticExample)
]


