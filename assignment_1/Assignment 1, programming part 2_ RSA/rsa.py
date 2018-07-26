def rsaencrypt(value, n, e):
    return ( pow(value, e, n) );

def rsadecrypt(code, n, d):
    return ( pow(code, d, n) );

def mInverse(a, n):
    r0, r1, t0, t1 = n, a, 0, 1
    while r1 > 1:
        q = r0 // r1
        r2 = r0 - r1 * q
        t2 = t0 - t1 * q
        r0, r1 = r1, r2
        t0, t1 = t1, t2
 
    if r1 == 1:
        return t1 % n
    return 0

def rsahack(n, e):
    i=2;
    while (n % i != 0):
        i+=1;
    else:
        p = i;
        q = n // p;
        x = (p-1)*(q-1);
    d = mInverse(e, x);
    return d;