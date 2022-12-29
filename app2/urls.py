from django.urls import path
from app2.views import *
app_name='laddu'

urlpatterns=[
    path('second/',second,name='second'),
]