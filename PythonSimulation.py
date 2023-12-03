import pygame as pg
import random
import sys
import time
import matplotlib.pyplot as plt

def simulate_game(width, height, snake_speed):
    pg.init() 

    snake_size = 10
    clock = pg.time.Clock()

    x, y = width / 2, height / 2
    x_speed, y_speed = 0, 0

    snake_pixels = []
    snake_length = 1

    target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
    target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0

    game_over = False
    
    start_time = time.time()
    checkpoint_int = 10
    next_checkpoint_time = start_time + checkpoint_int

    while not game_over:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                game_over = True

        food_direction = [target_x - x, target_y - y]
        if abs(food_direction[0]) > abs(food_direction[1]):
            x_speed = snake_size if food_direction[0] > 0 else -snake_size
            y_speed = 0
        else:
            x_speed = 0
            y_speed = snake_size if food_direction[1] > 0 else -snake_size
            
        current_time = time.time()
        if current_time >= next_checkpoint_time:
            next_checkpoint_time += checkpoint_int
            elapsed = current_time - start_time
            print(f"Score: {snake_length - 1}, Elapsed Time: {elapsed:.2f} seconds")

        x += x_speed
        y += y_speed

        snake_pixels.append([x, y])

        if len(snake_pixels) > snake_length:
            del snake_pixels[0]

        if x == target_x and y == target_y:
            target_x = round(random.randrange(0, width - snake_size) / 10.0) * 10.0
            target_y = round(random.randrange(0, height - snake_size) / 10.0) * 10.0
            snake_length += 1

        if x >= width or x < 0 or y >= height or y < 0:
            game_over = True
            
        clock.tick(snake_speed)
            
    end_time = time.time() 

    pg.quit()  
    
    duration = end_time - start_time
    print("Game Over! \nDuration:", duration, "seconds")
    print('Score: ', snake_length-1)

    return snake_length - 1, duration

def run_simulations(num_simulations, width, height, snake_speed):
    scores = []
    durations = []

    for _ in range(num_simulations):
        score, duration = simulate_game(width, height, snake_speed)
        scores.append(score)
        durations.append(duration)

    average_score = sum(scores) / num_simulations
    average_duration = sum(durations) / num_simulations

    print(f"\nAverage Score: {average_score:.2f}")
    print(f"Average Duration: {average_duration:.2f} seconds")

    plt.scatter(durations, scores)
    plt.title('Duration vs. Score')
    plt.xlabel('Duration (seconds)')
    plt.ylabel('Score')
    plt.show()



if __name__ == "__main__":
    size=input('Would you like to run a short simulation or long simulation (s/l): ')
    num_simulations = int(input('Enter the number of simulations to run: '))

    if size=='s':
        width=60
        height=40
        print('\nThis simulation will have an AI play Snake in a 60 by 40 pixel area. Unless the AI loses before, every 10 seconds you will be updated with its current score and time elapsed.\nAfter the simulation is over, you will be prompted with a graph that analizes the score the AI accumulated vs the duration it lasted of every game.\n')
    else:
        width=600
        height=400
        print('\nThis simulation will have an AI play Snake in a 600 by 400 pixel area. Unless the AI loses before, every 10 seconds you will be updated with its current score and time elapsed. If you wish to stop the program, force quit out of the pop up application named "Python" and results will still show up.\nAfter the simulation is over, you will be prompted with a graph that analizes the score the AI accumulated vs the duration it lasted of every game.\n')
    snake_speed=15
    
    run_simulations(num_simulations, width, height, snake_speed)
    sys.exit()