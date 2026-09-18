import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const here = path.dirname(fileURLToPath(import.meta.url));
const target = path.resolve(here, "..", "..", "yau_index.html");

const s = fs.readFileSync(target, "utf8");
const a = s.indexOf("const DATA=");
const b = s.indexOf("const $=", a);
if (a < 0 || b < 0) {
  console.log("MARKER_FAIL", a, b);
  process.exit(1);
}
const json = s.slice(a + "const DATA=".length, b).trim().replace(/;\s*$/, "");
let data;
try {
  data = JSON.parse(json);
} catch (e) {
  console.log("JSON_FAIL", String(e.message).slice(0, 200));
  process.exit(1);
}
const years = [...new Set(data.map(d => d.year))];
const subjects = [...new Set(data.map(d => d.subject))];
const empty = data.filter(d => !d.text || !d.n).length;
console.log("HTML_OK problems=" + data.length + " years=" + years.length +
            " subjects=" + subjects.length + " empty=" + empty);
console.log("subjects: " + subjects.join(" | "));
process.exit(data.length > 0 && empty === 0 ? 0 : 1);
