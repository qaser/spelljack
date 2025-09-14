import requests
import base64
from pathlib import Path
import random
import json
import time
from stage_config import ENVIRONMENT_THEMES, CLOTHING_BY_THEME, STAGE_CONFIG

# Настройки
OUTPUT_DIR = Path("static/mobs")
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
WEBUI_URL = "http://127.0.0.1:7860/sdapi/v1/txt2img"

NUM_CHARACTERS = 50
WIDTH = 832
HEIGHT = 1216
STEPS = 35
SAMPLER_NAME = "DPM++ 2M"
CFG_SCALE = 7
CLIP_SKIP = 2

# Базовые промпты
BASE_PROMPT = (
    "masterpiece, best quality, ultra-detailed, digital painting, toon, cartoon, "
    "very aesthetic, sexually suggestive, stylized skin shading, comic book, "
    "elegant curves, perfect anatomy, cinematic composition, soft lighting, depth of field, volumetric lighting, "
    "((long slender legs)):1.8, elegant legs, graceful limbs, illustrated skin, "
    "soft comic rendering, lengthy legs, highly detailed background, BREAK"
)

BASE_NEGATIVE_PROMPT = (
    "safe_neg, score_6, score_5, score_4, (source_pony, source_anime, "
    "source_painting, source_cartoon),((watermark:1.5), "
    "(worst quality:1.5), (normal quality:1.5), (bad quality:1.5), "
    "(ugly face), (ugly), (old), (old face), imperfect eyes, "
    "(worst face details), (skewed eyes), (bad eye details), male, muscular, "
    "unnatural face, unnatural eyes, unnatural body, monochrome, grayscale, 2d, "
    "3d, semi-realistic, burry, noise, abs, (multi colored hair), asian, "
    "((extra fingers)), distorted hands, distorted fingers, deformed, "
    "lowres, bad anatomy, simple background, censored, easynegative, moir pattern, "
    "downsampling, aliasing, distortedglossy, jpeg artifacts, compression artifacts, "
    "poorly drawn, bad, distortion, twisted, mixed characters,symmetrical, "
    "duplicate, cloned, error, pattern, glitch, overexposed, high-contrast, bad-contrast"
)

# Атрибуты персонажей
HAIR_STYLES = [
    "long straight hair", "long wavy hair", "long layered hair", "long messy hair",
    "waist-length hair", "hip-length hair", "ankle-length hair", "floor-length hair",
    "shoulder-length hair", "medium layered cut", "shaggy medium cut", "curtained hair",
    "pixie cut", "bob cut", "lob cut", "asymmetrical bob", "undercut style",
    "low ponytail", "high ponytail", "side ponytail", "messy bun", "neat bun",
    "top knot", "half-up half-down", "braided crown", "space buns",
    "single braid", "twin braids", "french braid", "dutch braid", "fishtail braid",
    "boxer braids", "waterfall braid", "rope braid",
    "loose curls", "tight curls", "natural curls", "beach waves", "ringlet curls",
    "sleek straight", "voluminous hair", "textured hair",
    "asymmetrical cut", "side swept hair", "twin tails", "twin low tails",
    "hime cut", "wolf cut", "mullet cut", "shag cut",
    "chignon", "updo", "gibson roll", "victorian updo", "retro waves",
    "bedhead style", "tousled hair", "windblown hair", "natural texture"
]
HAIR_COLORS = [
    "black hair", "jet black hair", "dark brown hair", "chocolate brown hair",
    "chestnut brown hair", "light brown hair", "auburn hair", "red hair",
    "ginger hair", "strawberry blonde hair", "blonde hair", "platinum blonde hair",
    "dirty blonde hair", "ash blonde hair", "golden blonde hair",
]
EYE_COLORS = ["blue eyes", "green eyes", "yellow eyes", "gray eyes", "amber eyes", "brown eyes"]
BODY_TYPES = ["hourglass body", "curvy body", "petite body", "voluptuous body", "thin waist", "wide hips", "thick thighs", "cute small ass"]
BREAST_SIZES = ["large breasts", "busty chest", "full breasts", "large round breasts"]
SKIN_TONES = ["light", "tan", "deeply tanned with tan lines", "caramel"]
FACE_DETAILS = ["symmetric face", "face with delicate features", "face with sharp jawline", "face with soft facial features", "face with high cheekbones", "face with pointed chin", "round face shape"]
LIP_TYPES = [
    "full lips", "plump lips", "pouty lips", "thin lips",
    "bow-shaped lips", "cupid's bow lips", "rosebud lips",
    "heart-shaped lips", "wide lips", "small lips",
    "defined lips", "soft lips", "lush lips",
    "prominent lips", "natural lips", "bee-stung lips",
    "glossy lips", "matte lips", "painted lips",
    "natural lip color", "rosy lips", "pink lips"
]
FACIAL_FEATURES = ["high cheekbones", "dimples", "freckles", "elegant jawline", "delicate nose"]
AGE_LOOKS = [
    "youthful appearance",
    "mature beauty",
    "timeless goddess-like look"
]
THEME_EMOTION_BIAS = {
    "dark_fantasy": ["mysterious", "confident", "seductive"],
    "greek_mythology": ["graceful", "proud", "elegant"],
    "gothic_victorian": ["melancholic", "elegant", "innocent"],
    "metal_concert": ["wild", "rebellious", "playful"]
}


