import math
import secrets

bits = 64  # abuse global
message = "A faster GPU can process more frames per second."
e = 7


def miller_rabin(
    n: int, rounds: int = 40
) -> bool:  # http://stackoverflow.com/questions/6325576/how-many-iterations-of-rabin-miller-should-i-use-for-cryptographic-safe-primes
    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2
    for _ in range(rounds):
        a = secrets.randbelow(n - 1)
        while a <= 2:
            a = secrets.randbelow(n - 1)
        x = pow(a, d, n)
        for _ in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != n - 1:
                return False
            x = y
        if y != 1:
            return False
    return True


def gen_probable_prime() -> int:  # using Miller-Rabin test
    while True:
        t_p = secrets.randbits(bits)
        valid = True
        if t_p % 2 == 0:
            continue  # 2 is factor, retry
        if miller_rabin(t_p):
            return t_p


def mult_inverse(e, n):
    t = 0
    new_t = 1
    r = n
    new_r = e

    while new_r != 0:
        quotient = r // new_r
        t, new_t = new_t, t - quotient * new_t
        r, new_r = new_r, r - quotient * new_r

    if r > 1:
        return "Unable to invert"
    if t < 0:
        t = t + n
    return t


while True:
    p = gen_probable_prime()  # 7
    q = gen_probable_prime()  # 11

    n = p * q

    totient = (p - 1) * (q - 1)

    d = mult_inverse(e, totient)
    if type(d) == int:
        break

    print("Uninvertable, Retrying")

print(f"Generating a {bits} bit RSA keypair")
print(f"Secrets: {d=}, {p=}, {q=}")
print(f"{n=}, {e=}")

n_bits = int(math.log(n, 2))
print(f"n is {n_bits} bits long")
split_len = n_bits // 8  # split into chunks less than n has bits, 8 bit ascii
split_message = [
    int.from_bytes(bytes(message[i : i + split_len], encoding="ascii"))
    for i in range(0, len(message), split_len)
]

for m in split_message:
    encrypted = pow(m, e, n)
    print(f"Encrypted Message: {encrypted}")
    decrypted = pow(encrypted, d, n)
    print(f"Decrypted Message: {decrypted}")
    unencoded = decrypted.to_bytes(length=split_len).decode("ascii")
    print(f"Unencoded Message: {unencoded}")
