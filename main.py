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

s = time.time()

for i in range(100):
  data['js'].append(js())

for i in range(100): 
  data['go'].append(go())

e = round(time.time() - s * 1000)

print(data)
print("total time:", e)

with open('out/performance.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)