meat = "chicken"
drink = "Diet-Coke"
Rice = "Jollof"
Salad = "Coslaw"

order = f'your order: \n2pcs of {meat}\n1lrg {drink}\n3spn of {Rice}\n{Salad}\n'
customer = "Kofi"
message = f"Hello {customer}...\n\n{order}\nthanks for buying "

print (message) 

with open("oderlog.txt", "a") as f:
    f.write(order)

print('Order logged to file.')