import unittest
from q2 import longestRange

class TestLongestRange(unittest.TestCase):
  def test_longest_range(self):
    # Caso de prueba con un arreglo de números enteros
    arr = [4, 7, 3, 2, 8, 1]
    expected = [1, 4]
    result = longestRange(arr)
    self.assertEqual(result, expected)
    
    # Caso de prueba con un arreglo de números enteros que contiene repetidos
    arr = [4, 4, 7, 3, 2, 2, 8, 1, 1]
    expected = [1, 4]
    result = longestRange(arr)
    self.assertEqual(result, expected)
    
    # Caso de prueba con un arreglo de números enteros que está ordenado
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    expected = [1, 9]
    result = longestRange(arr)
    self.assertEqual(result, expected)
    
    # Caso de prueba con un arreglo de números enteros que está ordenado en orden inverso
    arr = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    expected = [1, 9]
    result = longestRange(arr)
    self.assertEqual(result, expected)
    
    # Caso de prueba con un arreglo de números enteros que sólo contiene un elemento
    arr = [5]
    expected = [5, 5]
    result = longestRange(arr)
    self.assertEqual(result, expected)
    
    # Caso de prueba con un arreglo vacío
    arr = []
    expected = [0, 0]
    result = longestRange(arr)
    self.assertEqual(result, expected)
    
    
if __name__ == '__main__':
  unittest.main()