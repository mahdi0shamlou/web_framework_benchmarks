import http from "k6/http";
import { check, sleep } from "k6";

export const options = {
  vus: 50,          // number of users
  duration: "30s",  // test time
};

const targets = [
  { name: "fastapi", url: "http://localhost:8001/hello" },
  { name: "flask",   url: "http://localhost:8002/hello" },
];

export default function () {
  for (const t of targets) {
    const res = http.get(t.url);
    check(res, {
      [`${t.name} status 200`]: (r) => r.status === 200,
    });
  }
  sleep(1);
}