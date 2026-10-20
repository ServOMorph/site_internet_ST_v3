const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const OUT = path.join(__dirname, "..", "_site");
const BUDGET_PAGE = 100 * 1024;
const BUDGET_JS = 20 * 1024;
let failures = 0;
const fail = (m) => { failures++; console.log("ECHEC  " + m); };
const ok = (m) => console.log("ok     " + m);
const gz = (buf) => zlib.gzipSync(buf, { level: 9 }).length;
const kb = (n) => (n / 1024).toFixed(1) + " Ko";

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => {
    const p = path.join(dir, e.name);
    return e.isDirectory() ? walk(p) : [p];
  });
}

const pages = walk(OUT).filter((f) => f.endsWith(".html"));
if (!pages.length) { fail("aucune page construite"); process.exit(1); }

const assetSize = (url) => {
  const f = path.join(OUT, url.split("?")[0]);
  if (!fs.existsSync(f)) return null;
  const buf = fs.readFileSync(f);
  return /\.woff2$/.test(f) ? buf.length : gz(buf);
};

const fontFaces = (css) => [...css.matchAll(/url\((\/assets\/fonts\/[^)]+)\)/g)].map((m) => m[1]);

for (const file of pages) {
  const rel = path.relative(OUT, file).split(path.sep).join("/");
  const html = fs.readFileSync(file, "utf8");

  if (!/<h1[ >]/.test(html)) fail(rel + " : pas de h1");
  if (!/<title>[^<]+<\/title>/.test(html)) fail(rel + " : pas de title");
  if (!/<meta name="description" content="[^"]+"/.test(html)) fail(rel + " : pas de meta description");
  if (!/<html lang="fr">/.test(html)) fail(rel + " : lang manquant");

  const refs = [...html.matchAll(/(?:href|src)="(\/[^"#]*)"/g)].map((m) => m[1]);
  for (const r of refs) {
    const target = r.endsWith("/") ? path.join(OUT, r, "index.html") : path.join(OUT, r);
    if (!fs.existsSync(target)) fail(rel + " : lien cassé " + r);
  }

  let total = gz(Buffer.from(html));
  let js = 0;
  for (const m of html.matchAll(/<script[^>]+src="([^"]+)"/g)) {
    const s = assetSize(m[1]); if (s) { js += s; total += s; }
  }
  let cssText = "";
  for (const m of html.matchAll(/<link[^>]+rel="stylesheet"[^>]+href="([^"]+)"/g)) {
    const s = assetSize(m[1]); if (s) total += s;
    cssText += fs.readFileSync(path.join(OUT, m[1]), "utf8");
  }
  let fontBytes = 0;
  for (const m of html.matchAll(/<link[^>]+rel="preload"[^>]+href="([^"]+\.woff2)"/g)) {
    fontBytes += assetSize(m[1]) || 0;
  }
  const totalAvecPolices = total + fontBytes;
  if (js > BUDGET_JS) fail(rel + " : JS " + kb(js) + " > 20 Ko");
  if (totalAvecPolices > BUDGET_PAGE) fail(rel + " : page " + kb(totalAvecPolices) + " > 100 Ko");
  if (/<script(?![^>]*src)/.test(html) && !/application\/ld\+json/.test(html)) fail(rel + " : script en ligne");
  ok(rel + " : HTML+CSS+JS " + kb(total) + ", JS " + kb(js) + ", police(s) préchargée(s) " + kb(fontBytes));
}

const css = fs.readFileSync(path.join(OUT, "assets/css/app.css"), "utf8");
const allFonts = fontFaces(css);
const fontTotal = allFonts.reduce((a, f) => a + (assetSize(f) || 0), 0);
console.log("info   polices déclarées : " + allFonts.length + ", " + kb(fontTotal) + " au total (toutes chargées si tous les styles sont utilisés)");
if (!/prefers-reduced-motion/.test(css)) fail("prefers-reduced-motion absent du CSS");
else ok("prefers-reduced-motion présent");

const jsRequired = pages.filter((f) => /<script[^>]+src/.test(fs.readFileSync(f, "utf8"))).length;
ok("contenu servi en HTML : " + pages.length + " pages avec h1, lien internes vérifiés, " + jsRequired + " avec script différé");

console.log(failures ? "\n" + failures + " échec(s)" : "\nTous les contrôles passent");
process.exit(failures ? 1 : 0);
