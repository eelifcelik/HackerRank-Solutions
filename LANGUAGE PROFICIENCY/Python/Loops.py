#The provided code stub reads and integer,n , from STDIN.
# For all non-negative integers i < n, print i**2 .

if __name__ == '__main__':
    n = int(input("n: "))

    list = []

    for i in range(n):
        list.append(i)

    for i in range(len(list)):
        print(i * i)
