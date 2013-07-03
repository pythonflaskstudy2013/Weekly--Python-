filename = "portfolio.csv"
portfolio = []
for line in open(filename):
    fields = line.split(",")
    name = fields[0]
    shares = int(fields[1])
    price = float(fields[2])
    stock = (name,shares,price)
    portfolio.append(stock)

def total():
    total = 0.0
    for name, shares, price in portfolio:
        total += shares * price
    return(total)
