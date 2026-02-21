import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  stages: [
    { duration: "30s", target: 50 },   // ramp-up to 50 VUs
    { duration: "1m", target: 200 },   // hold 200 VUs
    { duration: "30s", target: 0 },    // ramp-down
  ],
  thresholds: {
    "http_req_duration": ["p(95)<200"], // 95% of requests should be below 200ms
  },
  discardResponseBodies: false,
};

const routes = [
  { name: "hello", url: "http://localhost:8001/hello" }
];

export default function () {
  for (const route of routes) {
    const res = http.get(route.url);

    check(res, {
      [`${route.name} status 200`]: (r) => r.status === 200,
    });
  }

  sleep(1); // simulate user think time
}