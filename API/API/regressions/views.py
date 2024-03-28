from django.shortcuts import render
from django.contrib.auth.decorators import login_required
@login_required(login_url="http://localhost:8000/login")
def main_page(request):
    return render(request, "reg.html")
