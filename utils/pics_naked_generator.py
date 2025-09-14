import requests
import base64
from pathlib import Path
import json
import time
import random

# --- Настройки ---
SOURCE_DIR = Path("static/mobs")
WEBUI_URL_IMG2IMG = "http://127.0.0.1:7860/sdapi/v1/img2img"
WEBUI_URL_TXT2IMG = "http://127.0.0.1:7860/sdapi/v1/txt2img"

# Параметры генерации
STRENGTH = 0.75
STEPS = 30
SAMPLER_NAME = "Euler a"
CFG_SCALE = 7
CLIP_SKIP = 2
WIDTH = 768
HEIGHT = 1152

# --- Базовые промпты ---
BASE_PROMPT = (
    "masterpiece, best quality, amazing quality, absurdres, "
    "very aesthetic, sexually suggestive, elegant curves, perfect skin, "
    "cinematic composition, depth of field, volumetric lighting, soft shadows, "
    "flawless skin, smooth skin, ((long slender legs)):1.8, elegant legs, graceful limbs, "
    "lengthy legs, highly detailed background, toon, cartoon, dynamic angle, dutch angle, "
)

BASE_NEGATIVE_PROMPT = (
    "child, underage, teen, adolescent, minor, malformed anatomy, unnatural proportions, "
    "bad hands:1.4, extra hands:1.5, missing fingers, extra fingers, fused fingers, malformed face, cloned face, "
    "asymmetric face, distorted face, bad eyes, unnatural eyes, cross-eyed, (heterochromia:1.8), "
    "uneven skin tone, patchy skin, blotchy skin, skin discolorations, pale skin, lowres, "
    "low quality, worst quality:1.2, blurry, pixelated, jpeg artifacts, censored, mosaic, "
    "obscured, hidden, text, words, letters, signature, watermark, username, logo, brand, "
    "sketch, abstract, glitch, noise, grain, futa, hermaphrodite, intersex, non-human, furry, "
    "beast-like, animal features, tail, claws, wings, horns, scales, insects, spiders, bugs, "
    "wildlife, animals, pets, multiple people, crowd, unwanted people, background characters, "
    "out of frame, cropped, truncated, incomplete, leaf on crotch:1.8, conveniently covered, "
    "strategically placed, bound hands, tied hands, severed hand, amputated, injury, wound, "
    "blood, gore, speech bubble:2.0, thought bubble, comic bubble, text bubble, word balloon, "
    "dialogue bubble, chat bubble, conversation bubble, comic book balloon, caption box, "
    "narrative box, comic panel, comic sound effects, onomatopoeia, pow, bang, boom, censorship"
    "comic book style, cartoon bubbles, manga bubbles, any text, written words, dialogue text, "
    "subtitles, captions, bbc, simple background, plain background, empty background"
)

# --- Промпты для трансформаций ---
TRANSFORMATION_PROMPTS = {
    "demonstration_naked_breasts": {
        "positive": "(completely topless:2.0), (naked breasts:2.2), (bare chest:2.0), "
                   "(no clothing on upper body:2.0), (fully exposed breasts:2.0), "
                   "(nipples visible:2.0), (bare shoulders:1.8), (upper body nude:2.0), "
                   "(shy embarrassment:1.6), (blushing:1.5), (modest covering:1.4), "
                   "(hands covering breasts:1.7), (arms crossed over chest:1.5)",
        "negative": "clothing, dress, top, shirt, bra, bikini, covered, fabric, cloth, "
                   "wool, linen, silk, wearing, garment, apparel, outfit, strategically placed, (cum:1.8)"
    },
    "demonstration_naked_ass": {
        "positive": "(completely naked ass:2.2), (bare butt:2.0), (no panties:2.0), "
                   "(skirt lifted:2.0), (fully exposed:2.0), (nude lower body:2.0), "
                   "(bare cheeks:2.0), (seductive smile:1.6), (flirtatious glance:1.5), "
                   "(bent over:1.7), (looking back:1.6), (provocative pose:1.5)",
        "negative": "panties, underwear, bottom, clothing, dress, skirt, covered, "
                   "fabric, cloth, wearing, garment, strategically placed, (cum:1.8)"
    }
}

