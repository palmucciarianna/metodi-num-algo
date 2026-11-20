#import
    import numpy as np
    import numpy.linalg as npl
    import matplotlib.pyplot as plt
    import scipy.linalg as spl
    import SolvTriangular as ST
#Zeri di Funzione (Bisezione, Falsa Pos, Corde, Newton, Newton Modificato, Secanti)
   
    #Condizioni per non applicabile
        #Bisezione | Falsa_Pos
            if np.sign(fa)*np.sign(fb)>=0
        #(Corde)
            if np.abs(coeff_ang) <= np.spacing(1):
        #Newton | Newton Modificato
            if np.abs(fpxk)<=np.spacing(1)
        #Secanti
            if np.abs(c_ang_k)<=np.spacing(1)

    #Condizioni di arresto
        #Bisezione
            while np.abs(b - a) > tolx#to do #l'intervallo non è troppo piccolo
        #False_Pos
            while it < maxit  and np.abs(fxk) > tolf and errore > tolx
        #Corde | Newton | Newton Modificato | Secanti
            while it<nmax and  erroref>=tolf and errorex>=tolx

    #Assegnamento valori
        #Bisezione
            xk = a+(b-a)/2#to do
        #Falsa_Pos
            xk = a-fa*(b-a)/(fb-fa)#to do
        #Corde
            d=fxk/coeff_ang# to do    
        #Newton | Ne wton Modificato
            d=fxk/fpxk#to do
        #Secanti
            c_ang_k = (fxk-fxkm1)/(xk-xkm1)
            d=fxk/c_ang_k#to do 
        #Corde | Newton | Secanti
            xk1=xk-d#to do
        #Newton Modificato
            x1=xk-m*d#to do

    #Aggiornamento valori alla fine di un iterazione
        #Bisezione / Falsa_Pos
            if  np.sign(fxk)*np.sign(fb)>=0 #to do   #la radice si trova nell'intervallo [a, xk].
                b = xk
                fb=fxk
            elif np.sign(fxk)*np.sign(fa)>=0#to do   #la radice si trova nell'intervallo [xk, b].
                a = xk
                fa=fxk 
        #Secanti
            xm1=x0#to do 
            x0=x1#to do

    #Calcolo Errore
        #Falsa_Pos
            if xk!=0:
                errore= np.abs(xk-xprec)/np.abs(xk)#to do
            else:
                errore=np.abs(xk-xprec)#to do
        #Corde | Newton | Newton Modificato | (Secanti)
            if xk1!=0:
                errorex=np.abs(d)/np.abs(xk1)#to do 
           else:
                errorex=np.abs(d)#to do
        

