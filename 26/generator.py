from random import randint, choice
import json

def strep(output, size = -1):
	result = ''
	if size != -1:
		result += str(size) + ' '
	result += str(len(output)) + '\n'
	for x in output:
		result += str(x) + '\n'
	return result

def generate_max_subset(n):
	output = [0] * n
	for i in range(n):
		output[i] = randint(1, 10000)
	size = randint(50000, 200000)
	def f_max(output, size):
		arr = sorted(output)
		cnt = 0
		sum = 0
		for x in arr:
			if x + sum > size:
				break
			cnt += 1
			sum += x
		mx_w = arr[cnt - 1]
		for i in range(cnt, n):
			if arr[i] <= size - sum + arr[cnt - 1]:
				mx_w = arr[i]
		return [cnt, mx_w]

	def f_min(output, size):
		arr = sorted(output)[::-1]
		cnt = 0
		sum = 0
		for x in arr:
			if x + sum > size:
				break
			cnt += 1
			sum += x
		return [cnt, arr[0]]

	options = [
	('максимальное', f_max),
	('минимальное', f_min)
	]
	option = choice(options)
	template = '''Системный администратор раз в неделю создаёт архив пользовательских
файлов. Однако объём диска, куда он помещает архив, может быть меньше,
чем суммарный объём архивируемых файлов.
Известно, какой объём занимает файл каждого пользователя.
По заданной информации об объёме файлов пользователей и свободном
объёме на архивном диске определите {0} число пользователей,
чьи файлы можно сохранить в архиве, а также максимальный размер
имеющегося файла, который может быть сохранён в архиве, при условии,
что сохранены файлы максимально возможного числа пользователей.

Входные данные.
В первой строке входного файла находится число N – количество пользователей (натуральное число, не превышающее
1000). В следующих N строках находятся элементы последовательности (все числа натуральные, не превышающие 10000), каждое
в отдельной строке.'''.format(option[0])
	return (template, option[1](output, size), strep(output, size=size))


def generate_moda(n):
	output = [0] * n
	for i in range(n):
		output[i] = randint(1, 100)

	def f_median(output):
		arr = sorted(output)
		if len(arr) % 2 == 1:
			return arr[len(arr) // 2]
		return (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) / 2

	def f_moda(output):
		arr = sorted(output)
		max_cnt = 0
		cur_cnt = 0
		last = arr[0] - 1
		ans = last
		for x in arr:
			if x > last:
				cur_cnt = 0
			cur_cnt += 1
			if max_cnt <= cur_cnt:
				max_cnt = cur_cnt
				ans = x
			last = x
		return ans

	def f_clip(output):
		arr = sorted(output)[5:-5]
		return sum(arr) / len(arr)

	def f_unique(output):
		arr = sorted(output)
		last = -1
		ans = 0
		for x in arr:
			if x != last:
				ans += 1
			last = x
		return ans

	options = [
	('медиану последовательности (https://ru.wikipedia.org/wiki/%D0%9C%D0%B5%D0%B4%D0%B8%D0%B0%D0%BD%D0%B0_(%D1%81%D1%82%D0%B0%D1%82%D0%B8%D1%81%D1%82%D0%B8%D0%BA%D0%B0)', f_median),
	('самый часто встречающийся элемент (если есть несколько самых частых — самый большой по значению)', f_moda),
	('среднее арифметическое для всех чисел последовательности, кроме 5 наименьших и 5 наибольших', f_clip),
	('количество различных чисел в последовательности', f_unique)
	]
	option = choice(options)
	template = '''Вам дана последовательность из N чисел. От вас требуется найти {0}.

Входные данные.
В первой строке входного файла находится число N – количество элементов последовательности (натуральное число, не превышающее 1000). В следующих N строках находятся значения объёмов файлов каждого пользователя (все числа натуральные, не превышающие 100), каждое в отдельной строке.'''.format(option[0])
	return (template, option[1](output), strep(output))

print(json.dumps(choice([generate_moda, generate_max_subset])(choice(range(700, 1000)))))