from random import randint, choice
import json

def strep(output, size = -1, pairs=0):
	result = ''
	if size != -1:
		result += str(size) + ' '
	result += str(len(output)) + '\n'
	for x in output:
		if pairs == 0:
			result += str(x) + '\n'
		else:
			result += str(x[0]) + ' ' + str(x[1]) + '\n'
	return result

def generate_pairs(n):
	output = []
	for i in range(n):
		output.append((randint(1, 5000), randint(1, 5000)))
	binary = ['', ' не']
	mod = [2, 3, 5]
	func = [('максимально', lambda s, x: max(s, x), -100), ('минимально', lambda s, x: min(s, x), 10 ** 10)]
	a = choice(binary)
	b = choice(mod)
	c = choice(func)
	template = '''Имеется набор данных, состоящий из пар положительных целых чисел.
Необходимо выбрать из каждой пары ровно одно число так, чтобы сумма
всех выбранных чисел{0} делилась на {1} и при этом была {2}
возможной. Гарантируется, что искомую сумму получить можно.
Программа должна напечатать одно число – {2} возможную
сумму, соответствующую условиям задачи.

Даны два входных файла (файл A и файл B), каждый из которых содержит
в первой строке количество пар N (1 ≤ N ≤ 100000). Каждая из следующих
N строк содержит два натуральных числа, не превышающих 5000.
'''.format(a, b, c[0])
	
	def f(output, a, b, c):
		cur = 0
		mods = [c[2]] * b
		for i in range(n):
			best = c[1](output[i][0], output[i][1])
			other = output[i][0] + output[i][1] - best
			cur += best
		if a == '':
			forward_mod = (best - other) % b
			if other > best:
				forward_mod = (other - best) % b
			mods[forward_mod] = c[1](mods[forward_mod], other - best)
			if cur % b == 0:
				return [cur]
			if mods[cur % b] == c[2]:
				return list(generate_pairs(n))
			assert mods[cur % b] != c[2]
			return [cur + mods[cur % b]]
		if cur % b != 0:
			return [cur]
		bst = c[2]
		for i in range(1, b):
			bst = c[1](bst, mods[i])
		if bst == c[2]:
			return list(generate_pairs(n))
		assert bst != c[2]
		return [cur + bst]
	ans = f(output, a, b, c)
	if len(ans) == 1:
		return (template, ans[0], strep(output, pairs=1))
	return ans

def generate_subsets(n):
	output = []
	for i in range(n):
		output.append(randint(-5000, 5000))
	binary = ['', ' не']
	mod = [2, 3, 5]
	a = choice(binary)
	b = choice(mod)
	template = '''Имеется набор данных, состоящий из целых чисел.
Необходимо выбрать некоторое подмножество чисел так, чтобы сумма
всех выбранных чисел{0} делилась на {1} и при этом была максимально
возможной. Гарантируется, что искомую сумму получить можно.
Программа должна напечатать одно число – максимально возможную
сумму, соответствующую условиям задачи.

Даны два входных файла (файл A и файл B), каждый из которых содержит
в первой строке количество пар N (1 ≤ N ≤ 100000). Каждая из следующих
N строк содержит целое число от -5000 до 5000.
'''.format(a, b)
	
	def f(output, a, b):
		cur = 0
		mods = [-(10 ** 10)] * b
		for i in range(n):
			if output[i] > 0:
				cur += output[i]
				mods[output[i] % b] = max(mods[output[i] % b], -output[i])
			else:
				mirror_mod = (b - output[i] % b) % b
				mods[mirror_mod] = max(mods[mirror_mod], output[i])
		if a == '':
			if cur % b == 0:
				return [cur]

			if mods[cur % b] == -(10 ** 10):
				return tuple(generate_subsets(n))
			assert mods[cur % b] != -(10 ** 10)
			return [cur + mods[cur % b]]
		if cur % b != 0:
			return [cur]
		bst = -(10 ** 10)
		for i in range(1, b):	
			bst = max(bst, mods[i])
		if bst == -(10 ** 10):
			return list(generate_subsets(n))
		assert bst != -(10 ** 10)
		return [cur + bst]
	ans = f(output, a, b)
	if len(ans) == 1:
		return (template, ans[0], strep(output))
	return ans
print(json.dumps(choice([generate_subsets, generate_pairs])(choice(range(16, 22)))))
