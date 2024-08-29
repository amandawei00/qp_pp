# to do still:
# 1. somehow insert tracker to keep track of how many iterations of binary was called. What parity information about what sets of bits have been made available to eve?


import numpy as np

# in: x, n-bit string (numpy array)
# out: 0 or 1 (parity of x)

def par(x):
    return np.sum(x) % 2

# only when a parity disagreement is detected in block i is binary called. This is basically a binary search algorithm to find an error. Errors are detected only when it produces parity 1. This means even bit flips may go undetected
# Alice's x stays unchanged, while Bob's is corrected

# in: x, Alice's i'th block
#     y, Bob's i'th block
# out: y', Bob's corrected block 
# missing feature: i, indices of corrected bits

def binary(n, x, y):
    if par(x) == par(y):
        return y
    # stopping condition
    if n <= 1:
        return x
    else:
        y = np.concatenate(binary(len(x[:n//2]),x[:n//2],y[:n//2]),binary(len(x[n//2:]), y[n//2:])))
        return y

# method to add noise
# in: arr, n-bit string passed as array
#     per, percent error to add (default 2%)
# out: n-bit array which differs from arr by per %

def add_noise(arr, per=0.02):
    err_num = np.round(per * len(arr))
    pos = np.int32(np.round(np.random.rand(np.int32(np.round(err_num))) * len(arr)))
    for i in range(len(pos)):
        arr[pos[i]] = (arr[pos[i]] + 1) % 2

    return arr


# method to generate random n-bit string with probability dist. {p, 1-p}
# in: n, length of string to be generated
#     p, probability of seeing bit 0. default is even distribution
# out: n-bit string with entropy H(p)

def bitstring(n, p=0.5):
    string = np.concatenate((np.zeros(np.int32(np.round(n*p))), np.ones(np.int32(np.round(n*p)))))
    np.random.shuffle(string)
    return string

# in: QBER, used to determine first block size
#     x, y: Alice and Bob's raw keys
#     kfrac: determines block size of first pass
#     passes: number of passes (default: 4)
# out: xout, yout, Alice and Bob's keys after information reconciliation. Ideally, the keys are perfectly correlated, Xout=Yout=W)

def cascade(qber, x, y, kfrac=0.73, passes=4):
    k = round(kfrac/qber + 0.5) # block size for first pass
    for i in range(passes):
        # Alice and Bob split their bit strings
        xarr = np.split(x, np.arange(0, len(x), k))[1:]
        yarr = np.split(y, np.arange(0, len(y), k))[1:]

        # Alice and Bob calculate and compare parities for each section
        xarr_par = np.array([par(xarr[i]) for i in range(len(xarr))])
        yarr_par = np.array([par(yarr[i]) for i in range(len(yarr))])

        for j in range(len(xarr_par)):
            if xarr_par[j] != yarr_par[j]:
                yarr[i] = binary(len(xarr[j]), xarr[j], yarr[j])

        
        y = np.concatenate(yarr)
        k *= 2
    return y



# use bitstring to generate n-bit string
# x = bitstring(1000)
# print(x)

# use add_noise to generate Bob's string, which is almost Alice's + some noise (given by qber)
# y = add_noise(x, 0.02)

# call cascade
# cascade(0.02, x, y)

