import unittest
import matrix

class TestMatrix(unittest.TestCase):

	def test_eq(self):
		self.assertTrue(matrix.MatrixType([[4, 2, -1], [3, -2, 2], [1, -3, 1]]) == matrix.MatrixType([[4, 2, -1], [3, -2, 2], [1, -3, 1]]))

	def test_height(self):
		self.assertEqual(matrix.MatrixType([[3, 2, -4], [2, -7, 0], [4, -1, 4], [3, 2, -4], [0, 0, 1]]).height(), 5)

	def test_width(self):
		self.assertEqual(matrix.MatrixType([[3, 2, -4], [2, -7, 0], [4, -1, 4], [3, 2, -4], [0, 0, 1]]).width(), 3)

	def test_withoutRowAndColumn(self):
		self.assertEqual(matrix.MatrixType([[3, 2, -4], [2, -7, 0], [4, -1, 4], [3, 2, -4], [0, 0, 1]]).withoutRowAndColumn(2, 3),
			matrix.MatrixType([[3, 2], [4, -1], [3, 2], [0, 0]]))

	def test_elementAt(self):
		self.assertEqual(matrix.MatrixType([[3, 2, -4], [2, -7, 0], [4, -1, 4], [3, 2, -4], [0, 0, 1]]).elementAt(3, 2), -1)

	def test_minor(self):
		self.assertEqual(matrix.MatrixType([[1, 3, -2], [4, 1, 0], [2, -1, 4]]).minor(3, 2), 8)

	def test_algebraicComplement(self):
		self.assertEqual(matrix.MatrixType([[-5, 4, 1], [1, -2, 3], [0, 6, 2]]).algebraicComplement(2, 3), 30)

	def test_determinant(self):
		self.assertEqual(matrix.MatrixType([[-5, 4, 1], [1, -2, 3], [0, 6, 2]]).determinant(), 108)

	def test_transposed(self):
		self.assertEqual(matrix.MatrixType([[-1, 3, 1, 0], [5, 7, -2, 4]]).transposed(), matrix.MatrixType([[-1, 5], [3, 7], [1, -2], [0, 4]]))

	def test_union(self):
		self.assertEqual(matrix.MatrixType([[1, 1, 1], [1, 2, 3], [1, 3, 6]]).union(), matrix.MatrixType([[3, -3, 1], [-3, 5, -2], [1, -2, 1]]))

	def test_negate(self):
		self.assertEqual(matrix.MatrixType([[-5, 4, 1], [1, -2, 3], [0, 6, 2]]).negate(), matrix.MatrixType([[5, -4, -1], [-1, 2, -3], [0, -6, -2]]))

	def test_add(self):
		self.assertEqual(matrix.MatrixType([[4, -1], [3, 2]]).add(matrix.MatrixType([[-1, 5], [0, 1]])), matrix.MatrixType([[3, 4], [3, 3]]))

	def test_subtract(self):
		self.assertEqual(matrix.MatrixType([[4, -1], [3, 2]]).subtract(matrix.MatrixType([[1, -5], [0, -1]])), matrix.MatrixType([[3, 4], [3, 3]]))

	def test_inverse(self):
		self.assertEqual(matrix.MatrixType([[1, 1, 1], [1, 2, 3], [1, 3, 6]]).inverse(), matrix.MatrixType([[3, -3, 1], [-3, 5, -2], [1, -2, 1]]))

	def test_multiply(self):
		self.assertEqual(matrix.MatrixType([[4, -1], [3, 2]]).multiply(4), matrix.MatrixType([[16, -4], [12, 8]]))
		self.assertEqual(matrix.MatrixType([[2, 1], [0, -1]]).multiply(matrix.MatrixType([[-3, 4], [2, -2]])), matrix.MatrixType([[-4, 6], [-2, 2]]))

	def test_divide(self):
		self.assertEqual(matrix.MatrixType([[16, -4], [12, 8]]).divide(4), matrix.MatrixType([[4, -1], [3, 2]]))
		self.assertEqual(matrix.MatrixType([[12], [-7], [-10]]).divide(matrix.MatrixType([[4, 2, -1], [3, -2, 2], [1, -3, 1]])),
			matrix.MatrixType([[1], [3], [-2]]))

if __name__ == "__main__":
	unittest.main()
