import numpy as np

# hash functions map {0,1}^n --> {0,1}^m.
# compression rate: alpha = m/n


# compression rate: m/n <= 1/2, requires random seed of length n-m
# family of hash functions is indexed by r \in (R1,...,R_l-1), l=n/m, and R takes values in F_(2^m)
def f_f1(n, m, r):
    l = np.round(len(n)/m + 0.5)

    # if l does not evenly divide len(n), pad beginning with 0's
    pad_width = np.int32(l - len(n)%l)
    n = np.pad(n, (pad_width,0), 'constant')
    # split a F_2^n bit-string into F_(2^m)^l string with characters in finite field F_(2^m)
    n_split = np.split(n, l)
    
    return n_split


n_test = np.array([0,1,0,0,1,1,1,0,1,0,1,1,1])
print(f_f1(n_test, 5, np.array([])))
    
