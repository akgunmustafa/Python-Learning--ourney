# Enumerate

a=1

names = ['Tyler', 'Dias', 'Cory', 'Cameron']
for i, e in enumerate(names, start=3):
    print(i, "indexing : ", e)

# Zip()

sale_price = [3500.00, 76300.00, 67200.00]
cost_price = [2445.00, 45789.00, 12256.00]
for s, c in zip(sale_price, cost_price):
    profit = s - c
    print(f'Total profit : {profit}')
