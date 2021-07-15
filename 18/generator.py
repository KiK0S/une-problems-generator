from random import randint, choice
import json

def tostr(matrix):
	result = ''
	for i in range(len(matrix)):
		for x in matrix[i]:
			result += str(x)
			result += '\t'
		result += '\n'
	return result

def generate_turtle(n):
	matrix = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			matrix[i][j] = randint(1, 100)
	option = choice([0, 1])
	template = '''Квадрат разлинован на N×N клеток (1 < N < 17). Исполнитель Робот может
перемещаться по клеткам, выполняя за одно перемещение одну из двух
команд: вправо или {2}. По команде вправо Робот перемещается
в соседнюю правую клетку, по команде {2} – в соседнюю {3}. При
попытке выхода за границу квадрата Робот разрушается. Перед каждым
запуском Робота в каждой клетке квадрата лежит монета достоинством
от 1 до 100. Посетив клетку, Робот забирает монету с собой; это также
относится к начальной и конечной клетке маршрута Робота.
Определите максимальную и минимальную денежную сумму, которую
может собрать Робот, пройдя из левой {0} клетки  в правую {1}.
В ответе укажите два числа – сначала максимальную сумму, затем
минимальную.\n\n 
'''.format(['верхней', 'нижней'][option], ['нижнюю', 'верхнюю'][option], ['вниз', 'вверх'][option], ['нижнюю', 'верхнюю'][option])
	
	res_str = tostr(matrix)
	if option == 1:
		for i in range(0, (n + 1) // 2):
			matrix[i], matrix[n - 1 - i] = matrix[n - 1 - i], matrix[i]
	

	dp_max = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			a = 0
			if i > 0:
				a = dp_max[i - 1][j]
			if j > 0:
				a = max(a, dp_max[i][j - 1])
			dp_max[i][j] = matrix[i][j] + a
	dp_min = [[10**6] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			a = 10**6
			if i > 0:
				a = dp_min[i - 1][j]
			if j > 0:
				a = min(a, dp_min[i][j - 1])
			if a == 10**6:
				a = 0
			dp_min[i][j] = matrix[i][j] + a
	return (template, [dp_max[n - 1][n - 1], dp_min[n - 1][n - 1]], res_str)

def generate_path(n):
	matrix = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			matrix[i][j] = randint(1, 100)
# 	c > a so we guarantee every cell is visited once
	global a, b, c, d
	a, b = randint(1, 4), randint(1, 5)
	c, d =  randint(a + 1, 5), randint(1, 5) 
	template = '''Квадрат разлинован на N×N клеток (1 < N < 17). В каждой клетке квадрата лежит монета достоинством
от 1 до 100. Исполнитель Робот встает в произвольную клетку поля, после чего делает следующий алгоритм:
Сделай {0} шагов вправо;
Сделай {1} шагов вниз;
Сделай {2} шагов влево;
Сделай {3} шагов вверх;
Посетив клетку, Робот забирает монету с собой; это также
относится к начальной и конечной клетке маршрута Робота. При
попытке выхода за границу квадрата Робот разрушается. После конца работы алгоритма Робот подсчитывает сумму достоинств собранных монет. 
В ответе укажите два числа – сначала максимальную сумму, которую Робот может собрать, а затем
минимальную.\n\n 
'''.format(a, b, c, d)
	def g(x, y):
		global a, b, c, d
		dx = [0] * a + [1] * b + [0] * c + [-1] * d + [0]
		dy = [1] * a + [0] * b + [-1] * c + [0] * d + [0]
		result = 0
		for ca, cb in zip(dx, dy):
			if x < 0 or y < 0 or x >= n or y >= n:
				return 10 ** 6
			result += matrix[x][y]
			x += ca
			y += cb
		return result
	max_ans = 0
	min_ans = 10 ** 6
	for x in range(n):
		for y in range(n):
			result = g(x, y)
			if result == 10 ** 6:
				continue
			min_ans = min(min_ans, result)
			max_ans = max(max_ans, result)

	return (template, [max_ans, min_ans], tostr(matrix))

def generate_subsquare(n):
	matrix = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			matrix[i][j] = randint(1, 100)
	global side
	side = randint(3, 8)
	template = '''Квадратное поле разлиновано на N×N клеток (1 < N < 17). В каждой клетке поля лежит монета достоинством
от 1 до 100. Исполнитель Робот встает в произвольную клетку поля, которая будет для него стартовой. После этого он собирает все монетки, которые находятся в квардате {0}x{0}, левым верхним углом которого является стартовая клетка.
Если квадрат выходит за границы поля, то Робот ломается.
В ответе укажите два числа – сначала максимальную сумму достоинств монет, которую Робот может собрать, а затем
минимальную.\n\n
'''.format(side)
	def g(x, y):
		global side
		if x + side > n or y + side > n:
			return 10 ** 6
		result = 0
		for i in range(x, x + side):
			for j in range(y, y + side):
				result += matrix[i][j]
		return result
	max_ans = 0
	min_ans = 10 ** 6
	for x in range(n):
		for y in range(n):
			result = g(x, y)
			if result == 10 ** 6:
				continue
			min_ans = min(min_ans, result)
			max_ans = max(max_ans, result)

	return (template, [max_ans, min_ans], tostr(matrix))

def generate_row(n):
	matrix = [[0] * n for _ in range(n)]
	for i in range(n):
		for j in range(n):
			matrix[i][j] = randint(1, 100)
	template = '''Квадратное поле разлиновано на N×N клеток (1 < N < 17). В каждой клетке квадрата лежит монета достоинством
от 1 до 100. Исполнитель Робот начинает работу в левой клетке некоторого ряда.
Алгоритм, записанный в память Робота, такой:
НАЧАЛО
ПОКА СПРАВА НЕ КОНЕЦ ПОЛЯ
НАЧАЛО
ПОДНЯТЬ МОНЕТУ
ВПРАВО
КОНЕЦ
ПОДНЯТЬ МОНЕТУ
КОНЕЦ
В ответе укажите два числа – сначала максимальную сумму достоинств монет, которую Робот может собрать, а затем
минимальную.\n\n
'''
	max_ans = 0
	min_ans = 10 ** 6
	for x in range(n):
		sum = 0
		for y in range(n):
			sum += matrix[x][y]
		min_ans = min(min_ans, sum)
		max_ans = max(max_ans, sum)
	return (template, [max_ans, min_ans], tostr(matrix))


print(json.dumps(choice([generate_row, generate_subsquare, generate_path, generate_turtle])(choice(range(13, 16)))))
