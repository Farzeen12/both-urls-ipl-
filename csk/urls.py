from csk.views import *
from django.urls import path

urlpatterns=[
    path('best_batsman/',best_batsman,name='best_batsman'),
    path('best_bowler/',best_bowler,name='best_bowler')
]