def generate_theme_clothing(theme_name, rng):
    """Генерирует одежду по тематике."""
    theme = CLOTHING_BY_THEME[theme_name]
    underwear_color = rng.choice(theme["colors"])
    return {
        "dress": {
            "type": rng.choice(theme["dress"]),
            "color": rng.choice(theme["colors"]),
            "details": rng.choice(["elegant", "revealing", "form-fitting", "decorative"])
        },
        "lingerie": {
            "type": rng.choice(theme["lingerie"]),
            "color": underwear_color,
            "details": rng.choice(["sexy", "lace", "sheer", "provocative"])
        },
        "stockings": {
            "type": rng.choice(theme["stockings"]),
            "color": underwear_color,
            "details": rng.choice([
                "sexy", "delicate mesh", "thigh-high", "provocative",
                "patterned lace", "lace-trimmed", "seductive fishnet",
                "slipping off thighs", "transparent shimmering",
                "bridal with garter", "half-rolled down"
            ])
        },
        "accessories": rng.choice(theme["accessories"]),
        "shoes": rng.choice(["high heels", "barefoot", ""])
    }


def generate_character_appearance(seed=None):
    """Генерация персонажа с вариативными особенностями"""
    if seed is None:
        seed = random.randint(1000000, 9999999)
    rng = random.Random(seed)
    # случайная тема и время суток
    theme_name = rng.choice(list(ENVIRONMENT_THEMES.keys()))
    time_of_day = rng.choice(["day", "night"])
    # 🎭 базовое описание
    appearance = {
        "seed": seed,
        "theme": theme_name,
        "environment": ENVIRONMENT_THEMES[theme_name],
        "time_of_day": time_of_day,
        "hair": {
            "style": rng.choice(HAIR_STYLES),
            "color": rng.choice(HAIR_COLORS),
            "texture": rng.choice(["shiny", "silky", "glossy", "messy", "wet look"])
        },
        "eyes": {
            "color": rng.choice(EYE_COLORS),
            "makeup": rng.choice(["smoky eyes", "natural makeup", "glitter", "winged eyeliner"]),
            "expression": rng.choice(["seductive", "innocent", "mysterious", "teasing", "dreamy"])
        },
        "body": {
            "type": rng.choice(BODY_TYPES),
            "breasts": rng.choice(BREAST_SIZES),
            "skin": rng.choice(SKIN_TONES),
            "details": rng.choice(["flawless skin", "smooth skin", "soft skin", "delicate complexion"]),
            "age_look": rng.choice(AGE_LOOKS)
        },
        "face": {
            "shape": rng.choice(FACE_DETAILS),
            "lips": rng.choice(LIP_TYPES),
            "features": rng.choice(FACIAL_FEATURES),
        },
        "poses": {},
        "view_angles": {}
    }
    # 🎭 подбираем позы и углы для каждой сцены
    for name, cfg in STAGE_CONFIG.items():
        appearance["poses"][name] = rng.sample(cfg["poses"], min(cfg["variations"], len(cfg["poses"])))
        appearance["view_angles"][name] = rng.sample(cfg["view_angles"], min(cfg["variations"], len(cfg["view_angles"])))
    return appearance


