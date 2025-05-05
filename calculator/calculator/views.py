from django.http import HttpResponse
from django.shortcuts import render

def calculator(request):
    result= None
    if request.method == 'POST':
        num1= float(request.POST.get('num1'))
        num2= float(request.POST.get('num2'))
        operation = request.POST.get('operation')
        
        if operation == '+':
            result= num1+num2
        elif operation == '-':
            result= num1- num2
        elif operation == '*':
            result= num1*num2
        elif operation == '/':
            if num2==0:
                result="Cannot divided by 0"
            else:
                result= num1/num2
        
    return render(request, 'calculator/cal.html', locals()) 

