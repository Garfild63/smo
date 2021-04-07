import matrix
n = int(input("Введите количество состояний: "))
print("Введите таблицу интенсивностей потоков: ")
t = n * [n * [0]]
for i in range(n):
	t[i] = t[i].copy()
	arr = input().split(' ')
	for j in range(n):
		t[i][j] = int(arr[j])
am = n * [n * [0]]
bm = n * [[0]]
for i in range(n):
	am[i] = am[i].copy()
	bm[i] = bm[i].copy()
	for j in range(n):
		am[i][j] = 0
		if i == 0:
			bm[i][0] = 1
			am[i][j] = 1
		elif i == j:
			bm[i][0] = 0
			for k in range(n):
				if t[i][k] > 0:
					am[i][j] = am[i][j] + t[i][k]
		else:
			bm[i][0] = 0
			if t[j][i] > 0:
				am[i][j] = -t[j][i]
a = matrix.MatrixType(am)
b = matrix.MatrixType(bm)
c = b.divide(a)
print("Вероятности состояний: ")
for i in range(1, n + 1):
	print("p" + str(i) + "=" + str(c.elementAt(i, 1)))
