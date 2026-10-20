import json, sys, time, shutil, urllib.request
from pathlib import Path

SERVER = "http://127.0.0.1:8189"
COMFY_OUT = Path(r"D:\ServOMorph\ComfyUI-Qwen\output")
ROOT = Path(__file__).resolve().parent.parent
BRUT = ROOT / "src" / "assets" / "brut"
IMG = ROOT / "src" / "assets" / "img"
STYLE = ("minimalist flat vector illustration, simple geometric shapes, limited palette of deep teal green, soft sea-green and pale mint, "
         "one small warm amber accent, plain pale mint background, lots of empty space, calm, clean, no text, no letters")
def STYLE2(palette):
    return ("minimalist flat vector illustration, simple geometric shapes, limited palette of " + palette
            + ", one small amber accent, plain pale background in the same hue, lots of empty space, calm, clean, no text, no letters")


NEGATIVE = "text, letters, watermark, logo, photo, realistic, 3d render, busy, cluttered, dark, gloomy, gradient noise, blurry"
ITEMS = [
    {"id": "parcours", "prompt": "a winding path across gentle rounded green hills leading to a small glowing amber sun, " + STYLE},
    {"id": "explorer", "prompt": "a simple paper boat sailing on calm sea-green waves with a tiny compass leaf, " + STYLE},
    {"id": "pourquoi", "prompt": "a simple glowing lightbulb with a small leaf growing inside it, " + STYLE2("soft peach, warm terracotta and cream")},
    {"id": "leviers", "prompt": "a simple seesaw balancing a small green leaf on one side and a small round cloud on the other, " + STYLE2("fresh leaf green, sage and pale lime")},
    {"id": "essayer", "prompt": "a simple notepad with a pencil and a small spark above it, " + STYLE2("sunny yellow, soft gold and cream")},
    {"id": "outils", "prompt": "a simple wrench crossed with a gear, " + STYLE2("soft blue, cornflower and pale sky")},
    {"id": "donnees", "prompt": "a simple shield with a keyhole and a tiny leaf, " + STYLE2("soft lilac, lavender and pale violet")},
    {"id": "aller-plus-loin", "prompt": "a simple signpost with two arrows pointing toward a small sun, " + STYLE2("soft teal, aqua and pale mint")},
    {"id": "formation", "prompt": "a young sprout growing out of an open book, two round leaves, " + STYLE},
]
W = H = 768
SEED = 7
STEPS = 25


def build(item):
    return {
        "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": "qwen-image-2.1-Q4_K_M.gguf"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen3vl_8b_bf16.safetensors", "type": "qwen_image", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_2.1_vae_bf16.safetensors"}},
        "4": {"class_type": "TextEncodeQwenImage21", "inputs": {"clip": ["2", 0], "prompt": item["prompt"], "negative_prompt": NEGATIVE, "resolution": 1024}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": W, "height": H, "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": ["4", 0], "negative": ["4", 1], "latent_image": ["5", 0],
              "seed": SEED, "control_after_generate": "fixed", "steps": STEPS, "cfg": 1, "sampler_name": "euler", "scheduler": "simple", "denoise": 1}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["3", 0]}},
        "8": {"class_type": "SaveImage", "inputs": {"images": ["7", 0], "filename_prefix": "st_v3_ill_" + item["id"]}},
    }


def post(path, data):
    req = urllib.request.Request(SERVER + path, json.dumps(data).encode(), {"Content-Type": "application/json"})
    return json.load(urllib.request.urlopen(req))


def wait(pid):
    while True:
        h = json.load(urllib.request.urlopen(f"{SERVER}/history/{pid}"))
        if pid in h:
            return h[pid]
        time.sleep(5)


def to_webp(src, dst, size=480):
    from PIL import Image
    im = Image.open(src).convert("RGB").resize((size, size), Image.LANCZOS)
    q = 80
    while True:
        im.save(dst, "WEBP", quality=q, method=6)
        if dst.stat().st_size <= 100 * 1024 or q <= 40:
            break
        q -= 10
    print(dst.name, round(dst.stat().st_size / 1024, 1), "Ko, qualite", q)


def main():
    only = set(sys.argv[1:])
    BRUT.mkdir(parents=True, exist_ok=True)
    IMG.mkdir(parents=True, exist_ok=True)
    for it in ITEMS:
        if only and it["id"] not in only:
            continue
        pid = post("/prompt", {"prompt": build(it)})["prompt_id"]
        out = wait(pid)
        for node in out.get("outputs", {}).values():
            for img in node.get("images", []):
                src = COMFY_OUT / img.get("subfolder", "") / img["filename"]
                dst = BRUT / ("ill_" + it["id"] + ".png")
                shutil.copy(src, dst)
                to_webp(dst, IMG / (it["id"] + ".webp"))


if __name__ == "__main__":
    main()
