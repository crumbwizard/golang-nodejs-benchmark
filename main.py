import subprocess
import time
import json

def go():
  start = time.time()
  subprocess.run(['go', 'run', 'scripts/golang.go'])
  elapse = time.time() - start
  
  return round(elapse * 1000)

def js():
  start = time.time()
  subprocess.run(['node', 'scripts/node.js'])
  elapse = time.time() - start

  return round(elapse * 1000)

data = {
  "go": [],
  "js": []
}

for i in range(50):
  data['js'].append(js())

for i in range(50): 
  data['go'].append(go())

print(data)

with open('performance.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)