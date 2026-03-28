#!/usr/bin/env python3
import urllib.request
import json

API_KEY = '2007'
BASE_URL = 'http://127.0.0.1:42001'

def get_scores(lab_id):
    req = urllib.request.Request(
        f'{BASE_URL}/analytics/scores?lab={lab_id}',
        headers={'Authorization': f'Bearer {API_KEY}'}
    )
    try:
        response = urllib.request.urlopen(req, timeout=5)
        data = json.loads(response.read())
        return data
    except Exception as e:
        return f"Error: {e}"

# Get all labs
req = urllib.request.Request(
    f'{BASE_URL}/items?type=lab',
    headers={'Authorization': f'Bearer {API_KEY}'}
)
response = urllib.request.urlopen(req, timeout=5)
labs = json.loads(response.read())

print("=== LMS Lab Scores ===\n")
for lab in labs:
    if lab.get('type') == 'lab':
        lab_id = lab.get('id')
        # Try both numeric ID and lab-XX format
        for query_id in [str(lab_id), f"lab-{lab_id:02d}"]:
            scores = get_scores(query_id)
            if not isinstance(scores, str) and scores:
                print(f"\n{lab.get('title')} (ID: {lab_id})")
                print("-" * 50)
                for bucket in scores:
                    print(f"  {bucket['bucket']}: {bucket['count']} students")
                break
