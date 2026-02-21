import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 100,
  duration: "60s",
};

export default function () {
  const res = http.get("http://localhost:8002/hello");

  check(res, {
    "flask status 200": (r) => r.status === 200,
  });

  sleep(1);
}