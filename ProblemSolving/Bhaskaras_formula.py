import math
a, b, c = map(float, input().split())
ac4 = (b**2)-(4*a*c)

if a==0 or ac4<0: print("Impossivel calcular")
else:
    r1 = (-b+ac4**0.50)/(2*a)
    r2 = (-b-ac4**0.50)/(2*a)
    print("R1 = %.5f" % r1)
    print("R2 = %.5f" % r2)