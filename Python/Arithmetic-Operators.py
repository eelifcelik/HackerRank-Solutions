#The provided code stub reads two integers from STDIN, a and b . Add code to print three lines where:

#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input("a: "))
    b = int(input("b: "))


    sum = a+b
    print(sum)

    difference = a-b
    print(difference)

    prod = a*b
    print(prod)
