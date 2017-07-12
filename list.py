#Python program to insert an element before each element of a list

num=['1','2','3','4']
print('original list:',num)
num=[v for edit in num for v in('no.',edit)]
print('updtaed list:',num)

