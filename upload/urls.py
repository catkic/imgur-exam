from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^list$', views.list, name='list'),
    url(r'^test$', views.test, name='test'),
    url(r'^api', views.api, name='api'),

]
