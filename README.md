# Web Framework Benchmarks

**Fair and reproducible benchmarks comparing web frameworks using Docker-isolated environments.**

Author: Mahdi Shamlou

---

## 📌 Project Goal

This repository provides **real, fair, and reproducible benchmarks** for modern web frameworks using identical APIs, identical hardware limits, and identical load‑testing tools.

Many benchmark articles online are outdated, biased, or not reproducible. This project solves that by using:

* ✅ Same API logic
* ✅ Same CPU & RAM limits (Docker isolation)
* ✅ Same load testing tool
* ✅ Same Python/Go versions
* ✅ Open-source and reproducible setup

So anyone can clone this repo and verify the results.

---

## 🧠 Frameworks Compared (Initial List)

Python Frameworks:

* FastAPI
* Flask
* Django

(Go benchmarks may be added later.)

Each framework implements **exactly the same routes**.

---

## ⚙️ Benchmark Strategy

Every framework is tested under the same conditions:

* Docker container isolation
* Same CPU limits
* Same memory limits
* Same OS image
* Same Python version
* Same ASGI/WSGI server where possible
* Same load testing script

This makes results fair and meaningful.

---

## 📊 Metrics Measured

We don’t just measure speed. We measure:

* Requests per second
* Average latency
* p95 latency
* CPU usage
* Memory usage
* Error rate
* Startup time

Because real-world performance is more than just req/sec.

---

## 🧪 Load Testing Tools

Benchmarks are executed using tools like:

* k6
* wrk

Scripts are included in the repo so tests are reproducible.

---

## 📁 Project Structure

```
web_framework_benchmarks/
│
├── fastapi/
├── flask/
├── django/
├── starlette/
├── django-ninja/
├── docker-compose.yml
├── k6-tests/
├── results/
└── README.md
```

Each framework folder contains:

* Dockerfile
* Identical API routes
* Server configuration

---

## ▶️ How To Run Benchmarks

### 1. Clone Repo

```
git clone https://github.com/<your-username>/web_framework_benchmarks.git
cd web_framework_benchmarks
```

### 2. Build Containers

```
docker compose build
```

### 3. Start APIs

```
docker compose up
```

### 4. Run Load Test

```
k6 run k6-tests/basic.js
```

### 5. Check Results

Results will be saved inside the `results/` folder.

---

## 🧠 Important Notes

Benchmark results depend on:

* Database usage
* Logging
* Middleware
* Payload size
* Hardware
* Network

So always run benchmarks in your own environment too.

---

## 📌 Why Docker Isolation?

Without isolation, benchmarks are unreliable.

Docker ensures:

* Same resources for every framework
* No background process interference
* Reproducible environment

This is similar to professional benchmark suites like TechEmpower.

---

## 🧩 Future Plans

* Add database benchmarks (PostgreSQL, Redis)
* Add authentication middleware tests
* Add async vs sync comparisons
* Add Go framework benchmarks
* Add CI automated benchmark reports

---

## 🤝 Contributing

Contributions are welcome!

You can help by:

* Adding new frameworks
* Improving benchmark scripts
* Reporting bugs
* Sharing results from your hardware

Please open a Pull Request.

---

## 📜 License

MIT License

---

## ⭐ If You Like This Project

Please star the repo and share it ❤️

It helps more developers run fair benchmarks and choose the right framework.
