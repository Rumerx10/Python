x, y, z = map(float, input().split())
if x+y>z and y+z>x and x+z>y:
    print('Perimetro = %.1f' %(x+y+z))
else: print('Area = %.1f' % ((x+y)/2*z))
