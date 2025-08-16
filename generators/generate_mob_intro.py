import random

from text_constants.mobs_quotes import QUOTES
from text_constants.battle_stories import (
    FINAL_TOUCH,
    BODY_DESCRIPTIONS,
    EPIGRAPH_PHRASES,
    MAGIC_EFFECTS,
)


def generate_mob_intro(mob_data):
    name = mob_data['name']
    title = mob_data['title']
    sub_title = mob_data['sub_title']
    persona = mob_data['persona']
    appearance = mob_data['appearance']
    temperament = mob_data['temperament']

    # Шаблоны для вариативности
    intro_templates = [
        "Перед вами <b>{name}</b>, {title} {sub_title}, чья {appearance} аура пленяет чувства.",
        "<b>{name}</b>, {title} {sub_title}, излучает {appearance} соблазн, манящий в бездну.",
        "Сквозь магический туман выступает <b>{name}</b>, {title} {sub_title}, чья {appearance} притягательность неотвратима.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} красота заставляет сердце биться чаще.",
        "Перед вами <b>{name}</b>, {title} {sub_title}, чья {appearance} аура обещает запретное наслаждение.",
        "Словно из грёз, появляется <b>{name}</b>, {title} {sub_title}, чья {appearance} сущность манит к греху.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} притягательность заставляет забыть о битве.",
        "Сквозь тени выступает <b>{name}</b>, {title} {sub_title}, чья {appearance} красота сводит с ума.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} сущность — как зов запретного плода.",
        "Перед вами <b>{name}</b>, {title} {sub_title}, чья {appearance} аура дразнит самые сокровенные желания.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} притягательность заставляет кровь кипеть.",
        "Из магического вихря возникает <b>{name}</b>, {title} {sub_title}, чья {appearance} красота ослепляет.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} сущность обещает ночь полную страсти.",
        "Словно мираж, перед вами <b>{name}</b>, {title} {sub_title}, чья {appearance} аура ласкает чувства.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} притягательность — как яд, пьянящий душу.",
        "Перед вами <b>{name}</b>, {title} {sub_title}, чья {appearance} красота зажигает пламя в груди.",
        "Сквозь лунный свет выступает <b>{name}</b>, {title} {sub_title}, чья {appearance} сущность гипнотизирует.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} притягательность заставляет забыть о контроле.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} красота — как заклинание, сковывающее волю.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} аура манит в пучину запретных фантазий.",
        "<b>{name}</b>, {title} {sub_title}, чья {appearance} сущность — как мелодия страсти, звучащая в ночи.",
    ]
    body_templates = [
        "{body_desc}. Её {temperament} движения заставляют кровь бурлить в жилах.",
        "{body_desc}. Её {temperament} походка — как вызов, от которого невозможно отвести взгляд.",
        "{body_desc}. Каждое её {temperament} движение дразнит, обещая запретное наслаждение.",
        "{body_desc}. Её {temperament} грация гипнотизирует, разжигая огонь внутри.",
        "{body_desc}. Её {temperament} жесты манят, словно приглашение к греховному танцу.",
        "{body_desc}. Её {temperament} изгибы притягивают взгляд, обещая сладкую капитуляцию.",
        "{body_desc}. Её {temperament} движения — как шёпот страсти, звучащий в тишине.",
        "{body_desc}. Её {temperament} походка заставляет ваше тело дрожать от предвкушения.",
        "{body_desc}. Её {temperament} грация — как ласка, от которой сердце замирает.",
        "{body_desc}. Каждое её {temperament} движение — как искра, разжигающая пожар желания.",
        "{body_desc}. Её {temperament} жесты — как магический ритуал, манящий вас ближе.",
        "{body_desc}. Её {temperament} изгибы дразнят, словно зовут ваши руки к исследованию.",
        "{body_desc}. Её {temperament} походка — как танец, обещающий интимный финал.",
        "{body_desc}. Её {temperament} движения заставляют забыть о битве, оставляя лишь вожделение.",
        "{body_desc}. Её {temperament} грация — как яд, медленно растекающийся по венам.",
        "{body_desc}. Её {temperament} жесты гипнотизируют, заставляя желать большего.",
        "{body_desc}. Её {temperament} изгибы — как лабиринт, в котором хочется заблудиться.",
        "{body_desc}. Её {temperament} походка — как пульс страсти, бьющийся в такт вашему сердцу.",
        "{body_desc}. Её {temperament} движения — как магическая сеть, опутывающая ваши чувства.",
        "{body_desc}. Её {temperament} грация — как пламя, обжигающее ваши самые сокровенные мысли.",
        "{body_desc}. Её {temperament} жесты — как шёлк, скользящий по вашей коже.",
        "{body_desc}. Её {temperament} изгибы манят, словно запретный плод, жаждущий быть сорванным.",
        "{body_desc}. Её {temperament} походка — как вызов, от которого кровь кипит в жилах.",
    ]

    # Выбираем элементы
    intro = random.choice(intro_templates).format(
        name=name, title=title, sub_title=sub_title, appearance=appearance
    )
    body_desc = random.choice(BODY_DESCRIPTIONS)
    body_text = random.choice(body_templates).format(
        body_desc=body_desc, temperament=temperament
    )
    quote = random.choice(QUOTES['entry'].get(persona, QUOTES['entry']['кокетливая']))
    final_touch = random.choice(FINAL_TOUCH)
    epigraph = random.choice(EPIGRAPH_PHRASES)
    final_text = '{final_touch} {epigraph}'.format(
        final_touch=final_touch, epigraph=epigraph
    )

    # Собираем текст
    intro_parts = [
        f"{intro}\n",
        f"<i>{body_text}</i>\n",
        f"<blockquote>{quote}</blockquote>\n",
        f"<i>{final_text}</i>",
    ]

    return "\n".join(intro_parts)
