const fs = require("fs");
const path = require("path");

const RACINE = path.resolve(__dirname, "..");
const SORTIE = path.join(RACINE, "dist_ressources_claudecode");
const data = JSON.parse(fs.readFileSync(path.join(RACINE, "src", "_data", "ressources.json"), "utf8"));
const site = JSON.parse(fs.readFileSync(path.join(RACINE, "src", "_data", "site.json"), "utf8"));

const parties = data.pages.filter((p) => p.guide === "agents");
if (!parties.length) throw new Error("Aucune partie du guide agents dans ressources.json");

function liste(items) {
  const lis = items
    .map((it) =>
      it.l
        ? `<li class="arbre__feuille">${it.l}</li>`
        : `<li><details class="arbre__noeud arbre__noeud--sous"><summary>${it.t}</summary>${
            it.note ? `<p class="arbre__note">${it.note}</p>` : ""
          }${liste(it.k)}</details></li>`
    )
    .join("\n");
  return `<ul class="arbre__liste">\n${lis}\n</ul>`;
}

const blocs = parties
  .map(
    (p) =>
      `<li><details class="arbre__noeud arbre__noeud--sous"><summary>Partie ${p.partie} : ${p.titre}</summary>${liste(p.T)}</details></li>`
  )
  .join("\n");

const html = `<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow, noarchive">
<title>La création d'agents IA avec Claude Code : économiser les tokens, donc l'énergie | ${site.nom}</title>
<meta name="color-scheme" content="dark">
<meta name="theme-color" content="#050d08">
<link rel="icon" href="data:,">
<link rel="stylesheet" href="assets/css/app.css">
</head>
<body data-section="ressources">
<header class="topbar">
  <span class="brand">${site.nom}</span>
</header>
<main id="contenu">
<section class="hero">
  <p class="eyebrow">Se former · ressources</p>
  <h1>La création d'agents IA avec <em>Claude Code</em> : économiser les tokens, donc l'énergie</h1>
</section>
<div class="arbre__racine">
  <details class="arbre__noeud" style="--tint:#5fd4ff" open>
    <summary>Les cinq parties du guide</summary>
    <p class="mention">${data.mention}</p>
    <ul class="arbre__liste">
${blocs}
    </ul>
  </details>
</div>
</main>
</body>
</html>
`;

let css = fs.readFileSync(path.join(RACINE, "src", "assets", "css", "app.css"), "utf8");
css = css
  .replace(/url\(\/assets\/fonts\//g, "url(../fonts/")
  .replace(/url\(\/assets\/img\/[^)]*\)/g, "none");
const restes = css.match(/url\(\s*(?!\.\.\/fonts\/)[^)]*\)/g);
if (restes) throw new Error("Ressource CSS non embarquee : " + restes.join(", "));

fs.rmSync(SORTIE, { recursive: true, force: true });
fs.mkdirSync(path.join(SORTIE, "assets", "css"), { recursive: true });
fs.mkdirSync(path.join(SORTIE, "assets", "fonts"), { recursive: true });
fs.writeFileSync(path.join(SORTIE, "index.html"), html);
fs.writeFileSync(path.join(SORTIE, "assets", "css", "app.css"), css);
for (const f of fs.readdirSync(path.join(RACINE, "src", "assets", "fonts"))) {
  fs.copyFileSync(path.join(RACINE, "src", "assets", "fonts", f), path.join(SORTIE, "assets", "fonts", f));
}
fs.writeFileSync(path.join(SORTIE, "robots.txt"), "User-agent: *\nDisallow: /\n");
fs.writeFileSync(path.join(SORTIE, "_headers"), "/*\n  X-Robots-Tag: noindex, nofollow, noarchive\n");

console.log(`Genere : ${SORTIE} (${parties.length} parties)`);
