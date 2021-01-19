x = 1.0;
y = 1.0;
s = 0.0;
n = int(input());
for i in range(n):
    s += x / (1 + abs(y));
    y += x;
    x *= 0.3;
print(s);