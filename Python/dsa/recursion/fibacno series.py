def fibannico(n):
    if n==1 or n==2:
        return 1
    facc_1 = fibannico(n-1)
    facc_2 = fibannico(n-2)
    output = facc_1 +facc_2
    return output
    
    
    
print(fibannico(1))