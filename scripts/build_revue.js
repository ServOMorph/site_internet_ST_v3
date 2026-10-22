const fs = require("fs");
const path = require("path");

const ROOT = path.join(__dirname, "..");
const SITE = path.join(ROOT, "_site");
const labels = {
  "/": "Accueil", "/parcours/": "Comprendre", "/parcours/pourquoi/": "1 Pourquoi", "/parcours/ia-locale/": "2 IA locale",
  "/parcours/leviers/": "3 Leviers", "/parcours/donnees/": "4 Données", "/parcours/garder-la-main/": "5 Garder la main",
  "/parcours/essayer/": "6 Essayer", "/parcours/outils/": "7 Outils", "/parcours/aller-plus-loin/": "8 Aller plus loin", "/fiches/": "Fiches", "/fiches/consommation-requete/": "Fiche exemple",
  "/quiz/": "Quiz", "/glossaire/": "Glossaire", "/sources/": "Sources", "/a-propos/": "À propos", "/se-former/": "Se former",
};
const sectionOf = (r) => (r === "/" ? "/" : "/" + r.split("/")[1] + "/");

const routes = Object.keys(labels);
const read = (r) => fs.readFileSync(path.join(SITE, r === "/" ? "" : r, "index.html"), "utf8");
const first = read("/");

let css = fs.readFileSync(path.join(SITE, "assets/css/app.css"), "utf8");
css = css.replace(/url\((\/assets\/fonts\/([^)]+))\)/g, (_, u, f) => {
  const b = fs.readFileSync(path.join(SITE, "assets/fonts", f)).toString("base64");
  return "url(data:font/woff2;base64," + b + ")";
});

const header = first.match(/<header class="topbar">[\s\S]*?<\/header>/)[0].replace(/ aria-current="page"/g, "")
  .replace(/src="(\/assets\/img\/[^"]+)"/g, (_, u) => 'src="data:image/webp;base64,' + fs.readFileSync(path.join(SITE, u)).toString("base64") + '"');
const footer = first.match(/<footer class="pied">[\s\S]*?<\/footer>/)[0]
  .replace(/src="(\/assets\/img\/[^"]+)"/g, (_, u) => 'src="data:image/webp;base64,' + fs.readFileSync(path.join(SITE, u)).toString("base64") + '"');
const sections = routes.map((r) => {
  const main = read(r).match(/<main id="contenu">([\s\S]*?)<\/main>/)[1];
  const inlined = main.replace(/src="(\/assets\/img\/[^"]+)"/g, (_, u) => 'src="data:image/webp;base64,' + fs.readFileSync(path.join(SITE, u)).toString("base64") + '"');
  return '<div class="route" data-route="' + r + '" hidden>' + inlined + "</div>";
}).join("\n");

const script = `
var routes=${JSON.stringify(routes)};
function sec(r){return r==="/"?"/":"/"+r.split("/")[1]+"/";}
function show(r){
  if(routes.indexOf(r)<0)return;
  var els=document.querySelectorAll(".route");
  for(var i=0;i<els.length;i++)els[i].hidden=els[i].getAttribute("data-route")!==r;
  var links=document.querySelectorAll(".nav a");
  for(var j=0;j<links.length;j++){
    if(links[j].getAttribute("href")===sec(r))links[j].setAttribute("aria-current","page");else links[j].removeAttribute("aria-current");
  }
  window.scrollTo(0,0);
  parent.postMessage({route:r},"*");
}
document.addEventListener("click",function(e){
  var a=e.target.closest&&e.target.closest("a[href]");
  if(!a)return;
  var h=a.getAttribute("href");
  if(h.charAt(0)==="/"){e.preventDefault();show(h);}
});
window.addEventListener("message",function(e){if(e.data&&e.data.go)show(e.data.go);});
show("/");
`;

const doc = '<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>'
  + css + "</style></head><body>" + header + "<main>" + sections + "</main>" + footer + "<script>" + script.replace(/<\//g, "<\/") + "</script></body></html>";

const data = { doc, pages: routes.map((r) => ({ route: r, label: labels[r] })) };
const json = Buffer.from(JSON.stringify(data), "utf8").toString("base64");
const modele = fs.readFileSync(path.join(ROOT, "revue", "_modele.html"), "utf8");
fs.writeFileSync(path.join(ROOT, "revue", "revue_site.html"), modele.replace("__SITE_JSON__", () => json));
console.log("revue/revue_site.html : " + (Buffer.byteLength(json) / 1024).toFixed(0) + " Ko de données");
