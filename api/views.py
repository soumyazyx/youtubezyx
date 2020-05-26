from django.shortcuts import render, redirect
from django.http import JsonResponse
from apiclient.discovery import build


def apiOverview(request):
    api_key = "AIzaSyBfAUjIhI718gwmsKNdqmSrZ3EU9kwwdz4"
    youtube = build("youtube", "v3", developerKey=api_key)
    req = youtube.search().list(q="avengers", part="snippet", type="video")
    res = req.execute()
    print(res)
    return JsonResponse(res)
