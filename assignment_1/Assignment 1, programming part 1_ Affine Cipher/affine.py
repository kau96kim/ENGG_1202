def afencode (c, a, b):
    ans="";
    for t in c:
        if (ord( t ) >= ord( 'a' ) and ord( t ) <= ord( 'z' )):
            num = (a*(ord(t)-ord('a'))+b)%26;
            ans += chr(num+ord('a'));
        elif (ord( t ) >= ord( 'A' ) and ord( t ) <= ord( 'Z' )):
            num = (a*(ord(t)-ord('A'))+b)%26;
            ans += chr(num+ord('A'));
        else:
            ans += t;
    return ans;
    
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

def afdecode (c, a, b):
    ans="";
    inverse = mInverse(a, 26);
    for t in c:
        if (ord( t ) >= ord( 'a' ) and ord( t ) <= ord( 'z' )):
            num = (inverse*(ord(t)-b-ord('a')))%26;
            ans += chr(num+ord('a'));
        elif (ord( t ) >= ord( 'A' ) and ord( t ) <= ord( 'Z' )):
            num = (inverse*(ord(t)-b-ord('A')))%26;
            ans += chr(num+ord('A'));
        else:
            ans += t;
    return ans;