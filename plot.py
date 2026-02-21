import json
import numpy as np
import matplotlib.pyplot as plt

files = {
    "FastAPI": "results/fastapi_advanced.json",
    "Flask": "results/flask_advanced.json"
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
        req_count = len(durations)
        fail_rate = fails / total if total else 0
        summary[name] = {
            "avg": avg,
            "p95": p95,
            "requests": req_count,
            "fail_rate": fail_rate,
        }

print("=== Benchmark Summary ===")
for k, v in summary.items():
    print(f"{k}: {v}")

# ---- Charts ----
names = list(summary.keys())
avg_vals = [summary[n]["avg"] for n in names]
p95_vals = [summary[n]["p95"] for n in names]
reqs = [summary[n]["requests"] for n in names]
fail_rates = [summary[n]["fail_rate"]*100 for n in names]

# Average Latency Chart
plt.figure()
plt.bar(names, avg_vals, color=["skyblue","orange"])
plt.title("Average Response Time (ms)")
plt.ylabel("ms")
plt.show()

# P95 Latency Chart
plt.figure()
plt.bar(names, p95_vals, color=["skyblue","orange"])
plt.title("P95 Response Time (ms)")
plt.ylabel("ms")
plt.show()

# Total Requests Chart
plt.figure()
plt.bar(names, reqs, color=["skyblue","orange"])
plt.title("Total Requests Completed")
plt.ylabel("count")
plt.show()

# Failure Rate Chart
plt.figure()
plt.bar(names, fail_rates, color=["skyblue","orange"])
plt.title("Failure Rate (%)")
plt.ylabel("%")
plt.show()