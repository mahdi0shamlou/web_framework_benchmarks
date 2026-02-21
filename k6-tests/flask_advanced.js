import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  stages: [
    { duration: "30s", target: 50 },
    { duration: "1m", target: 200 },
    { duration: "30s", target: 0 },
  ],
  thresholds: {
    http_req_duration: ["p95<200"],
  },
  discardResponseBodies: false,
};

const routes = [
  { name: "hello", url: "http://localhost:8002/hello" },
  { name: "sleep", url: "http://localhost:8002/sleep" }, // optional sleep route
];

export default function () {
  for (const route of routes) {
    const res = http.get(route.url);

    check(res, {
      [`${route.name} status 200`]: (r) => r.status === 200,
    });
  }

  sleep(1);
}