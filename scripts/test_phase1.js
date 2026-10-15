const fs = require("fs");
const path = require("path");
const zlib = require("zlib");

const SITE = path.join(__dirname, "..", "_site");
const BUDGET_ACCUEIL_GZIP = 50 * 1024;
let echecs = 0;

function check(ok, msg) {
  console.log((ok ? "OK    " : "ECHEC ") + msg);
  if (!ok) echecs++;
}

function walk(dir) {
  return fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) =>
    e.isDirectory() ? walk(path.join(dir, e.name)) : [path.join(dir, e.name)]
  );
}

const htmls = walk(SITE).filter((f) => f.endsWith(".html"));
check(htmls.length > 0, `${htmls.length} pages HTML generees`);

for (const f of htmls) {
  const rel = path.relative(SITE, f);
  const h = fs.readFileSync(f, "utf8");
  check(/<html lang="fr">/.test(h), `${rel} : lang fr`);
  check(/<meta name="viewport" content="width=device-width, initial-scale=1">/.test(h), `${rel} : viewport`);
  check(/<title>[^<]+<\/title>/.test(h), `${rel} : title`);
  check(/<meta name="description" content="[^"]+">/.test(h), `${rel} : description`);
  check(/<link rel="canonical" href="https:\/\/serenia-tech\.fr[^"]*">/.test(h), `${rel} : canonical`);
  check(!/<script(?![^>]*ld\+json)[^>]*>/.test(h), `${rel} : aucun JavaScript`);
  check((h.match(/<h1[ >]/g) || []).length === 1, `${rel} : un seul h1`);
  for (const m of h.matchAll(/<script type="application\/ld\+json">([^<]*)<\/script>/g)) {
    try { JSON.parse(m[1]); check(true, `${rel} : JSON-LD valide`); }
    catch (e) { check(false, `${rel} : JSON-LD invalide`); }
  }
}

const sitemap = fs.readFileSync(path.join(SITE, "sitemap.xml"), "utf8");
const locs = [...sitemap.matchAll(/<loc>https:\/\/serenia-tech\.fr([^<]*)<\/loc>/g)].map((m) => m[1]);
for (const l of locs) {
  const f = path.join(SITE, l, l.endsWith("/") ? "index.html" : "");
  check(fs.existsSync(f), `sitemap : ${l} existe`);
}
for (const f of htmls) {
  const h = fs.readFileSync(f, "utf8");
  for (const m of h.matchAll(/href="(\/[^"#]*)/g)) {
    const t = path.join(SITE, m[1], m[1].endsWith("/") ? "index.html" : "");
    if (!fs.existsSync(t)) check(false, `${path.relative(SITE, f)} : lien casse ${m[1]}`);
  }
}

const robots = fs.readFileSync(path.join(SITE, "robots.txt"), "utf8");
check(/Sitemap: https:\/\/serenia-tech\.fr\/sitemap\.xml/.test(robots), "robots.txt reference le sitemap");

const home = fs.readFileSync(path.join(SITE, "index.html"));
const css = fs.readFileSync(path.join(SITE, "css", "site.css"));
const brut = home.length + css.length;
const gz = zlib.gzipSync(home).length + zlib.gzipSync(css).length;
console.log(`Poids accueil : HTML ${home.length} o + CSS ${css.length} o = ${brut} o ; gzip ${gz} o`);
check(gz < BUDGET_ACCUEIL_GZIP, `accueil < ${BUDGET_ACCUEIL_GZIP} o gzip (hors images)`);

process.exit(echecs ? 1 : 0);
