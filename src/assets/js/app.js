(function () {
  var KEY = "st-parcours";
  var card = document.querySelector("article[data-card]");
  var seen = [];
  try { seen = JSON.parse(localStorage.getItem(KEY)) || []; } catch (e) {}
  if (card) {
    var slug = card.getAttribute("data-card");
    if (seen.indexOf(slug) === -1) seen.push(slug);
    try { localStorage.setItem(KEY, JSON.stringify(seen)); } catch (e) {}
  }
  var links = document.querySelectorAll("a.card[data-card]");
  for (var i = 0; i < links.length; i++) {
    if (seen.indexOf(links[i].getAttribute("data-card")) !== -1) links[i].classList.add("card--seen");
  }
  var resume = document.querySelector("[data-resume]");
  if (resume && seen.length) {
    var all = document.querySelectorAll("a.card[data-card]");
    for (var j = 0; j < all.length; j++) {
      if (seen.indexOf(all[j].getAttribute("data-card")) === -1) {
        resume.setAttribute("href", all[j].getAttribute("href"));
        resume.textContent = "Reprendre";
        break;
      }
    }
  }
})();
