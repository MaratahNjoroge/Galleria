from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.home,name='home'),
    url('^gallery/$',views.gallery,name='gallery'),
    url(r'^image/(\d+)', views.image, name='image'),
    url('^gallery/$',views.gallery,name='gallery')
]
