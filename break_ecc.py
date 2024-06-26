

# This file was *autogenerated* from the file break_ecc.sage
from sage.all_cmdline import *   # import sage library

_sage_const_32 = Integer(32); _sage_const_0 = Integer(0)
import gencurve

curve, Q = gencurve.generate_ecdlp(_sage_const_32 )
G = curve.gen(_sage_const_0 )

print("\nCracking Q")
__time__ = cputime(); __wall__ = walltime(); dl = discrete_log(Q, G, G.order(), operation='+'); print("Time: CPU {:.2f} s, Wall: {:.2f} s".format(cputime(__time__), walltime(__wall__)))
print(f"Found Private Key: {dl}")

print(f"Verifying with key*generator point: {dl*G=}")
assert dl*G == Q
print(f"Assertion Successful: Private Key Found")

