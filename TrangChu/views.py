from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def trangchu(request):
    return render(request, 'TrangChu.html')


def student(request):
    return render(request, 'SinhVien.html')


def teacher(request):
    return render(request, 'GiaoVien.html')


def login(request):
    return render(request, 'DangNhap.html')


def edit(request):
    return render(request, 'index4.html')