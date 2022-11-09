key = int(input("Enter the number:"))

def main(n):
    if n==0:
        return n
    else:
        return main(n-1)+n
    
    
print(main(key))