import random


class MobAI:
    STRATEGIES = {
        'careful': 0,    # Осторожный
        'balanced': 1,    # Сбалансированный
        'aggressive': 2   # Агрессивный
    }

    def __init__(self, strategy='balanced'):
        self.strategy = self.STRATEGIES[strategy]
        self.influence = 6  # Начальные очки влияния
        self.energy = 0     # Текущая энергия в раунде

    def make_decision(self, player_influence):
        """Возвращает 'draw' или 'stand' с умной рандомизацией"""
        # Сначала вычисляем риск
        risk_factor = self.calculate_risk(player_influence)
        # Базовые пороги для стратегий
        thresholds = {
            0: 14 + risk_factor * 2,  # Осторожный
            1: 16 + risk_factor * 1,   # Сбалансированный
            2: 18 + risk_factor * 0.5  # Агрессивный
        }
        # Логическое решение без рандомизации
        logical_decision = 'draw' if self.energy < thresholds[self.strategy] else 'stand'
        # Рассчитываем вероятность нестандартного решения
        randomness_chance = self.calculate_randomness_chance(risk_factor)
        # Применяем рандомизацию
        if random.random() < randomness_chance:
            return self.get_unexpected_decision(logical_decision, risk_factor)
        return logical_decision

    def calculate_randomness_chance(self, risk_factor):
        """Вычисляем вероятность неожиданного хода"""
        # Базовый шанс (5%) + дополнительный риск (до 15%)
        base_chance = 0.05
        additional_chance = min(0.15, risk_factor * 0.3)  # Ограничиваем макс. шанс 20%
        return base_chance + additional_chance

    def get_unexpected_decision(self, logical_decision, risk_factor):
        """Возвращает неожиданное решение в зависимости от ситуации"""
        # В опасных ситуациях (высокий риск) моб чаще делает консервативный выбор
        if risk_factor > 0.7:
            return 'stand'  # Даже агрессивный моб остановится при высоком риске
        # В обычных условиях - случайный выбор
        return random.choice(['draw', 'stand'])

    def calculate_risk(self, player_influence):
        """Вычисляет риск"""
        energy_risk = (21 - self.energy) / 21  # Риск перебора
        influence_risk = (6 - self.influence) / 6  # Риск потери влияния
        # Весовые коэффициенты (исключен opponent_risk)
        weights = {
            0: [0.7, 0.3],  # Осторожный (70% на свой перебор, 30% на влияние)
            1: [0.5, 0.5],   # Сбалансированный
            2: [0.3, 0.7]    # Агрессивный (70% на влияние, 30% на перебор)
        }
        w = weights[self.strategy]
        return w[0] * energy_risk + w[1] * influence_risk

    def process_round_result(self, result, player_influence):
        """Обновляет очки влияния (без изменений)"""
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

    def add_energy(self, value):
        self.energy += value
        return self.energy > 21
