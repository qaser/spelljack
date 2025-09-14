import random


STAGE_CONFIG = {
    "blowjob": {
        "environment": "park",
        "interaction": "blowjob",
        "characters": [
            {
                "gender": "girl",
                "pose": "on knees",
                "clothing_style": "nude",
                "clothing_substyle": "erotic",
                "emotion": "shy",
                'gaze': 'looking at viewer'
            },
            {
                "gender": "boy",
                "pose": "standing",
                "clothing_style": "nude",
                "clothing_substyle": "erotic",
                "emotion": "smiling",
                'gaze': 'eyes closed'
            }
        ],
        'view_angle': 'three-quarter view',
    },
    "holding_hands": {
        "environment": "park",
        "interaction": "holding hands",
        "characters": [
            {
                "gender": "girl",
                "pose": "walking",
                "clothing_style": "home",
                "clothing_substyle": "strict",
                "emotion": "smiling",
                'gaze': 'looking at viewer'
            },
            {
                "gender": "boy",
                "pose": "walking",
                "clothing_style": "home",
                "clothing_substyle": "strict",
                "emotion": "smiling",
                'gaze': 'looking at viewer'
            }
        ]
    },
    "hugging": {
        "environment": "park",
        "interaction": "hugging",
        "characters": [
            {"gender": "girl", "pose": "standing", "clothing_style": "work", "clothing_substyle": "erotic", "emotion": "blushing"},
            {"gender": "boy", "pose": "standing", "clothing_style": "work", "clothing_substyle": "strict", "emotion": "smiling"}
        ]
    },
    "talking_on_bench": {
        "environment": "park",
        "interaction": "talking",
        "characters": [
            {"gender": "girl", "pose": "sitting", "clothing_style": "home", "clothing_substyle": "strict", "emotion": "happy"},
            {"gender": "boy", "pose": "sitting", "clothing_style": "home", "clothing_substyle": "strict", "emotion": "serious"}
        ]
    },
    "chasing_game": {
        "environment": "park",
        "interaction": "chasing",
        "characters": [
            {"gender": "girl", "pose": "running", "clothing_style": "sport", "clothing_substyle": "strict", "emotion": "laughing"},
            {"gender": "boy", "pose": "running", "clothing_style": "sport", "clothing_substyle": "strict", "emotion": "smiling"}
        ]
    }
}


# ==== БАЗОВЫЕ АРОМАТЫ ====
BASE_PROMPT = (
    "masterpiece, best quality, amazing quality, absurdres, "
    "4k, high resolution, ultra-detailed, newest, "
    "very aesthetic, elegant curves, perfect skin, "
    "cinematic composition, depth of field, volumetric lighting, soft shadows, "
    "highly detailed background, toon, cartoon, western comic style"
)

BASE_NEGATIVE_PROMPT = (
    "malformed anatomy, unnatural proportions, bad hands, extra hands, missing fingers, extra fingers, fused fingers, "
    "malformed face, cloned face, asymmetric face, distorted face, "
    "bad eyes, cross-eyed, "
    "uneven skin tone, patchy skin, blotchy skin, "
    "lowres, low quality, worst quality, blurry, pixelated, jpeg artifacts, "
    "text, words, letters, signature, watermark, username, logo, brand, "
    "speech bubble, thought bubble, text bubble, word balloon, caption box, comic sound effects, subtitles, captions, "
    "futa, hermaphrodite, non-huboy, furry, animal features, tail, claws, wings, "
    "crowd, unwanted people, background characters, "
    "out of frame, cropped, truncated, incomplete, "
    "injury, wound, blood, gore, "
    "censored, mosaic, obscured, hidden, "
    "realistic, photorealistic, photograph, 3d render, anime, boyga, "
    "painting, sketch, graphite, watercolor"
)


