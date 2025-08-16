import random


class MobAI:
    STRATEGIES = {
        'careful': 0,  # Осторожный
        'balanced': 1,  # Сбалансированный
        'aggressive': 2,  # Агрессивный
    }

    def __init__(self, strategy='balanced'):
        self.strategy = self.STRATEGIES[strategy]
        self.influence = 6  # Начальные очки влияния
        self.energy = 0  # Текущая энергия в раунде
        self.buff = None  # Активный баф

    def make_decision(self, player_influence, mirror_event=False, fog_event=False):
        """Возвращает 'draw' или 'stand' с учётом событий и бафов."""
        # Минимальный порог для взятия карты, выше при fog_event
        min_energy = 13 if fog_event else 11
        if self.energy < min_energy:
            return 'draw'

        # Учитываем бафы и события
        risk_factor = self.calculate_risk(player_influence, mirror_event, fog_event)
        thresholds = {
            0: 13 + risk_factor * 2,  # Осторожный
            1: 15 + risk_factor * 1,  # Сбалансированный
            2: 17 + risk_factor * 0.5,  # Агрессивный
        }
        # Повышаем порог для extra_draw
        if self.buff == "extra_draw":
            thresholds = {k: v + 2 for k, v in thresholds.items()}
        # Понижаем порог для fog_event, но менее агрессивно
        if fog_event:
            thresholds = {k: v - 1 for k, v in thresholds.items()}
        # Понижаем порог для mirror_event
        if mirror_event:
            thresholds = {k: v - 1 for k, v in thresholds.items()}
        # Если есть preserve_outfit, можно рисковать
        if self.buff == "preserve_outfit":
            thresholds = {k: v + 1 for k, v in thresholds.items()}

        logical_decision = (
            'draw' if self.energy < thresholds[self.strategy] else 'stand'
        )
        randomness_chance = self.calculate_randomness_chance(risk_factor, fog_event)
        if random.random() < randomness_chance:
            return self.get_unexpected_decision(logical_decision, risk_factor)
        return logical_decision

    def calculate_randomness_chance(self, risk_factor, fog_event):
        """Вычисляет вероятность неожиданного хода."""
        base_chance = 0.05
        # Снижаем случайность при fog_event
        fog_modifier = 0.5 if fog_event else 1
        # Снижаем случайность при высокой энергии
        energy_modifier = max(0, 1 - self.energy / 21)  # 0% при 21, 100% при 0
        additional_chance = min(0.05, risk_factor * 0.2)  # Макс. 10% итого
        return (base_chance + additional_chance) * energy_modifier * fog_modifier

    def get_unexpected_decision(self, logical_decision, risk_factor):
        """Возвращает неожиданное решение."""
        if risk_factor > 0.7 or self.energy > 17:
            return 'stand'  # Консервативно при высоком риске
        return random.choice(['draw', 'stand'])

    def calculate_risk(self, player_influence, mirror_event, fog_event):
        """Вычисляет риск с учётом событий."""
        energy_risk = (21 - self.energy) / 21  # Риск перебора
        influence_risk = (6 - self.influence) / 6  # Риск потери влияния
        # Увеличиваем риск при mirror_event и fog_event
        event_risk = 0.3 if mirror_event else 0
        event_risk += 0.2 if fog_event else 0
        weights = {
            0: [0.6, 0.3, 0.1],  # Осторожный: 60% энергия, 30% влияние, 10% события
            1: [0.4, 0.4, 0.2],  # Сбалансированный
            2: [0.3, 0.5, 0.2],  # Агрессивный
        }
        w = weights[self.strategy]
        return w[0] * energy_risk + w[1] * influence_risk + w[2] * event_risk

    def process_round_result(self, result, player_influence):
        """Обновляет очки влияния."""
        if result == "player_win":
            self.influence = max(0, self.influence - 1)
        elif result == "mob_win":
            self.influence = min(6, self.influence + (1 if self.influence < 6 else 0))
        elif result == "double_bust":
            self.influence = max(0, self.influence - 1)
        elif result == "player_win_mob_bust":
            if player_influence == 6:
                self.influence = max(0, self.influence - 2)
            else:
                self.influence = max(0, self.influence - 1)
        elif result == "mob_win_player_bust":
            if self.influence == 6:
                pass
            else:
                self.influence = min(6, self.influence + 1)

    def reset_energy(self):
        self.energy = 0
        self.buff = None

    def add_energy(self, value):
        self.energy += value
        return self.energy > 21

    def set_buff(self, buff):
        self.buff = buff
