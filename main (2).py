import random
import sympy

def primenumber(y):
    while True:
        n = random.randint(2**(y-1), 2**y)
        if sympy.isprime(n):
            return n

def totient(p, q):
    return (p-1)*(q-1)

def e_func(totient):
    while True:
        e = random.randint(2, totient)
        if sympy.gcd(e, totient) == 1:
            return e

def d_func(totient, e):
    d = 0
    while (d*e) % totient != 1:
        d += 1
    return d

def encrypt(m, e, n):
    return pow(m, e, n)

def decrypt(c, d, n):
    return pow(c, d, n)

def main():
    p = primenumber(512)
    q = primenumber(512)
    n = p*q
    totient_val = totient(p, q)
    public_key = e_func(totient_val)
    private_key = d_func(totient_val, public_key)
    print("p =", p)
    print("q =", q)
    print("n =", n)
    print("totient =", totient_val)
    print("public key (e) =", public_key)
    print("private key (d) =", private_key)
    
    plaintext = random.randint(1, n)
    ciphertext = encrypt(plaintext, public_key, n)
    
    print("plaintext (m) =", plaintext)
    print("ciphertext (c) =", ciphertext)
    decrypted_text = decrypt(ciphertext, private_key, n)
    print("decrypted text =", decrypted_text)

main()
  
      