x1 = [1, 1, -1, -1]
x2 = [1, -1, 1, -1]

y = [1, -1, -1, -1]

w1 = 0.1
w2 = 0.1
b = 0.1

tE =0

learning_rate = 0.1
epoch = 5

for i in range (epoch):
    print(f"__________EPOCH {i+1}_________")
    for j in range(len(x1)):
        yIn = b + x1[j] * w1 + x2[j] * w2

        wDelta1 = learning_rate * (y[j] - yIn) * x1[j]
        wDelta2 = learning_rate * (y[j] - yIn) * x2[j]
        bDelta = learning_rate * (y[j] - yIn)

        w1 = w1 + wDelta1
        w2 = w2 + wDelta2
        b = b + bDelta

        e = (y[j] - yIn)**2

        tE += e 
        print(f"|Delta_w1: {round(wDelta1, 2)}\t\t|Delta_w2: {round(wDelta2, 2)}\t\t|Delta_b: {round(bDelta, 2)}\t\t|w1: {round(w1, 2)}\t\t|w2: {round(w2, 2)}\t\t|b: {round(b, 2)}\t\t|Error: {round(e, 1)}")

    print(f"Total Error: {round(tE)}")    
