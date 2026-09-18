
import numpy as np, sys
sys.stdout.reconfigure(encoding='utf-8')
np.set_printoptions(precision=4, suppress=True)
def rhoIminusA(X):
    n,m = X.shape
    A = np.zeros((n+m,n+m))
    A[:n,:n] = np.eye(n)
    A[:n,n:] = X
    A[n:,:n] = X.T
    M = np.eye(n+m) - A
    ev = np.linalg.eigvals(M)
    return np.max(np.abs(ev)), np.linalg.eigvals(A)
for s in [0.01,0.1,0.5,1.0,1.4,1.5,2.0,5.0]:
    X = np.array([[s],[0.0]])   # n=2, m=1, sigma_1 = s
    r, evA = rhoIminusA(X)
    print(f'sigma1={s:5}  rho(I-A)={r:.6f}   eig(A)={np.sort(np.real(evA))}')
# random check m=n
X = np.random.randn(3,3)*0.3
r,evA = rhoIminusA(X)
print('random 3x3 sigma_max', np.linalg.norm(X,2), 'rho(I-A)', r)
print('eig(A)', np.sort(np.real(evA)))
# does rho(I-A)<1 ever hold? scan sigma1
for s in np.arange(0.001,3,0.1):
    X=np.array([[s],[0.0]]); r,_=rhoIminusA(X)
    if r<1: print('CONVERGES at', s)
print('min over scan of rho(I-A):', min(rhoIminusA(np.array([[s],[0.0]]))[0] for s in np.arange(0.0001,3,0.01)))
