(function () {
  var e = document.querySelector(".stat__num");
  if (!e || window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
  var cible = 415, duree = 2200, debut = null;
  e.textContent = "0";
  function pas(t) {
    if (debut === null) debut = t;
    var p = Math.min((t - debut) / duree, 1);
    e.textContent = Math.round(cible * (1 - Math.pow(1 - p, 3)));
    if (p < 1) requestAnimationFrame(pas);
  }
  requestAnimationFrame(pas);
})();
