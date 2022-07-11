import math

def integrate(f, a, b, n):
   """The integral of f(x) for x between a and b.
   Aproximated using the trapezoidal rule with n uniform subintervals."""
   assert n >= 1
   s = 0
   for i in range(n+1):
      xi = a + ( ( ( b - a ) * i ) / n )
      fx = f(xi)
      if i == 0 or i == n:
         s += fx
      else:
         s += 2*fx
   result = ((b-a)/(2*n))*s
   return result

def example(n):
   def f(x): return ( ( x - 2 ) / ( x + 3 ) )
   a = integrate(f, 0, 1, n)
   return a

test1 = example(100)
test2 = example(1000)
test1CodeCheck = -0.43841238771835106
test2CodeCheck = -0.43841038251353437
print("{} - {} - {}".format("Pass" if test1 == test1CodeCheck else "Fail", test1, test1CodeCheck))
print("{} - {} - {}".format("Pass" if test2 == test2CodeCheck else "Fail", test2, test2CodeCheck))