import json
import statistics

def collect_stats(data):
  # MIN, Q1, MED, Q2, MAX, RANGE, IQR, STD_DEV, MEAN, OUTLIERS
  stats = {
    "go": calc(data, "go"),
    "js": calc(data, "js")
  }

  return stats

def calc(data, population):
  data_set = data[population]
  q = statistics.quantiles(data_set, n=4)
  sorted_data = sorted(data_set)
  

  sum = 0
  stats = {
    "MIN": data_set[0],
    "Q1": q[0],
    "MED": (sorted_data[len(sorted_data) // 2] + sorted_data[~(len(sorted_data) // 2)]) / 2,
    "Q3": q[2],
    "MAX": data_set[0],
    "IQR": q[2] - q[0],
    "OUTLIERS": []
  }

  

  for point in data_set:
    # MIN
    if point < stats["MIN"]:
      stats["MIN"] = point
    # MAX
    if point > stats["MAX"]:
      stats["MAX"] = point
    # outliers - Q1
    if point < q[0] - (1.5 * stats["IQR"]):
      stats["OUTLIERS"].append(point)
    # outliers - Q2
    if point > q[2] + (1.5 * stats["IQR"]):
      stats["OUTLIERS"].append(point)

    sum += point

  stats["RANGE"] = stats["MAX"] - stats["MIN"]
  stats["MEAN"] = sum / len(data_set)

  return stats
    
file = open("out/performance.json")
stats = collect_stats(json.load(file))
file.close

with open('out/stats.json', 'w') as f:
    json.dump(stats, f, ensure_ascii=False, indent=4)