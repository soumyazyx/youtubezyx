from django.shortcuts import render, redirect


def home(request):
    return render(request, "frontend/home.html")
