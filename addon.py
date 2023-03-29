Python 3.10.8 (tags/v3.10.8:aaaf517, Oct 11 2022, 16:50:30) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import pandas as pd
>>> x=pd.Series([1,2,3,4,5])
>>> print(x)
0    1
1    2
2    3
3    4
4    5
dtype: int64

>>> import numpy as np
>>> x=np.array([[1,2],[2,3]])
>>> y=np.array([[2,2],[3,3]])
>>> z=x+y
>>> print(z)
[[3 4]
 [5 6]]
>>> import matplotlib.pyplot as a
>>> a.plot([1,2,3,4])
[<matplotlib.lines.Line2D object at 0x000002AD0E7A47C0>]
>>> a.show()
