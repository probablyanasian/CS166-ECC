import gencurve

curve, _ = gencurve.generate_ecdlp(32)
G = curve.gen(0)

A = randint(0, curve.order())
B = randint(0, curve.order())

print("") # Newline
print(f"A's Private Key: {A=}")
A_pub = A*G
print(f"A's Public Key A*G: {A_pub=}")

print("")
print(f"B's Private Key: {B=}")
B_pub = B*G
print(f"B's Public Key B*G: {B_pub=}")

print("")
print(f"Shared key A_priv*B_pub: {A*B_pub=}")
print(f"Shared key B_priv*A_pub: {B*A_pub=}")

assert A*B_pub == B*A_pub
print("Assertion Successful: Shared Key Matches")