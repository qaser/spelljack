import random

BODY_AREAS = {
    "лиф": "пышную грудь",
    "трусики": "соблазнительную попку",
    "чулки": "длинные стройные ножки",
    "пояс": "тонкую талию",
    "перчатки": "изящные ручки",
    "плащ": "плечи и изгиб спины",
}

def outfit_review_generator(name: str, outfits: dict, outfit_left: int) -> str:
    worn_parts = sorted(list(outfits.items())[:outfit_left])
    removed_parts = sorted(list(outfits.items())[outfit_left:])

    intro = f"Перед тобой предстала {name} — как персонаж из запретных сказаний, полная магии и греховного очарования.\n\n"

    worn_descriptions = []
    for _, item in worn_parts:
        body_area = BODY_AREAS.get(item.lower(), "тело")
        worn_descriptions.append(
            random.choice([
                f"На {name} всё ещё оставалась {item}, едва прикрывающая её {body_area}.",
                f"{item.capitalize()} обтягивал(а) её {body_area}, возбуждая воображение до предела.",
                f"Ткань {item} соблазнительно облегала её {body_area}, оставляя слишком мало загадки.",
                f"Её {body_area} маняще скрывались под {item}, будто дразня тебя на каждый взгляд.",
            ])
        )

    removed_descriptions = []
    for _, item in removed_parts:
        body_area = BODY_AREAS.get(item.lower(), "обнажённую плоть")
        removed_descriptions.append(
            random.choice([
                f"{item.capitalize()} уже была сорвана, обнажив её {body_area} без всякого стыда.",
                f"Следы от {item} ещё теплились на её {body_area}, но ткань давно покинула её тело.",
                f"Когда {item} соскользнула с неё, твоему взгляду открылась её {body_area} во всей красе.",
                f"Сняв {item}, {name} оставила лишь воспоминание о том, как она обнимала её {body_area}.",
            ])
        )

    erotic_finale = random.choice([
        f"\n{name} стояла перед тобой, сочетающая невинность и похоть, словно готовая к новому магическому поединку, где желания — главное оружие.",
        f"\nКаждый взгляд на неё казался грехом, но устоять перед {name} было бы ещё большим.",
        f"\nСловно сцена из самых запретных хроник, её образ останется в твоей памяти надолго.",
        f"\n{random.choice(['Магия', 'Желание', 'Искушение'])} витала в воздухе, когда ты смотрел на {name}, сгорая от вожделения.",
    ])

    return intro + "\n".join(worn_descriptions + removed_descriptions) + erotic_finale
