import math
n = 576.98
notes = [100, 50, 20, 10, 5, 2]
coins = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print("NOTAS:")
for x in notes:
    if n >= x:
        note = math.floor(n/x)
        print("%d nota(s) de R$ %d.00" % (note, x))
        n = round(n - note * x,2)
    else: print("0 nota(s) de R$ %d.00" % x)
print("MOEDAS:")
for x in coins:
    if n >= x:
        coins = math.floor(n/x)
        print("%d moeda(s) de R$ %.2f" % (coins, x))
        n = round(n - coins*x,2)
    else: print("0 moeda(s) de R$ %.2f" % x)
