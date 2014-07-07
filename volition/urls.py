from django.conf.urls import url

from volition import views

urlpatterns = [
    url(r'^$', views.index, name='index')
]
