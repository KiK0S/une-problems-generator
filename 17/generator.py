from random import randint, choice
import json

def generate():
	divs = [2, 3, 5, 7, 11]
	non_divs = [13, 17, 19, 23, 29]
	left_border = randint(1000, 2999)
	right_border = randint(7000, 9999)
	func = [
	('сумму', lambda s, x: s + x, 0),
	('количество', lambda s, x: s + 1, 0),
	('максимум среди', lambda s, x: max(s, x), 0),
	('минимум среди', lambda s, x: min(s, x), 10 ** 6)
	]
	a = choice(divs)
	b = choice(non_divs)
	c = choice(func)
	template = 'Посчитайте {4} чисел, находящихся в промежутке [{0}, {1}], которые делятся на {2} и не делятся на {3}'.format(
		left_border, right_border, a, b, c[0]
	)
	ans = c[2]
	for x in range(left_border, right_border + 1):
		if x % a == 0 and x % b != 0:
			ans = c[1](ans, x)
	return (template, ans, '')

print(json.dumps(generate()))