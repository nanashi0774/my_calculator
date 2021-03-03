from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

text = ""
flg = {"sum_flg":False,"sub_flg":False,"pro_flg":False,"div_flg":False}

def calc(request):
    global text, flg
    sum_flg = flg["sum_flg"]
    sub_flg = flg["sub_flg"]
    pro_flg = flg["pro_flg"]
    div_flg = flg["div_flg"]
    if request.method == 'POST':
        if '1' in request.POST:
            text += "1"
        elif '2' in request.POST:
            text += "2"
        elif '3' in request.POST:
            text += "3"
        elif '4' in request.POST:
            text += "4"
        elif '5' in request.POST:
            text += "5"
        elif '6' in request.POST:
            text += "6"
        elif '7' in request.POST:
            text += "7"
        elif '8' in request.POST:
            text += "8"
        elif '9' in request.POST:
            text += "9"
        elif '0' in request.POST:
            text += "0"
        elif 'AC' in request.POST:
            text = ""
            return render(request,'index.html')
        elif '+' in request.POST:
            text += "+"
        elif '-' in request.POST:
            text += "-"
        elif '*' in request.POST:
            text += "×"
        elif '÷' in request.POST:
            text += "÷"
        elif '%' in request.POST:
            text += "%"
        elif '=' in request.POST:
            text = show_result(text)
        
    return render(request, 'index.html', {"text":text})

#一桁ずつの計算に対応 2021/03/04
def show_result(text):
    result = 0
    calc = text
    input1 = int(calc[0])
    input2 = int(calc[2])
    math_method = calc[1]
    if math_method == "+":
        return str(input1 + input2)
    elif math_method == "-":
        return str(input1 - input2)
    elif math_method == "×":
        return str(input1 * input2)
    elif math_method == "÷":
        return str(input1 // input2)