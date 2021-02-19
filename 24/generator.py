from random import randint, choice
import json

def generate_XYZ(n):
	output = ''
	for i in range(n):
		output += choice(['X', 'Y', 'Z'])
	rnd_idx = randint(50, 100)

	def f_x_in_a_row(n, output, rnd_idx):
		cur = 0
		ans = 0
		for c in output:
			if c == 'X':
				cur += 1
			else:
				cur = 0
			ans = max(ans, cur)
		return ans

	def f_in_a_row(n, output, rnd_idx):
		cur = 0
		ans = 0
		last = 'a'
		for c in output:
			if c == last:
				cur += 1
			else:
				cur = 1
			ans = max(ans, cur)
			last = c
		return ans

	def f_three_different(n, output, rnd_idx):
		cur = 0
		ans = 0
		last = 'a'
		pre_last = 'a'
		for c in output:
			if c != last and c != pre_last:
				cur += 1
			else:
				if c != last:
					cur = 2
				else:
					cur = 1
			ans = max(ans, cur)
			pre_last = last
			last = c
		return ans

	def f_two_different(n, output, rnd_idx):
		cur = 0
		ans = 0
		last = 'a'
		for c in output:
			if c != last:
				cur += 1
			else:
				cur = 1
			ans = max(ans, cur)
			last = c
		return ans

	def f_idx(n, output, rnd_idx):
		cur = 1
		for c in output:
			if c == 'Z':
				rnd_idx -= 1
				if rnd_idx == 0:
					return cur
			cur += 1
		return cur

	problem = [
	('максимальное количество подряд идущих символов X', f_x_in_a_row),
	('максимальное количество одинаковых символов, идущих подряд', f_in_a_row),
	('максимальное количество подряд идущих символов, среди которых каждые три соседних символа различны', f_three_different),
	('максимальное количество идущих подряд символов, среди которых каждые два соседних различны', f_two_different),
	('каким по счету от начала файла окажется {0}-й символ Z'.format(rnd_idx), f_idx)
	]
	idx = randint(0, len(problem) - 1)
	template = '''Текстовый файл состоит не более чем из 1.000.000 символов X, Y и Z.
Определите {0}.
Для выполнения этого задания следует написать программу.
'''.format(problem[idx][0])
	return (template, problem[idx][1](n, output, rnd_idx), str(output))

def generate_brackets(n):
	output = ''
	for i in range(n):
		output += choice(['(', ')'])

	def f_open_in_a_row(n, output):
		cur = 0
		ans = 0
		for c in output:
			if c == '(':
				cur += 1
			else:
				cur = 0
			ans = max(ans, cur)
		return ans

	def f_pair_in_a_row(n, output):
		cur = 0
		ans = 0
		last = 'a'
		for c in output:
			if c != last:
				cur += 1
			else:
				cur = 1
			if c == ')':
				ans = max(ans, cur // 2)
			else:
				ans = max(ans, (cur - 1) // 2)
			last = c
		return ans

	def f_pair(n, output):
		ans = 0
		last = 'a'
		for c in output:
			if c == ')' and last == '(':
				ans += 1
			last = c
		return ans


	problem = [
	('максимальное количество подряд идущих открывающих скобок \'(\'', f_open_in_a_row),
	('максимальное количество подряд идущих пар скобок \"()\"', f_pair_in_a_row),
	('количество пар скобок \"()\"', f_pair),
	]
	idx = randint(0, len(problem) - 1)
	template = '''Текстовый файл состоит не более чем из 1.000.000 символов ().
Определите {0}.
Для выполнения этого задания следует написать программу.
'''.format(problem[idx][0])
	return (template, problem[idx][1](n, output), str(output))

print(json.dumps(choice([generate_XYZ, generate_brackets])(choice(range(5 * 10 ** 5, 10 ** 6 - 1)))))