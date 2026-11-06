import shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_illustrations as g

SORTIE = g.BRUT / "c"
STYLE = ("minimal elegant illustration on a very dark deep green background, glowing {hue} neon line art with soft bioluminescent glow, "
         "tiny floating particles of light, one small warm amber spark, centered subject, lots of empty dark space, high-end tech aesthetic, no text")
NEG = "text, letters, watermark, logo, people, faces, cluttered, blurry, low quality, white background, pastel, flat colors"

ITEMS = [
    ("parcours", "a winding glowing path across rounded hills leading to a small bright sun", "lime green and mint"),
    ("explorer", "a simple paper boat sailing on glowing waves with a small compass leaf", "cyan and mint"),
    ("pourquoi", "a lightbulb with a small leaf growing inside it", "warm amber and orange"),
    ("leviers", "a seesaw balancing a small leaf on one side and a small cloud on the other", "lime green"),
    ("essayer", "a notepad with a pencil and a small spark above it", "golden yellow"),
    ("outils", "a wrench crossed with a gear", "electric blue and cyan"),
    ("donnees", "a shield with a keyhole and a tiny leaf", "violet and lilac"),
    ("aller-plus-loin", "a signpost with two arrows pointing toward a small sun", "teal and aqua"),
    ("formation", "a young sprout growing out of an open book, two round leaves", "mint and lime"),
    ("en-pratique", "a pair of open hands gently shaping a small glowing leaf out of light, with a few tiny sparks floating above", "lime green and gold"),
    ("actualites", "a radar sweep screen with rising concentric signal waves and a small glowing leaf blip", "cyan and mint"),
    ("evenements", "a stage spotlight beam shining down onto a small glowing leaf on a dark floor, scattered particles of light", "warm amber and coral"),
    ("garder-main-a", "a human hand gently holding a small glowing leaf whose veins are circuit lines", "coral and warm peach"),
    ("garder-main-b", "a level balance scale with a glowing leaf on one side and a small glowing circuit chip on the other", "coral and warm peach"),
    ("atelier", "a round table seen from the side with several leaf-shaped speech bubbles floating above it, linked by thin lines", "lime green and mint"),
    ("conference", "a podium microphone with concentric sound waves spreading out and a small glowing leaf", "warm amber and orange"),
    ("formation-groupe", "a small staircase of stones climbing up to a glowing leaf at the top", "mint and cyan"),
    ("res-agents", "a small round helper robot tending a tiny glowing sprout with a watering can", "electric blue and cyan"),
    ("res-ia-locale", "a small house whose window glows with a computer chip shaped like a leaf", "teal and aqua"),
    ("res-images", "an empty picture frame with a glowing paintbrush drawing a leaf inside it", "violet and lilac"),
    ("actualites-b", "a folded newspaper with a small glowing leaf rising from its fold, thin lines of light around it", "cyan and mint"),
    ("evenements-b", "a string of glowing paper lanterns hanging over a night garden, one lantern shaped like a leaf", "warm amber and coral"),
    ("formation-b", "a classroom chalkboard with a glowing leaf drawn in chalk and a piece of chalk resting below", "mint and lime"),
    ("essayer-b", "a question mark made of a curved vine ending in a small glowing leaf", "golden yellow and lime"),
    ("formation-c", "a young plant in a small pot on a desk beside an open notebook and a pencil, a glowing leaf above the plant", "mint and lime"),
    ("formation-groupe-c", "three round wooden stools in a circle around a softly glowing lamp shaped like a leaf", "mint and cyan"),
    ("res-images-c", "a camera lens with a glowing green leaf reflected in the glass, soft rays of light", "violet and lilac"),
]


def main():
    only = set(sys.argv[1:])
    SORTIE.mkdir(parents=True, exist_ok=True)
    for id_, sujet, hue in ITEMS:
        if only and id_ not in only:
            continue
        wf = g.build({"id": "c_" + id_, "prompt": sujet + ", " + STYLE.format(hue=hue)})
        wf["4"]["inputs"]["negative_prompt"] = NEG
        pid = g.post("/prompt", {"prompt": wf})["prompt_id"]
        out = g.wait(pid)
        for node in out.get("outputs", {}).values():
            for img in node.get("images", []):
                src = g.COMFY_OUT / img.get("subfolder", "") / img["filename"]
                dst = SORTIE / ("ill_" + id_ + ".png")
                shutil.copy(src, dst)
                g.to_webp(dst, g.IMG / (id_ + ".webp"))
                print(id_, "ok", flush=True)


if __name__ == "__main__":
    main()
