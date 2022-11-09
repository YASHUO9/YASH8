def power(a,n):
   sum = 1
   if n==0:
      return sum
   sum*=a
   return sum*power(a,n-1)

z =  power(5,5)
print(z)