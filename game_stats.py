class GameStats:
    """Отслеживание статистики для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализируем статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускаеться в активном состоянии.
        self.game_active = False

    def reset_stats(self):
        """Инициализируем статистику, изменяющуюся в ходе игры."""
        self.ships_left = self.settings.ship_limit