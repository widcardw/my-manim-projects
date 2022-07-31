

def exp_continued_fraction(z,iterations=10):
    f = iterations-1
    for i in range(iterations-1,1,-1):
        f = z/(2-f,i-1+f)[i%2==0]
    return 1/(1-f)


def exp_continued_fraction2(z,iterations=10):
    iterations=iterations-1
    f = 2*(2*iterations-1)*(2*iterations+1)
    for i in range(iterations-1,1,-1):
        f = (2*i-3)*(2*i+1)*z**2/(2*(2*i-1)*(2*i+1)+2*z+f)
    f = 3*z**2/(2*(1*3)+2*z+f)
    return 1/(1-z+f)


def log_continued_fraction(z,iterations=10):
    z=z-1
    f = iterations
    for i in range(iterations-1,1,-1):
        f = int(i/2)**2*z/(i+f)
    return z/(1+f)


def tan_continued_fraction(z,iterations=10):
    f = 2*iterations-1
    for i in range(iterations-1,0,-1):
        f = 1/((2*i-1)/z-f)
    return f


def cot_continued_fraction(z,iterations=10):
    f = 2*iterations+1
    for i in range(iterations-1,0,-1):
        f = 1/((2*i+1)/z-f)
    return 1/z-f


def sin_continued_fraction(z,iterations=20):
    f = (2*iterations-2)*(2*iterations-1)-z**2
    for i in range(iterations-1,2,-1):
        f = (2*i-4)*(2*i-3)*z**2/((2*i-2)*(2*i-1)-z**2+f)
    f = z**2/(2*3-z**2+f)
    return z/(1+f)


def cos_continued_fraction(z,iterations=20):
    f = (2*iterations-3)*(2*iterations-2)-z**2
    for i in range(iterations-1,2,-1):
        f = (2*i-5)*(2*i-4)*z**2/((2*i-3)*(2*i-2)-z**2+f)
    f = z**2/(2-z**2+f)
    return 1/(1+f)


def atanh_continued_fraction(z,iterations=20):
    f = 2*iterations-1
    for i in range(iterations-1,1,-1):
        f = (i-1)**2*z**2/(2*i-1-f)
    return z/(1-f)


def tanh_continued_fraction(z,iterations=10):
    f = 2*iterations-1
    for i in range(iterations-1,0,-1):
        f = 1/((2*i-1)/z+f)
    return f


def atan_continued_fraction(z,iterations=20):
    f = 2*iterations-1
    for i in range(iterations-1,1,-1):
        f = (i-1)**2*z**2/(2*i-1+f)
    return z/(1+f)


def sqrt_continued_fraction(z,iterations=10):
    f = 2
    for i in range(iterations-1,1,-1):
        f = 2+(z-1)/f
    return 1+(z-1)/f


def asinh_continued_fraction(z,iterations=10):
    return 0


def asinh_continued_fraction(z,iterations=20):
    f = 2*iterations-1
    for i in range(iterations-1,3,-1):
        a = 2*int(i/2)-1
        f = a*(a+1)/(2*i-1+f)
    f = 2*z**2/(5+f)
    f = 2*z**2/(3+f)
    return z/(1+f)
