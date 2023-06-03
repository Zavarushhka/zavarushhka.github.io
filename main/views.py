import requests
import hashlib
import re
import json

from django.shortcuts import render, redirect
from .models import Order
from django.http import JsonResponse

from .forms import OrderForm

def home(request):
    return render(request, 'index.html')

def send_info(name, phone):
    TOKEN = "5983154594:AAGIF21jGeNH7xe9Y0EQywJa-3O4Kk3PDr0"
    chat_id = "5983154594"
    message = f"Заявка с сайта!\nИмя заказчика: {name}\nТелефон для связи: {phone}"
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()

def get_order(request):
    name_error = ''
    email_error = ''
    phone_error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            error = False
            if len(name) > 20 or len(name) < 4 or re.match(r'^[A-ZА-ЯЁ]', ) is None:
                name_error = 'Имя должно начинаться с заглавной буквы и быть от 4 до 20 символом'
                error = True
            if len(email) > 50 or len(email) < 4 or re.match(
                    r'(?=.*[@.])[@.]{4,20}', email) is None:
                email_error = "Проверьте правильность введённой почты"
                error = True
            if len(phone) > 20 or len(phone) < 9 or re.match(
                    r'^[0-9+()- ]', phone) is None:
                phone_error = "Проверьте корректность введенного номера"
                error = True
            if not error:
                f = Order(
                    name = request.POST.get("name"),
                    email=hashlib.sha1(request.POST.get("email").encode('utf-8')).hexdigest(),
                    phone=hashlib.sha1(request.POST.get("phone").encode('utf-8')).hexdigest(),
                )
                f.save()
                send_info(name, phone)
                return redirect('home')
    form = OrderForm()
    data = {
        'form': form,
        'name_error': name_error,
        'email_error': email_error,
        'phone_error': phone_error,
    }
    return render(request, 'main/index.html', data)
