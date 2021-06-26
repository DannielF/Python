import sys #bookcase

# def fibonacci_recursive(n):
#     if n == 0 or n == 1:
#         return 1
#     return fibonacci_recursive(n - 1) + fibonacci_recursive(n -2)

def fibonacci_dynamic(n, memo = { }):
    if n == 0 or n == 1:
        return 1

    try: #mecanismo de control de flujo
        return memo [n] #return n and if not ⬇
    except KeyError: #catch into keyerror
        result = fibonacci_dynamic(n - 1, memo) + fibonacci_dynamic(n - 2, memo)
        memo [n] = result
    return result    

if __name__ == "__main__":
    sys.setrecursionlimit(10001) #change recursion limit
    n = int(input('Choose a number: '))
    result = fibonacci_dynamic(n)
    # result = fibonacci_recursive(n)
    print(result)
