import pygame
import time
from random import randint

pygame.init()

# Constants
BLACK = (0, 0, 0)
BLUE = (65, 105, 255)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
SCREEN_WIDTH = 735
SCREEN_HEIGHT = 475

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Snake.SP')
        self.clock = pygame.time.Clock()
        self.sound = pygame.mixer.Sound('duck.wav')
        self.sound1 = pygame.mixer.Sound('chip.wav')
        
        # Tải hình ảnh con rắn
        try:
            self.snake_image = pygame.image.load('snake.png').convert_alpha()
            self.snake_image = pygame.transform.scale(self.snake_image, (130, 155))  # Điều chỉnh kích thước theo ý muốn
        except pygame.error as e:
            print("Không thể tải hình ảnh con rắn:", e)
            self.snake_image = None
        
        # Game variables
        self.snake_pos = [100, 60]
        self.snake_body = [[100, 60]]
        self.food_pos = self.generate_food_position()
        self.food_flat = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.running = True
        self.check = True
        self.difficulty = 50  # Mức độ khó mặc định (nhỏ hơn là nhanh hơn)

    def generate_food_position(self):
        food_x = randint(1, 70)
        food_y = randint(1, 45)
        if food_x % 2 != 0:
            food_x += 1
        if food_y % 2 != 0:
            food_y += 1
        return [food_x * 10, food_y * 10]

    def show_score(self):
        score_font = pygame.font.SysFont('sa', 20)
        score_txt = score_font.render("Score: " + str(self.score), True, WHITE)
        self.screen.blit(score_txt, (50, 20))

    def reset_game(self):
        self.snake_pos = [100, 60]
        self.snake_body = [[100, 60]]
        self.food_pos = self.generate_food_position()
        self.direction = 'RIGHT'
        self.change_to = self.direction
        self.score = 0
        self.check = True

    def handle_key_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.change_to = 'RIGHT'
        if event.key == pygame.K_LEFT:
            self.change_to = 'LEFT'
        if event.key == pygame.K_UP:
            self.change_to = 'UP'
        if event.key == pygame.K_DOWN:
            self.change_to = 'DOWN'

    def update_direction(self):
        if (self.change_to == "LEFT") and not (self.direction == "RIGHT"):
            self.direction = "LEFT"
        if (self.change_to == "RIGHT") and not (self.direction == "LEFT"):
            self.direction = "RIGHT"
        if (self.change_to == "UP") and not (self.direction == "DOWN"):
            self.direction = "UP"
        if (self.change_to == "DOWN") and not (self.direction == "UP"):
            self.direction = "DOWN"

    def update_snake_position(self):
        if self.direction == "RIGHT":
            self.snake_pos[0] += 10
        if self.direction == "LEFT":
            self.snake_pos[0] -= 10
        if self.direction == "UP":
            self.snake_pos[1] -= 10
        if self.direction == "DOWN":
            self.snake_pos[1] += 10
        self.snake_body.insert(0, list(self.snake_pos))

    def check_food_collision(self):
        if self.snake_pos == self.food_pos:
            pygame.mixer.Sound.play(self.sound1)
            self.score += 1
            self.food_flat = False
        else:
            self.snake_body.pop()

    def spawn_food(self):
        if not self.food_flat:
            self.food_pos = self.generate_food_position()
        self.food_flat = True

    def check_wall_collision(self):
        if (self.snake_pos[0] >= SCREEN_WIDTH or self.snake_pos[0] < 0 or
                self.snake_pos[1] >= SCREEN_HEIGHT or self.snake_pos[1] < 0):
            pygame.mixer.Sound.play(self.sound)
            self.check = False

    def check_self_collision(self):
        for block in self.snake_body[1:]:
            if self.snake_pos == block:
                pygame.mixer.Sound.play(self.sound)
                self.check = False


    def run_game(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    self.handle_key_event(event)

            self.update_direction()
            self.update_snake_position()
            self.check_food_collision()
            self.spawn_food()
            self.check_wall_collision()
            self.check_self_collision()

            if not self.check:
                self.show_game_over_screen()
                self.reset_game()

            self.screen.fill(BLACK)
            self.show_score()
            pygame.draw.rect(self.screen, RED, pygame.Rect(self.food_pos[0], self.food_pos[1], 20, 20))
            for pos in self.snake_body:
                pygame.draw.rect(self.screen, BLUE, pygame.Rect(pos[0], pos[1], 20, 20))

            pygame.display.flip()

            self.clock.tick(self.difficulty)
        def set_difficulty(self):
        # Tạo một giao diện đơn giản để chọn độ khó
            selecting = True
            while selecting:
                self.screen.fill(BLACK)
                prompt_font = pygame.font.SysFont('sa', 40)
                prompt_text = prompt_font.render("Level", True, WHITE)
                easy_text = prompt_font.render("1. Hard", True, WHITE)
                medium_text = prompt_font.render("2. Normal", True, WHITE)
                hard_text = prompt_font.render("3. Easy", True, WHITE)
                
                # Vẽ văn bản
                self.screen.blit(prompt_text, (SCREEN_WIDTH // 2 - prompt_text.get_width() // 2, 100))
                self.screen.blit(easy_text, (SCREEN_WIDTH // 2 - easy_text.get_width() // 2, 200))
                self.screen.blit(medium_text, (SCREEN_WIDTH // 2 - medium_text.get_width() // 2, 250))
                self.screen.blit(hard_text, (SCREEN_WIDTH // 2 - hard_text.get_width() // 2, 300))
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                        if easy_text.get_rect(center=(SCREEN_WIDTH // 2, 200)).collidepoint(pos):
                            self.difficulty = 50
                            selecting = False
                        elif medium_text.get_rect(center=(SCREEN_WIDTH // 2, 250)).collidepoint(pos):
                            self.difficulty = 30
                            selecting = False
                        elif hard_text.get_rect(center=(SCREEN_WIDTH // 2, 300)).collidepoint(pos):
                            self.difficulty = 10
                            selecting = False

                pygame.display.flip()
        

# Run the game
if __name__ == "__main__":
    game = SnakeGame()
    game.show_start_screen()
    game.run_game()
