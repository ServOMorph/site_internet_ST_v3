import json, sys, time, shutil, urllib.request, urllib.parse
from pathlib import Path

SERVER = "http://127.0.0.1:8189"
COMFY_OUT = Path(r"D:\ServOMorph\ComfyUI-Qwen\output")
DEST = Path(__file__).resolve().parent.parent / "src" / "assets" / "brut"
PROMPTS = Path(__file__).resolve().parent / "prompts_b.json"
NEGATIVE = "text, watermark, logo, harsh white background, overexposed, dull colors, gloomy, scary, murky, dim, muddy colors, creepy"
SEED = 42
STEPS = 25


def build(item):
    return {
        "1": {"class_type": "UnetLoaderGGUF", "inputs": {"unet_name": "qwen-image-2.1-Q4_K_M.gguf"}},
        "2": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen3vl_8b_bf16.safetensors", "type": "qwen_image", "device": "default"}},
        "3": {"class_type": "VAELoader", "inputs": {"vae_name": "qwen_image_2.1_vae_bf16.safetensors"}},
        "4": {"class_type": "TextEncodeQwenImage21", "inputs": {"clip": ["2", 0], "prompt": item["prompt"], "negative_prompt": NEGATIVE, "resolution": 1024}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": item["w"], "height": item["h"], "batch_size": 1}},
        "6": {"class_type": "KSampler", "inputs": {"model": ["1", 0], "positive": ["4", 0], "negative": ["4", 1], "latent_image": ["5", 0],
              "seed": SEED, "control_after_generate": "fixed", "steps": STEPS, "cfg": 1, "sampler_name": "euler", "scheduler": "simple", "denoise": 1}},
        "7": {"class_type": "VAEDecode", "inputs": {"samples": ["6", 0], "vae": ["3", 0]}},
        "8": {"class_type": "SaveImage", "inputs": {"images": ["7", 0], "filename_prefix": "st_v3_" + item["id"]}},
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


def main():
    items = json.loads(PROMPTS.read_text(encoding="utf-8"))
    only = set(sys.argv[1:])
    DEST.mkdir(parents=True, exist_ok=True)
    for it in items:
        if only and it["id"] not in only:
            continue
        pid = post("/prompt", {"prompt": build(it)})["prompt_id"]
        out = wait(pid)
        for node in out.get("outputs", {}).values():
            for img in node.get("images", []):
                src = COMFY_OUT / img.get("subfolder", "") / img["filename"]
                shutil.copy(src, DEST / f"{it['id']}.png")
                print("ok", it["id"])


if __name__ == "__main__":
    main()
