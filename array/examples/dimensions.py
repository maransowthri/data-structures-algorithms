from array import array as arr
from numpy import array as nparr

arrInt1D = arr('i', [1, 2, 3, 4, 5])
arrFloat1D = arr('d', [1.3, 2.3, 3.5, 4.2, 5.6])
print(arrInt1D)
print(arrFloat1D)

arrInt2D = nparr([[0, 1], [2, 3]])
print(arrInt2D)