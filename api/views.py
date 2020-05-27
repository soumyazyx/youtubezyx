from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from apiclient.discovery import build


def apiOverview(request):
    return JsonResponse({"wow": "beep"})


def youtubesearch(request, search):
    urls = []
    api_key = "AIzaSyBfAUjIhI718gwmsKNdqmSrZ3EU9kwwdz4"
    youtube = build("youtube", "v3", developerKey=api_key)
    req = youtube.search().list(
        part="snippet",
        eventType="completed",
        maxResults=10,
        order="date",
        q=search,
        type="video",
    )
    res = req.execute()
    return JsonResponse(res)