def random_stockings():
    """Генерирует случайные чулки."""
    stockings_variants = {
        "innocent": [
            "white bridal stockings with garter",
            "delicate mesh stockings",
            "transparent shimmering stockings",
            "soft pastel stockings with lace trim"
        ],
        "elegant": [
            "sheer black thigh-high stockings",
            "lace-trimmed stockings",
            "glossy silk stockings",
            "stockings with elegant floral patterns",
            "patterned lace stockings"
        ],
        "provocative": [
            "sexy stockings",
            "sexy stockings with straps and belt",
            "seductive fishnet stockings",
            "torn sexy fishnet stockings",
            "torn sexy stockings",
            "shiny stockings",
            "half-rolled down stockings",
            "silky stockings with bow",
            "sexy stockings slipping off thighs"
        ]
    }
    mood = random.choice(list(stockings_variants.keys()))
    return random.choice(stockings_variants[mood])


def build_clothing_description(appearance, stage_name):
    """Формирует описание одежды из theme + stage + logic"""
    stage_cfg = STAGE_CONFIG[stage_name]
    theme_name = appearance["theme"]
    rng = random.Random(appearance["seed"])
    logic = stage_cfg.get("clothing_logic", "full_dressed")
    mod = stage_cfg.get("clothing_logic_mod", "normal")
    theme = CLOTHING_BY_THEME.get(theme_name, {})
    desc_parts = []
    if logic == "naked":
        return "nude, no clothing"
    if logic == "underwear":
        panties = rng.choice(theme.get("underwear", {}).get("panties", ["panties"]))
        bra = rng.choice(theme.get("underwear", {}).get("bra", ["bra"]))
        color = rng.choice(theme.get("underwear", {}).get("color", ["white"]))
        desc_parts.append(f"{color} {bra}, {color} {panties}")
    elif logic == "stockings":
        stockings = rng.choice(theme.get("stockings", ["stockings"]))
        color = rng.choice(theme.get("colors", ["black"]))
        desc_parts.append(f"{color} {stockings}")
    elif logic == "full_dressed":
        cloth = rng.choice(theme.get("dress", ["casual dress"]))
        color = rng.choice(theme.get("colors", ["black"]))
        desc_parts.append(f"{color} {cloth}")
        if theme.get("accessories") and rng.random() < 0.6:  # 60% шанс аксессуара
            desc_parts.append(rng.choice(theme["accessories"]))
        if theme.get("objects") and rng.random() < 0.3:  # 30% шанс предмета
            desc_parts.append(rng.choice(theme["objects"]))
    if mod != "normal":
        desc_parts = [f"{mod} {x}" for x in desc_parts]
    return ", ".join(desc_parts)


def build_prompt(appearance, stage_name, variation_idx=0, lora_mix_prompt=''):
    cfg = STAGE_CONFIG[stage_name]
    rng = random.Random(appearance["seed"] + variation_idx)
    # 🎭 собираем эмоции
    scene_emotions = cfg.get('emotion', [])
    theme_emotions = THEME_EMOTION_BIAS.get(appearance["theme"], [])
    all_emotions = scene_emotions + theme_emotions
    # 🎲 bias: эмоции от темы чаще встречаются
    if theme_emotions and rng.random() < 0.6:
        emotion = rng.choice(theme_emotions)
    else:
        emotion = rng.choice(all_emotions) if all_emotions else "neutral"
    # 👗 одежда
    clothing_desc = build_clothing_description(appearance, stage_name)
    # 📝 собираем промпт
    parts = [
        BASE_PROMPT,
        f"{appearance['environment']}",
        f"{appearance['hair']['color']}, {appearance['hair']['style']}, {appearance['hair']['texture']}",
        f"{appearance['eyes']['color']}, {appearance['eyes']['expression']}, {appearance['eyes']['makeup']}",
        f"{appearance['face']['shape']}, {appearance['face']['lips']}, {appearance['face']['features']}",
        f"{appearance['body']['type']}, {appearance['body']['breasts']}, {appearance['body']['skin']} skin",
        f"{appearance['body']['age_look']}",
        f"expression: {emotion}",
        f"pose: {appearance['poses'][stage_name][variation_idx]}",
        f"{appearance['view_angles'][stage_name][variation_idx]}",
        clothing_desc,
        lora_mix_prompt,
    ]
    if "extra_prompts" in cfg:
        parts.extend(cfg["extra_prompts"])
    return ", ".join([p for p in parts if p])


def build_negative_prompt(stage_name):
    """Строит негативный промпт."""
    cfg = STAGE_CONFIG[stage_name]
    return BASE_NEGATIVE_PROMPT + ", " + cfg.get("negative_prompt", "")


