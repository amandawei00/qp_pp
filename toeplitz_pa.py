# simple privacy amplification protocol using the modified Toeplitz matrix, as described in appendix B in Hayashi2016

# the security of this method of PA is determined by the min-entropy of the random seed r, H_min(R)=h

# for large seed key lengths, the vector/matrix multipliation can be optimized to O(n log n) with FFT

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
#     m, final string length

def toeplitz_pa(w, r, seed):
    return np.matmul(mod_toeplitz(seed, r), w) 
