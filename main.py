import subprocess
import time

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

go_times = []
js_times = []

for i in range(1):
  js_times.append(js())

for i in range(1): 
  go_times.append(go())

print("NodeJS:", js_times)
print("Golang:", go_times)