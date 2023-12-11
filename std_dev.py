import json
import math

file = open("out/performance.json")
data = json.load(file)
file.close

go = 0
js = 0

for point in data["go"]:
  go += (point - 3713.79) ** 2

for point in data["js"]:
  js += (point - 5001.83) ** 2

print("go: ", math.sqrt(go / 99))
print("js: ", math.sqrt(js / 99))