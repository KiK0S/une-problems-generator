from random import randint, choice
import json

def generate(n):
	l = randint(1000, 5000)
	r = l + n

	def f_two(n):
		cnt = 0
		for i in range(2, n):
			if i * i > n:
				break
			if n % i == 0:
				cnt += 1
				if n // i != i:
					cnt += 1
		return cnt == 2

	def f_one(n):
		cnt = 0
		for i in range(2, n):
			if i * i > n:
				break
			if n % i == 0:
				cnt += 1
				if n // i != i:
					cnt += 1
		return cnt == 1

	def f_primes(n):
		cnt = 0
		for i in range(2, n):
			if i * i > n:
				break
			if n % i == 0:
				return False
		return True

	def f_not_squares(n):
		cnt = 0
		for i in range(2, n):
			if i * i > n:
				break
			if n % i == 0:
				if (n // i) % i == 0:
					return False
		return True

	def f_ascending_digits(n):
		last = 10
		copy = n
		while copy > 0:
			x = copy % 10
			copy //= 10
			if last < x:
				return False
			last = x
		return True

	def f_odd_digits(n):
		copy = n
		while copy > 0:
			x = copy % 10
			copy //= 10
			if x % 2 == 0:
				return False
		return True

	m_7 = randint(0, 3)
	m_8 = randint(8, 16)
	def f_div_7(n):
		copy = n
		while copy > 0:
			x = copy % m_8
			copy //= m_8
			if x == m_7:
				return True
		return False

	options = [
		('имеющие ровно два различных натуральных делителя, не считая единицы и самого числа', f_two), 
		('имеющие ровно один натуральный делитель, не считая единицы и самого числа', f_one),
		('которые являются простыми', f_primes),
		('не делящиеся на вторую степень какого-либо числа, кроме единицы', f_not_squares),
		('все цифры которых расположены в порядке неубывания', f_ascending_digits),
		('все цифры которых нечетные', f_odd_digits),
		('которые содержат цифру {0}, если записать их в системе счисления с основанием {1}'.format(m_7, m_8), f_div_7),
	]
	option = choice(options)
	red_fs = [
		('сумма', lambda s, x: s + x, 0),
		('сумма цифр', lambda s, x: s + sum(map(int, list(str(x)))), 0),
		('количество', lambda s, x: s + 1, 0),
		('максимум среди', lambda s, x: max(s, x), 0),
		('минимум среди', lambda s, x: min(s, x), 10 ** 10)
	]
	red_f = choice(red_fs)
	template = '''Напишите программу, которая ищет среди целых чисел, принадлежащих
числовому отрезку [{0}; {1}], числа, {2}. Ответом на задачу будет {3} найденных чисел. 
'''.format(l, r, option[0], red_f[0])
	s = red_f[2]
	for x in range(l, r + 1):
		if option[1](x):
			s = red_f[1](s, x)
	assert s != red_f[2]
	return (template, s, '')

print(json.dumps(generate(choice(range(10000, 30000)))))