# ==== СЛОВАРИ ОДЕЖДЫ, ВОЛОС, ВНЕШНОСТИ ====
clothing_styles = {
    "girl": {
        "home": {
            "strict": ["pajamas", "bathrobe", "slippers"],
            "erotic": ["transparent nightgown", "loose shirt", "barefoot"]
        },
        "work": {
            "strict": ["blazer", "pencil skirt", "dress shirt"],
            "erotic": ["tight office dress", "short skirt", "unbuttoned blouse", "high heels"]
        },
        "nude": {
            "strict": ["underwear set", "simple bra and panties", "stockings"],
            "erotic": ["lace lingerie", "thong", "garter belt", "corset"]
        },
        "sport": {
            "strict": ["tracksuit", "jersey", "running shoes"],
            "erotic": ["tight leggings", "sports bra", "crop top"]
        },
        "fantasy": {
            "strict": ["armor", "robe", "cape"],
            "erotic": ["revealing armor", "succubus outfit", "tight bodysuit"]
        }
    },
    "boy": {
        "home": {
            "strict": ["pajamas", "bathrobe", "slippers"],
            "erotic": ["boxer briefs", "open robe"]
        },
        "work": {
            "strict": ["suit", "blazer", "dress shirt", "tie", "formal trousers"],
            "erotic": ["unbuttoned shirt", "slim-fit trousers"]
        },
        "nude": {
            "strict": ["boxers", "briefs"],
            "erotic": ["low-rise briefs"]
        },
        "sport": {
            "strict": ["sports jersey", "training shorts", "sneakers"],
            "erotic": ["compression shorts", "open hoodie"]
        },
        "fantasy": {
            "strict": ["knight armor", "cape", "wizard robe"],
            "erotic": ["barbarian loincloth", "tight leather armor", "open chest tunic"]
        }
    }
}

hair_styles = {
    "girl": {
        "colors": ["blonde hair", "black hair", "red hair", "brown hair", "white hair", "blue hair", "pink hair"],
        "styles": ["long straight hair", "wavy hair", "curly hair", "braided hair", "ponytail", "twin tails", "messy bun", "short bob cut"]
    },
    "boy": {
        "colors": ["blonde hair", "black hair", "red hair", "brown hair", "white hair"],
        "styles": ["short messy hair", "buzz cut", "undercut", "slicked back hair", "side part", "spiky hair", "curly short hair"]
    }
}
eye_colors = ["blue eyes", "green eyes", "brown eyes", "hazel eyes", "purple eyes"]
body_types = ["slim body", "curvy body", "athletic body", "muscular body"]


def pick_clothes(gender, style, substyle):
    return random.choice(clothing_styles.get(gender, {}).get(style, {}).get(substyle, ["casual clothes"]))


def random_appearance(gender):
    return {
        "hair": f"{random.choice(hair_styles[gender]['colors'])}, {random.choice(hair_styles[gender]['styles'])}",
        "eyes": random.choice(eye_colors),
        "body": random.choice(body_types)
    }


def describe_character(c, idx):
    appearance = random_appearance(c["gender"])
    clothes = pick_clothes(c["gender"], c["clothing_style"], c["clothing_substyle"])
    pose = c.get("pose", "standing")
    emotion = c.get("emotion", "neutral")
    gaze = c.get("gaze", "looking forward")

    return (
        f"(Character {idx}: {c['gender']}, {appearance['body']}, {appearance['hair']}, {appearance['eyes']}, "
        f"{clothes}, {emotion}, {pose}, {gaze}):1.25"
    )


def count_characters(characters):
    girls = sum(1 for c in characters if c["gender"] == "girl")
    boys = sum(1 for c in characters if c["gender"] == "boy")
    parts = []
    if girls > 0:
        parts.append(f"{girls}girl{'s' if girls > 1 else ''}")
    if boys > 0:
        parts.append(f"{boys}boy{'s' if boys > 1 else ''}")
    return ", ".join(parts)


def group_tag(characters):
    n = len(characters)
    return "solo" if n == 1 else "couple" if n == 2 else "group"


def generate_prompt(stage_name):
    scenario = STAGE_CONFIG[stage_name]
    characters = scenario["characters"]

    char_count = count_characters(characters)
    gtag = group_tag(characters)

    char_blocks = " BREAK ".join(describe_character(c, i+1) for i, c in enumerate(characters))
    interaction = f", {scenario['interaction']}" if scenario.get("interaction") else ""
    environment = scenario.get("environment", "")
    view_angle = scenario.get("view_angle", "")
    extra = ", ".join(scenario.get("extra_prompts", []))

    positive = (
        f"{char_count}, {gtag}{interaction}, {environment}, "
        f"{char_blocks} BREAK {view_angle}, {extra}, {BASE_PROMPT}"
    )
    negative = BASE_NEGATIVE_PROMPT
    return positive, negative


# ==== ТЕСТ ====
if __name__ == "__main__":
    pos, neg = generate_prompt("holding_hands")
    print("=== Positive ===")
    print(pos)
    print("\n=== Negative ===")
    print(neg)
