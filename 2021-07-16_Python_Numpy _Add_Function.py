#Python program numpy.add() function
"ComputerPogrammingTutor,July16th,2021"

"py_maths"


import numpy as n1

arr1 = n1.array([[2,-7,5],[-6,2,0]])
arr2 = n1.array([[5,8,-5],[3,6,9]])
arr2 = n1.array([[20,7,5],[1,2,0]])
arr3 = n1.array([[5,8,6],[2,6,9]])
print("1st array: ",arr1)
print("2nd array: ",arr2)


arr = n1.add(arr1,arr2)
print("Output Added array : ",arr)

arr = n1.add(arr2,arr3)
print("Output Added array : ",arr)

