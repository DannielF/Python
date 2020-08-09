#funcion recursiva / exponencial O(2**n) ya que se llama otra dos veces por llamada
def bag(size_bag, weight, values, n): # n es el indice
    if n == 0 or size_bag == 0:
        return 0
    print(n)# muestra como se recorren los indices
    if weight [n -1] > size_bag:
        return bag(size_bag, weight, values, n - 1) # n - 1 indica revisar el siguiente indice
        
    return max(values[n -1] + bag(size_bag - weight[n - 1], weight, values, n - 1),
                bag(size_bag, weight, values, n - 1))        

if __name__ == "__main__":
    values = [60, 120, 100]
    weight = [10, 30, 20]
    size_bag = 50
    n = len(values)
    

    result = bag(size_bag, weight, values, n)
    print(result)