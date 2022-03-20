from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def hello_world(requests):
    return HttpResponse('반갑습니다.')
