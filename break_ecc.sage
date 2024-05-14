import gencurve

curve, Q = gencurve.generate_ecdlp(32)
G = curve.gen(0)

print("\nCracking Q")
time dl = discrete_log(Q, G, G.order(), operation='+')
print(f"Found Private Key: {dl}")

print(f"Verifying with key*generator point: {dl*G}")
assert dl*G == Q
print(f"Assertion Success")