def collision(width, height, bar_width, bar_y, bar_x, ball_pos_y, ball_speed_x, ball_speed_y, ball_radius, ball_pos_x, score):

    if ball_pos_y + ball_radius >= bar_y and bar_x <= ball_pos_x <= bar_x + bar_width:
        ball_speed_y *= -1
        score += 1
    elif ball_pos_y <= 2:
        ball_speed_y *= -1
    if ball_pos_x >= width:
        ball_speed_x *= -1
    elif ball_pos_x <= ball_radius:
        ball_speed_x *= -1
    if ball_pos_y > height + ball_radius:
        ball_speed_x = 0
        ball_speed_y = 0
    if ball_pos_y == 430 and ball_pos_x == bar_x:
        # ball_speed_x *= -1
        ball_speed_y *= -1
    return score, ball_speed_x, ball_speed_y
