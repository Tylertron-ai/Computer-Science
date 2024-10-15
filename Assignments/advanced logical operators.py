# Amazon free shipping eligibility
# Prime customers OR purchase of over $25
# under 18, you need parent consent to purchase

def free_shipping(age, prime, cost, consent):
    if (prime == True or cost >= 25) and (age >= 18 or consent == True):
        print("Your all set")
    else:
        print("You must pay the shipping tax")

a = 15
p = False
cos = 18
con = True
free_shipping(p, cos, a, con)