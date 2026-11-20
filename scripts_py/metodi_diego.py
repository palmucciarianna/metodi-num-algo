import numpy as np
import numpy.linalg as npl
import scipy.linalg as spl
import SolveTriangular as st

def metodo_bisezione(fname, a, b, tolx, tolf):
    
    fa = fname(a)
    fb = fname(b)

    if np.sign(fa) * np.sign(fb) >= 0:
        print("Impossibile applicare la bisezione")
        return None, None, None

    it = 0
    v_xk = []
    maxit = int(np.ceil(np.log(((b - a) / np.spacing(1))))) - 1

    while np.abs(b - a) > tolx:
        xk = a + (b-a)/2
        fxk = fname(xk)
        v_xk.append(xk)

        if fxk < tolf:
            return xk, it, np.array(v_xk) 
        
        if np.sign(fa) * np.sign(fxk) < 0:
            b = xk
            fb = fxk
        
        elif np.sign(fb) * np.sign(fxk) < 0:
            a = xk
            fa = fxk

        it += 1
    
    return xk, it, np.array(v_xk)

def falsi(fname, a, b, itmax, tolx, tolf):

    fa = fname(a)
    fb = fname(b)

    if np.sign(fa) * np.sign(fb) >= 0:
        print("Impossibile applicare la bisezione")
        return None, None, None

    it = 0
    v_xk = []
    fxk = tolf + 1

    while it < itmax and np.abs(b - a) > tolx and fxk > tolf:
        xk = a + fa*(b - a)/(fb - fa)
        fxk = fname(xk)
        v_xk.append(xk)

        if fxk < tolf:
            return xk, it, np.array(v_xk)
        
        if np.sign(fa) * np.sign(fxk) < 0:
            b = xk
            fb = fxk
        
        elif np.sign(fb) * np.sign(fxk) < 0:
            a = xk
            fa = fxk

        it += 1
    
    return xk, it, np.array(v_xk)

def corde(fname, m, x0, tolx, tolf, itmax):

    it = 1
    v_xk = []
    fx0 = fname(x0)
    d = fx0 / m
    x1 = x0 - d
    fx1 = fname(x1)
    v_xk.append(x1)

    while it < itmax and np.abs(fx1) > tolf and np.abs(d) >= tolx * np.abs(x1):

        x0 = x1
        fx0 = fname(x0)
        d = fx0/m

        x1 = x0 - d
        fx1 = fname(x1)
        v_xk.append(x1)

        it += 1

    return x1, it, np.array(v_xk)

def secanti(fname, xm1, x0, tolx, tolf, itmax):

    it = 1
    v_xk = []
    fx0 = fname(x0)
    fxm1 = fname(xm1)
    m = (fx0 - fxm1)/(x0 - xm1)
    d = fx0/m
    x1 = x0 - d
    fx1 = fname(x1)
    v_xk.append(x1)

    while it < itmax and np.abs(fx1) >= tolf and np.abs(d) >= np.abs(x1) * tolx:
        xm1 = x0
        x0 = x1
        fxm1 = fname(xm1)
        fx0 = fname(x0)
        
        m = (fx0 - fxm1)/(x0 - xm1)
        d = fx0/m
        x1 = x0 - d
        fx1 = fname(x1)
        v_xk.append(x1)

        it += 1
    
    return x1, it, np.array(v_xk)

def newton(fname, fpname, x0, tolx, tolf, itmax): # NEWTON MODIFICATO HA ANCHE m (molteplicità radice!)

    v_xk = []
    it = 1
    fx0 = fname(x0)
    fpx0 = fpname(x0)

    if np.abs(fpname(x0)) <= np.spacing(1):
        print("Derivata prima nulla")
        return None, None, None
    
    d = fx0/fpx0
    x1 = x0 - d # NEWTON MODIFICATO DIVENTA x0 - m*d
    fx1 = fname(x1)
    v_xk.append(x1)

    while it < itmax and np.abs(d) > np.abs(x1) * tolx and np.abs(fx1) > tolf:
        x0 = x1
        fx0 = fname(x0)
        fpx0 = fpname(x0)

        if np.abs(fpx0) < np.spacing(1):
            print("Derivata prima nulla")
            return None, None, None

        d = fx0/fpx0
        x1 = x0 - d # NEWTON MODIFICATO DIVENTA x0 - m*d
        fx1 = fname(x1)
        v_xk.append(x1)

        it += 1
    
    return x1, it, np.array(v_xk)

