def fibonacchi(x):
    if x <= 2:
        return 1
    if x > 2:
        return fibonacchi(x - 1) + fibonacchi(x - 2)


print("Hello Samar")

for num in range(1, 35):
    print(f" {num} ==> {fibonacchi(num)}")
