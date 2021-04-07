class MatrixType:
	def __init__(self, *args):
		if len(args) == 2:
			self.mx = args[0] * [args[1] * [0]]
			for i in range(args[0]):
				self.mx[i] = self.mx[i].copy()
			self.m = args[0]
			self.n = args[1]
		elif len(args) == 1:
			self.mx = args[0]
			self.m = self.height()
			self.n = self.width()
	
	def __str__(self):
		return str(self.mx)
		
	def height(self):
		return len(self.mx)

	def width(self):
		return len(self.mx[0])

	def withoutRowAndColumn(self, i, j):
		mx = self.mx.copy()
		mx.pop(i - 1)
		for k in range(len(mx)):
			mx[k] = mx[k].copy()
			mx[k].pop(j - 1)
		return MatrixType(mx)

	def elementAt(self, i, j):
		return self.mx[i - 1][j - 1]

	def minor(self, i, j):
		return self.withoutRowAndColumn(i, j).determinant()

	def algebraicComplement(self, i, j):
		return (-1) ** (i + j) * self.minor(i, j)

	def determinant(self):
		if self.width() == 1 and self.height() == 1:
			s = self.elementAt(1, 1)
		else:
			s = 0
			for j in range(1, self.width() + 1):
				s = s + (self.algebraicComplement(1, j) * self.elementAt(1, j))
		return s

	def transposed(self):
		mx = self.width() * [self.height() * [0]]
		for i in range(1, self.width() + 1):
			mx[i - 1] = mx[i - 1].copy()
			for j in range(1, self.height() + 1):
				mx[i - 1][j - 1] = self.elementAt(j, i)
		return MatrixType(mx)

	def union(self):
		mx = self.width() * [self.height() * [0]]
		for i in range(1, self.width() + 1):
			mx[i - 1] = mx[i - 1].copy()
			for j in range(1, self.height() + 1):
				mx[i - 1][j - 1] = self.algebraicComplement(j, i)
		return MatrixType(mx)
		
	def inverse(self):
		return self.union().divide(self.determinant())

	def multiply(self, arg):
		if isinstance(arg, int) or isinstance(arg, float):
			mx = self.mx.copy()
			for i in range(len(mx)):
				mx[i] = mx[i].copy()
				for j in range(len(mx[i])):
					mx[i][j] = mx[i][j] * arg
			return MatrixType(mx)
		elif isinstance(arg, MatrixType) and self.width() == arg.height():
			mx = self.height() * [arg.width() * [0]]
			for i in range(1, self.height() + 1):
				mx[i - 1] = mx[i - 1].copy()
				for j in range(1, arg.width() + 1):
					mx[i - 1][j - 1] = 0
					for k in range(1, self.width() + 1):
						mx[i - 1][j - 1] = mx[i - 1][j - 1] + self.elementAt(i, k) * arg.elementAt(k, j)
			return MatrixType(mx)
		
	def divide(self, arg):
		if isinstance(arg, int) or isinstance(arg, float):
			mx = self.mx.copy()
			for i in range(len(mx)):
				mx[i] = mx[i].copy()
				for j in range(len(mx[i])):
					mx[i][j] = mx[i][j] / arg
			return MatrixType(mx)
		elif isinstance(arg, MatrixType):
			return arg.inverse().multiply(self)
