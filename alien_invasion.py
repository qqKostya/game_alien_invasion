import sys
import pygame


class AlienInvasion:
    """Класс для управления рексурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def ran_game(self):
        """ЗАпуск основного цикла игры."""
        while True:
            # Отслживание событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Отображение последнего прорисованного экрана.
            pygame.display.flip()


if __name__ == "__main__":
    # Создание экземпляра и запуки игры.
    ai = AlienInvasion()
    ai.ran_game()
