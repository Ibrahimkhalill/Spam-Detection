import email
from email import message
from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import redirect, render
import joblib
# Create your views here.

def home(request):
    return render(request,'mainapp/home.html')

def getPredictions(text):

    model = joblib.load(open('spam_model.sav', 'rb'))
    vect = joblib.load(open('vectorizer.sav', 'rb'))
    p=vect.transform(text)
    result=model.predict(p)

    if result == 0:
        return 'yes'
    elif result == 1:
        return 'no'
    else:
        return 'error'

    
def result(request):
    text1 = request.GET['email']
    text=[text1]
    
    result = getPredictions(text)
    context={
        'result': result,
        'text1':text1

    }

    return render(request,'mainapp/result.html',context )