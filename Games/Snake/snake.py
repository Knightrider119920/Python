import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint


class Snake:
    def __init__(self, screen_y, screen_x):
        self.screen_y = screen_y
        self.screen_x = screen_x
        self.score = 0

    def get_food_coordinates(self, snake_body):
        food = [
            randint(2, self.screen_y - 2),
            randint(2, self.screen_x - 2)
        ]
        if food not in snake_body:
            return food
        else:
            self.get_food_coordinates(snake_body)

    def snake_movement(self, snake_head, command):
        snake_head[1] = snake_head[1] + 1 if command == KEY_RIGHT else snake_head[1]
        snake_head[1] = snake_head[1] - 1 if command == KEY_LEFT else snake_head[1]
        snake_head[0] = snake_head[0] - 1 if command == KEY_UP else snake_head[0]
        snake_head[0] = snake_head[0] + 1 if command == KEY_DOWN else snake_head[0]
        return snake_head

    def snake_movement_through_wall(self, snake_head):
        snake_head[0] = self.screen_y - 2 if snake_head[0] == 0 else snake_head[0]
        snake_head[0] = 1 if snake_head[0] == self.screen_y - 1 else snake_head[0]
        snake_head[1] = self.screen_x - 2 if snake_head[1] == 0 else snake_head[1]
        snake_head[1] = 1 if snake_head[1] == self.screen_x - 1 else snake_head[1]
        return snake_head

    def main(self):
        curses.initscr()
        win = curses.newwin(self.screen_y, self.screen_x, 0, 0)  # newwin(height, width, begin_y, begin_x)
        curses.curs_set(0)
        curses.noecho()
        win.keypad(1)

        snake_body = [[6, 7], [6, 6]]
        snake_head = snake_body[0]

        food = self.get_food_coordinates(snake_body)
        win.addstr(food[0], food[1], '')

        command = KEY_RIGHT
        last_command = command
        while command != 27:  # if input key is esc => escape_game
            win.border(0)
            timeout_ms = 200 - 5 * self.score
            win.timeout(timeout_ms)  # wait X ms for the getch
            win.addstr(0, self.screen_x // 2, str(f" Score: {self.score} "))

            command = win.getch()  # refreshes the screen and then waits for the user to hit a key returns an integer; if it’s between 0 and 255, it represents the ASCII code of the key pressed

            if command == -1:
                command = last_command

            new_head = snake_head[:]
            snake_head = self.snake_movement(snake_head, command)
            snake_head = self.snake_movement_through_wall(snake_head)
            last_command = command

            snake_body.insert(0, new_head)

            if new_head in snake_body[1:]:
                break

            win.addstr(new_head[0], new_head[1], '#')

            if new_head == food:
                self.score = self.score + 1
                food = self.get_food_coordinates(snake_body)
                win.addstr(food[0], food[1], '')
            else:
                snake_tail = snake_body.pop()
                win.addstr(snake_tail[0], snake_tail[1], ' ')

        curses.endwin()



snake = Snake(20, 50)  #window height, width
snake.main()