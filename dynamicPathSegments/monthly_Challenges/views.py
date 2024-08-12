from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
# Create your views here.
def monthlyChallenges(request , month):
    text=None
    if month=="January":
        text = "This is a January Month"
    elif month=="Februray":
        text = "This is a Februray Month"
    elif month=="March":
        text = "This is a March Month"
    elif month=="April":
        text = "This is a April Month"
    elif month=="May":
        text = "This is a May Month"
    elif month=="June":
        text = "This is a June Month"
    elif month=="July":
        text = "This is a July Month"
    elif month=="August":
        text = "This is a August Month"
    else :
        return HttpResponseNotFound("This month is not Supported")
    return HttpResponse(text)
    