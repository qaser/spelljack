import random
import pymorphy3

# Инициализация морфологического анализатора
morph = pymorphy3.MorphAnalyzer()

# Константы заклинаний (можно расширить)
SPELLS = [
    "Вихрь Астрального Разрыва",
    "Струя Лунного Ветра",
    "Шепот Разоблачения",
    "Исчезающий Жест",
    "Порыв Соблазна",
    "Космическое Раздевание",
    "Заклинание Скользящего Шёлка",
    "Энергия Разнузданности"
]

# Словарь одежды с возможными вариантами для каждого слоя (именительный падеж)
OUTFIT = {
    'accessories': ["ожерелье", "браслет", "кольцо", "магический амулет", "пояс с подвесками"],
    'outwear': ["мантия", "плащ", "накидка", "шаль", "капюшон"],
    'prime': ["корсет", "кисет", "жилет заклинателя", "магический доспех"],
    'second': ["рубашка с заклинаниями", "туника", "кожаный топ", "шелковая блуза"],
    'top': ["лифчик", "бюстье", "магический топ", "узкий бандаж"],
    'bottom': ["юбка", "шаровары", "штаны-кюлоты", "ленты чародейки"]
}

# Эротические описания для разных частей тела
EROTIC_DESCRIPTIONS = {
    'accessories': [
        "кожа загорается от прикосновения магии",
        "лёгкий румянец покрывает тело",
        "противник непроизвольно вздрагивает от магического прикосновения"
    ],
    'outwear': [
        "фигура становится более заметной",
        "ветерок ласкает обнажённые плечи",
        "противник слегка прикрывается руками, чувствуя себя уязвимым"
    ],
    'prime': [
        "грудь заметно вздымается от волнения",
        "талия выглядит особенно изящной без корсета",
        "противник слегка краснеет, чувствуя прохладу"
    ],
    'second': [
        "кожа покрывается мурашками",
        "противник невольно проводит рукой по животу",
        "дыхание становится чуть более частым"
    ],
    'top': [
        "грудь показывается, заставляя замереть",
        "противник инстинктивно прикрывает грудь, но ненадолго",
        "соски слегка твердеют от прохлады"
    ],
    'bottom': [
        "ноги полностью открываются взгляду",
        "противник слегка раздвигает ноги, затем быстро смыкает их",
        "бёдра выглядят соблазнительно без одежды"
    ]
}

def get_accusative(noun):
    """Возвращает существительное в винительном падеже (кого? что?)"""
    parsed = morph.parse(noun)[0]
    return parsed.inflect({'accs'}).word

def get_genitive(noun):
    """Возвращает существительное в родительном падеже (кого? чего?)"""
    parsed = morph.parse(noun)[0]
    return parsed.inflect({'gent'}).word

def generate_undressing_text(opponent_name, clothing_type, spell):
    # Выбираем случайный предмет одежды и склоняем его
    clothing_item_nominative = random.choice(OUTFIT[clothing_type])
    clothing_item_accusative = get_accusative(clothing_item_nominative)
    clothing_item_genitive = get_genitive(clothing_item_nominative)

    erotic_desc = random.choice(EROTIC_DESCRIPTIONS[clothing_type])

    # Вариации основного текста (без склонения имен и заклинаний)
    undressing_variations = [
        f"С мощным взмахом руки {opponent_name} получает '{spell}', и {clothing_item_nominative} "
        f"растворяется в клубах магического дыма. {erotic_desc.capitalize()}.",

        f"Заклинание '{spell}' поражает {opponent_name}, и {clothing_item_nominative} "
        f"начинает медленно соскальзывать, будто невидимые руки снимают её. {erotic_desc.capitalize()}.",

        f"Мощь '{spell}' обрушивается на {opponent_name}. {clothing_item_nominative.capitalize()} "
        f"вспыхивает ярким светом и исчезает. {erotic_desc.capitalize()}.",

        f"Магические символы вспыхивают вокруг {opponent_name} после '{spell}'. "
        f"{clothing_item_nominative.capitalize()} разлетается на лоскуты. {erotic_desc.capitalize()}.",

        f"Энергия '{spell}' окутывает {opponent_name}. {clothing_item_nominative.capitalize()} "
        f"постепенно становится прозрачной, пока совсем не исчезает. {erotic_desc.capitalize()}.",

        f"'{spell}' поражает {clothing_item_accusative} {opponent_name}. "
        f"Ткань превращается в лепестки и уносится ветром. {erotic_desc.capitalize()}.",

        f"Под действием '{spell}' {clothing_item_nominative} {opponent_name} развязывается "
        f"и соскальзывает, обнажая тело. {erotic_desc.capitalize()}."
    ]

    # Дополнительные эффекты (30% chance)
    if random.random() < 0.3:
        extra_effects = [
            f" {opponent_name} кокетливо улыбается, будто наслаждаясь процессом.",
            f" Кажется, {opponent_name} собирается что-то сказать, но останавливается.",
            f" Дыхание {opponent_name} заметно участилось.",
            f" {opponent_name} проводит рукой по месту, где была одежда, будто проверяя.",
            f" Губы {opponent_name} слегка приоткрываются от неожиданности.",
            f" {opponent_name} делает полушаг назад, но затем снова выпрямляется."
        ]
        return random.choice(undressing_variations) + random.choice(extra_effects)

    return random.choice(undressing_variations)

# Пример использования:
opponent_name = "Моргана"
spell = random.choice(SPELLS)
clothing_type = "top"  # Это будет приходить из логики игры

print(generate_undressing_text(opponent_name, clothing_type, spell))
