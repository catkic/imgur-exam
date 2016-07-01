from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index', views.index, name='index'),
    url(r'^list$', views.list, name='list'),
    url(r'^test$', views.test, name='test'),
    url(r'^api', views.api, name='api'),

]