def stima_ordine(xk, iterazioni):
    
    k = iterazioni - 4
    pnum = np.log( np.abs(xk[k + 2] - xk[k + 3]) / np.abs(xk[k + 1] - xk[k + 2]) )
    pden = np.log( np.abs(xk[k + 1] - xk[k + 2]) / np.abs(xk[k + 1] - xk[k]) )

    return (pnum/pden)

def newtonSys(fun, jac, x0, tolx, tolf, itmax):
    
    errV = []
    matjac = jac(x0)
    matfun = fun(x0)

    if npl.det(matjac) == 0:
        print("Matrice jacobiana singolare")
        return None, None, None
    
    it = 1
    s = -npl.solve(matjac, matfun)
    x1 = x0 + s
    fx1 = fun(x1)

    errV.append(npl.norm(s, 1) / npl.norm(x1, 1))

    while it < itmax and npl.norm(fx1, 1) > tolf and npl.norm(s, 1) > npl.norm(x1) * tolx:
        
        x0 = x1
        matjac = jac(x0) # NELLE CORDE SI TOGLIE QUESTA LINEA DI CODICE, IN SHAMANSKII SI USA UN UPDATE OGNI it % num == 0 ITERAZIONI
        matfun = fun(x0)

        if npl.det(matjac) == 0:
            print("Matrice nel ciclo singolare")
            return None, None, None
        
        s = -npl.solve(matjac, matfun)
        x1 = x0 + s
        errV.append(npl.norm(s, 1) / npl.norm(x1, 1))
    
    return x1, it, errV

def newtonMin(gradiente, hess, x0, tolx, tolf, itmax):

    mathess = hess(x0)
    
    if npl.det(mathess) == 0:
        print("Matrice hessiana singolare")
        return None, None, None
    
    it = 1
    gradfx0 = gradiente(x0)
    s = -npl.solve(mathess, gradfx0)
    x1 = x0 + s
    gradfx1 = gradiente(x1)
    errV = []
    errV.append(npl.norm(s, 1))

    while it < itmax and npl.norm(gradfx1, 1) > tolf and npl.norm(s, 1) > tolx * npl.norm(x1, 1):
        x0 = x1
        mathess = hess(x0)
    
        if npl.det(mathess) == 0:
            print("Matrice hessiana singolare")
            return None, None, None
    
        it += 1
        gradfx0 = gradiente(x0)
        s = -npl.solve(mathess, gradfx0)
        x1 = x0 + s
        gradfx1 = gradiente(x1)
        errV.append(npl.norm(s, 1))
    
    return x1, it, errV

def jacobi(A, b, x0, toll, itmax):
    d = np.diag(A)
    n = A.shape[0]

    invM = np.diag(1/d) # M alla meno 1
    E = np.tril(A, -1) 
    F = np.triu(A, 1)
    N = -(E+F)

    T = invM @ N
    q = invM @ b

    autovalori = npl.eigvals(T)
    raggiospettrale = np.max( np.abs(autovalori) )
    if raggiospettrale > 1:
        print("Non converge")
        return None, None, None

    it = 0
    errV = []
    errore = toll + 1

    while it < itmax and errore >= toll:
        xk = T @ x0 + q

        errore = npl.norm(xk - x0) / npl.norm(xk)
        errV.append(errore)

        x0 = xk.copy()
        it += 1
    
    return xk, it, errV

def gaussSeidel(A, b, x0, toll, itmax):
    
    d = np.diag(A)
    D = np.diag(d)
    E = np.tril(A, -1)
    F = np.triu(A, 1)

    M = (D+E)
    invM = npl.inv(M)
    N = -F

    T = invM @ N
    q = invM @ b

    autovalori = npl.eigvals(T)
    raggiospettrale = np.max( np.abs(autovalori) )
    if raggiospettrale > 1:
        print("Non converge")
        return None, None, None
    
    it = 0
    errore = toll + 1
    errV = []

    while it < itmax and errore >= toll:
        xk = T @ x0 + q
        errore = npl.norm(xk - x0) / npl.norm(xk)
        errV.append(errore)

        x0 = xk.copy()
        it += 1
    
    return xk, it, errV

