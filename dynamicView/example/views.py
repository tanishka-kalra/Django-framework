from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
#Dict containing all the months
months_dict={
    "January":"This is a January Month",
    "February":"This is a Februray Month",
    "March":"This is a March Month",
    "April":"This is a April Month",
    "May":"This is a May Month",
    "June":"This is a June Month",
    "July":"This is a July Month",
    "August":"This is a August Month",
    "September":"This is a September Month",
    "October":"This is a October Month",
    "November":"This is a November Month",
    "December":"This is a December Month"
}
def int_month(request,month):
    months=list(months_dict.keys())
    print(months)
    redirect_month=months[month-1]
    print(redirect_month)
    redirect_path=reverse("string-month",args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
    

def str_month(request,month):
    #for text other then months present in the months dict
    try:
        text=months_dict[month]
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("This is not a Month")

