#! python3
# -- coding = utf-8 --
import random, sys

class Food:
	def __init__(self, height, widge, kind):
		self.height = height
		self.widge = widge
		self.kind = kind
		self.food_xy()

	def food_xy(self):
		self.x = random.randint(0, self.widge-1)
		self.y = random.randint(0, self.height-1)

class Snake:
	def __init__(self, head_kind, tail_kind):
		self.head_kind = head_kind
		self.tail_kind = tail_kind
		self.point = 0
		self.x = 0
		self.y = 0
		self.xy_dic = {"x":[0], "y":[0]}

	def up(self):
		self.y -= 1
		self.xy_dic["x"].append(self.x)
		self.xy_dic["y"].append(self.y)

	def down(self):
		self.y += 1
		self.xy_dic["x"].append(self.x)
		self.xy_dic["y"].append(self.y)

	def left(self):
		self.x -= 1
		self.xy_dic["x"].append(self.x)
		self.xy_dic["y"].append(self.y)

	def right(self):
		self.x += 1
		self.xy_dic["x"].append(self.x)
		self.xy_dic["y"].append(self.y)

class Screen:
	def __init__(self, height=24, widge=80):
		self.height = height
		self.widge = widge
		self.screen()

	def screen(self):
		self.screen = []
		
		for i in range(self.height):
			screen_row = []
			for j in range(self.widge):
				screen_row.append(" ")
			self.screen.append(screen_row)

	def show(self):
		screen_str = ""
		screen_str += ("#"*(self.widge + 2) + "\n")
		for i in self.screen:
			screen_str += "#"
			for j in i:
				screen_str += j
			screen_str += "#\n"
		screen_str += ("#"*(self.widge + 2) + "\n")
		print(screen_str)

def game(height, widge, head_kind, tail_kind, food_kind):
	
	food = Food(height, widge, food_kind)
	snake = Snake(head_kind, tail_kind)
	while True:
		screen = Screen(height, widge)
		if (snake.x == food.x) and (snake.y == food.y):
			snake.point += 1
			food.food_xy()
		screen.screen[food.y][food.x] = food.kind
		screen.screen[snake.y][snake.x] = snake.head_kind
		if snake.point != 0:
			for i in range(2, (snake.point + 2)):
				screen.screen[snake.xy_dic["y"][-i]][snake.xy_dic["x"][-i]]\
				= snake.tail_kind
		screen.show()
		key = input()
		if key == "w":
			snake.up()
		elif key == "a":
			snake.left()
		elif key == "s":
			snake.down()
		elif key == "d":
			snake.right()
		else:
			pass

if __name__ == "__main__":
        try:
                game(10, 10, "O", "o", "*")
        except:
                print("game over")
                sys.exit()
