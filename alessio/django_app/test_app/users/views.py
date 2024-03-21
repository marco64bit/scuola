from django.shortcuts import render
from . import models
from django.http import HttpResponse, JsonResponse


def get_users(request):
    user =  models.User.objects.all()[0]
    return JsonResponse({
        "username": user.username,
        "age": user.age
    })


def create_user(request):
    user = models.User(username="marco", age=30)
    user.save()
    return HttpResponse("ok")
