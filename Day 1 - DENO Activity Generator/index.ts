import { serve } from "https://deno.land/std@0.67.0/http/server.ts";
import activity from "./activity.ts";

const s = serve({ port: 8000 });
console.log("http://localhost:8000/");

for await (const req of s) {
  console.log(req.url);
  const res = await fetch('https://www.boredapi.com/api/activity');
  const resJson = await res.json();
  console.table(resJson);
  req.respond({ body: activity(resJson) });
}


