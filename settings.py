import random
import pygame


def screen_settings():
    # Screen setup
    width = 640
    height = 480
    return width, height


def bar_settings():
    bar_width = 70
    bar_length = 20
    bar_x = 135
    bar_y = 450
    bar_speed = 5
    return bar_width, bar_length, bar_y, bar_x, bar_speed


def ball_settings():
    # Settings for ball
    ball_radius = 13
    ball_pos_x = random.randint(12, 640 - ball_radius)
    # ball_pos_x = 100
    ball_pos_y = 70
    ball_speed_y = 2
    ball_speed_x = 2
    return ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x

def display_game_over(screen, max_score):
    width, height = screen_settings()
    font = pygame.font.Font(None, 74)
    game_over_text = font.render('Game Over', True, (255, 255, 255))
    screen.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - game_over_text.get_height() // 2))

    font = pygame.font.Font(None, 36)
    restart_text = font.render('Restart', True, (255, 255, 255))
    restart_button = pygame.draw.rect(screen, (0, 255, 0), [width // 2 - 50, height // 2 + 50, 100, 50])
    screen.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 65))

    font = pygame.font.Font(None, 36)
    score_text = font.render(f'Max Score: {max_score}', True, (255, 255, 255))
    screen.blit(score_text, (width // 2 - score_text.get_width() // 2, height // 2 + 125))

    return restart_button

