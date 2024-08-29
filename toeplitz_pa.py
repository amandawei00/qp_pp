# privacy amplificaiton, referencing the protocol presented in "High Speed and Large Scale Privacy Amplification Scheme for QKD by Tang, B. Y. et al 2019

# in: a, n-bit random seed string
#     r, calculated finall key length

def get_toeplitz(a, r):
    tmat = np.empty((r, len(a)-r))
    for i in range(len(tmat)):
        for j in range(len(tmat[i])):
            tmat[i][j] = a[j-i+r-1]

    return tmat


# returns modified toeplitz matrix, eq.1 in tang2019
def mod_toeplitz(a, r):
    return np.concatenate((np.identity(r), get_toeplitz(a, len(a), r)), axis=1)

# in: w, weakly secure key, length n
#     r, final length,
#     seed, random seed of length n-1
#     m, sub-block size

def toeplitz_pa(w, r, seed, m):
    return
