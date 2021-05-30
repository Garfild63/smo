class MatrixType:
	def __init__(self, *args):
		if len(args) == 2:
			self.mx = args[0] * [args[1] * [0]]
			for i in range(args[0]):
				self.mx[i] = self.mx[i].copy()
		elif len(args) == 1:
			self.mx = args[0]
	
	def __str__(self):
		return str(self.mx)
		
	def height(self):
		return len(self.mx)

	def width(self):
		return len(self.mx[0])

	def withoutRowAndColumn(self, i, j):
		if (i - 1) in range(self.height()) and (j - 1) in range(self.width()):
			mx = self.mx.copy()
			mx.pop(i - 1)
			for k in range(self.height()):
				mx[k] = mx[k].copy()
				mx[k].pop(j - 1)
			return MatrixType(mx)
		else:
			raise Error

	def elementAt(self, i, j):
		if (i - 1) in range(self.height()) and (j - 1) in range(self.width()):
			return self.mx[i - 1][j - 1]
		else:
			raise Error

	def minor(self, i, j):
		return self.withoutRowAndColumn(i, j).determinant()

	def algebraicComplement(self, i, j):
		return (-1) ** (i + j) * self.minor(i, j)

	def determinant(self):
		if self.width() != self.height():
			raise Error
		if self.width() == 1:
			s = self.elementAt(1, 1)
		else:
			s = 0
			for j in range(self.width()):
				s = s + (self.algebraicComplement(1, j + 1) * self.elementAt(1, j + 1))
		return s

	def transposed(self):
		mx = self.width() * [self.height() * [0]]
		for i in range(self.width()):
			mx[i] = mx[i].copy()
			for j in range(self.height()):
				mx[i][j] = self.elementAt(j + 1, i + 1)
		return MatrixType(mx)

	def union(self):
		mx = self.width() * [self.height() * [0]]
		for i in range(self.width()):
			mx[i] = mx[i].copy()
			for j in range(self.height()):
				mx[i][j] = self.algebraicComplement(j + 1, i + 1)
		return MatrixType(mx)
		
	def inverse(self):
		return self.union().divide(self.determinant())

	def multiply(self, arg):
		if isinstance(arg, int) or isinstance(arg, float):
			mx = self.mx.copy()
			for i in range(self.height()):
				mx[i] = mx[i].copy()
				for j in range(self.width()):
					mx[i][j] = mx[i][j] * arg
			return MatrixType(mx)
		elif isinstance(arg, MatrixType):
			if self.width() != arg.height():
				raise Error
			mx = self.height() * [arg.width() * [0]]
			for i in range(self.height()):
				mx[i] = mx[i].copy()
				for j in range(arg.width()):
					mx[i][j] = 0
					for k in range(self.width()):
						mx[i][j] = mx[i][j] + self.elementAt(i + 1, k + 1) * arg.elementAt(k + 1, j + 1)
			return MatrixType(mx)
		
	def divide(self, arg):
		if isinstance(arg, int) or isinstance(arg, float):
			mx = self.mx.copy()
			for i in range(self.height()):
				mx[i] = mx[i].copy()
				for j in range(self.width()):
					mx[i][j] = mx[i][j] / arg
			return MatrixType(mx)
		elif isinstance(arg, MatrixType):
			return arg.inverse().multiply(self)
