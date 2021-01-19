a = 1;
b = 1;
k = 2;
c = True;
while (b < 100):
    k += 1;
    b += a;
    a = b - a;
    c = True;
    for i in range(2, b//2):
        if (b%i == 0):
            c = False;
    if (c):
       print("Element #" + str(k) + ": " + str(b));