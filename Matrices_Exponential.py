import numpy as np #using numpy, we can convert lists to arrays, which will be easier to work with

def matrix_mult(m, y): #m is the matrix you're multiplying by, y is the multiple
    if type(y)==list: #you're multiplying two lists/matrices
        array1=np.array(m) #convert the first list to an array
        array2=np.array(y) #convert the second list to an array
        checkRows=array2.shape #get the shape of the first array
        checkColumns=array1.shape #get the shape of the second array
        if checkColumns[1] != checkRows[0]: #if the number of columns in the first array does not equal the rows in the second arrat
            return "Sorry, these matrices cannot be multiplied" 
        else: #the columns of the first array do match the rows in the second
            finalMat=array1.dot(array2) #get the dot product
            return finalMat

    if type(y)== int or type(y)== float: #you're multiplying the matrix by a scalar
        matList=[]
        for j in m: #go through the rows
            newList=[]
            for i in range(0, len(j)): #go through the columns
                    val=j[i] * y #multiply each item by the scalar
                    newList.append(val) #add the product to a new list (this will be the columns in the new array)
            matList.append(newList) #creates the separate rows in the list
        newMat=np.array(matList) #convert the list to an array
        finalMat=np.reshape(matList, (len(m), len(j))) #make sure the new array has the same dimensions as the original m list
        return finalMat




def exp_by_squaring(x, n): #x is the base number, n is the exponent
    if n ==0: #if the exponent is 0
        return 1 #the result is one
    elif n % 2==0: #if the exponent is even
        return exp_by_squaring(x*x, n/2) #this is a recursive algorithm, x is multiplied by itself and raised to the power of n/2
    else: #if the exponent is odd
        return x* exp_by_squaring(x*x, (n-1)/2) #x is multiplied by itself and raised to the power of n-1 divided by 2
    

newList=[[1, 2, 3, 4], [1, 2, 3, 4]]
list2=[[1, 2], [3,4], [1,2], [3,4]]

#print(matrix_mult(newList, 2)) driver code, test if matrix_mult works with a scalar

#print(matrix_mult(newList, list2)) driver code, test if matrix_mult works with two matrices

#print(exp_by_squaring(2, 20)) driver code, test if exp_by_squaring works

numRows=input("How many rows in the first matrix? ")
numColumns=input("How many columns in the first matrix? ")
userMatrix=[]
for j in range (0, int(numRows)): #go through the rows
            uList=[]
            for i in range(0, int(numColumns)): #go through the columns
                    uNum=input("Add a value to the array ")
                    uList.append(float(uNum))
            userMatrix.append(uList) #creates the separate rows in the list

scalMat=input("Enter 0 to multiply by a number, 1 to multiply by another matrix ")

while(scalMat!="0" and scalMat !="1"):
     scalMat=input("Invalid input, please try again ") #if the user inputs something other than a 0 or a 1, they cannot move on

if scalMat=="0":
     multiplier=float(input("Enter the multiplier "))
     print("Your final matrix is: ", matrix_mult(userMatrix, multiplier))
else:
     multiplierRows=input("How many rows in the second matrix? ")
     mutliplierColumns=input("How many columns in the second matrix? ")
     mMatrix=[]
     for x in range(0, int(multiplierRows)): #go through the rows
            mList=[]
            for i in range(0, int(mutliplierColumns)): #go through the columns
                    mNum=input("Add a value to the array ")
                    mList.append(float(mNum)) #add the product to a new list (this will be the columns in the new array)      
            mMatrix.append(mList)
     print("Your final matrix is: ", matrix_mult(userMatrix, mMatrix))

userBase=input("What is your base number? ")
userExp=input("What power would you like to raise the base to? ")
print("Your product is ", exp_by_squaring(float(userBase), float(userExp)))

     
            


     
     