def generate_image(payload, output_path):
    """Генерирует изображение через API."""
    try:
        response = requests.post(WEBUI_URL, json=payload)
        response.raise_for_status()
        result = response.json()
        with open(output_path, "wb") as f:
            f.write(base64.b64decode(result['images'][0]))
        return True
    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return False


def random_lora_mix():
    """Генерирует случайный микс Lora."""
    lora_parts = ['<lora:EldritchComicsXL1.2:1>']
    roll = random.random()
    if roll < 0.10:
        lora_parts.append("<lora:JAB_Comix_Ay_Papi_17_All_Star_Cast_r1:1.0>, jabay17")
        return lora_parts
    elif roll < 0.20:
        lora_parts.append("<lora:tendertroupe_v0.1-pony:1.0>")
        return lora_parts
    aypapi_w = round(random.uniform(0.3, 0.4), 1)
    lora_parts.append(f"<lora:JAB_Comix_Ay_Papi_17_All_Star_Cast_r1:{aypapi_w}>, jabay17")
    western_w = round(random.uniform(0.2, 0.4), 1)
    lora_parts.append(f"<lora:Wester_Cartoon_Style_2:{western_w}>, w3st3rnt00n2")
    tender_w = round(random.uniform(0.2, 0.7), 1)
    lora_parts.append(f"<lora:tendertroupe_v0.1-pony:{tender_w}>")
    croc_w = round(random.uniform(0.0, 0.2), 1)
    if croc_w > 0:
        lora_parts.append(f"<lora:ACrocsComics_style:{croc_w}>, CrocXL")
    return ", ".join(lora_parts)


def process_character(character, char_dir, lora_mix_prompt, repair_mode=False):
    """Обрабатывает генерацию изображений для персонажа."""
    meta_path = char_dir / "mob_meta.json"
    for stage_name, cfg in STAGE_CONFIG.items():
        variations = cfg.get("variations", 1)
        for v in range(variations):
            expected_name = f"mob_{character['seed']}_{stage_name}_var{v+1}.png"
            output_path = char_dir / expected_name
            if repair_mode and output_path.exists():
                continue  # Пропуск существующих в repair

            prompt = build_prompt(character, stage_name, v, lora_mix_prompt)
            print(prompt)
            negative_prompt = build_negative_prompt(stage_name)
            payload = {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "width": WIDTH,
                "height": HEIGHT,
                "sampler_name": SAMPLER_NAME,
                "steps": STEPS,
                "cfg_scale": CFG_SCALE,
                "seed": character['seed'] + v,
                "clip_skip": CLIP_SKIP,
                "tiling": False,
                "enable_hr": False
            }
            print(f"▶ {'Восстановление' if repair_mode else 'Генерация'}: {output_path.name}")
            print(f"Тема: {character['theme']}, Время: {character['time_of_day']} ---- {lora_mix_prompt}")
            success = generate_image(payload, output_path)
            try:
                character["generated_images"][stage_name].append({
                    "variation": v + 1,
                    "file": expected_name,
                    "prompt": prompt,
                    "negative_prompt": negative_prompt,
                    "success": success
                })
            except:
                pass
            with open(meta_path, "w", encoding="utf-8") as f:
                json.dump(character, f, indent=2, ensure_ascii=False)
            time.sleep(0.5)  # Уменьшил задержку


def main():
    """Основная функция генерации."""
    for _ in range(NUM_CHARACTERS):
        lora_mix_prompt = random_lora_mix()
        character = generate_character_appearance()
        character["lora_mix_prompt"] = lora_mix_prompt
        char_dir = OUTPUT_DIR / f"mob_{character['seed']}_{character['theme']}"
        char_dir.mkdir(exist_ok=True)
        meta_path = char_dir / "mob_meta.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(character, f, indent=2, ensure_ascii=False)
        process_character(character, char_dir, lora_mix_prompt)


def repair_missing_images():
    """Восстанавливает недостающие изображения."""
    for char_dir in OUTPUT_DIR.iterdir():
        if not char_dir.is_dir():
            continue
        meta_file = char_dir / "mob_meta.json"
        if not meta_file.exists():
            continue
        with open(meta_file, "r", encoding="utf-8") as f:
            character = json.load(f)
        lora_mix_prompt = character.get("lora_mix_prompt", random_lora_mix())  # Используем сохраненный, если есть
        process_character(character, char_dir, lora_mix_prompt, repair_mode=True)


if __name__ == "__main__":
    # repair_missing_images()
    main()
