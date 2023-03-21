import sys
import pygame
from settings import Settings


class AlienInvasion:
    """Класс для управления рексурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Invasion")

    def ran_game(self):
        """Запуск основного цикла игры."""
        while True:
            # Отслживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # При каждом проходе цеикла перерисовываеться экран
            self.screen.fill(self.settings.bg_color)

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуки игры.
    ai = AlienInvasion()
    ai.ran_game()
