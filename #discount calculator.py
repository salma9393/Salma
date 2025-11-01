#discount calculator
#>10000-->30%
#5000-->20%
#1000-->10%
#<=1000-->0%
amount=15000
if amount>10000:
    discount=amount*0.3
elif amount>5000:
    discount=amount*0.2
elif amount>1000:
    discount=amount*0.1
else:
    amount=0

final_amount=amount+discount
print(final_amount)