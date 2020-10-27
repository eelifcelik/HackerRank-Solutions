#The included code stub will read an integer, , from STDIN.

#Without using any string methods, try to print the following: 12....n

if __name__ == '__main__':
    n = int(input("n: "))

    string = ""

    for i in range(n):
        string = string + str(i + 1)

    print(string)




