import json
import requests
import pprint
import http.client
import urllib.request


async def GET(url, *args, **kwargs):
    r = requests.get(url)
    return r


async def POST(url, data: str, *args, **kwargs):
    r = requests.post(url, data=data)
    # s = json.dumps(r.json()).strip('[]').replace('},', '}')
    response = urllib.request.Request(url, method='POST')
    parsed = json.loads(response)
    print(parsed)

    return r.content


async def PUT(url, data: dict, *args, **kwargs):
    r = requests.post(url, data=data)
    return r


async def DELETE():
    pass