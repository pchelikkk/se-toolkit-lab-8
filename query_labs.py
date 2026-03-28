#!/usr/bin/env python3
import urllib.request
import json

req = urllib.request.Request(
    'http://127.0.0.1:42001/items?type=lab',
    headers={'Authorization': 'Bearer 2007'}
)
try:
    response = urllib.request.urlopen(req, timeout=5)
    data = json.loads(response.read())
    print("Labs found:")
    for item in data:
        if item.get('type') == 'lab':
            print(f"  - {item.get('id')}: {item.get('title')}")
except Exception as e:
    print(f"Error: {e}")