TARGET_STAGE_NAMES = {
    "demonstration_breasts": "demonstration_naked_breasts",
    "demonstration_ass": "demonstration_naked_ass"
}


def random_stockings():
    stockings_variants = {
        "innocent": [
            "white bridal stockings with garter",
            "delicate mesh stockings",
            "transparent shimmering stockings",
            "soft pastel stockings with lace trim",
        ],
        "elegant": [
            "sheer black thigh-high stockings",
            "lace-trimmed stockings",
            "glossy silk stockings",
            "stockings with elegant floral patterns",
            "patterned lace stockings",
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
            "sexy stockings slipping off thighs",
        ],
    }
    # выбираем случайную категорию
    mood = random.choice(list(stockings_variants.keys()))
    # берем случайный вариант из категории
    stockings = random.choice(stockings_variants[mood])
    return random.choice(['', stockings])


def build_prompt_from_meta(meta_data, transformation_type):
    """
    Собирает промпт с нуля из данных meta.json
    """
    # Базовые характеристики персонажа
    character_parts = [
        BASE_PROMPT,
        meta_data["environment"],
        f"{meta_data['hair']['color']}, {meta_data['hair']['style']}, {meta_data['hair']['texture']}",
        f"{meta_data['eyes']['color']}, {meta_data['eyes']['expression']}, {meta_data['eyes']['makeup']}",
        f"{meta_data['face']['shape']}, {meta_data['face']['lips']}, {meta_data['face']['features']}",
        f"{meta_data['body']['type']}, {meta_data['body']['breasts']}, {meta_data['body']['skin']} skin, {meta_data['body']['details']}",
    ]

    # Добавляем трансформацию
    transformation = TRANSFORMATION_PROMPTS[transformation_type]
    character_parts.append(transformation["positive"])

    # Одежда (только то, что не противоречит трансформации)
    clothing = meta_data["clothing"]
    stockings = random_stockings()
    if transformation_type == "demonstration_naked_breasts":
        # Для обнаженной груди оставляем только нижнюю часть одежды
        character_parts.extend([
            # f"{clothing['stockings']['color']} {clothing['stockings']['type']}",
            stockings,
            clothing["shoes"]
        ])
    elif transformation_type == "demonstration_naked_ass":
        # Для обнаженной попы оставляем только верхнюю часть одежды
        character_parts.extend([
            f"{clothing['dress']['color']} {clothing['dress']['type']} pulled up to waist",
            clothing["accessories"],
            clothing["shoes"]
        ])

    # Выражение и поза (берем из первого варианта)
    stage_key = transformation_type.replace("naked_", "")
    if stage_key in meta_data.get("poses", {}):
        character_parts.append(f"expression: {meta_data['poses'][stage_key][0]}")

    if stage_key in meta_data.get("view_angles", {}):
        character_parts.append(meta_data['view_angles'][stage_key][0])

    # Добавляем LoRA если есть
    if "lora_mix_prompt" in meta_data:
        character_parts.append(meta_data["lora_mix_prompt"])

    return ", ".join([p for p in character_parts if p])

def build_negative_prompt_from_meta(meta_data, transformation_type):
    """
    Собирает негативный промпт
    """
    transformation = TRANSFORMATION_PROMPTS[transformation_type]
    return f"{BASE_NEGATIVE_PROMPT}, {transformation['negative']}"

def generate_via_img2img(original_image_b64, prompt, negative_prompt, seed):
    """Генерация через img2img"""
    payload = {
        "init_images": [original_image_b64],
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "denoising_strength": STRENGTH,
        "steps": STEPS,
        "sampler_name": SAMPLER_NAME,
        "cfg_scale": CFG_SCALE,
        "clip_skip": CLIP_SKIP,
        "width": WIDTH,
        "height": HEIGHT,
        "seed": seed,
        "tiling": False,
        "enable_hr": False
    }

    response = requests.post(WEBUI_URL_IMG2IMG, json=payload)
    response.raise_for_status()
    return response.json()

