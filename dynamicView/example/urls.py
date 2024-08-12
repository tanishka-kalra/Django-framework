from django.urls import path
from . import views

urlpatterns=[
    path('<int:month>',views.int_month),
    path('<str:month>',views.str_month,name="string-month")
    
]