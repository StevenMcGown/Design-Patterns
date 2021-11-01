import math
import random

from random import randint as rand
from math import gcd, sqrt, floor

def isPrime(x):
    if x == 2:
        return True
    elif x < 2:
        return False
    else:
        #Save computation by only testing the sqrt of the range of x
        for i in range(2,floor(sqrt(x))+1):
            #if the modulus of x%i is 0, that means it is not prime
            if (x % i) == 0:
                return False
        return True

#inverse of an integer such that a*x is congruent to 1
def modInv(e, phi):
    for x in range(1, phi):
        if (e * x) % phi == 1:
            return x
    return None

#verifies if keys were generated correctly
def verify(e,d,phi):
    print("Verify: (" + str(e) + "*" + str(d) + ")%" + str(phi) + "=" + str((e*d)%phi))
    if((e * d) % phi == 1):
        print("Keys generated correctly")
    else:
        print("Keys were not generated correctly")

def genKeys():
    while(True):
        maxByte = 4
        try:
            byteLength = int(input("Please input a prime number length greater than 1 and less than or equal to " + str(maxByte) + "\n"))
        except ValueError:
            print("Invalid input")
            continue
        if byteLength >= maxByte + 1 or byteLength < 2:
            print("Prime number length must be greater than 1 and less than " + str(maxByte + 1))
            continue
        print("Generating keys...")
        #minimum and maximum range of prime numbers
        minPr = 0
        maxPr = int(math.pow(10,byteLength)) 
        cached_primes = [i for i in range(minPr,maxPr) if isPrime(i)]
        #pick random prime numbers
        p = random.choice([i for i in cached_primes if minPr < i < maxPr])
        q = random.choice([i for i in cached_primes if minPr < i < maxPr])
        n = p*q
        #calculate the totient
        totient = (p-1)*(q-1)
        #public key e has to be greater than 1 and less than the totient and gcd(e,totient) = 1
        #e = random.choice([i for i in cached_primes if 1 < i < totient and gcd(i,totient)==1])       
        e = 113
        #private key d is calculated using the extended euclidean algorithm
        d = modInv(e,totient)

        print("p: ", end = str(p) + "\n")
        print("q: ", end = str(q) + "\n")
        print("n: ", end = str(n) + "\n")
        print("totient (phi): ", end = str(totient) + "\n")
        print("e: ", end = str(e) + "\n")
        print("d: ", end = str(d) + "\n")
        verify(e,d,totient)
        pubKey = (e,n)
        privKey = (d,n)
        print("public key: " + str(pubKey))
        print("private key: " + str(privKey))
        return(pubKey,privKey)
        break

def parse(message):
    keys = genKeys()
    n = 2
    split = [message[i:i+n] for i in range(0, len(message), n)]
    intMsg = 0
    byteCount = 0
    for x in split:
        print("\n")
        print("BYTES " + str(byteCount*8) + "-" + str((byteCount*8)+len(x)-1) + "'" + x + "'")
        print("BLOCKSIZE = " + str(len(x)))
        byteCount += 1
        count = 0
        for y in x:
            intMsg += ord(y) * pow(256, count)
            print(y + "\t" + str(ord(y)) + "\t" + "\t" + str(intMsg))
            count+=1

        c = encrypt(keys[0], intMsg)
        p = decrypt(keys[1], c)
        intMsg = 0


def encrypt(key, messageInt):
    #indexes 0 and 1 are e and n resepctively
    #pow(base, exponent, modulus)
    print("Encrypting message...")
    print("MESSAGE AS INTEGER:\t" + str(messageInt))
    encrypted = pow(messageInt, key[0]) % key[1]
    print("Encrypted message:\t" + str(encrypted))
    return(encrypted)

def decrypt(key, cipher):
    print("Decrypting message...")
    dec = pow(cipher, key[0], key[1])
    print("DECRYPTED:\t" + str(dec))

print("Welcome to the RSA Encryption Algorithm")

m = input("Enter a message to be encrypted:")


print(parse(m))