def generate_via_txt2img(prompt, negative_prompt, seed):
    """Генерация через txt2img"""
    payload = {
        "prompt": prompt,
        "negative_prompt": negative_prompt,
        "steps": STEPS,
        "sampler_name": SAMPLER_NAME,
        "cfg_scale": CFG_SCALE,
        "clip_skip": CLIP_SKIP,
        "width": WIDTH,
        "height": HEIGHT,
        "seed": seed,
        "tiling": False,
        "enable_hr": False
    }

    response = requests.post(WEBUI_URL_TXT2IMG, json=payload)
    response.raise_for_status()
    return response.json()

def load_image_as_base64(image_path):
    """Загружает изображение в base64"""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode('utf-8')

def find_images_to_process(directory):
    """Находит все изображения для обработки"""
    images_to_process = []
    for meta_file in directory.rglob("mob_meta.json"):
        char_dir = meta_file.parent
        with open(meta_file, 'r', encoding='utf-8') as f:
            meta_data = json.load(f)

        # Ищем исходные изображения
        for stage in ["demonstration_breasts", "demonstration_ass"]:
            if stage in meta_data.get("generated_images", {}):
                for img_data in meta_data["generated_images"][stage]:
                    if img_data.get("success", True):
                        image_path = char_dir / img_data["file"]
                        if image_path.exists():
                            target_stage = TARGET_STAGE_NAMES[stage]
                            target_path = char_dir / img_data["file"].replace(stage, target_stage)

                            if not target_path.exists():
                                images_to_process.append({
                                    "image_path": image_path,
                                    "meta_path": meta_file,
                                    "meta_data": meta_data,
                                    "source_stage": stage,
                                    "target_stage": target_stage,
                                    "variation": img_data["variation"],
                                    "seed": meta_data["seed"] + img_data["variation"]
                                })

    return images_to_process

def process_images(mode="img2img"):
    """
    Обрабатывает изображения в указанном режиме
    mode: "img2img" или "txt2img"
    """
    print(f"Поиск изображений для обработки в режиме {mode}...")
    images_to_process = find_images_to_process(SOURCE_DIR)

    if not images_to_process:
        print("Не найдено подходящих изображений для обработки.")
        return

    print(f"Найдено {len(images_to_process)} изображений для обработки.")

    success_count = 0
    for i, item in enumerate(images_to_process, 1):
        print(f"\n[{i}/{len(images_to_process)}] Обработка: {item['image_path'].name}")

        try:
            # Собираем промпты с нуля
            prompt = build_prompt_from_meta(item["meta_data"], item["target_stage"])
            negative_prompt = build_negative_prompt_from_meta(item["meta_data"], item["target_stage"])

            if mode == "img2img":
                # Режим img2img
                original_image_b64 = load_image_as_base64(item["image_path"])
                result = generate_via_img2img(original_image_b64, prompt, negative_prompt, item["seed"])
            else:
                # Режим txt2img
                result = generate_via_txt2img(prompt, negative_prompt, item["seed"])

            # Сохраняем результат
            output_filename = item["image_path"].name.replace(item["source_stage"], item["target_stage"])
            output_path = item["image_path"].parent / output_filename

            with open(output_path, "wb") as f:
                f.write(base64.b64decode(result['images'][0]))

            # Обновляем meta.json
            meta_data = item["meta_data"]
            if item["target_stage"] not in meta_data["generated_images"]:
                meta_data["generated_images"][item["target_stage"]] = []

            meta_data["generated_images"][item["target_stage"]].append({
                "variation": item["variation"],
                "file": output_filename,
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "source_image": item["image_path"].name,
                "mode": mode,
                "strength": STRENGTH if mode == "img2img" else None,
                "seed": item["seed"],
                "success": True
            })

            with open(item["meta_path"], 'w', encoding='utf-8') as f:
                json.dump(meta_data, f, indent=2, ensure_ascii=False)

            print(f"  Успешно создано: {output_filename}")
            success_count += 1

            time.sleep(1)

        except Exception as e:
            print(f"  Ошибка: {str(e)}")
            continue

    print(f"\nОбработка завершена. Успешно: {success_count}/{len(images_to_process)}")

if __name__ == "__main__":
    # Для img2img (рекомендуется):
    # process_images(mode="img2img")

    # Для txt2img (если нужна полностью новая генерация):
    process_images(mode="txt2img")
