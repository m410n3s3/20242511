# n = int(input())

# def fat(n):

#     if n==1: 
#         return 1
#     else:
#         return n*fat(n-1)



def FatorialInterativo(n):
    NumeroFatorial = 1
    for i in range (1,n):
        NumeroFatorial *= (i+1)
    return NumeroFatorial

def FibonacciInterativo(n):
    inicial = 0
    final = 1

    for i in range (n-1):
        inicial,final = final, inicial+final
    return final

def FibonacciRecursivo(n):
    if n<2:
        return n
    return FibonacciRecursivo(n-1)+FibonacciRecursivo(n-2)




if __name__=="__main__":
    n = int(input())
    print(f"O termo {n} da sequencia de Fibonacci é {FibonacciInterativo(n)}")
    print(f"{n} fatorial é {FatorialInterativo(n)}")
    print(f"O termo {n} da sequencia de Fibonacci é {FibonacciRecursivo(n)}")