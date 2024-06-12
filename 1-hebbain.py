x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]
bIn = [1, 1, 1, 1]
y = [1, -1, -1, -1]

w1 = 0
w2 = 0
b = 0


for j in range(len(x1)):
    w1 = w1 + x1[j] * y[j]
    w2 = w2 + x2[j] * y[j]
    b = b + y[j]
    print(f"w1(new): {w1}\tw2(new): {w2}\tb(new): {b}")

print("final weghts: ",w1,w2,b)

print("testing the network: ") 
for j in range(len(x1)):
    y = x1[j] * w1 + x2[j] * w2 + bIn[j] *b 
    print("y= ",y)

print(f"Decision Boundary: {w1}x1 + {w2}x2 + ({b})b = 0")
