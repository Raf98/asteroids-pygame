import pygame
import sys

from constants import BLINK_INTERVAL

class GameOverScreen():
    def __init__(self, screen: pygame.Surface, center_x: int, center_y: int):
        self.screen = screen
        pygame.font.init()
        self.title_font = pygame.font.SysFont(None, 96) 
        self.prompt_font = pygame.font.SysFont(None, 48)
        self.center_x = center_x
        self.center_y = center_y


    def draw_game_over_screen(self):
        last_blink_time = pygame.time.get_ticks()
        show_prompt_text = True
        while True:
            current_time = pygame.time.get_ticks()

            if current_time - last_blink_time >= BLINK_INTERVAL:
                show_prompt_text = not show_prompt_text
                last_blink_time = current_time

            self.draw_text(show_prompt_text)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    return


    def draw_text(self, show_prompt_text: bool):
        #self.screen.fill("green")

        title_text = self.title_font.render("Game Over", True, "white")
        self.screen.blit(title_text, title_text.get_rect(center=(self.center_x, self.center_y)))

        if show_prompt_text:
            prompt_text = self.prompt_font.render("Press any key to close the screen", True, "white")
            prompt_text_rect = prompt_text.get_rect(center=(self.center_x, self.center_y + 100))
            self.screen.blit(prompt_text, prompt_text_rect)
        pygame.display.flip()
