import random
import string
LETTERS = string.ascii_letters
NUMS = "01234568789"
SPE = "-+*%&$!"
SYMBOLS = LETTERS + NUMS + SPE
Len = int(input("ENTER PASS. LENGTH: "))
pass_no = int(input("ENTER No.(PASSWORD REQUIRE): "))

print(f"\nThere are your {Len} letter & {pass_no} Strong password is ready ")
i = 0
while i < (pass_no+1):
    password = "".join(random.sample(SYMBOLS, Len))
    print(f"({i+1})", password)
    i += 1
print()
