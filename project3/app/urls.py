from django.urls import path, include
from . import views

#TEMPLATE TAGINGS
app_name = 'app'

urlpatterns = [
    path('other/', views.other, name='other'),
    path('relative/', views.rel, name='relative')
]


