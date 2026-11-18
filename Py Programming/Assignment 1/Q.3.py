amount = float(input("Enter order amount: Rs "))
membership = input("Are you a member? (yes/no): ").lower()

if amount <0 or amount>100000:
    print("Invalid Order Amount")
else:
    if amount >= 5000:
        discount =15

    elif amount >= 2000 and membership == "yes":
        discount = 10

    else:
        discount= 0

    discount_amount = amount * discount / 100
    final_amount = amount - discount_amount

    print("Original Amount: Rs ", amount)
    print("Discount Percentage:", discount, "%")
    print("Discount Amount: Rs ", discount_amount)
    print("Final Payable Amount: Rs ", final_amount)

    if discount > 0:
        print("Eligibility Status: Eligible for discount")
    else:
        print("Eligibility Status: Not eligible for discount")