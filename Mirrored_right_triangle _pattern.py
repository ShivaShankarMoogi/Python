total_rows = int(input("Enter a Number : "))
for rows in range(1,total_rows+1):
    for spaces in range(1,(total_rows - rows)+1):
        print(" ",end = " ")
    for symbol in range(1,rows+1):
        print("*",end = " ")
    print()

