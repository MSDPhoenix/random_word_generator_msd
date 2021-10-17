from django.shortcuts import render
from django.utils.crypto import get_random_string
def index1(request):
    request.session['attempt_number']=0
    request.session['random_word']='Random word appears here.'
    return render(request,'index.html')

def index2(request):
    request.session['attempt_number']=request.session['attempt_number']+1
    request.session['random_word']=get_random_string(length=14)
    return render(request,'index.html')

