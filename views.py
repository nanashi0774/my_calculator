from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
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
            if check_percent(text):
                text += "1"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '2' in request.POST:
            if check_percent(text):
                text += "2"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '3' in request.POST:
            if check_percent(text):
                text += "3"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '4' in request.POST:
            if check_percent(text):
                text += "4"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '5' in request.POST:
            if check_percent(text):
                text += "5"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '6' in request.POST:
            if check_percent(text):
                text += "6"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '7' in request.POST:
            if check_percent(text):
                text += "7"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '8' in request.POST:
            if check_percent(text):
                text += "8"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '9' in request.POST:
            if check_percent(text):
                text += "9"
            else:
                messages.error(request, '%の後は記号を入力してください。')
        elif '0' in request.POST:
            if check_percent(text):
                text += "0"
            else:
                mmessages.error(request, '%の後は記号を入力してください。')
        elif 'AC' in request.POST:
            text = ""
            return render(request,'index.html')
        elif '+' in request.POST:
            if check_symbol(text):
                text += "+"
            else:
                messages.error(request, '記号を連続で入力できません。')
        elif '-' in request.POST:
            if check_symbol(text):
                text += "-"
            else:
                messages.error(request, '記号を連続で入力できません。')
        elif '*' in request.POST:
            if check_symbol(text):
                text += "×"
            else:
                messages.error(request, '記号を連続で入力できません。')
        elif '÷' in request.POST:
            if check_symbol(text):
                text += "÷"
            else:
                messages.error(request, '記号を連続で入力できません。')
        elif '%' in request.POST:
            if check_symbol(text) and check_percent(text):
                text += "%"
            else:
                messages.error(request, '記号を連続で入力できません。')
        elif '=' in request.POST:
            text = show_result2(text)
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
        return str(input1 / input2)

# 複数桁の計算に対応 2021/03/05
def show_result2(text):
    result = 0
    calc_list = []
    if text.find("+") != -1:
        calc_list = text.split("+")
        calc_list.append("+")
    elif text.find("-") != -1:
        calc_list = text.split("-")
        calc_list.append("-")
    elif text.find("×") != -1:
        calc_list = text.split("×")
        calc_list.append("×")
    elif text.find("÷") != -1:
        calc_list = text.split("÷")
        calc_list.append("÷")
    stack = []
    for i in range(len(calc_list)):
        if calc_list[i] == '+':
            stack.append(stack.pop() + stack.pop())
        elif calc_list[i] == '-':
            stack.append(-(stack.pop() - stack.pop()))
        elif calc_list[i] == '×':
            stack.append(stack.pop() * stack.pop())
        elif calc_list[i] == '÷':
            input1 = stack.pop()
            input2 = stack.pop()
            stack.append(input2 / input1)
        else:
            stack.append(int(calc_list[i]))
    result = stack[-1]
    return result

def check_symbol(text):
    symbol = text[-1]
    if symbol == "+" or symbol == "-" or symbol == "÷" or symbol == "×":
        return False
    else:
        return True

def check_percent(text):
    if text == "":
        return True
    symbol = text[-1]
    if symbol == "%":
        return False
    else:
        return True