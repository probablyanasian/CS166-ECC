"""
Adapted From: https://github.com/brichard19/ecdl/blob/master/scripts/gencurve.sage

Sage script for generating an elliptic curve over a prime field
of the given bit size. The curve has a prime order. A generator
of the group and a random element are also selected.
"""


def generate_ecdlp(bits, filename):
    print("Generating " + str(bits) + "-bit curve")

    curve, a, b, n, p = generate_curve(bits)
    g = curve.gens()
    q = curve.random_element()
    gx = g[0][0]
    gy = g[0][1]
    qx = q.xy()[0]
    qy = q.xy()[1]

    print("Modulus: " + str(p))
    print("a:       " + str(a))
    print("b:       " + str(b))
    print("order:   " + str(curve.order()))
    print("G:      (" + str(gx) + "," + str(gy) + ")")
    print("Q:      (" + str(qx) + "," + str(qy) + ")")
    exit()


def randint(low, high):
    return low + int((high - low) * random())


def generate_curve(bits):
    low = 2 ^ (bits - 1) + 1
    high = 2 ^ (bits) - 1
    p = next_prime(randint(low, high))
    field = GF(p)

    while True:
        a = randint(1, p)
        b = randint(1, p)
        curve = EllipticCurve(field, [a, b])
        order = curve.order()
        if order < p and order > low and order in Primes():
            return curve, a, b, order, p
