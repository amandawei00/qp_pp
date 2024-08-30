import numpy as np

# hash functions map {0,1}^n --> {0,1}^m.
# compression rate: alpha = m/n

# takes bit-string n and converts to value in field F_2^(len(n))
def bit_to_dit(n):
    x = 0
    for i in range(len(n)):
        if n[i] != 0:
            x += np.power(2, len(n) - i - 1)
    
    return x

# compression rate: m/n <= 1/2, requires random seed of length n-m
# family of hash functions is indexed by r \in (R1,...,R_l-1), l=n/m, and R takes values in F_(2^m)
def f_f1(n, m, r):

    l = np.round(len(n)/m + 0.5)

    if len(r) != m*(l - 1):
        print("random seed is not of the correct length")
        return

    # if l does not evenly divide len(n), pad beginning with 0's
    pad_width = np.int32(l - len(n)%l)
    n = np.pad(n, (pad_width,0), 'constant')
    
    # split F_2^n bit-string into F_(2^m)^l string with characters in finite field F_(2^m)
    n = np.split(n, l)
    r = np.split(r, l-1)
    
    # convert 2^n bits into l 2^m-its
    n = np.array([bit_to_dit(n[i]) for i in range(len(n))])
    
    hashed = np.zeros((m,1))
    for i in range(len(n)):
        hashed[i] += # r_i1 * n1 + r_i2 * n2 + ... + nl
    return n


x = np.array([0,1,1,0,0,1,0,1,0,1,0])
print(f_f1(x, 4, np.array([1,2,1,3,1,])))
