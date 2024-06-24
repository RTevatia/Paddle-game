"""
main_game is about working on pygame - the ball bouncing on a paddle game
Author: Rahul Tevatia
"""
import pygame
from settings import *
from collision_settings import collision

def run_game():
    width, height = screen_settings()

    bar_width, bar_length, bar_y, bar_x, bar_speed = bar_settings()
    ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x = ball_settings()
    score = 0
    max_score = 0
    level = 1

    # Initialize pygame
    pygame.init()
    # Screen setup
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()
    dt = 0

    running = True
    game_over = False
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if game_over and event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = event.pos
                if restart_button.collidepoint(mouse_x, mouse_y):
                    game_over = False
                    score = 0
                    bar_width, bar_length, bar_y, bar_x, bar_speed = bar_settings()
                    ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x = ball_settings()

        if not game_over:
            # fill the screen with a color to wipe away anything from last frame
            screen.fill("black")
            # When a key is pressed move it either to the left or the right
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and bar_x > 0:
                bar_x -= bar_speed
            if keys[pygame.K_RIGHT] and bar_x < width - bar_width:
                bar_x += bar_speed

            # Draw the basket
            paddle = pygame.draw.rect(screen, (255, 255, 255), [bar_x, bar_y, bar_width, bar_length])

            # Draw the ball
            ball = pygame.draw.circle(screen, "red", (ball_pos_x, ball_pos_y), ball_radius)
            # Start the ball movement
            ball_pos_y += ball_speed_y
            ball_pos_x += ball_speed_x


            # simple collision detection
            new_score, ball_speed_x, ball_speed_y = collision(width, height, bar_width, bar_y, bar_x, ball_pos_y, 
                                                        ball_speed_x, ball_speed_y, ball_radius, ball_pos_x, score)
            
            # Increase level if score is a multiple of 5
            if new_score > score and new_score // 5 > level - 1:
                level += 1
                ball_speed_x *= 1.2  # Increase speed by 20%
                ball_speed_y *= 1.2

            score = new_score

            # Check if ball misses the paddle
            if ball_pos_y + ball_radius >= height:
                game_over = True

            
            # Display the score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Score: {score}', True, (255, 255, 255))
            screen.blit(score_text, (10, 10))

            # Display the score
            font = pygame.font.Font(None, 36)
            score_text = font.render(f'Max Score: {max_score}', True, (255, 255, 255))
            screen.blit(score_text, (10, 40))

            # Display the level
            level_text = font.render(f'Level: {level}', True, (255, 255, 255))
            screen.blit(level_text, (500, 10))

            if score >= max_score:
                max_score = score
                
        else:
            screen.fill("black")
            restart_button = display_game_over(screen, max_score)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000

    pygame.quit()


def main():
    run_game()


if __name__ == "__main__":
    main()