def gaussSeidelSOR(A, b, x0, toll, itmax, omega): # omega ottimale tra 0 < w < 2
    d = np.diag(A)
    D = np.diag(d)
    E = np.tril(A, -1)
    F = np.triu(A, 1)
    Momega = D + omega * E
    Nomega = (1 - omega) * D - omega * F
    
    T = npl.inv(Momega) @ Nomega
    q = npl.inv(Momega) @ (omega * b)
    it = 0

    autovalori = npl.eigvals(T)
    raggiospettrale = np.max( np.abs(autovalori) )
    if raggiospettrale > 1:
        print("Non converge")
        return None, None, None
    
    it = 0
    errore = toll + 1
    errV = []
    xold = x0.copy()
    xnew = x0.copy()

    while it < itmax and errore >= toll:
        xnew = T @ xold + q
        errore = npl.norm(xnew -xold) / npl.norm(xnew)
        errV.append(errore)
        xold = xnew.copy()
        it += 1
    
    return xnew, it, errV

def steepestDescent(A, b, x0, itmax, toll):
    
    n,m = A.shape
    if n != m:
        print("Matrice non quadrata")
        return None, None, None, None
    
    x = x0
    r = A @ x - b
    p = -r
    it = 0
    errore = npl.norm(r) / npl.norm(b)
    
    solV = []
    solV.append(x)
    errV = []
    errV.append(errore)

    while errore >= toll and it < itmax:
        
        Ap = A @ p
        alpha = - (r.T @ p) / (p.T @ Ap)
        x = x + alpha*p
        solV.append(x)                      # NEL CONIUGATO QUI MI SALVO rold = r.copy()
        r = r + alpha*Ap                    # POI CALCOLO GAMMA gamma = (r.T @ r) / (rold.T @ rold)
        errore = npl.norm(r) / npl.norm(b)
        errV.append(errore)
        p = -r                              # QUI DIVENTA p = -r + gamma*p
        it += 1
    
    return x, errV, solV, it

def eqnorm(A, b):
    
    G = A.T @ A
    f = A.T @ b

    L = spl.cholesky(G, lower=True) # G = L @ L.T
    U = L.T

    y, flag = st.Lsolve(L, f) # Ly = f
    if flag == 0:
        x, flag = st.Usolve(U, y) # Ux = y
    else:
        print("E' esploso tutto")
        return None
    
    return x

def QRLS(A, b):

    n = A.shape[1]
    Q,R = spl.qr(A)
    
    h = Q.T @ b
    h1 = h[:n]
    h2 = h[n:]
    R1 = R[:n,:]

    x, flag = st.Usolve(R1,h1)
    residuo = npl.norm(h2)**2

    return x, residuo

def SVDLS(A, b):
    
    m,n = A.shape
    U, s, VT = spl.svd(A) # ritorna U, il vettore diagonale della matrice sigma e V.T
    V = VT.T
    
    tresh = np.spacing(1) * m * s[0]
    k = np.count_nonzero(s > tresh) # rango = numero di valori singolari non nulli 

    d = U.T @ b
    d1 = d[:k].reshape(k,1)
    d2 = d[k:].copy()
    s1 = s[:k].reshape(k,1) # gli altri valori sono da scartare in quanto nulli (nel senso di macchina)

    c = d1 / s1
    x = V[:,:k] @ c
    residuo = npl.norm(d2)**2

    return x, residuo

def plagr(xnodi, j): 

    xzeri = np.zeros_like(xnodi)
    n = xnodi.size

    if j == 0:
        xzeri = xnodi[1:n]
    else:
        xzeri = np.append(xnodi[:j],xnodi[j+1:n]) # escludo il nodo j dal polinomio di Lagrange
    
    num = np.poly(xzeri) # costruisce il polinomio Produttoria(xi - xk) con k diverso da i
    den = np.polyval(num, xnodi[j])
        
    return (num/den)

def interpL(x, y, xx): # x sono i nodi, y i valori dei nodi e xx i punti dove calcolare il polinomio
        
    n = x.size
    m = xx.size
    L = np.zeros((m,n)) # matrice valutazione del polinomio

    for j in range(n):
        p = plagr(x, j)
        L[:,j] = np.polyval(p, xx) # tutta la colonna j diventa il valore del polinomio di Lagrange

    return L @ y # ricorda che l'errore è dato dalla costante di Lebesque


