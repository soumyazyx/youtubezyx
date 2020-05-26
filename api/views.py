from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from apiclient.discovery import build


def apiOverview(request):
    urls = []
    api_key = "AIzaSyBfAUjIhI718gwmsKNdqmSrZ3EU9kwwdz4"
    youtube = build("youtube", "v3", developerKey=api_key)
    req = youtube.search().list(
        part="snippet",
        eventType="completed",
        maxResults=50,
        order="date",
        q="cartoon",
        type="video",
    )
    res = req.execute()
    for item in res["items"]:
        url = "https://www.youtube.com/watch?v={}".format(item["id"]["videoId"])
        title = item["snippet"]["title"]
        href = "<a href={}>{}</a>".format(url, title)
        embed = "<iframe width='420' height='345' src='{}'></iframe><br/><br/>".format(
            url
        )
        urls.append(href)
    str1 = "<br/><br/>".join(urls)
    # return JsonResponse(res)
    return HttpResponse(str1)
