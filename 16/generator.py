from random import randint, choice
import json

def gen_single_odd():
	n = randint(20, 50)
	start_value = randint(2, 4)
	adds = [
	('n', lambda n: n),
	('n * n', lambda n: n * n),
	('5 * n * n', lambda n: 5 * n * n),
	('n * n * n', lambda n: n * n * n),
	('n / 2', lambda n: n // 2),
	('n - 1', lambda n: n - 1),
	('1', lambda n: 1),
	('2', lambda n: 2),
	('3', lambda n: 3),
	('4', lambda n: 4),
	('7', lambda n: 7)]
	next_value = [
	('n / 2', lambda n: n // 2),
	('n / 3', lambda n: n // 3)]
	for i in range(1, start_value + 1):
		next_value.append(('n - ' + str(i), lambda n: n - i))
	idx = []
	template = '''F(n) = n при n ≤ ''' + str(start_value) + ';\n'
	for i in range(start_value):
		id_a, id_b = randint(0, len(adds) - 1), randint(0, len(next_value) - 1)
		template += 'F(n) = {0} + F({1}), если n > {2} и дает остаток {3} при делении на {4}\n'.format(adds[id_a][0],
		next_value[id_b][0],
		str(start_value),
		str(i),
		str(start_value))
		idx.append((id_a, id_b))
	template += 'В качестве ответа на задание выведите значение F({0})\n'.format(n)
	def f(n):
		if n <= start_value:
			return n
		for i in range(start_value):
			if n % start_value == i:
				return adds[idx[i][0]][1](n) + f(next_value[idx[i][1]][1](n))
	return (template, f(n), '')


def gen_single_less():
	n = randint(41, 50)
	a, b, c = randint(3, 10), randint(2, 4), randint(30, 40)
	template = 'F(n) = n при n ≤ {0};\nF(n) = n / {1} + F(n - {0}), если n > {0} и n ≤ {2};\nF(n) = 2 * F(n - 5), если n > {2}\n'.format(a, b, c)
	template += 'В качестве ответа на задание выведите значение F({0})\n'.format(n)
	def f(n):
		if n <= a:
			return n
		if n <= c:
			return n // b + f(n - a)
		return 2 * f(n - 5)
	return (template, f(n), '')


print(json.dumps(choice([gen_single_less, gen_single_odd])()))