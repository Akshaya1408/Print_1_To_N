def num(n):
    if n>0:
        num(n-1)
        print(n,end=" ")
    return " "
    
n=int(input())
print(num(n))