#Soluzione di sistemi di equazioni non lineari (Newton Raphson, Newton Raphson Corde, Newton Raphson Sham)

    #Condizioni per non applicabile
        #Newton Raphson | Raphson Corde |Rpahson Sham
            if np.linalg.det(jx) == 0:#to do
                
    #Condizioni di arresto
        #Newton Raphson | Raphson Corde | Raphson Sham
            while it<max_iterations and erroreF>= tolF and erroreX >= tolX:

    #Assegnamento valori
        #Newton Raphson | Raphson Corde | Raphson Sham
            jx = np.array(J_numerical(X[0], X[1], dtype=float)#to do                          
            fx = np.array(F_numerical(X[0], X[1], dtype=float)#To do                
            s = np.linalg.solve(jx, -fx)#to do         
            Xnew = X + s#to do

    #Aggiornamento valori alla fine di un iterazione
        #Newton Raphson | Raphson Crode | Raphson Sham
            if normaXnew !=0:
                erroreX=np.linalg.norm(s,1)/normaXnew#to do 
            else:
                erroreX=np.linalg.norm(s,1)#to do 
        #Newton Raphson | Raphosn Corde | Raphson Sham
            fxnew=np.array(F_numerical(Xnew[0], Xnew[1], dtype=float).squeeze()#to do

#Metodi Diretti per solzuione di sistemi di eqauzioni lineari (Gauss LUsolve, QR QRsolve, Cholesky CHSolve)

    #LUsolve (P ottenuto da spl.lu() è PT quindi PT.T)
        def LUsolve(P, L, U, b):             
            pb = P@b   
            y, flag = ST.Lsolve(L, pb)    
            
            if flag == 0:            
                x, flag = ST.Usolve(U, y)    
            
            return x, flag
    #QRsolve
        def QRsolve(Q,R,b):
            y=Q.T@b
            xqr,flag = ST.Usolve(R,y)
        
            return xqr,flag
            
    #CHsolve
        def CHsolve(L,b):
            LT = L.T
            
            z,flag = ST.Lsolve(L,b)

            if flag == 0:
                x, flag =ST.Usolve(LT,z)
                
            return x

#Metodi Iterativi basati sullo splitting della matrice( Jacobi, Gauss Seidel,  Gauss Seidel SOR)
            
    #Inizializzazione dei valori
        #Jacobi | Gauss Siedel | Gauss Siedel SOR
            d=np.diag(A)#to do 
            D=np.diag(d)#to do
            E=np.tril(A,-1)#to do 
            F=np.triu(A,1)#to do            
            raggiospettrale=np.max(np.abs(autovalori))#to do     
            
        #Jacobi
            M=D
            N=-(E+F)#to do
            
        #Gauss Siedel | Gauss Siedel SOR
            M=D+E#to do 
            N=-F#to do
        
        #Jacobi | Gauss Siedel 
            invM = np.inv(M) # to do
            T=invM@N#to do

        #Gauss Siedel SOR
            invMomemga = np.linalg.inv(Momega)
            T=invMomemga@Nomega
            
    #Condizioni di arresto
        #Jacobi | Gasus Siedel | Gauss Siedel SOR
            while it< it_max and errore >=toll:
                
    #Assegnamento valori nell'iterazione
        #Jacobi
            x=(b+N@x0)/d.reshape(n,1)#to do 

        #Gauss Siedel
            x,_=ST.Lsolve(M,b-F@x0)#to do 

        #Gauss Siedel SOR
            xtilde, _= ST.Lsolve(M,b-F@x0)#to do 
            x=(1-omega)*x0+omega*xtilde#to do  

    #Errore
        #Jacobi | Gauss Siedel | Gauss Siedel SOR
            errore=np.linalg.norm(x-x0)/np.linalg.norm(x)#to do 

#Metodi di Discesa (Steep Descent, Conjugate Gradient)

    #Inizializzazione dei valori
        #Steep Descent | Conjugate Gradient
            r = A@x-b#to do 
            p = -r#to do
            errore =np.linalg.norm(r)/nb#to do

    #Assegnamento valori nell'iterazione
        #Steep Descent |Conjugate Gradient
            Ap=A@p#to do 
            alpha = -(r.T@p)/(p.T@Ap)# to do                
            x = x + alpha*p#to do 
            r=r+alpha*Ap#to do  
            errore =np.linalg.norm(r)/nb

        #Steep Descent
            p =-r#to do 
            
        #Conjugate Gradient
            rtr_old=r.T@r#to do
            gamma=r.T@r/rtr_old#to do
            p = -r+gamma*p#to do

#Soluzione di sistemi sovradeterminati (eqnorm, qrLS, SVDLS)

    #eqnorm
        G=A.T@A#to do  
        f=A.T@b#to do

    #qrLS
        Q, R =spl.qr(A)#to do # Si calcola la fattorizzazione QR della matrice A.
        x,_ =ST.Usolve(R[0:n,:],h[0:n])#to do
        residuo=np.linalg.norm(h[n:])**2#to do 

    #SVDLS    
        d=U.T@b#to do 
        d1=d[:k].reshape(k,1)#to do 
        s1=s[:k].reshape(k,1)#to do         
        c=d1/s1#to do 
        x=V[:,:k]@c #to do 
        residuo=np.linalg.norm(d[k:])**2#to do

#Interpolazione

    #plagr
        if j==0:
           xzeri==xondi[1:n]#to do 
        else:
           xzeri=np.append(xondi[0:j],xondi[j+1:n])#to do
        
        num=np.poly(xzeri) #to do #Calcola i coef del polinomio di grado n che si annulla in xzeri
        den=np.polyval(num,xnodi[j]) #to do#Lo valuta nel nodo escluso (-jesimo)
        p = num/den

    #InterpL
        p=plagr(x,j)#to do 
        L[:,j]=np.polyval(p,xx)#to do 
        pol=L@y

        