import json
import matplotlib.pyplot as plt
import numpy as np

files = {
    "FastAPI": "results/fastapi.json",
    "Flask": "results/flask.json"
}

summary = {}

for name, file in files.items():
    durations = []
    fails = 0
    total = 0

    with open(file) as f:
        for line in f:
            try:
                obj = json.loads(line)

                if obj.get("type") == "Point":
                    if obj.get("metric") == "http_req_duration":
                        durations.append(obj["data"]["value"])
                    if obj.get("metric") == "http_req_failed":
                        fails += obj["data"]["value"]
                        total += 1
            except:
                pass

    if durations:
        avg = np.mean(durations)
        p95 = np.percentile(durations, 95)

        summary[name] = {
            "avg": avg,
            "p95": p95,
            "requests": len(durations),
            "fail_rate": fails / total if total else 0
        }

print(summary)

# ---- Charts ----
names = list(summary.keys())
avg_vals = [summary[n]["avg"] for n in names]
p95_vals = [summary[n]["p95"] for n in names]

plt.figure()
plt.bar(names, avg_vals)
plt.title("Average Response Time (ms)")
plt.ylabel("ms")
plt.show()

plt.figure()
plt.bar(names, p95_vals)
plt.title("P95 Response Time (ms)")
plt.ylabel("ms")
plt.show()