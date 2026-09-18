import fs from "node:fs";
const p = String.raw`E:\deepseek_exclusive\math\.tmp\burn2026\yau_index.html`;
const s = fs.readFileSync(p, "utf8");
const a = s.indexOf("const DATA=");
const b = s.indexOf("const $=", a);
if (a < 0 || b < 0) { console.log("MARKER_FAIL", a, b); process.exit(1); }
let json = s.slice(a + "const DATA=".length, b).trim().replace(/;\s*$/, "");
let data;
try { data = JSON.parse(json); } catch (e) { console.log("JSON_FAIL", e.message.slice(0, 200)); process.exit(1); }
const years = [...new Set(data.map(d => d.year))];
const subjects = [...new Set(data.map(d => d.subject))];
console.log("HTML_OK problems=" + data.length + " years=" + years.length + " subjects=" + subjects.length);
console.log("subjects: " + subjects.join(" | "));
console.log("empty_text=" + data.filter(d => !d.text).length + " empty_n=" + data.filter(d => !d.n).length);
const sample = data.find(d => d.subject.includes("Physics"));
console.log("sample_physics: " + JSON.stringify({ y: sample?.year, n: sample?.n, len: sample?.text.length }));
