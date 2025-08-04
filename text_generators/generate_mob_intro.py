import random

from text_constants import battle_stories


def generate_mob_intro(mob_data):
    appearance_key = None
    for key in battle_stories.APPEARANCE.keys():
        if key in mob_data['descriptors']['appearance'].lower():
            appearance_key = key
            break
    if not appearance_key:
        appearance_key = 'улыбка'
    # outfit_text = generate_outfit_description(mob_data['outfit'])
    intro_parts = [
        f"Перед вами <b>{mob_data['name']}</b> — {mob_data['title']} {mob_data['sub_title']}.\n",
        f"<i>{random.choice(battle_stories.APPEARANCE[appearance_key])}.</i>",
        f"<i>{random.choice(battle_stories.BODY_DESCRIPTIONS)}.</i>\n",
        f"<blockquote>{mob_data['quotes']['entry']}</blockquote>\n",
        f"{random.choice(battle_stories.FINAL_TOUCH)} {random.choice(battle_stories.EPIGRAPH_PHRASES)}"
    ]
    return "\n".join(intro_parts)
