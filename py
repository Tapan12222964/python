arr1=[5,7,8,4]
arr2=[2,1,3,4]
arr3=[10,3,7,1]
zipped1= zip(arr1,arr2)
zipped2= zip(arr1,arr2,arr3)
zipped3= zip(arr1,zipped1)
for index,value in enumerate(zipped1):
    print(index,value)
for index,value in enumerate(zipped2):
    print(index,value)
for index,value in enumerate(zipped3):
    print(index,value)