x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]

y = [1, -1, -1, -1]


w1 = 0
w2 = 0
b = 0

learning_rate = 1
epoch = 2

for i in range (epoch):
    print(f"__________EPOCH {i+1}_________")
    for j in range(len(x1)):
        yIn = b + x1[j] * w1 + x2[j] * w2
        if yIn > 0:
            yDash = 1
        elif yIn == 0:
            yDash = 0
        elif yIn < 0:
            yDash = -1
        

        if y[j] == yDash:
            wDelta1 = 0
            wDelta2 = 0
            bDelta = 0
        else:

            wDelta1 = learning_rate * x1[j] * y[j]
            wDelta2 = learning_rate * x2[j] * y[j]
            bDelta = learning_rate * y[j]

            w1 = w1 + wDelta1
            w2 = w2 + wDelta2
            b = b + bDelta
                
        print(f"y^: {yDash}\t|Delta_w1: {wDelta1}\t|Delta_w2: {wDelta2}\t|Delta_b: {bDelta}\t|w1: {w1}\t|w2: {w2}\t|b: {b}")


