#prompt user to input num1 and num2 values
#print num1 and num2 respectively
#introduce a third variable to have a fixed num1
#reassign num2 value to num1
#reassign third variable(same as original num1) value to num2
#print the new num1 and num2 respectively

num1=input("Enter a number: ")
num2=input("Entet a number: ")
print(num1)
print(num2)
#temporary value methodology refrenceed from blog
num_swap=num1

num1=str(num2)
num2=str(num_swap)
print(num1)
print(num2)