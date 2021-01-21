def isPrime(n):
    for i in range(2, n//2):
        if (n%i == 0):
            return False;
    return True;

n = int(input());
for i in range(n, 2*n - 1):
    if (isPrime(i) & isPrime(i+2)):
        print(str(i) + " " + str(i+2));
