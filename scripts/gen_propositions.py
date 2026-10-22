import shutil, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import gen_illustrations as g

SORTIE = g.ROOT / "src" / "assets" / "brut" / "propositions"
W, H = 1344, 768
NEG = "text, letters, watermark, logo, people, faces, cluttered, blurry, low quality"

PROPOSITIONS = [
    {"id": "A_canopee_neon",
     "prompt": "futuristic eco city in the canopy of a giant forest, slender glass towers covered with green vegetation, "
               "glowing emerald and cyan light lines like circuits running along tree trunks, soft mist, deep night blue-green sky "
               "with a pale aurora, small amber lights, cinematic wide shot, elegant, clean, high detail, no text"},
    {"id": "B_oceans_solaires",
     "prompt": "clean futuristic coastline at dawn, translucent solar panels shaped like leaves floating on calm turquoise water, "
               "white organic architecture with rounded forms, wind turbines in the distance, luminous gradient sky from teal to soft peach, "
               "minimal, airy, modern vector-like illustration, no text"},
    {"id": "C_circuit_vivant",
     "prompt": "abstract macro of a green leaf whose veins become glowing circuit traces and data nodes, floating particles of light, "
               "deep forest green background fading to black, bioluminescent mint and lime highlights, one small amber spark, "
               "elegant minimal composition with empty space, high-end tech aesthetic, no text"},
]


def main():
    SORTIE.mkdir(parents=True, exist_ok=True)
    for p in PROPOSITIONS:
        item = {"id": "prop_" + p["id"], "prompt": p["prompt"]}
        wf = g.build(item)
        wf["5"]["inputs"]["width"] = W
        wf["5"]["inputs"]["height"] = H
        wf["4"]["inputs"]["negative_prompt"] = NEG
        wf["6"]["inputs"]["seed"] = 11
        pid = g.post("/prompt", {"prompt": wf})["prompt_id"]
        out = g.wait(pid)
        for node in out.get("outputs", {}).values():
            for img in node.get("images", []):
                src = g.COMFY_OUT / img.get("subfolder", "") / img["filename"]
                shutil.copy(src, SORTIE / (p["id"] + ".png"))
                print(p["id"], "ok", flush=True)


if __name__ == "__main__":
    main()
