def km_m(unit1):
    ans = float(num1) * 1000

def m_cm(unit1):
    ans = float(num1) * 100

def cm_mm(unit1):
    ans = float(num1) * 10

def mm_km(unit1):
    ans = float(num1) * 1 * (10 ** -5)

while True:
    print("""
    Hi! Welcome to the unit converter app.
    What would you like to convert?
    """)
    cat = input("We support (L)ength, (W)eight, (T)emperature and (Ti)me").lower()

    if cat == "l":
        unit1 = input("From: ").lower()
        unit2 = input("To: ").lower()
        val = input("Enter your value: ")