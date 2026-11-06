#!/usr/bin/env python3
import requests
import sys

query = "claude-mem"
url = "https://api.github.com/search/repositories"
params = {'q': query}

try:
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()
    
    if 'items' in data:
        items = data['items']
        print(f"Found {len(items)} repositories.")
        for item in items[:5]:
            print(f"- {item['full_name']} (Stars: {item['stargazers_count']})")
    else:
        print(f"Error: 'items' key not found. Keys: {data.keys()}")
        
except Exception as e:
    print(f"Request failed: {e}")
    sys.exit(1)
