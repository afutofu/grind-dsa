def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fast_fib(n)["curr"]


def fast_fib(n):
    if n == 2:
        return {"prev": 1, "curr": 1}
    else:
        fib = fast_fib(n - 1)
        return {"prev": fib["curr"], "curr": fib["prev"] + fib["curr"]}


if __name__ == "__main__":
    for i in range(10):
        print(fib(i))
