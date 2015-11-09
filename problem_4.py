##using only two digit numbers, or three digit numbers, create a full matrix
##of potential products
array1 = range(1000,0,-1)
array2 = array1

productList = []

for num1 in array1:
    for num2 in array2:
        daProduct = num1*num2
        productList.append(daProduct)

##sort productList from big to small
orderedProductList = sorted(productList, reverse = True)
    
##test each number to see if palindrome. Loop breaks after first success.

for number in orderedProductList:
    if str(number) == str(number)[::-1]:
        print str(number) + " is a palindrome."
        break
    else:
        pass