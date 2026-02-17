def to_be_paid(bill_amount ,amount_amount):
    duo=bill_amount-amount_amount
    return max( duo, 0 )
bill=int(input("Enter a bill amount:$"))
payment=int(input("Enter a payment amountL:$"))
duo = to_be_paid(bill, payment)
print(f"The total amount is to be paid is{duo}")