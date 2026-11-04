import shutil, sys, time, urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_illustrations as g
import gen_theme_c as c

W, H = 1024, 576
SUJET = "three round speech bubbles shaped like leaves, softly glowing, linked by thin circuit lines, spread across the wide frame"
HUE = "lime green and mint"
LARGEUR_WEBP = 1024


def attendre_serveur(delai=600):
    debut = time.time()
    while time.time() - debut < delai:
        try:
            urllib.request.urlopen(g.SERVER + "/system_stats", timeout=5)
            return
        except Exception:
            time.sleep(5)
    raise SystemExit("ComfyUI injoignable")


def vers_webp(src, dst):
    from PIL import Image
    im = Image.open(src).convert("RGB")
    im = im.resize((LARGEUR_WEBP, round(LARGEUR_WEBP * im.height / im.width)), Image.LANCZOS)
    q = 80
    while True:
        im.save(dst, "WEBP", quality=q, method=6)
        if dst.stat().st_size <= 100 * 1024 or q <= 40:
            break
        q -= 10
    print(dst.name, round(dst.stat().st_size / 1024, 1), "Ko, qualite", q, flush=True)


def main():
    attendre_serveur()
    c.SORTIE.mkdir(parents=True, exist_ok=True)
    wf = g.build({"id": "c_temoignages", "prompt": SUJET + ", " + c.STYLE.format(hue=HUE)})
    wf["4"]["inputs"]["negative_prompt"] = c.NEG
    wf["5"]["inputs"]["width"] = W
    wf["5"]["inputs"]["height"] = H
    pid = g.post("/prompt", {"prompt": wf})["prompt_id"]
    out = g.wait(pid)
    for node in out.get("outputs", {}).values():
        for img in node.get("images", []):
            src = g.COMFY_OUT / img.get("subfolder", "") / img["filename"]
            dst = c.SORTIE / "ill_temoignages.png"
            shutil.copy(src, dst)
            vers_webp(dst, g.IMG / "temoignages.webp")
            print("temoignages ok", flush=True)


if __name__ == "__main__":
    main()
