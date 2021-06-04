import unittest
import matrix

class TestMatrix(unittest.TestCase):

	def test_eq(self):
		self.assertFalse(matrix.MatrixType([[4, 2, -1], [3, 2, 2], [1, -3, 1]]) == matrix.MatrixType([[4, 2, -1], [3, -2, 2], [1, -3, 1]]))

	def test_withoutRowAndColumn(self):
		with self.assertRaises(Exception) as context:
			matrix.MatrixType([[3, 2, -4], [2, -7, 0], [4, -1, 4], [3, 2, -4], [0, 0, 1]]).withoutRowAndColumn(2, 4)
		self.assertEqual(str(context.exception), 'Координаты вне диапазона матрицы')

	def test_elementAt(self):
		with self.assertRaises(Exception) as context:
			matrix.MatrixType([[3, 2, -4], [2, -7, 0], [4, -1, 4], [3, 2, -4], [0, 0, 1]]).withoutRowAndColumn(-2, 2)
		self.assertEqual(str(context.exception), 'Координаты вне диапазона матрицы')

	def test_determinant(self):
		with self.assertRaises(Exception) as context:
			matrix.MatrixType([[3, 2, -4], [2, -7, 0], [4, -1, 4], [3, 2, -4], [0, 0, 1]]).determinant()
		self.assertEqual(str(context.exception), 'Нельзя вычислить определитель неквадратной матрицы')

	def test_add(self):
		with self.assertRaises(Exception) as context:
			matrix.MatrixType([[4, -1], [3, 2]]).add(matrix.MatrixType([[-1, 5, 6], [0, 1, 7]]))
		self.assertEqual(str(context.exception), 'Матрицы должны быть одного размера')

	def test_subtract(self):
		with self.assertRaises(Exception) as context:
			matrix.MatrixType([[4, -1], [3, 2]]).subtract(matrix.MatrixType([[-1, 5], [0, 1], [6, 7]]))
		self.assertEqual(str(context.exception), 'Матрицы должны быть одного размера')

	def test_multiply(self):
		with self.assertRaises(Exception) as context:
			matrix.MatrixType([[2, 1, 3], [0, -1, 8]]).multiply(matrix.MatrixType([[-3, 4], [2, -2]]))
		self.assertEqual(str(context.exception), 'Ширина первого множителя должна быть равна высоте второго множителя')

	def test_divide(self):
		with self.assertRaises(Exception) as context:
			matrix.MatrixType([[16, -4], [12, 8]]).divide(0)
		self.assertEqual(str(context.exception), 'division by zero')

if __name__ == "__main__":
	unittest.main()
