# Computational & Applied — 全部题面 (135 题)


---

## [2011 | individual | n=1] 2011_2_AppliedMathProb_Individual_2011  (chars=1174)

Given a weight function ρ(x) > 0, let the inner-product correspond-
ing to ρ(x) be defined as follows:
(f, g) :=
Z b
a
ρ(x)f(x)g(x)dx,
and let ∥f∥:= (f, f).
(1) Define a sequence of polynomials as follows:
p0(x)
=
1,
p1(x) = x −a1,
pn(x)
=
(x −an)pn−1(x) −bnpn−2(x),
n = 2, 3, · · ·
where
an
=
(xpn−1, pn−1)
(pn−1, pn−1) ,
n = 1, 2, · · ·
bn
=
(xpn−1, pn−2)
(pn−2, pn−2) ,
n = 2, 3, · · · .
Show that {pn(x)} is an orthogonal sequence of monic polyno-
mials.
(2) Let {qn(x)} be an orthogonal sequence of monic polynomials
corresponding to the ρ inner product. (A polynomial is called
monic if its leading coefficient is 1.) Show that {qn(x)} is unique
and it minimizes ∥qn∥amongst all monic polynomials of degree
n.
(3) Hence or otherwise, show that if ρ(x) = 1/
√
1 −x2 and [a, b] =
[−1, 1], then the corresponding orthogonal sequence is the Cheby-
shev polynomials:
Tn(x) = cos(n arccos x),
n = 0, 1, 2, · · · .
and the following recurrent formula holds:
Tn+1(x) = 2xTn(x) −Tn−1(x),
n = 1, 2, · · · .
(4) Find the best quadratic approximation to f(x) = x3 on [−1, 1]
using ρ(x) = 1/
√
1 −x2.
1
附件/试卷 2
Appendix/Contest Paper 2

 
Applied Math. Prob. Stat., 2011-Individual


---

## [2011 | individual | n=2] 2011_2_AppliedMathProb_Individual_2011  (chars=146)

2. If two polynomials p(x) and q(x), both of fifth degree, satisfy
p(i) = q(i) = 1
i ,
i = 2, 3, 4, 5, 6,
and
p(1) = 1,
q(1) = 2,
find p(0) −q(0).


---

## [2011 | individual | n=3] 2011_2_AppliedMathProb_Individual_2011  (chars=426)

Lay aside m black balls and n red balls in a jug. Supposes 1 ≤r ≤
k ≤n. Each time one draws a ball from the jug at random.
1) If each time one draws a ball without return, what is the prob-
ability that in the k-th time of drawing one obtains exactly the
r-th red ball?
2) If each time one draws a ball with return, what is the probability
that in the first k times of drawings one obtained totally an odd
number of red balls?


---

## [2011 | individual | n=4] 2011_2_AppliedMathProb_Individual_2011  (chars=172)

Let X and Y be independent and identically distributed random
variables. Show that
E[|X + Y |] ≥E[|X|].
Hint: Consider separately two cases: E[X+] ≥E[X−] and E[X+] <
E[X−].


---

## [2011 | individual | n=5] 2011_2_AppliedMathProb_Individual_2011  (chars=632)

Suppose that X1, · · · , Xn are a random sample from the Bernoulli
distribution with probability of success p1 and Y1, · · · , Yn be an inde-
pendent random sample from the Bernoulli distribution with probabil-
ity of success p2.
(a) Give a minimum sufficient statistic and the UMVU (uniformly
minimum variance unbiased) estimator for θ = p1 −p2.
(b) Give the Cramer-Rao bound for the variance of the unbiased
estimators for v(p1) = p1(1 −p1) or the UMVU estimator for
v(p1).
(c) Compute the asymptotic power of the test with critical region
|√n(ˆp1 −ˆp2)/
p
2ˆpˆq| ≥z1−α
when p1 = p and p2 = p + n−1/2∆, where ˆp = 0.5ˆp1 + 0.5ˆp2.


---

## [2011 | individual | n=6] 2011_2_AppliedMathProb_Individual_2011  (chars=1484)

Suppose that an experiment is conducted to measure a constant θ.
Independent unbiased measurements y of θ can be made with either
of two instruments, both of which measure with normal errors: for
i = 1, 2, instrument i produces independent errors with a N(0, σ2
i )
distribution. The two error variances σ2
1 and σ2
2 are known. When a
measurement y is made, a record is kept of the instrument used so that
after n measurements the data is (a1, y1), . . . , (an, yn), where am = i if
ym is obtained using instrument i. The choice between instruments is
made independently for each observation in such a way that
P(am = 1) = P(am = 2) = 0.5,
1 ≤m ≤n.
附件/试卷 2
Appendix/Contest Paper 2

 
Applied Math. Prob. Stat., 2011-Individual
3
Let x denote the entire set of data available to the statistician, in this
case (a1, y1), . . . , (an, yn), and let lθ(x) denote the corresponding log
likelihood function for θ. Let a =
n
X
m=1
(2 −am).
(a) Show that the maximum likelihood estimate of θ is given by
ˆθ =
Ã
n
X
m=1
1/σ2
am
!−1 Ã
n
X
m=1
ym/σ2
am
!
.
(b) Express the expected Fisher information Iθ and the observed
Fisher information Ix in terms of n, σ2
1, σ2
2, and a. What hap-
pens to the quantity Iθ/Ix as n →∞?
(c) Show that a is an ancillary statistic, and that the conditional
variance of ˆθ given a equals 1/Ix. Of the two approximations
ˆθ
·∼N(θ, 1/Iθ)
and
ˆθ
·∼N(θ, 1/Ix),
which (if either) would you use for the purposes of inference,
and why?
附件/试卷 2
Appendix/Contest Paper 2


---

## [2011 | team | n=1] 2011_6_AppliedMathProb_Team_2011  (chars=492)

Let A be an N-by-N symmetric positive definite matrix. The con-
jugate gradient method can be described as follows:
r0 = b −Ax0, p0 = r0, x0 = 0
FOR n = 0, 1, . . .
αn = ∥rn∥2
2/(pT
nApn)
xn+1 = xn + αnpn
rn+1 = rn −αnApn
βn = −rT
k+1Apk/pT
k Apk
pn+1 = rn+1 + βnpn
END FOR
Show
(a) αn minimizes f(xn + αpn) for all α ∈R where
f(x) ≡1
2xTAx −bTx.
(b) pT
i rn = 0 for i < n and pT
i Apj = 0 if i ̸= j.
(c) Span{p0, p1, . . . , pn−1}= Span{r0, r1, . . . , rn−1} ≡Kn.
(d) rn is orthogonal to Kn.


---

## [2011 | team | n=2] 2011_6_AppliedMathProb_Team_2011  (chars=895)

We use the following scheme to solve the PDE ut + ux = 0:
un+1
j
= aun
j−2 + bun
j−1 + cun
j
where a, b, c are constants which may depend on the CFL number λ =
∆t
∆x. Here xj = j∆x, tn = n∆t and un
j is the numerical approximation
to the exact solution u(xj, tn), with periodic boundary conditions.
(i) Find a, b, c so that the scheme is second order accurate.
(ii) Verify that the scheme you derived in Part (i) is exact (i.e. un
j =
u(xj, tn)) if λ = 1 or λ = 2. Does this imply that the scheme is stable
for λ ≤2? If not, find λ0 such that the scheme is stable for λ ≤λ0.
Recall that a scheme is stable if there exist constants M and C, which
are independent of the mesh sizes ∆x and ∆t, such that
∥un∥≤MeCT∥u0∥
for all ∆x, ∆t and n such that tn ≤T. You can use either the L∞
norm or the L2 norm to prove stability.
1
附件/试卷 6
Appendix/Contest Paper 6

 
Applied Math. Prob. Stat., 2011-Team
2


---

## [2011 | team | n=3] 2011_6_AppliedMathProb_Team_2011  (chars=572)

Let X and Y be independent random variables, identically dis-
tributed according to the Normal distribution with mean 0 and variance
1, N(0, 1).
(a) Find the joint probability density function of (R, θ), where
R = (X2 + Y 2)1/2
and
θ = arctan(Y/X).
(b) Are R and θ independent? Why, or why not?
(c) Find a function U of R which has the uniform distribution on
(0, 1), Unif(0, 1).
(d) Find a function V of θ which is distributed as Unif(0,1).
(e) Show how to transform two independent observations U and V
from Unif(0,1) into two independent observations X, Y from
N(0, 1).


---

## [2011 | team | n=4] 2011_6_AppliedMathProb_Team_2011  (chars=124)

Let X be a random variable such that E[|X|] < ∞. Show that
E[|X −a|] = inf
x∈R E[|X −x|],
if and only if a is a median of X.


---

## [2011 | team | n=5] 2011_6_AppliedMathProb_Team_2011  (chars=459)

Let Y1, . . . , Yn be iid observations from the distribution f(x −θ),
where θ is unknown and f( ) is probability density function symmetric
about zero.
Suppose a priori that θ has the improper prior θ ∼Lebesgue (flat)
on (−∞, ∞). Write down the posterior distribution of θ.
Provides some arguments to show that this flat prior is noninforma-
tive.
Show that with the posterior distribution in (a), a 95% probability
interval is also a 95% confidence interval.


---

## [2011 | team | n=6] 2011_6_AppliedMathProb_Team_2011  (chars=557)

Suppose we have two independent random samples {Y1, i = 1, . . . , n}
from Poisson with (unknown) mean λ1 and {Yi, i = n+1, . . . , 2n} from
Poisson with (unknown) mean λ2 Let θ = λ1/(λ1 + λ2).
(a) Find an unbiased estimator of θ
(b) Does your estimator have the minimum variance among all un-
biased estimators? If yes, prove it. If not, find one that has the
minimum variance (and prove it).
(c) Does the unbiased minimum variance estimator you found at-
tain the Fisher information bound? If yes, show it. If no, why
not?
附件/试卷 6
Appendix/Contest Paper 6


---

## [2012 | individual | n=1] 2012_Applied2012individual  (chars=324)

In the numerical integration formula
(1)
Z 1
−1
f(x)dx ≈af(−1) + bf(c),
if the constants a, b, c can be chosen arbitrarily, what is the highest
degree k such that the formula is exact for all polynomials of degree
up to k? Find the constants a, b, c for which the formula is exact for
all polynomials of degree up to this k.


---

## [2012 | individual | n=2] 2012_Applied2012individual  (chars=1002)

Here is the definition of a moving least square approximation of a
function f(x) near a point x given K points xk around x in R, k ∈
[1, · · · , K].
(2)
min
Px∈Πm
K
X
k=1
|Px(xk) −fk|2
where fk = f(xk), Πm is the space of polynomials of degree less or
equal to m, i.e.
Px(x) = bx(x)Tc(x),
c(x) = [c0, c1, · · · , cm]T is the coefficient vector to be determined by (2),
bx(x) is the polynomial basis vector, bx(x) = [1, x −x, (x −x)2, . . . , (x −x)m]T.
Assume that there are K > m different points xk and f(x) is smooth,
(a) prove that there is a unique solution P x(x) to (2)
(b) denote h = maxk |xk −x|, prove
|ci −1
i!f (i)(x)| = C(f, i)hm+1−i, i = 0, 1, . . . , m,
where f (i)(·) is the i-th derivative of f and C(f, i) denote some constant
depending on f, i.
1

 
2
(c) if S = {xk|k = 1, 2, . . . , K} are symmetrically distributed around
x, that is, if xk ∈S then 2x −xk ∈S, prove that
|ci −1
i!f (i)(x)| = C(f, i)hm+2−i, i = 0, 1, . . . , m,
for i (∈{0, 1, · · · , m}) with the same parity of m.


---

## [2012 | individual | n=3] 2012_Applied2012individual  (chars=394)

Describe the forward-in-time and center-in-space finite difference
scheme for the one-wave wave equation:
ut + ux = 0.
(i). Conduct the von Neumann stability analysis and comment on
their stability property.
(ii).
Under what condition on ∆t and ∆x would this scheme be
stable and convergent?
(iii). How many ways you can modify this scheme to make it stable
when the CFL condition is satisfied.


---

## [2012 | individual | n=4] 2012_Applied2012individual  (chars=1284)

Let C and D in Cn×n be Hermitian matrices. Denote their eigen-
values by
λ1 ≥λ2 ≥· · · ≥λn
and
µ1 ≥µ2 ≥· · · ≥µn,
respectively. Then it is known that
n
X
i=1
(λi −µi)2 ≤∥C −D∥2
F.
1) Let A and B be in Cn×n. Denote their singular values by
σ1 ≥σ2 ≥· · · ≥σn
and
τ1 ≥τ2 ≥· · · ≥τn,
respectively. Prove that the following inequality holds:
n
X
i=1
(σi −τi)2 ≤∥A −B∥2
F.
2) Given A ∈Rn×n and its SVD is A = UΣV T, where U =
(u1, u2, . . . , un), V = (v1, v2, . . . , vn) are orthogonal matrices,
and
Σ = diag(σ1, σ2, . . . , σn),
σ1 ≥σ2 ≥· · · ≥σn ≥0.
Suppose rank(A) > k and denote by
Uk = (u1, u2, . . . , uk),
Vk = (v1, v2, . . . , vk),
Σk = diag(σ1, σ2, . . . , σk),
and
Ak = UkΣkV T
k =
k
X
i=1
σiuivT
i .
Prove that
min
rank(B)=k ∥A −B∥2
F = ∥A −Ak∥2
F =
n
X
i=k+1
σ2
i .

 
3
3) Let the vectors xi ∈Rn, i = 1, 2, . . . , n, be in the space W with
dimension d, where d ≪n. Let the orthonormal basis of W be
W ∈Rn×d. Then we can represent xi by
xi = c + Wri + ei, i = 1, 2, . . . , n,
where c ∈Rn is a constant vector, ri ∈Rd is the coordinate
of the point xi in the space W, and ei is the error. Denote
R = (r1, r2, . . . , rn) and E = (e1, e2, . . . , en). Find W, R and c
such that the error ∥E∥F is minimized.
(Hint: write X = [x1, x2, . . . , xn] = c(1, 1, . . . , 1) + WR + E.)


---

## [2012 | individual | n=5] 2012_Applied2012individual  (chars=338)

Two primes p and q are called twin primes if q = p + 2.
For
example, 5 and 7, 11 and 13, 29 and 31 are twin primes. There is
a still unproven (but extensively numerically verified) conjecture that
there are infinitely many twin primes and that they are rather common.
Show how to factor an integer N which is a product of two twin primes.


---

## [2012 | team | n=1] 2012_Applied2012team  (chars=363)

If the function u(x) is in Ck+1 (has continuous (k + 1)-th deriva-
tive) on the interval [0, 2], and a sequence of polynomials pn(x) (n =
1, 2, 3, ...) of degree at most k satisfies
(1)
|u(x) −pn(x)| ≤
C
nk+1
∀0 ≤x ≤1
n,
where the constant C is independent of n, prove
|u(x) −pn(x)| ≤
˜C
nk+1
∀1
n ≤x ≤2
n,
with another constant ˜C which is also independent of n.


---

## [2012 | team | n=2] 2012_Applied2012team  (chars=576)

Consider the one-dimensional elliptic equation
−d2
dx2u(x) = f(x),
0 < x < 1,
with homogeneous boundary condition, u(0) = 0 and u(1) = 0, f ∈
L2(0, 1).
(i) Describe the standard piecewise linear finite element method for
this boundary value problem.
(ii) Is this method stable and convergent? If so, what is the order of
convergence?
(iii). In this case, the linear finite element method has a super con-
vergence property at the nodal point xj (j = 1, 2, ..., N), i.e. uh(xj) =
u(xj), here uh is the finite element solution and u is the exact solution.
Could you explain why?


---

## [2012 | team | n=3] 2012_Applied2012team  (chars=984)

Let A = (aij) ∈MN×N(C) be strictly diagonally dominant, that is,
|aii| >
N
X
j=1,j̸=i
|aij| for all 1 ≤i ≤N,
Assume that A = I + L + U where I is the identity matrix, L and U
are the lower and upper triangular matrices with zero diagonal entries.
1

 
2
Now, we consider solving the linear system Ax = b by the following
iterative scheme:
(∗)
xk+1 = (I +αΩL)−1[(I −Ω)−(1−α)ΩL−ΩU)]xk +(I +αΩL)−1b
where Ω:= diag(ω1, ...ωN) and 0 ≤α ≤1. (When α = 1, it gives the
SOR method.)
(1) Prove that the linear system Ax = b has a unique solution.
(2) Prove that the necessary condition for the convergence of (*) is
N
Y
i=1
|1 −ωi| < 1
(3) Let M = (I + αΩL)−1[(I −Ω) −(1 −α)ΩL −ΩU)]. Prove that
the spectral radius ρ(M) of M is bounded by:
ρ(M) ≤max
i
|1 −ωi| + |ωi|(|1 −α|li + ui)
1 −|ωiα|li
whenever |ωiα|li < 1 for all 1 ≤i ≤N where li = P
j<i |aij|
and ui = P
j>i |aij|.
(4) Using (c), prove that the sufficient condition for the convergence
of (*) is
0 < ωi <
2
1 + li + ui
for all 1 ≤i ≤N


---

## [2012 | team | n=4] 2012_Applied2012team  (chars=1012)

The famous RSA cryptosystem is based on the assumed difficulty of
factoring integers N = pq (called RSA integers) which are products of
two large primes p and q which should be kept secret. Currently p and
q are chosen to be about 500 bits long, that is,
p, q ≈2500.
Assume someone uses the following algorithm to find secret n-bit primes
p and q to form an RSA integer N = pq:
• Choose a random odd 500-bit integer s.
• Test the odd numbers s, s+2, s+4, etc. for primality until the
first prime p is found (note the primality testing is very easy
nowdays).
• Continue testing p + 2, p + 4, p + 6, etc. for primality until the
second prime q is found.
• Compute and publish N = pq, but keep p and q secret.
How secure is this procedure? Can you suggest an algorithm to factor
an RSA integer N = pq generated this way?
Note that there are about x/ log x primes up to x, where log x is
the natural logarithm. This means that the expected gap between two
consecutive n-bit primes is
log 2n = n log 2 ≈0.69 · n.

 
3


---

## [2012 | team | n=5] 2012_Applied2012team  (chars=881)

The solution h(r, t) of the following Boussinesq equation describes
the hight of a circular drop of fluid spreading on a dry surface h = 0:
∂h
∂t = ∆r(h2) = 1
r
∂
∂r
µ
r∂(h2)
∂r
¶
,
r > 0,
t > 1
with
∂h
∂r
¯¯¯
r=0 = 0,
Z ∞
0
h(r, t)rdr ≡1
64
The solution is positive on a finite range 0 ≤r ≤r∗(t) with h(r∗(t), t) =
0 defining a moving "edge" position with no fluid outside of the droplet.
For r > r∗(t) truncate the solution beyond the edge to be zero ( h ≡0
for r > r∗(t)).
(a): Show that this problem is scale invariant by finding relations
h(r, t) = H(T)˜h(˜r, ˜t), r = R(T)˜r, t = T˜t so that the problem
for ˜h(˜r, ˜t) is identical to the original problem.
(b): Determine the ODE for the similarity function Φ(η) with
h(r, t) = tαΦ(η), r = ηtβ.
(c): Determine the explicit solution for Φ(η) and then use h(r, t) =
tαΦ(η) to find r∗(t) for t ≥1.
Hint
R ∞
0 hrdr =
R r∗
0 hrdr.


---

## [2013 | individual | n=1] 2013_applied2013_individual  (chars=1026)

We consider the wave equation utt = ∆u in R3 × R+.
(a): (5 pts) A right going pulse with speed 1
u(x, y, z, t) = 1 for t < x < t + 1;
u(x, y, z, t) = 0 else
is clearly a solution to the wave equation.
However, it is a
discontinuous solution, explain in which sense it is a solution to
the equation.
(b): (5 pts) Surprisingly, one can construct smooth progressive
wave solutions with speed larger than 1.
In astronomy this
kind of wave known as superluminal wave. Try a solution of
the form
u(x, y, z, t) = v( x −ct
√
c2 −1, y, z),
c ∈R3,
|c| > 1.
Derive an equation for v and show that there is a nontrivial
solution with compact support in (y, z) for any fixed x, t.
(c): (5 pts) For any R > 0, 0 < t < R, show that energy
E(t) :=
∫
|⃗x|≤R−t
(
|ut(·, t)|2 + |∇u(·, t)|2)
d⃗x
is a decreasing function.
(c): (10 pts) Show that smooth superluminal progressive wave
solutions of the form
u(⃗x, t) = v(⃗x −⃗ct),⃗c ∈R3,
|⃗c| > 1.
cannot have a finite energy.
Hint: Using (c) and look at the energy of the solution in
various balls.


---

## [2013 | individual | n=2] 2013_applied2013_individual  (chars=668)

Finite time extinction and hyper-contractiveity are important prop-
erties in modeling of some physical and biology systems. The essence
of estimates is given by the following problem for ODE.
Assume y(t) ≥0 is a C1 function for t > 0 satisfying y′(t) ≤α −
βy(t)a for α > 0, β > 0, then
(a) (10 points) For a > 1, y(t) has the following hyper-contractive
property
y(t) ≤(α/β)1/a +
[
1
β(a −1)t
]
1
a−1
,
for t > 0.
1

 
2
(b) (2 points) For a = 1, y(t) decays exponentially
y(t) ≤α/β + y(0)e−βt.
(c) (10 points) For a < 1, α = 0, y(t) has finite time extinction,
which means that there exists Text such that 0 < Text ≤y1−a(0)
β(1−a)
and that y(t) = 0 for all t > Text.


---

## [2013 | individual | n=3] 2013_applied2013_individual  (chars=163)

Consider the speed v of a ball (density ρ, radius R) falling through
a viscous fluid (density ρf, viscosity µ) with drag coefficient given by
Stokes' law ζ = 6πRµ:


---

## [2013 | individual | n=4] 2013_applied2013_individual  (chars=1413)

3πR3ρdv
dt = 4
3πR3(ρ −ρf)g −ζv,
v(0) = v0
(a): (5 points) Nondimensionalize the equation by writing, v(t) =
V ˜v(˜t) with t = T˜t. Select V , T (characteristic scales known
as terminal velocity and settling time respectively) so that all
coefficients in the ODE but one are equal to 1. Your equation
will have a single dimensionless parameter given by the ratio of
the initial speed v0 to the characteristic speed V .
(b): (2 points) Solve the nondimensional problem for ˜v(˜t).
(c): (8 points) Describe the behavior of the solution if the initial
speed v0 is (i) faster than and (ii) slower than the characteristic
speed V . Compute the time to reach (v0 + V )/2.
4. Let
Vh = {v : v|Ij ∈P k(Ij)
1 ≤j ≤N}
where
Ij = (xj−1, xj),
1 ≤j ≤N
with
xj = jh,
h = 1
N .
Here P k(Ij) denotes the set of polynomials of degree at most k in the
interval Ij.
Recall the L2 projection of a function u(x) into the space Vh is defined
by the unique function uh ∈Vh which satisfies
||u −uh|| ≤||u −v||
∀v ∈Vh
where the norm is the usual L2 norm. We assume u(x) has at least
k + 2 continuous derivatives.
(1) (5 points) Prove the error estimate
||u −uh|| ≤Chk+1
Explain how the constant C depends on the derivatives of u(x).

 
3
(2) (10 points)
If another function φ(x) also has at least k + 2
continuous derivatives, prove
|
∫1
0
(u(x) −uh(x))φ(x)dx| ≤Ch2k+2
Explain how the constant C depends on the derivatives of u(x)
and φ(x).


---

## [2013 | individual | n=5] 2013_applied2013_individual  (chars=324)

(15 points)
Let G(V, E) be a simple graph of order n and δ the
minimum degree of vertices. Suppose that the degree sum of any pair
of nonadjacent vertices is at least n and F ⊂E with |F| ≤⌊δ−2
2 ⌋. Let
G−F be the graph obtained from G by deleting the edges in F. Prove
that
(1) G −F is connected and
(2) G −F is Hamiltonian.


---

## [2013 | individual | n=6] 2013_applied2013_individual  (chars=540)

(15 points)
Let (Fn)n be the Fibonacci sequence. Namely, F0 =
0, F1 = 1, . . . , Fn+2 = Fn+1 + Fn.
Establish a relation between
(
0
1
1
1
)n
and Fn and use it to design
an efficient algorithm that for a given n computes the n-th Fibonacci
number Fn. In particular, it must be more efficient than computing
Fn in n consecutive steps.
Give an estimate on the number of steps of your algorithm.
Hint: Not that if m is even then
(
0
1
1
1
)m
=
((
0
1
1
1
)m/2)2
and if m is odd then
(
0
1
1
1
)m
=
(
0
1
1
1
)m−1
·
(
0
1
1
1
)
and m −1 is even.


---

## [2013 | team | n=1] 2013_TeamProblems2013  (chars=1221)

Scaling behavior is one of the most important phenomena in sci-
entific modeling and mathematical analysis.
The following problem
shows the universality and rigidity of scaling limits.
(a): (10 points) Suppose U > 0 is an increasing function on [0, ∞)
and there is a function 0 < ψ(x) < ∞for x > 0 such that
lim
t→∞
U(tx)
U(t) = ψ(x),
for all x > 0
Then ψ(x) = xα for some α ≥0.
(b): (10 points) The above problem can be generalized as:
Suppose U > 0 is an increasing function on [0, ∞) and there
is an extended function 0 ≤ψ(x) ≤∞and a set A dense in
[0, ∞) such that
lim
t→∞
U(tx)
U(t) = ψ(x),
for all x ∈A
Then ψ(x) = xα for some α ∈[0, ∞].
(c): (15 points) (Warming: this part is hard).
A function L : (0, ∞) →(0, ∞) is called slowly varying at ∞
if
lim
t→∞
L(tx)
L(t) = 1,
for all x ∈A dense in (0, ∞)
The function U in (a) and (b) can be recast as U(x) = c xαL(x)
for some c ≥0. Now we can extend (b) to an even more general
setting:
Suppose U > 0 is increasing on (0, ∞), set A dense in [0, ∞)
and
lim
n→∞anU(bnx) = ψ(x) ≤∞, for all x ∈A.
where bn →∞and an+1
an
→1 for some interval. Then there is a
real number α ∈[0, ∞], constant c ≥0, and a function L slowly
varying at ∞such that ψ(x) = xα and U(x) = c xαL(x).


---

## [2013 | team | n=2] 2013_TeamProblems2013  (chars=601)

The following three operators are important for many mathematics
and physics problems. Let ϕ(x) be a smooth periodic function in Tn, ∆,
∇, ∇· be the standard Laplacian, gradient and divergence operators.
(i): Fokker-Planck operator: Fu = −∆u −∇· (u∇ϕ)
1

 
2
(ii): Witten Laplacian operator: Wu = −∆u + ∇ϕ · ∇u
(iii): Schr¨odinger operator: Su = −∆u +
(1
4|∇ϕ|2 −1
2∆ϕ
)
u
Show that
(a): (5 points) The Fokker-Planck operator can be recast as Fu =
−∇· (e−ϕ∇(eϕu).
(b): (10 points) These three operators have same eigenvalues.
(c): (5 points) Find all equilibrium solutions for these three op-
erators.


---

## [2013 | team | n=3] 2013_TeamProblems2013  (chars=508)

(15 points) Let f(x) defined on [0, 1] be a smooth function with
sufficiently many derivatives. xi = ih, where h = 1
N and i = 0, 1, · · · , N
are uniformly distributed points in [0, 1]. What is the highest integer
k such that the numerical integration formula
IN = 1
N
(
a0(f(x0) + f(xN)) + a1(f(x1) + f(xN−1)) +
N−2
∑
i=2
f(xi)
)
is k-th order accurate, namely
IN −
∫1
0
f(x)dx
 ≤Chk
for a constant C independent of h? Please describe the procedure to
obtain the two constants a0 and a1 for this k.


---

## [2013 | team | n=4] 2013_TeamProblems2013  (chars=1193)

The wave guide problem is defined as
ut + ux = 0,
vt −vx = 0
with the boundary condition
u(−1, t) = v(−1, t),
v(1, t) = u(1, t)
and the initial condition
u(x, 0) = f(x),
v(x, 0) = g(x).
The upwind scheme for the guide problem is defined as
un+1
j
−un
j
∆t
+ un
j −un
j−1
∆x
= 0,
j = −N + 1, · · · , N;
vn+1
j
−vn
j
∆t
−vn
j+1 −vn
j
∆x
= 0,
j = −N, · · · , N −1;
with the boundary condition
un+1
−N = vn+1
−N ,
vn+1
N
= un+1
N
where un
j and vn
j approximate u(xj, tn) and v(xj, tn) respectively at the
grid point (xj, tn), with xj = j∆x, tn = n∆t, ∆x = 1
N .

 
3
(1) (5 points) For the solution to the wave guide problem with the
above boundary condition, prove the energy conservation
d
dt
∫1
−1
(u2 + v2)dx = 0.
(2) (5 points) For the numerical solution of the the upwind scheme,
if we define the discrete energy as
En =
N
∑
j=−N+1
(un
j )2 +
N−1
∑
j=−N
(vn
j )2,
prove the discrete energy stability
En+1 ≤En
under a suitable time step restriction ∆t
∆x ≤λ0. You should first
find λ0.
(3) (10 points) Under the same time step restriction, is the numer-
ical solution stable in the maximum norm? That is, can you
prove
max
−N≤j≤N max(|un+1
j
|, |vn+1
j
|) ≤
max
−N≤j≤N max(|un
j |, |vn
j |)?


---

## [2013 | team | n=5] 2013_TeamProblems2013  (chars=559)

(15 points)
Let G = (V, E) be a graph of order n. Let X1, X2,
. . . , Xq with 2 ≤q ≤κ(X) be subsets of the vertex set V such that
X = X1 ∪X2 ∪. . . ∪Xq. If for each i, i = 1, 2, . . . , q, and for any pair
of nonadjacent vertices x, y ∈Xi, we have
d(x) + d(y) ≥n,
then X is cyclable in G (i.e., there is a cycle containing all vertices of
X.).
Where d(x) is the degree of x and κ(X) is the smallest number of
vertices separating two vertices of X if X does not induce a complete
subgraph of G, otherwise we put κ(X) = |X| −1 if |X| ≥2 and
κ(X) = 1 if |X| = 1.


---

## [2013 | team | n=6] 2013_TeamProblems2013  (chars=600)

(15 points)
Let (Fn)n be the Fibonacci sequence. Namely, F0 =
0, F1 = 1, . . . , Fn+2 = Fn+1 + Fn.
Establish a relation between
(
0
1
1
1
)n
and Fn and use it to design
an efficient algorithm that for a given n computes the n-th Fibonacci
number Fn. In particular, it must be more efficient than computing
Fn in n consecutive steps.
Give an estimate on the number of steps of your algorithm.
Hint: Not that if m is even then
(
0
1
1
1
)m
=
((
0
1
1
1
)m/2)2

 
4
and if m is odd then
(
0
1
1
1
)m
=
(
0
1
1
1
)m−1
·
(
0
1
1
1
)
and m −1 is even.

 
S.-T. Yau College Student Mathematics Contests 2013


---

## [2014 | individual | n=1] 2014_applied2014_individual  (chars=428)

(20 pts) Ming Antu (1692-1763) is one of the greatest Chinese/Mongolian
mathematicians. In the 1730s, he first established and used what was
later to be known as Catalan numbers (Euler (1707-1763) rediscov-
ered them around 1756; Belgian mathematician Eugene Catalan (1814-
1894) "rediscovered" them again in 1838),
cn =
1
n + 1
(2n
n
)
,
n = 0, 1, 2, · · ·
and Ming Antu derived the following half-angle formula in 1730:
sin2 θ


---

## [2014 | individual | n=2] 2014_applied2014_individual  (chars=761)

=
∞
∑
n=1
cn−1
(sin θ
2
)2n
Prove this formula.
Hint: you may use generating function
F(z) =
∞
∑
n=0
cnzn
and show that ∑
m+k=n cmck = cn+1 and then show zF(z)2 = F(z)−1.
2. Many algorithms, including polynomial factorisation in finite fields,
require to compute gcd(f(X), XN −1) for a polynomial f of reasonably
small degree n and a binomial XN −1 of very large degree N. Since
N is very large the direct application of the Euclid algorithm is very
inefficient.
Questions:
(i) (10 pts) Suggest a more efficient approach the direct computa-
tion of gcd(f(X), XN −1) via the Euclid algorithm.
(ii) (10 pts) Generalise it to gcd(f(X), A1XN1 + . . . + AmXNm +
Am+1).
Hint: If for three polynomials f, g and h we have g ≡h (mod f)
then
gcd(f, g) = gcd(f, h).
1

 
2


---

## [2014 | individual | n=3] 2014_applied2014_individual  (chars=636)

For solving the following partial differential equation
ut + f(u)x = 0,
0 ≤x ≤1
(1)
where f ′(u) ≥0, with periodic boundary condition, we can use the
following semi-discrete upwind scheme
d
dtuj + f(uj) −f(uj−1)
∆x
= 0,
j = 1, 2, · · · , N,
(2)
with periodic boundary condition
u0 = uN,
(3)
where uj = uj(t) approximates u(xj, t) at the grid point x = xj = j∆x,
with ∆x = 1
N .
(i) (15 pts) Prove the following L2 stability of the scheme
d
dtE(t) ≤0
(4)
where E(t) = ∑N
j=1 |uj|2∆x.
(ii) (15 pts) Do you believe (4) is true for E(t) = ∑N
j=1 |uj|2p∆x for
arbitrary integer p ≥1? If yes, prove the result. If not, give a
counter example.


---

## [2014 | individual | n=4] 2014_applied2014_individual  (chars=766)

Let A be an n × n matrix with real and positive eigenvalues and b
be a given vector. Consider the solution of Ax = b by the following
Richardson's iteration
x(k+1) = (I −ωA)x(k) + ωb
where ω is a damping coefficient. Let λ1 and λn be the smallest and
the largest eigenvalues of A. Let Gω = I −ωA.
(i) (4 points) Prove that the Richardson's iteration converges if
and only if
0 < ω < 2
λn
.
(ii) (8 points) Prove that the optimal choice of ω is given by
ωopt =
2
λ1 + λn
.
Prove also that
ρ(Gω) =





1 −ωλ1
ω ≤ωopt
(λn −λ1)/(λn + λ1)
ω = ωopt
ωλn −1
ω ≥ωopt
where ρ(Gω) is the spectral radius of Gω.

 
3
(iii) (8 points) Prove that, if A is symmetric and positive definite,
then
ρ(Gωopt) = κ2(A) −1
κ2(A) + 1
where κ2(A) is the spectral condition number of A.


---

## [2014 | individual | n=5] 2014_applied2014_individual  (chars=742)

(10 pts) For solving the following heat equation on interval
ut = uxx,
0 ≤x ≤1
(5)
with boundary condition
u(0) = u0,
u(1) = u1,
(6)
we first discretize the interval [0, 1] into N subintervals uniformly, that
is, the mesh size h = 1/N. We choose a temporal step size k and ap-
proximate the solution u(jh, nk) by U n
j , j = 1, ..., N −1, n = 0, 1, 2, ....
Using the backward Euler method in time and central finite difference
in space, the discrete function U n
j satisfies:
U n+1
j
−U n
j = λ(U n+1
j−1 −2U n+1
j
+ U n+1
j+1 ),
j = 1, ..., N −1,
(7)
where λ = k/h2, and
U n+1
0
= u0, U n+1
N
= u1.
Show that
1
2
N−1
∑
j=1
(
(U n+1
j
)2 −(U n
j )2)
≤−λ
N−2
∑
j=1
(U n+1
j+1 −U n+1
j
)2
−λ
2((U n+1
1
)2 + (U n+1
N−1)2) + λ
2(u2
0 + u2
1)
(8)


---

## [2014 | team | n=1] 2014_applied2014_team  (chars=311)

(15 pts)
Given a finite positive (Borel) measure dµ on [0, 1], define its sequence
of moments as follows
cj =
∫1
0
xj dµ(x) ,
j = 0, 1, . . . .
Show that the sequence is completely monotone in the sense that that
(I −S)kcj ≥0
for all j, k ≥0,
where S denotes the backshift operator given by Scj = cj+1 for j ≥0.


---

## [2014 | team | n=2] 2014_applied2014_team  (chars=707)

(20 pts)
We recall that a polynomial
f(X) = adXd + ad−1Xd−1 + · · · + a1X + a0 ∈Z[X]
is called an Eisenstein polynomial if for some prime p we have
(i) p | ai for i = 0, . . . , d −1,
(ii) p2 ∤a0,
(iii) p ∤ad.
Eisenstein polynomials are well-know to be irreducible over Z, so they
can be used to construct explicit examples of irreducible polynomials.
Questions:
(i) Prove that a composition f(g(X)) of two Eisenstein polynomi-
als f and g is an Eisenstein polynomial again.
(ii) Suggest a multivariate generalisation of the Eisenstein polyno-
mials. That is, describe a class polynomials F(X1, . . . , Xm) in
terms of the divisibility properties of their coefficients that are
guaranteed to be irreducible.


---

## [2014 | team | n=3] 2014_applied2014_team  (chars=746)

(20 pts) For solving the following partial differential equation
ut + f(u)x = 0,
0 ≤x ≤1
(1)
where f ′(u) ≥0, with periodic boundary condition, we can use the
following semi-discrete discontinuous Galerkin method: Find uh(·, t) ∈
Vh such that, for all v ∈Vh and j = 1, 2, · · · , N,
∫
Ij
(uh)tvdx−
∫
Ij
f(uh)vxdx+f((uh)−
j+1/2)v−
j+1/2−f((uh)−
j−1/2)v+
j−1/2 = 0,
(2)
1

 
2
with periodic boundary condition
(uh)−
1/2 = (uh)−
N+1/2;
(uh)+
N+1/2 = (uh)+
1/2,
(3)
where Ij = (xj−1/2, xj+1/2), 0 = x1/2 < x3/2 < · · · < xN+1/2 = 1,
h = maxj(xj+1/2 −xj−1/2), v±
j+1/2 = v(x±
j+1/2, t), and
Vh = {v : v|Ij is a polynomial of degree at most k for 1 ≤j ≤N}.
Prove the following L2 stability of the scheme
d
dtE(t) ≤0
(4)
where E(t) =
∫1
0 (uh(x, t))2dx.


---

## [2014 | team | n=4] 2014_applied2014_team  (chars=752)

Consider the linear system Ax = b. The GMRES method is a pro-
jection method which obtains a solution in the m-th Krylov subspace
Km so that the residual is orthogonal to AKm. Let r0 be the initial
residual and let v0 = r0. The Arnoldi process is applied to build an
orthonormal system v1, v2, · · · , vm−1 with v1 = Av0/∥Av0∥. The ap-
proximate solution is obtained from the following space
Km = span{v0, v1, · · · , vm−1}.
(i) (5 points) Show that the approximate solution is obtained as
the solution of a least-square problem, and that this problem is
triangular.
(ii) (5 points) Prove that the residual rk is orthogonal to {v1, v2, · · · , vk−1}.
(iii) (5 points) Find a formula for the residual norm.
(iv) (5 points) Derive the complete algorithm.


---

## [2014 | team | n=5] 2014_applied2014_team  (chars=287)

(10 pts)
(i) Set x0 = 0. Write the recurrence
xk = 2xk−1 + bk,
k = 1, 2, · · · , n,
in a matrix form A⃗x = ⃗b. For b1 = −1/3, bk = (−1)k, k =
2, 3, · · · , n, verify that xk = (−1)k/3, k = 1, 2, · · · , n is the
exact solution.
(ii) Find A−1 and compute condition number of A in L1 norm.


---

## [2015 | individual | n=1] 2015_applied2015_individual  (chars=225)

. Let r and s be relatively prime positive integers. Prove that the number
of lattice paths from (0, 0) to (r, s), which consists of steps (1, 0) and (0, 1) and never
go above the line ry = sx is given by
1
r + s
(r + s
s
)
.


---

## [2015 | individual | n=2] 2015_applied2015_individual  (chars=1267)

. The following 2 × 2 block matrix
C(α) =
[
αI
A
AT
0
]
plays a key role in an augmented system method to solve linear least squares problem, a
fundamental numerical linear algebra problem for fitting a linear model to observations
subject to errors in science, where A ∈Rm×n is of full rank n ≤m, I is a m×m identity
matrix, and α ≥0. Prove the following results which address the question of optimal
choice of scaling α for stabiltiy of the augmented system method.
(a) The eigenvalues of C(α) are
α
2 ±
(α2
4 + σ2
i
)1/2
for i = 1, 2, . . . , n,
and
α
(m −n times),
where σi for i = 1, 2, . . . , n are the singular values of A, arranged in the de-
creasing order, i.e., σ1 ≥σ2 ≥· · · ≥σn.
(b) The condition number κ2(C(α)) = ∥C(α)∥2 ∥[C(α)]−1∥2 has the following bounds:
√
2κ2(A) ≤min
α κ2(C(α)) ≤2κ2(A),
with minα κ2(C(α)) being achieved for α = σn/
√
2, and
max
α
κ2(C(α)) > κ2(A)2,
where ∥· ∥is the spectral norm of a matrix.
Recall that any matrix A ∈Rm×n has a singular value decomposition (SVD):
A = UΣV T,
Σ = diag(σ1, σ2, . . . , σp) ∈Rm×n,
p = min(m, n),
where σ1 ≥σ2 ≥· · · ≥σp ≥0, and U ∈Rm×m, V ∈Rn×n are both orthogonal. The σi
are the singular values of A and the columns of U and V are the left and right singular
vectors of A, respectively.
1

 
2


---

## [2015 | individual | n=3] 2015_applied2015_individual  (chars=811)

. Solve the following linear hyperbolic partial differential equation
ut + aux = 0,
t ≥0,
(1)
where a is a constant. Using the finite difference approximation, we can obtain the
forward-time central-space scheme as follows,
un+1
m
−un
m
k
+ aun
m+1 −un
m−1
2h
= 0,
(2)
where k and h are temporal and spatial mesh sizes.
(a) Show that when we fix λ = k/h as a positive constant, the forward-time central-
space scheme (2) is consistent with equation (1).
(b) Analyze the stability of this method. Is the method stable with λ = k/h being
fixed as a constant?
(c) How would the answer change if you are allowed to make λ = k/h small?
(d) Would this is a good scheme to use even if you can make it stable by making λ
small? If not, please provide a simple modification to make this scheme stable
by keeping λ fixed.


---

## [2015 | individual | n=4] 2015_applied2015_individual  (chars=249)

. Let A, H, Q ∈Cn×n and Q is non-singular. Assume that H = Q−1AQ
and H is properly upper Hessenberg. Show that
span{q1, q2, . . . , qj} = Kj(A, q1),
j = 1, 2, . . . , n
where qj is the j-th column of Q, and Kj(A, q1) = span{q1, Aq1, . . . , Aj−1q1}.


---

## [2015 | individual | n=5] 2015_applied2015_individual  (chars=513)

. Minkowski Problem.
n푖
퐹푖
퐴푖
Assume P is a convex polyhedron embedded in R3, the faces are {F1, F2, · · · , Fk},
the unit normal vector to the face Fi is ni, the area of Fi is Ai, 1 ≤i ≤k.
• Show that
(3)
A1n1 + A2n2 + · · · Aknk = 0,
• Given k unit vectors {n1, n2, · · · , nk} which can not be contained in any half
space, and k real positive numbers {A1, A2, · · · , Ak}, Ai > 0, and satisfying
the condition (3), show that there exists a convex polyhedron P, whose face
normals are ni's, face areas are Ai's.


---

## [2015 | team | n=1] 2015_team_applied2015  (chars=756)

. Consider the elliptic interface problem
(a(x)ux)x = f, x ∈(0, 1)
with the Dirichlet boundary condition
u(0) = u(1) = 0.
Here, f is a smooth function, the elliptic coefficient a(x) is discontinuous across an
interface point ξ, that is,
a(x) =
{
a0
for 0 < x < ξ
a1
for ξ < x < 1,
a0, a1 > 0 are positive constants, and 0 < ξ < 1 is an interface point. Across the
interface, we need to impose two jump conditions
u(ξ−) = u(ξ+), a(ξ−)ux(ξ−) = a(ξ+)ux(ξ+).
Question:
1. (25%) Design a numerical method to solve this problem. The method should
be at least first order. It is better to be high order (if your method is first order,
you get 20% points).
2. (75%) Prove your accuracy and convergence arguments (if your method is first
order, you get 60% points).


---

## [2015 | team | n=2] 2015_team_applied2015  (chars=612)

. Let G be graph of a social network, where for each pair of members there
is either no connection, or a positive or a negative one.
An unbalanced cycle in G is a a cycle which have odd number of negative edges.
Traversing along such a cycle with social rules such as friend of enemy are enemy would
result in having a negative relation of one with himself!
A resigning in G at a vertex v of G is to switch the type (positive or negative) of all
edges incident to v.
Question: Show that one can switch all edge of G into positive edges using a sequence
resigning if and only if there is no unbalanced cycle in G.


---

## [2015 | team | n=3] 2015_team_applied2015  (chars=670)

. We consider particles which are able to produce new particles of like kind.
A single particle forms the original, or zero, generation. Every particle has probability
pk (k = 0, 1, 2, . . . ) of creating exactly k new particles; the direct descendants of the
nth generation form the (n + 1)st generation. The particles of each generation act
independently of each other.
1

 
2
Assume 0 < p0 < 1. Let P(x) = ∑
k≥0 pkxk and µ = P ′(1) = ∑
k≥0 kpk be the
expected number of direct descendants of one particle. Prove that if µ > 1, then the
probability xn that the process terminates at or before the nth generation tends to the
unique root σ ∈(0, 1) of equation σ = P(σ).


---

## [2015 | team | n=4] 2015_team_applied2015  (chars=790)

. (Isopermetric inequality). Consider a closed plane curve described by a
parametric equation (x(t), y(t)), 0 ≤t ≤T with parameter t oriented counterclockwise
and (x(0), y(0)) = (x(T), y(T)).
(a): Show that the total length of the curve is given by
L =
∫T
0
√
(x′(t))2 + (y′(t))2) dt
(b): Show that the total area enclosed by the curve is given by
A = 1
2
∫T
0
(
x(t)y′(t) −y(t)x′(t)
)
dt
(c): The classical iso-perimetric inequality states that for closed plane curves
with a fixed length L, circles have the largest enclosed area A. Formulate this
question into a variational problem.
(d): Derive the Euler-Lagrange equation for the variational problem in (c).
(e): Show that there are two constants x0 and y0 such that
(x(t) −x0)2 + (y(t) −y0)2 ≡r2
where r = L/(2π). Explain your result.


---

## [2015 | team | n=5] 2015_team_applied2015  (chars=464)

. Let A ∈Rn×m with rank r < min(m, n). Let A = UΣV T be the SVD of
A, with singular values σ1 ≥σ2 ≥· · · ≥σr > 0.
(a) Show that, for every ϵ > 0, there is a full rank matrix Aϵ ∈Rn×m such that
||A −Aϵ||2 = ϵ.
(b) Let Ak = UΣkV T where Σk = diag(σ1, . . . , σk, 0, . . . , 0) and 1 ≤k ≤r −1.
Show that rank(Ak) = k and
σk+1 = ||A −Ak||2 = min {||A −B||2
|
rank(B) ≤k}
(c) Assume that r = min(m, n). Let B ∈Rn×m and assume that ||A −B||2 < σr.
Show that rank(B) = r.


---

## [2016 | individual | n=1] 2016_applied2016_individual  (chars=350)

. Consider the implicit leapfrog scheme
un+1
m
−un−1
m
2k
+ a
µ
1 + h2
6 δ2
¶−1
δ0un
m = f n
m
for the one-way wave equation
ut + aux = f.
Here δ2 is the central second difference operator, and δ0 is the central first difference
operator.
(1) show that the scheme is of order (2, 4).
(2) show that the scheme is stable if and only if |ak
h | <
1
√
3.


---

## [2016 | individual | n=2] 2016_applied2016_individual  (chars=1063)

. A simple version of an enzyme-mediate chemical reaction process is given
by
S + E
k1
←→
k2 C
k3
−→P + E
where S is the substrate reactant and P is the concentration of the desired product.
An enzyme (or catalyst) E is a compound whose special property is that it allows for
intermediate reaction steps that lead to a the overall reaction,
S −→P.
Assume the initial conditions
S(0) = S0,
E(0) = E0,
C(0) = 0,
P(0) = 0;
k1, k2, k3 are reaction rate constants.
(a) Convert the chemical reaction equation into a system of rate equations (ODEs) for
S(T), E(T), C(T), and P(T) where T is the dimensional time. Nondimensionalize
the equations using the scalings
T = t/(k1E0),
S(T) = S0s(t),
P(T) = S0p(t),
E(T) = E0s(t),
C(T) = E0c(t),
ϵ = E0
S0
≪1,
λ =
k2
k1S0
,
µ = k2 + k3
k1S0
.
(b) Use the expansions s(t) = s0(t)+ϵs1(t)+O(ϵ2), c(t) = c0(t)+ϵc1(t)+O(ϵ2), etc to
determine the equations for the leading order slow solution. Show that s0(t) and
p0(t) satisfies the following Michaelis-Menten equations
˙s0(t) = −(µ −λ)
s0
µ + s0
,
˙p0(t) = (µ −λ)
s0
µ + s0
.
1

 
2


---

## [2016 | individual | n=3] 2016_applied2016_individual  (chars=1471)

. We say that a vector u = (u1, . . . , un) ∈Nn is multiplicatively dependent
if there is a non-zero vector k = (k1, . . . , kn) ∈Zn for which
(1)
uk1
1 · · · ukn
n = 1.
This notion plays a very important role in many number theoretic algorithms, such
as factorisation and primality testing. It also (in a more general form) appears in
some questions in algebraic dynamics. However the algorithm to decide whether u
is multiplicatively dependent is not immediately obvious.
The following statement
informally means that if u is multiplicatively dependent the exponents k1, . . . , kn can
be chosen to be reasonably small. Prove that if u = (u1, . . . , un) ∈Nn is multiplicatively
dependent with ∥u∥∞≤H where ∥u∥∞= max1≤i≤n |ui|, then there is a non-zero vector
k = (k1, . . . , kn) ∈Zn with
∥k∥∞≤
µ2n log H
log 2
¶n−1
(and hence for a fixed n it can be found in polynomial time of order (log H)n(n−1)).
Comment: To solve this problem, you can use the following statement (without
proof) which informally means that if a system of homogeneous equations with integer
coefficients has a nontrivial solution then it has an integer solutions with reasonably
small components. It is required in many applications.
Let A = (aij)m,n
i,j=1 be an m × n matrix of rank r ≤n −1 with integer entries of size at
most H, that is,
|aij| ≤H,
1 ≤i ≤m, 1 ≤j ≤n.
Then there is an integer non-zero vector x = (x1, . . . , xn) ∈Zn such that Ax = 0 and
∥x∥∞≤(2nH)n−1
where ∥x∥∞= max1≤i≤n |xi|.


---

## [2016 | individual | n=4] 2016_applied2016_individual  (chars=945)

. Consider a symmetric matrix An×n, and let λi be a simple eigenvalue of
A with
|λj −λi| = O(1),
j ̸= i.
In inverse iteration of compute eigenvalue and eigenvector, one needs to solve the
following linear system
(A −µI)yk+1 = xk,
where µ is an approximation of eigenvalue λi, ∥xk∥= 1and obtain
xk+1 =
yk+1
∥yk+1∥.
However, for µ close to λi, A −µI has a very small eigenvalue and the linear system
will be ill-conditioned. So there may be large error in the numerical solution to the
linear system, denoted by ˜yk+1. Even though we may get large error in ˜yk+1, the ˜xk+1
we get from ˜xk+1 =
˜yk+1
∥˜yk+1∥is accurate.

 
3
(1) ˜yk+1 satisfies
(A −µI + δA)˜yk+1 = xk,
where ∥δA∥= O(ϵ) and ϵ is the machine precision. Show that
(A −λi) ˜yk+1
∥˜yk+1∥∥≤|µ −λi| + ∥δA∥+
1
∥˜yk+1∥.
(2) Let αi = xt
kqi, where qi is the normalized eigenvector corresponding to λi. Show
that
∥˜yk+1∥≥
|αi|
|µ −λi| + ∥δA∥.
(3) Conclude that
∥xk+1 −(±)qi∥= O(|λi −µ| + ϵ).


---

## [2016 | individual | n=5] 2016_applied2016_individual  (chars=363)

. A function f : Rn →R in C2 is called strongly convex if its Hessian
matrix satisfies ∇2f ⪰mI for some m > 0. Show that the following statements are
equivalent:
(a) f is strongly convex, i.e. ∇2f(x) ⪰mI for all x ∈Rn;
(b) For any t ∈[0, 1], any x, y ∈R,
f(tx + (1 −t)y) ≤tf(x) + (1 −t)f(y) −m
2 t(1 −t)∥x −y∥2;
(c) ⟨∇f(x) −∇f(y), x −y⟩≥m∥x −y∥2 for any x, y ∈Rn.


---

## [2016 | team | n=1] 2016_2016_team  (chars=984)

. For solving the following partial differential equation
(1)
ut + ux = 0,
−∞≤x ≤∞
with compactly supported initial condition, we consider the following one-step, three-
point scheme on a uniform mesh xj = j∆x with spatial mesh size ∆x:
(2)
un+1
j
= aun
j + bun
j−1 + cun
j−2,
j = · · · , −1, 0, 1, · · ·
where a, b, c are constants which may depend on the mesh ratio λ = ∆t
∆x. Here ∆t is
the time step, and un
j approximates the exact solution at u(xj, tn) with tn = n∆t.
(1) Find the constants a, b, c such that the scheme (2) is second order accurate.
(2) Find the CFL number λ0 such that the scheme (2), with the constants deter-
mined by the step above, is stable in L2 under the time step restriction λ ≤λ0.
(3) If the PDE (1) is defined on (0, ∞) with an initial condition compactly sup-
ported in (0, ∞) and a boundary condition u(0, t) = g(t), how would you modify
the scheme (2) so that it can be applied? Can you prove the stability and ac-
curacy of your modified scheme?


---

## [2016 | team | n=2] 2016_2016_team  (chars=810)

. Inverse problem. Answer the famous Mark Kac's equation: "can you
hear the shape of drum?" for the special case.
Consider the one-dimensional oscillator ¨x = −u′(x) with symmetric potential u(−x) =
u(x), u(0) = u′(0) = 0, u′(x) > 0 for x > 0, limx→∞u(x) = ∞. Denote the inverse
function of y = u(x), x ≥0 as x = u−1(y) = φ(y).
(a) For any solution x(t), show there is a conservation of energy
˙x2(t)
2
+ u(x(t)) ≡e
where e is a constant.
(b) For any energy e > 0, find a periodic solution with total energy e. Show that the
period is given by
P(e) = 2
√
2
Z xmax
0
dx
p
e −u(x)
,
xmax = φ(e) > 0 .
(c) Show that
φ(z) =
1
2π
√
2
Z z
0
P(e) de
√z −e .
(d) In the case of iso-chronous P(e) ≡2π, show that φ(z) =
√
2z. Then you have
u(x) = 1
2x2, x(t) = a cos(t) + b sin(t), the famous harmonic oscillator.
1

 
2


---

## [2016 | team | n=3] 2016_2016_team  (chars=511)

. The following statement informally means that if a system of homoge-
neous equations with integer coefficients has a nontrivial solution then it has an integer
solutions with reasonably small components. It is required in many applications.
Let A = (aij)m,n
i,j=1 be an m × n matrix of rank r ≤n −1 with integer entries of size at
most H, that is,
|aij| ≤H,
1 ≤i ≤m, 1 ≤j ≤n.
Prove that there is an integer non-zero vector x = (x1, . . . , xn) ∈Zn such that Ax = 0
and
∥x∥∞≤(2nH)n−1
where ∥x∥∞= max1≤i≤n |xi|.


---

## [2016 | team | n=4] 2016_2016_team  (chars=919)

. This problem considers an iterative scheme
xk+1 = xk + βkpk
for the linear system Ax = b, where A ∈Rn×n is a given n×n non-singular matrix and
b ∈Rn is a given vector. In the above scheme, xk denotes the approximate solution at
the k-th iteration, βk is a scalar and pk ∈Rn is a search direction. If xk is given, the
above scheme will determine xk+1 so that the residual rk+1 := b−Axk+1 is the smallest
possible with respect to the 2-norm.
(1) Determine βk.
(2) Prove that the residual rk+1 is orthogonal to Apk with respect to the usual
inner-product.
(3) Prove that the residuals satisfy
∥rk+1∥≤∥rk∥sin(α)
where α is the angle between rk and Apk, and ∥· ∥denotes the 2-norm.
(4) Assume that the inner product of rk and Apk is non-zero. Will the above scheme
always converge?
(5) Assume that A is positive definite. We take the search direction pk = rk. Show
that the above scheme converges for any initial guess x0.


---

## [2016 | team | n=5] 2016_2016_team  (chars=533)

. Let f : Rn →R be convex and in C1. Suppose f has a local minimum
x∗.
(1) Must this local minimum x∗be a global minimum?
(2) Consider the following backward gradient method: starting from any x0 ∈Rn,
define
xk = xk−1 −t∇f(xk),
k ≥1,
where t > 0 is a fixed step size. Do you need any condition on t to guarantee
{f(xk)} converge? Prove your convergence argument, if {f(xk)} converges.
(3) Suppose f is strongly convex, that is, ∃m > 0 such that ⟨∇f(x)−∇f(y), x−y⟩≥
m∥x −y∥2. Under this additional condition, show that {xk} converges.


---

## [2017 | individual | n=1] 2017_applied2017_individual  (chars=168)

The Chebyshev polynomial of the first kind is defined on [−1, 1] by
Tn(x) = cos(n arccos x).
Prove: The envelope for the extremals of Tn+1(x) −Tn−1(x) forms an ellipse.


---

## [2017 | individual | n=2] 2017_applied2017_individual  (chars=453)

Consider a fixed point iteration
xn = g(xn−1),
where g : R →R is a smooth function. Suppose this fixed point method does converge
to a fixed point x∗. The Steffensen algorithm is an acceleration method to find x∗
which reads
ˆxn = xn−2 −
(xn−1 −xn−2)2
xn −2xn−1 + xn−2
.
or
xn+1 = G(xn)
where
G(x) = x −
(g(x) −x)2
g(g(x)) −2g(x) + x.
(a) Show that the Steffensen algorithm {xk} converges quadratically.
(b) Can you extend this method to two dimensions?


---

## [2017 | individual | n=3] 2017_applied2017_individual  (chars=589)

We consider a piecewise smooth function
f(x) =
½
f1(x),
x ≤0,
f2(x),
x > 0
where f1(x) is a C∞function on (−∞, 0] and f2(x) is a C∞function on [0, ∞), but
f1(0) ̸= f2(0). Suppose p(x) is a k-th degree polynomial (k ≥1) interpolating f(x) at
k + 1 equally-spaced grid points xj, j = 0, 1, 2, · · · , k with xi < 0 < xi+1 for some i
between 0 and k −1. Prove that, when the grid size h = xj+1 −xj is small enough,
p′(x) ̸= 0 for xi ≤0 ≤xi+1, that is, p(x) is monotone in the interval [xi, xi+1]. (Hint:
first prove the case when f1(x) = c1, f2(x) = c2 and c1 ̸= c2 are two constants.)
1

 
2


---

## [2017 | individual | n=4] 2017_applied2017_individual  (chars=1229)

Let b ∈Rn. Suppose A ∈Mn×n(R) and B ∈Mn×n(R) are two n × n matrices. Let
A to be non-singular.
(a) Consider the iterative scheme: Axk+1 = b −Bxk.
State and prove the necessary and sufficient condition for the iterative scheme to
converge.
(b) Suppose the spectral radius of A−1B satisfies ρ(A−1B) = 0. Prove that the iterative
scheme converges in n iterations.
(c) Consider the following iterative scheme:
x(k+1) = ω1x(k) + ω2(c1 −Mx(k)) + ω3(c2 −Mx(k)) + ... + ωk(ck−1 −Mx(k))
where M is symmetric and positive definite, ω1 > 1, ω2, ..., ωk > 0 and c1, ..., ck−1 ∈
Rn. Deduce from (a) that the iterative scheme converges if and only if all eigen-
values of M (denote it as λ(M)) satisfies:
(ω1 −1)/(
k
X
i=2
ωi) < λ(M) < (ω1 + 1)/(
k
X
i=2
ωi).
(d) Let A be non-singular. Now, consider the following system of iterative scheme (*):
Ax(k+1)
1
= b1 −Bx(k)
2 ,
Ax(k+1)
2
= b2 −Bx(k)
1
Find and prove the necessary and sufficient condition for the iterative scheme (*)
to converge.
For the iterative scheme (**):
Ax(k+1)
1
= b1 −Bx(k)
2 ,
Ax(k+1)
2
= b2 −Bx(k+1)
1
Find and prove the necessary and sufficient condition for the iterative scheme (**)
to converge. Compare the rate of convergence of the iterative schemes (*) and (**).


---

## [2017 | individual | n=5] 2017_applied2017_individual  (chars=1365)

Consider the differential equation
−u′′ + αu = f, x ∈(0, 1).
Here, prime denotes for d/dx and α is a constant. We consider a mixed boundary
condition
u(0) = 0, u′(1) −bu(0) = 0.
This equation is approximated by a standard finite difference method:
−Uj−1 + 2Uj −Uj+1
h2
+ αUj = fj, j = 1, ..., N −1.
Here, N is the number of grid points, h = 1/N is the mesh size, Uj is the approximate
solution at xj := jh, and fj = f(xj). The noundary condition is approximated by
U0 = 0, UN −UN−1
h
−bUN = 0.

 
3
The resulting linear system is AU = F with


β
−1
0
· · ·
−1
β
−1
· · ·
...
−1
β
−1
0
−1
1 −bh




U1
U2...
UN−1
UN


=


h2f1
h2f2
...
h2fN−1
0


where β = 2 + αh2.
ut + aux = 0, a > 0.
We discretize this PDE by For solving the following partial differential equation
(1)
ut + f(u)x = 0,
0 ≤x ≤1
where f ′(u) ≥0, with periodic boundary condition, we can use the following semi-
discrete upwind scheme
(2)
d
dtuj + f(uj) −f(uj−1)
∆x
= 0,
j = 1, 2, · · · , N,
with periodic boundary condition
(3)
u0 = uN,
where uj = uj(t) approximates u(xj, t) at the grid point x = xj = j∆x, with ∆x = 1
N .
(a) Prove the following L2 stability of the scheme
(4)
d
dtE(t) ≤0
where E(t) = PN
j=1 |uj|2∆x.
(b) Do you believe (4) is true for E(t) = PN
j=1 |uj|2p∆x for arbitrary integer p ≥1?
If yes, prove the result. If not, give a counterexample.


---

## [2017 | team | n=1] 2017_2017_team  (chars=924)

Given an integer parameter K, one can test whether for a vector ⃗u = (u1, . . . , un) ∈
Nn there is non-zero vector ⃗k = (k1, . . . , kn) ∈Zn with
∥⃗k∥∞≤K and uk1
1 · · · ukn
n = 1,
where ∥⃗k∥∞= max1≤i≤n |ki| in about O((2K + 1)n) arithmetic operations with inte-
gers having about O(nK log(∥⃗u∥∞+1)) bits via testing all possible combinations of the
exponents (ordered lexicographically) and direct computation.
Assuming that the memory is essentially unlimited, suggest a better algorithm which
uses about O((2K + 1)n/2) arithmetic operations with integers of the same size as
above.
Hints: (i) Use the divide-and-conquer strategy; (ii) Recall that a list L of M real
numbers can be sorted via O(M log M) comparisons; (iii) A sorted list L of M real
numbers can be searched for x ∈L via O(log M) comparisons; (iv) To decide whether
a/b > c/d for two rational numbers with b, d > 0 we simply compare the products ad
and bc.


---

## [2017 | team | n=2] 2017_2017_team  (chars=826)

We have the following partial differential equation
(1)
ut = H(u)xx,
0 ≤x < 1
with an initial condition u(x, 0) = f(x) and periodic boundary condition. Here 0 ≤
H′(u) ≤d. Consider the following one-step, three-point scheme on a uniform mesh
xj = j∆x with spatial mesh size ∆x:
(2)
un+1
j
= un
j + aH(un
j−1) + bH(un
j ) + cH(un
j+1),
where a, b, c are constants which may depend on the mesh ratio µ =
∆t
∆x2, ∆t is the
time step, and un
j approximates the exact solution at u(xj, tn) with tn = n∆t.
(1) Find the constants a, b, c such that the scheme (2) is second order accurate.
(2) Find the CFL number µ0 such that the scheme (2), with the constants deter-
mined by Step 1 above, is stable under the time step restriction µ ≤µ0. Please
specify which norm you are using for stability, and prove this stability result.
1

 
2


---

## [2017 | team | n=3] 2017_2017_team  (chars=998)

Consider the problem describing projectile motion on the surface of the Earth,
written in physical variables as follows:
d2y
dt2 = −
GM
(R + y)2,
y(0) = 3m,
y′(0) = −V m/sec
Let y(t) = L˜y(˜t) and t = T˜t. Consider two out of the following four cases:
(a): R = O(1), V →∞, M = O(1): the fast projectile limit
(b): R = O(1), V = O(1), M →∞: the dense Earth limit
(c): R = O(1), V = O(1), M →0: the light Earth limit
(d): R →0, V = O(1), M = O(1): the small Earth limit (two possible scalings,
determine both)
In each case:
• Choose your scalings for L, T to normalize as many terms as possible. Pick your
scalings so that the time it takes for the projectile to fall to ˜y = 0 is ˜t = O(1).
• Write the scaled (normalized) problem, identify all remaining dimensionless
parameters.
• Identify a limiting small parameter and the leading order problem.
Note: DO NOT solve-out the problems, just write them!
Hint: If any scaled coefficients blow-up in the leading order problem, the scaling is
not good.


---

## [2017 | team | n=4] 2017_2017_team  (chars=1482)

Let f be an arbitrary function in Cn(R). Given n distinct points x1, x2, · · · , xn ∈R
and an extra point x0 ∈R, we want to approximate f ′(x0) using a linear combina-
tion of the function values at x1, x2, · · · , xn, i.e. we want to compute the coefficients
c1, c2, · · · , cn such that
f ′(x0) ≈c1f(x1) + c2f(x2) + · · · + cnf(xn)
in some sense.
(a) Consider the undetermined coefficients method. You use Taylor expansion to
expand each f(xi), i = 1, 2, · · · , n about the point x0,
f(xi) =
n−1
X
k=0
1
k!f (k)(x0)(xi −x0)k + 1
n!f (n)(ξi)(xi −x0)n,
ξi ∈[x0, xi] or [xi, x0],
and choose the coefficients so that the resulting approximation is as accurate
as possible. This gives you the linear system
1
k!
n
X
i=1
ci(xi −x0)k = δk,1,
k = 0, 1, · · · , n −1,
where δk,1 = 1 if k = 1; otherwise δk,1 = 0. Explain why this linear system
is nonsingular. Then use this method to solve the case when n = 3, x1 = x0,
x2 = x0 + h, x3 = x0 + 2h for some constant h.

 
3
(b) You can also make use of interpolation method. Consider the n-point interpo-
lating polynomial
p(x) =
n
X
i=1
³
n
Y
j=1,j̸=i
x −xj
xi −xj
´
f(xi),
and the approximation is given by
f ′(x0) ≈p′(x0).
This gives the coefficients as
ci =
³
n
Y
j=1,j̸=i
x −xj
xi −xj
´′¯¯¯
x=x0.
Show that the approximation of this method is exact if f is a polynomial of
degree no more than n −1.
(c) Show that the two methods given in (a) and (b) are essentially the same, i.e.
the coefficients obtained in (a) and (b) are the same.


---

## [2017 | team | n=5] 2017_2017_team  (chars=140)

Let
A =


2
−1
−1
2
−1
...
−1
2
−1
−1
γ


Find A−1 explicitly. Show that all entries of A−1 are nonnegative if and only if γ ≥1.


---

## [2018 | individual | n=1] 2018_applied2018_individual  (chars=798)

We consider the following convection-diffusion equation
(1)
ut + aux = buxx,
0 ≤x < 1
with an initial condition u(x, 0) = f(x) and periodic boundary condition, where a and
b > 0 are constants. The first order IMEX (implicit-explicit) time discretization and
second order central spatial discretization are used to give the following scheme:
(2)
un+1
j
−un
j
∆t
+ aun
j+1 −un
j−1
2∆x
= bun+1
j+1 −2un+1
j
+ un+1
j−1
∆x2
with a uniform mesh xj = j∆x with spatial mesh size ∆x and time step ∆t. Here un
j is
the numerical solution approximating the exact solution of (1) at x = xj and t = n∆t.
Prove that the scheme is L2 stable under the very mild time step restriction
(3)
∆t ≤c
with a constant c which is independent of ∆x. Can you determine the dependency of
c on the two constants a and b in (1)?


---

## [2018 | individual | n=2] 2018_applied2018_individual  (chars=959)

Velocity-Verlet method.
(a) Recast the following Newtonian formula for the acceleration and potential force
q′′(t) = −∇V (q),
into a Hamiltonian system and show that the corresponding map on the phase
space is symplectic.
(b) Show that the velocity-Verlet (recovered many times: Delambre 1791, Størmer in
1907, Cowell & Crommelin 1909, Verlet 1960s) method
pn+1/2 = pn −∆t
2 ∇V (qn);
qn+1 = qn + ∆tpn+1/2;
pn+1 = pn+1/2 −∆t
2 ∇V (qn+1)
is symplectic and is second order accurate.
Hint: Let u(t) = (p(t), q(t)) be a solution of the Hamiltonian system with initial data
u0 = (p0, q0) and we view the solution u(t) as a map map on the phase space ϕt :
Rd × Rd →Rd × Rd ϕt(u0) = u(t). We call the flow map is symplectic if its Jacobian
Φt(u0) = ∂ϕt(u0)
∂u0
=
Ã∂p(t)
∂p0
∂p(t)
∂q0
∂q(t)
∂p0
∂q(t)
∂q0
!
satisfies Φt(u0)TJΦt(u0) = J for any u0 ∈Rd × Rd. Here J =
¡ 0
I
−I 0
¢
.
A scheme ϕn(u0), n = 1, 2 . . . , is symplectic if the map ϕn(u0) is symplectic.
1

 
2


---

## [2018 | individual | n=3] 2018_applied2018_individual  (chars=1727)

We begin with some definitions.
(1) A graph G is a pair G = (V, E) where V is a finite set, called the vertices of G,
and E is a subset of P2(V ) (i.e., a set E of (unordered) two-element subsets of V ),
called the edges of G. A simple graph G is a graph without loops (edge that connects a
vertex to itself) or multiple edges between any pair of vertices. The order of the graph
is |V |. We often put V = {v1, v2, · · · , vn} and E = {vivj| vi and vj are adjacent}.
(2) Two vertices x and y are adjacent if xy ∈E. The neighborhood of a vertex x,
denoted by NG(x) or N(x), is the set of vertices that is adjacent to x. The degree
of a vertex x, denoted by dG(x) or d(x), is |N(x)| (i.e. the number of vertices that is
adjacent to x).
(3) A path is a collection of distinct vertices vi1vi2 · · · vik such that vijvij+1 ∈E for
all j, 1 ≤j < k. vi1 and vik are the ends of the path. A Hamiltonian path P is a
path containing all vertices of the graph. A cycle is a closed path with vi1 = vik. A
Hamiltonian cycle is a cycle containing all vertices of the graph. A graph is called
Hamiltonian if it has a Hamiltonian cycle.
(4) A graph G is (Hamilton) connected, if for every pair of vertices there is a (Hamil-
tonian) path between them.
An example of a simple graph: V = {v1, v2, v3, v4} and E = {v1v2, v2v3, v3v4, v2v4}.
In this graph, the order of the graph is 4, N(v1) = {v2}, N(v4) = {v2, v3}, d(v3) = 2,
d(v2) = 3 and v1v2v4v3 is a Hamiltonian path with ends v1 and v3.
Let G be a simple graph of order n. Suppose that the degree sum of any pair of
nonadjacent vertices is at least n+1. Show that G is Hamilton-connected (i.e. between
any pair of vertices x and y, there is a Hamiltonian path in which x and y are the ends).


---

## [2018 | individual | n=4] 2018_applied2018_individual  (chars=703)

Define the Hermite polynomials as
(4)
Hn(x) = (−1)n exp(x2
2 ) dn
dxn[exp(−x2
2 )],
x ∈(−∞, +∞), n = 0, 1, 2, · · · .
(a) Prove the weighted orthogonality of the Hermite polynomials:
(5)
⟨Hn(x), Hm(x)⟩ρ ≜
Z +∞
−∞
ρ(x)Hn(x)Hm(x)dx = n!
√
2πδn,m,
where ρ(x) = exp(−x2
2 ).
(b) Prove the three recurrence formula:
(6)
Hn+1(x) = xHn(x) −nHn−1(x),
n ≥1,
and then show that for all n ≥1, Hn(x) and Hn−1(x) share no common roots.
(c) Use the recurrence formula and induction to prove the differential relation:
(7)
d
dxHn(x) = nHn−1(x),
n ≥1,
and then prove that Hn is an eigenfunction of the following eigenvalue problem
(8)
xu′(x) −u′′(x) = λu.
You need to find the eigenvalue λn corresponding to Hn(x).

 
3


---

## [2018 | individual | n=5] 2018_applied2018_individual  (chars=678)

Take σi(A) to be the i-th singular value of the square matrix A ∈Rn×n. Define the
nuclear norm of A to be
∥A∥∗≡
n
X
i=1
σi(A).
(1) Show that ∥A∥∗= tr(
√
ATA).
(2) Show that ∥A∥∗= max
XT X=I tr(AX).
(3) Show that ∥A + B∥∗≤∥A∥∗+ ∥B∥∗
(4) Explain informally why minimizing ∥A −A0∥2
F + ∥A∥∗over A for a fixed A0 ∈
Rn×n might yield a low-rank approximation of A0.
Notation: The trace of a matrix tr(A) is the sum P
i aii of its diagonal elements. We
define the square root of a symmetric positive semidefinite matrix M to be
√
M ≡
UD1/2U T, where D1/2 is the diagonal matrix containing (nonnegative) square roots of
the eigenvalues of M and U contains the eigenvectors of M = UDU T.


---

## [2018 | team | n=1] 2018_2018_team  (chars=492)

Let H be a bipartite graph with the bipartition V = V1 ∪V2, where |V1| = |V2| = n.
We say that H satisfies the (p, q)-condition if (i) for all subsets I ⊆V1 of cardinality at
most p, the inequality |I| ≤|N(I)| holds, and (ii) for all subsets J ⊆V2 of cardinality
at most q, the inequality |J| ≤|N(J)| holds. Note that the (n, 0)-condition is Hall's
original condition in his marriage theorem.
Prove that if H satisfies the (p, q)-condition with n ≤p + q, then H contains a
matching of size n.


---

## [2018 | team | n=2] 2018_2018_team  (chars=1573)

Let Cn be the n dimensional hypercube, i.e., the graph whose vertex set V is {0, 1}n,
and whose edges are defined by: two vertices u = u1u2 . . . un and v = v1v2 . . . vn are
adjacent iffui ̸= vi for exactly one i ∈[n]. Let R[V ] be the vector space of all the
functions f : V →R. The space R[V ] has a natural inner product. For f, g ∈R[V ],
< f, g >=
X
u∈{0,1}n
f(u)g(u).
The standard basis of R[V ] is the set {fu : u ∈{0, 1}n} where fu(v) = δu,v, the
Kronecker delta, for u, v ∈{0, 1}n. Denote by B1 the standard basis.
(1) For any two vertices u, v ∈{0, 1}n, u · v is defined to be P
i uivi. For each
u ∈{0, 1}n, define a function χu ∈R[V ] by letting
χu(v) = (−1)u·v.
Prove that the set {χu : u ∈{0, 1}n} is orthogonal with respect to the inner
product of R[V ], i.e.,
< χu, χv >= δu,v2n,
for all u, v ∈{0, 1}n.
(2) Prove that the set {χu : u ∈{0, 1}n} forms a basis of the vector space R[V ].
Denoted by B2 this basis.
(3) For 1 ≤i ≤n, let ei = (0, . . . , 0, 1, 0, . . . , 0) ∈{0, 1}n where the only 1 occurs
in position i. Let S = {e1, e2, . . . , en}.
Define a linear transformation Φ : R[V ] →R[V ] as follows. For f ∈R[V ],
Φf is the element in R[V ] which is given by
(Φf)(v) =
X
ei∈S
f(v + ei)
where v + ei is the usual vector addition modulo 2.
Prove that the matrix of Φ with respect to the standard basis B1 is just
A(Cn), the adjacency matrix of the hypercube Cn.
1

 
2
(4) Prove that Φχu = λuχu for each u ∈{0, 1}n, where
λu =
X
e∈S
(−1)u·e = n −2|u|,
where |u| is the number of 1's in u = u1u2 . . . un.
(5) Compute the eigenvalues of the matrix A(Cn).


---

## [2018 | team | n=3] 2018_2018_team  (chars=578)

Let A ∈Rn×n, and assume that there are unitary matrix Q and diagonal matrix
D = diag(λ1, · · · , λn) such that A = QDQ∗. Let Ek be the space spanned by the first
k columns of Q. We let
bP =
µ
Ik
0
¶
,
P = Q bPQ∗
where Ik is the k × k identity matrix.
(1) Show that P is an orthogonal projection onto Ek.
(2) Assume that
|λ1| ≥· · · ≥|λk| > |λk+1| ≥· · · ≥|λn|.
Let X(0) ∈Rn×k and assume PX(0) is injective. We define the iterations
X(m+1) = AX(m).
Show that there is a matrix Λ ∈Rk×k such that
∥(AX(m) −X(m)Λ)y∥
∥PX(m)y∥
≤
³|λk+1|
|λk|
´m∥(AX(0) −X(0)Λ)y∥
∥PX(0)y∥
,
∀y ∈Rk\{0}.


---

## [2018 | team | n=4] 2018_2018_team  (chars=669)

For the one-way equation
(1)
ut + aux = f,
consider the multistep scheme given by
(2)
3un+1
m
−4un
m + un−1
m
2k
+ aun+1
m+1 −un+1
m−1
2h
= f n+1
m
.
(1) Show that the scheme is second order accurate.
(2) Show that the scheme is unconditionally stable.
(Hint: (i) apply von Neumann analysis to the scheme with f ≡0 and find
the characteristic polynomial.
(ii) show that for all k, h, the characteristic
polynomial satisfies the root condition: all roots reside in the unit disk, and
all roots on the unit circle are simple. (iii) for a root r of the characteristic
polynomial, it would be more convenient to study the form 1
r = X + iY and
prove that X2 + Y 2 ≥1.)

 
3


---

## [2018 | team | n=5] 2018_2018_team  (chars=1768)

For a convex function f : D →R, where D ⊆Rn is convex and open, define a
subgradient of f at x0 ∈D to be any vector s ∈Rn such that
f(x) −f(x0) ≥s · (x −x0)
for all x ∈D. The subgradient is a plausible choice for generalizing the notion of a
gradient at a point where f is not differentiable. The subdifferential ∂f(x0) is the set
of all subgradients of f at x0.
(1) What is ∂f(0) for the function f(x) = |x|.
(2) Suppose we wish to minimize a convex and continuous function f : Rn →
R, which may not differentiable everywhere. Propose an optimality condition
involving subdifferential for a point x∗to be a minimizer of f. Show that your
condition holds if and only if x∗is a globally minimizer f.
(3) The subgradient method extends the gradient descent to a wider class of func-
tions. Analogously to the gradient descent, the subgradient method performs
the iteration
xk+1 = xk −αgk,
where α > 0 is small stepsize that is known as the learning rate, and gk is any
subgradient of f at xk. This method might not decrease f in each iteration, so
instead we keep track of the best iterate we have seen so far, xbest
k
.
In the following parts, assume that f is Lipschitz continuous with constant
L > 0, ∥x1 −x∗∥2 ≤B for some B > 0. Under these assumptions we will show
that
(3)
lim
k→∞f(xbest
k
) ≤f(x∗) + L2
2 α,
a bound characterizing convergence of the subgradient method.
(a) Derive an upper bound for the error ∥xk+1 −x∗∥2
2 of xk+1 in terms of
∥xk −x∗∥2
2, gk, α, f(xk) and f(x∗).
(b) By recursively applying the result from Problem 3a, provide an upper
bound for ∥xk+1 −x∗∥2
2.
(c) Incorporate f(xbest
k
) into your upper bound in Problem 3b, and take a limit
as k →∞to obtain the desired convergence result (3).
(d) Suggest a best choice of the learning rate α.


---

## [2019 | individual | n=1] 2019_AppliedMath2019_individual  (chars=625)

(20 points)
Given a set X, m ∈N and a hypothesis space H, define
ΠH(m) =
max
{x1,x2,...,xm}⊆X |{(h(x1), h(x2), . . . , h(xm))|h ∈H}|
where |S| denotes the cardinality of the set S. The VC dimension of H is
VC(H) = max{m : ΠH(m) = 2m}.
(i) Let X = R. If a ⩽b, define h(x; a, b) = 1 if x ∈[a, b] and h(x) = −1 if x /∈[a, b]. Find the VC
dimension of the hypothesis space H = {h(x; a, b)|a, b ∈R, a ⩽b}.
(ii) Let X = Rd, H to be the set of linear classifiers, i.e. H = {f(x)|f(x) = sign(w⊤x + b), w ∈Rd, b ∈
R} where sign(x) = 1 if x > 0, sign(x) = −1 if x < 0 and sign(x) = 0 if x = 0. Show that the VC
dimension of H is d + 1.


---

## [2019 | individual | n=2] 2019_AppliedMath2019_individual  (chars=477)

(25 points)
Consider Richardson's difference scheme for the heat equation ut = uxx :
1
2k (u(x, t + k) −u(x, t −k)) = 1
h2 (u(x −h, t) −2u(x, t) + u(x + h, t)) .
(i) Show that this scheme has second-order truncation error.
(ii) Use either ODE principles or von Neumann analysis to show that this scheme is unconditionally
unstable.
(iii) Demonstrate a minor modification of the left-side of Richardson's scheme that yields a familiar
unconditionally stable scheme and prove it.


---

## [2019 | individual | n=3] 2019_AppliedMath2019_individual  (chars=552)

(25 points)
Let ∅̸= K be a closed convex set in Rn, i.e., K is a closed set and for any x, y ∈K and λ ∈(0, 1),
λx + (1 −λ)y ∈K. For any z ∈Rn, let ΠK(z) denote the metric projection of z onto K, which is the
unique optimal solution of following problem:
min 1
2∥y −z∥2
2,
s.t.
y ∈K.
(1)
Show that
(i) the point y ∈K solves (1) if and only if
(z −y)T (d −y) ⩽0,
∀d ∈K;
(ii) for any y, z ∈Rn,
∥ΠK(y) −ΠK(z)∥2 ≤∥y −z∥2;
(iii) Θ(·) is continuously differentiable with its gradient given by
∇Θ(z) = z −ΠK(z),
where for any z ∈Rn, Θ(z) := 1
2∥z −ΠK(z)∥2
2.
1


---

## [2019 | individual | n=4] 2019_AppliedMath2019_individual  (chars=884)

(25 points) The scientists FitzHugh (1961) and Nagumo, Arimoto, Yoshizawa (1962) derived a math-
ematical model to characterize the behavior of a neuron under the externally injected current I:
(
dV
dt
= V −1
3V 3 −W + I,
dW
dt
= 1
τ
¡
V + a −bW
¢
,
where the variable V describes the membrane potential of the neuron, the variable W describes the
current arising from opening and closing of ion channels on the neurons membrane. The variables τ,
a and b are parameters with typical values: a = 0.7,b = 0.8 and τ = 13.
(i) For a small positive constant current I, how the neuron behaves.
(ii) For a large positive constant current I, how the neuron behaves.
(iii) Suppose one injects a pulse current with different magnitude at some time t0, i.e., I = I0δ(t −t0),
where I0 describes the magnitude of the pulse, analyze the dynamical behavior of the neuron when I0
is small or large.
2


---

## [2019 | team | n=1] 2019_AppliedMath2019_team  (chars=170)

(10 points)
Show that the quadrature formula
Z 1
−1
f(x)
√
1 −x2 dx = π
n
n−1
X
k=0
f
µ
cosπ 2k + 1
2n
¶
is exact for all polynomials
of degree up to and including 2n −1.


---

## [2019 | team | n=2] 2019_AppliedMath2019_team  (chars=296)

(15 pointes) Let x = (x0, . . . , xN−1) ∈RN, x ̸= 0 and ˆx be its discrete Fourier transform, i.e.
ˆxw =
1
√
N
N−1
X
t=0
xt exp(−2πiwt/N), w = 0, . . . , N −1.
Prove that ∥x∥0∥ˆx∥0 ⩾N where ∥x∥0 denotes the number of nonzero entries in x. (Hint: show that ˆx
can not have ∥x∥0 consecutive zeros.)


---

## [2019 | team | n=3] 2019_AppliedMath2019_team  (chars=461)

(20 pointes)
Let m ⩽n. Consider the (n + m) × (n + m) real matrix defined by
A =
· I
X
X⊤
O
¸
,
where I is the n × n identity matrix, X is a full-rank n × m matrix, O is the m × m zero matrix.
(i) Show that A is nonsingular.
(ii) Find the eigenvalues of A, some of which are in terms of the singular values of X.
(iii) Under what conditions on X would the iteration
xn+1 = xn −(Axn −b)
converge to the solution of Ax = b for any (n + m) × (n + m) real vector b?


---

## [2019 | team | n=4] 2019_AppliedMath2019_team  (chars=566)

(25 pointes)
Let f be a continuously differentiable convex function defined on Rn, i.e., f : Rn →R is continuously
differentiable and for any x, y ∈Rn and any α ∈(0, 1), f(αx + (1 −α)y) ≤αf(x) + (1 −α)f(y).
Suppose that the gradient of f is Lipschitz continuous, i.e., there exists a constant L > 0 such that
∥∇f(x) −∇f(y)∥2 ≤L∥x −y∥2.
Prove the following inequalities:
(i). f(y) ≤f(x) + (∇f(x))T (y −x) + L
2 ∥y −x∥2
2,
∀x, y ∈Rn;
(ii). f(y) ≥f(x) + (∇f(x))T (y −x) +
1
2L∥∇f(y) −∇f(x)∥2
2,
∀x, y ∈Rn;
(iii).
1
L∥∇f(y) −∇f(x)∥2
2 ≤(∇f(y) −∇f(x))T (y −x),
∀x, y ∈Rn.


---

## [2019 | team | n=5] 2019_AppliedMath2019_team  (chars=452)

(30 pointes) Consider the following problems.
(i) Determine the order of St¨ormer's method,
yn+2 −2yn+1 + yn = h2f(tn+1, yn+1),
n ⩾0,
for solving the second order system of ODE's
y′′ = f(t, y),
t ⩾0,
with the initial conditions y(0) = y0 and y′(0) = y′
0.
(ii) Using the second order central differences in space and St¨ormer's method in time, construct a
scheme to solve the wave equation,
utt = uxx.
(iii) Determine the condition for its stability.
1


---

## [2020 | individual | n=1] 2020_Applied_Math_and_Computational_Math_computational_and_applied_20  (chars=389)

.
Let f ∈Ck+1[−1,1] and [−1,1] be partitioned into subintervals Ij = [(j −1)h, jh] of
width h. Assume p is a polynomial of degree k which approximates f in Ij with
max
x∈Ij
pj(x) −f (x)
 ≤C0hk+1,
where C0 is a constant independent of j. Show that there exists an another constant C, independent
of j, such that
max
x∈Ij±1
pj(x) −f (x)
 ≤Chk+1.
(as long as Ij±1 ⊂[−1,1], of course).


---

## [2020 | individual | n=2] 2020_Applied_Math_and_Computational_Math_computational_and_applied_20  (chars=253)

. Consider the iteration
xn+1 = xn −

xn −x0
f (xn) −f (x0)

f (xn)
for finding the roots of a two times continuous differentiable function f (x). Assuming the method
converges to a simple root x∗, what is the rate of convergence? Justify your answer.


---

## [2020 | individual | n=3] 2020_Applied_Math_and_Computational_Math_computational_and_applied_20  (chars=407)

.
Suppose A is an m × m matrix with a complete set of orthonormal eigenvectors
q1,. . .,qm and corresponding eigenvalues λ1,. . .,λm. Assume that |λ1| > |λ2| > |λ3| and λj ≥λj+1
for j = 3,. . .,m. Consider the power method v(k) = Av(k−1)/λ1, with v(0) = α1q1 + · · · + αmqm
where α1 and α2 are both nonzero. Show that the sequence {v(k)}∞
k=0 converges linearly to α1q1 with
asymptotic constant C = |λ2/λ1|.


---

## [2020 | individual | n=4] 2020_Applied_Math_and_Computational_Math_computational_and_applied_20  (chars=402)

.
For the initial value problem y′ = f (t, y), y(0) = y0 on the interval [0, T], consider
the implicit two-step method
yn+1 = 4
3 yn −1
3 yn−1 + 2h
3 f (tn+1, yn+1),
y1 = y0 + h f (t1, y0),
where h is the step size and tn = nh.
(a) What is the order of the accuracy of the scheme?
(b) Check the stability of the scheme by analyzing the stability polynomial?
(c) Find the stability region of the scheme.


---

## [2020 | individual | n=5] 2020_Applied_Math_and_Computational_Math_computational_and_applied_20  (chars=155)

. Suppose the difference scheme un+1 = Bun is stable, and C(∆t) is a bounded family of

 
operators. Show that the scheme
un+1 = (B + ∆tC(∆t))un
is stable.


---

## [2020 | individual | n=6] 2020_Applied_Math_and_Computational_Math_computational_and_applied_20  (chars=230)

.
Let A be an m × m nonsingular matrix. Suppose infpn ∈Pn ||pn(A)|| = ||p∗(A)|| > 0
where Pn denotes the set of all degree-n monic polynomials:
Pn = {p : p is a polynomial of degree n, p(z) = zn + · · · } .
Prove that p∗is unique.


---

## [2021 | individual | n=1] 2021_ExamPaper_21S_computational_and_applied_21s  (chars=336)

.
(a) Show that
Tn(x) = cos(n arccos x),
x ∈[−1,1],
is a polynomial of degree n with extrema at
xk = cos

k π
n

,
k = 0,1,. . .,n
and leading coefficient 2n−1.
(b) Show that if f ∈Cn+1[−1,1] and if P(x) is the polynomial with degree at most n that interpolates f
at xk, k = 0,1,. . .,n then
∥f (x) −P(x)∥∞≤
1
2n−1(n + 1)!

 f n+1

∞.


---

## [2021 | individual | n=2] 2021_ExamPaper_21S_computational_and_applied_21s  (chars=161)

.
Let S(x) be a cubic spline with knots {ti}n
i=0. If it is determined that S(x) is linear over [t1,t2]
and [t3,t4]. Prove that S(x) is also linear over [t2,t3].


---

## [2021 | individual | n=3] 2021_ExamPaper_21S_computational_and_applied_21s  (chars=503)

. Let f : R →R be defined by f (x) = 2x −cos x.
(a) Prove that the equation f (x) = 0 has a unique solution x∗∈R that lies in the interval (1
4, 1
2).
(b) Prove that the sequence defined by the fixed point iteration
x0,
xn = 1
2 cos xn−1,
n = 1,2,. . .
converges to x∗with any initial guess x0.
(c) For the fixed point iteration in (b) with x0 = π
6 , determine an n that guarantees |xn −x∗| < 1
2 × 10−8.
For the fixed point iteration in (b) with x0 = 20, determine an n that guarantees |xn −x∗| < 1
4.


---

## [2021 | individual | n=4] 2021_ExamPaper_21S_computational_and_applied_21s  (chars=562)

. Let matrix A ∈Rm×n with m ≥n and r = rank(A) < n, and assume A has the following SVD
decomposition
A = [U1,U2]
Σ1
0
0
0

[V1,V2]T = U1Σ1VT
1 ,
where Σ1 is r × r nonsingular and U1 and V1 have r columns. Let σ = σmin(Σ1), the smallest nonzero
singular value of A. Consider the following least square problem, for some b ∈Rm,
min
x∈Rn ∥Ax −b∥2 .

 
(a) Show that all solutions x can be written as
x = V1Σ−1
1 UT
1 b + V2z2,
with z2 an arbitrary vector.
(b) Show that the solution x has minimal norm ∥x∥2 precisely when z2 = 0, and in which case,
∥x∥2 ≤∥b∥2
σ .


---

## [2021 | individual | n=5] 2021_ExamPaper_21S_computational_and_applied_21s  (chars=372)

. Consider the family of semi-implicit Runge-Kutta methods
k1 = f (yn + βhk1),
k2 = f (yn + hk1 + βhk2),
yn+1 = yn + h

( 1
2 + β)k1 + (1
2 −β)k2

.
(a) Determine the order and the principal part of the local truncation error.
(b) Show that if β > 1
2, then the negative real axis {z : Re(z) < 0,Im(z) = 0} is contained in the region of
absolute stability of the method.


---

## [2021 | individual | n=6] 2021_ExamPaper_21S_computational_and_applied_21s  (chars=901)

. Consider the Beam equation from mechanics with boundary conditions that model a cantilever
beam:
u(4) = f (x),
x ∈(0, 1),
u(0) = u′(0) = u′′(1) = u′′′(1) = 0.
(1)
(a) Recast this equation into a variational problem, stating the trial and test function spaces.
(b) Interpret the variational problem as an energy minimization problem, clearly stating the energy
functional. Prove that the variational problem and the energy minimization problems are equivalent.
(c) Develop a CG(3) (cubic continuous Galerkin method) finite element method for this problem.
(d) Prove an a priori error estimate for this method in the energy norm:
∥e∥E =
 ∫1
0
(e′′)2dx
 1
2
,
Where e = u(x) −U(x), in which, u(x) is the exact solution to VP (variational problem), U(x) is the
FEM (finite element method) solution.
(e) Prove an a priori error estimate for this method in the L2 norm:
∥e∥L2 =: ∥e∥=
 ∫1
0
e2dx
 1
2
.


---

## [2022 | individual | n=1] 2022_ExamPaper_2022_computational_and_applied_22s  (chars=499)

. Consider {𝑝𝑖(𝑥)}∞
𝑖=0, a family of orthogonal polynomials associated with the inner product
⟨𝑓, 𝑔⟩= ∫
1
−1
𝑓(𝑥)𝑔(𝑥)𝑤(𝑥) 𝑑𝑥,
𝑤(𝑥) > 0
for 𝑥∈(−1, 1),
where 𝑝𝑖(𝑥) is a polynomial of degree 𝑖. Let 𝑥0, 𝑥1, … , 𝑥𝑛be the roots of 𝑝𝑛+1(𝑥). Construct an orthonormal
basis in the subspace of the polynomials of degree no more than 𝑛such that, for any polynomial in this subspace,
the coefficients of its expansion into the basis are equal to the scaled values of this polynomial at the nodes
𝑥0, 𝑥1, … , 𝑥𝑛.


---

## [2022 | individual | n=2] 2022_ExamPaper_2022_computational_and_applied_22s  (chars=506)

. Consider a 2D fixed point iteration of the form
𝑥𝑘+1 = 𝑓(𝑥𝑘, 𝑦𝑘), 𝑦𝑘+1 = 𝑔(𝑥𝑘, 𝑦𝑘).
(1)
Assume that the vector-valued function
⃗𝐻(𝑥, 𝑦) = (𝑓(𝑥, 𝑦), 𝑔(𝑥, 𝑦))𝑇is continuously-differentiable, and the infin-
ity norm of the Jacobian matrix is less than 1 at a unique fixed point (𝑥∞, 𝑦∞).
Now consider a new iteration:
𝑥𝑘+1 = 𝑓(𝑥𝑘, 𝑦𝑘),
𝑦𝑘+1 = 𝑔(𝑥𝑘+1, 𝑦𝑘).
(2)
Prove that iteration (2) is convergent, to the same fixed point as iteration (1), for the initial conditions sufficiently
close to the fixed point.


---

## [2022 | individual | n=3] 2022_ExamPaper_2022_computational_and_applied_22s  (chars=276)

. Let 𝐴∈𝐑𝐦×𝐦be a matrix with entries 𝑎𝑖𝑗which satisfy
𝑎𝑖𝑖≥∑
𝑗≠𝑖
|𝑎𝑖𝑗| + 2,
𝑎𝑖𝑖≤7.
(a) Prove that 𝐴−1 exists.
(b) Prove that ‖𝐴‖∞is the max row sum (of absolute values) of 𝐴.
(c) Find both a lower and upper bound for ‖𝐴‖∞.
(d) Now assume 𝐴= 𝐴𝑇. Find bounds for ‖𝐴‖2 and ‖𝐴−1‖2.


---

## [2022 | individual | n=4] 2022_ExamPaper_2022_computational_and_applied_22s  (chars=832)

. Consider a system of ODE initial value problems of the form:
𝑑
𝑑𝑡𝑢= 𝑓(𝑢),
𝑢(0) = 𝑢0.
Assume that 𝑓(𝑢) has the property that the forward Euler (FE) method:
𝑈𝑛+1 = 𝑈𝑛+ 𝑘𝑓(𝑈𝑛),
satisfies
‖𝑈𝑛+1‖ ≤‖𝑈𝑛‖

 
for some norm ‖ ⋅‖ and for all time-steps 𝑘, 0 < 𝑘≤𝑘𝐹𝐸. Now consider the 2-stage Runge-Kutta method:
𝑈(1) = 𝑈𝑛+ 𝑘𝛽10𝑓(𝑈𝑛),
𝑈𝑛+1 = {𝛼20𝑈𝑛+ 𝑘𝛽20𝑓(𝑈𝑛)} + {𝛼21𝑈(1) + 𝑘𝛽21𝑓(𝑈(1))}
where
𝛽10 ≥0,
𝛽20 ≥0,
𝛽21 ≥0,
𝛼20 ≥0,
𝛼21 ≥0,
𝛼20 + 𝛼21 = 1.
(a) Prove that the above 2-stage Runge-Kutta method also satisfies the inequality:
‖𝑈𝑛+1‖ ≤‖𝑈𝑛‖
under some appropriate time-step restriction: 0 ≤𝑘≤𝑘∗, where you need to explicitly determine 𝑘∗in
terms of 𝑘𝐹𝐸.
(b) Explicitly determine the coefficients:
𝛽10,
𝛽20,
𝛽21,
𝛼20,
𝛼21,
so that
(i) The method is second-order accurate; and
(ii) The maximum allowed time-step, 𝑘∗, is as large as possible.


---

## [2022 | individual | n=5] 2022_ExamPaper_2022_computational_and_applied_22s  (chars=538)

. Construct a third-order accurate Lax-Wendroff-type method for 𝑢𝑡+ 𝑎𝑢𝑥= 0 (𝑎> 0 is a constant)
in the following way:
(a)
• Expand 𝑢(𝑡+ 𝑘, 𝑥) in a Taylor series and keep the first four terms. Replace all time derivatives by
spatial derivatives using the equation.
• Construct a cubic polynomial passing through the points 𝑈𝑛
𝑗−2, 𝑈𝑛
𝑗−1, 𝑈𝑛
𝑗, 𝑈𝑛
𝑗+1.
• Approximate the spatial derivatives in the Taylor series by the exact derivatives of the above con-
structed cubic polynomial.
(b) Verify that the truncation error is 𝑂(𝑘3) if ℎ= 𝑂(𝑘).


---

## [2022 | individual | n=6] 2022_ExamPaper_2022_computational_and_applied_22s  (chars=594)

. Suppose you have $60K to invest and there are 3 investment options available. You must invest in
multiples of $10𝐾. If 𝑑𝑖dollars are invested in investment 𝑖then you receive a net value (as the profit) of 𝑟𝑖(𝑑𝑖)
dollars. For 𝑑𝑖> 0 we have
𝑟1(𝑑1) = (7𝑑1 + 2) × 10,
𝑟2(𝑑2) = (3𝑑2 + 7) × 10,
𝑟3(𝑑3) = (4𝑑3 + 5) × 10,
and 𝑑1(0) = 𝑑2(0) = 𝑑3(0). All are measured in $10𝐾dollars. The objective is to maximize the net value of your

 
investments. This can be formulated as a linear programming problem:
max
𝑑1,𝑑2,𝑑3
𝑟1(𝑑1) + 𝑟2(𝑑2) + 𝑟3(𝑑3),
such that
𝑑1 + 𝑑2 + 𝑑3 ≤6,
𝑑𝑖≥0
𝑖= 1, 2, 3
are integers.


---

## [2023 | individual | n=1] 2023_Computational_Applied  (chars=686)

Consider the forward and the centered finite difference formulas
D+
h f(x0) = f(x0 + h) −f(x0)
h
,
(1)
D0
hf(x0) = f(x0 + h) −f(x0 −h)
2h
,
(2)
to approximate the derivative of f at a point x0. Assume f is a smooth function in a
neighborhood of x0 containing the points x0 + h and x0 −h.
(a) Prove that D+
h f(x0) and D0
hf(x0) approximate f ′(x0) to O(h) and O(h2), respec-
tively.
(b) Derive an O(h2) approximation to f ′(x0) from D+
h f(x0) by doing Richardson
extrapolation.
(c) Take f(x) = sin x and x0 = 0.
Prove that both D+
h f(x0) and D0
hf(x0) con-
verge quadratically to f ′(x0) as h →0 and that in fact they produce the same
approximation to f ′(x0) in this particular case.


---

## [2023 | individual | n=2] 2023_Computational_Applied  (chars=886)

For functions defined on a closed interval [0, 1], we want to compute the following
definite integral,
I[f] =
Z 1
0
f(x) log(1/x)dx.
Here we consider the weight function log(1/x), and denote Pn(x) as the monic orthog-
onal polynomials for the corresponding weighted inner product.
(a) Let P0 = 1. Find P1(x), and the corresponding node x1
1 and weight ω1
1 for the
1-point Gaussian quadrature rule.
(b) Derive a recursive formula for Pn+1(x) using Pn(x) and Pn−1(x).
(c) Consider the normalized orthogonal polynomials Qn(x) = Pn(x)/||Pn||, where
||Pn|| =
p
Pn(x)2 log(1/x)dx.
Derive a recursive formula for Qn+1(x) using Qn(x) and Qn−1(x).
1

 
(d) Use the above recursive formula to show that x = λ is a node of the 4-point
Gaussian quadrature if and only if it is an eigenvalue of a symmetric, tridiagonal
matrix. Write out the form of the symmetric and tridiagonal matrix explicitly.


---

## [2023 | individual | n=3] 2023_Computational_Applied  (chars=356)

Let A be a real n × n matrix with distinct eigenvalues such that
|λ1| > |λ2| ≥|λ3| ≥· · · ≥|λn| ≥0,
with corresponding eigenvectors {vj}n
j=1.
(a) Show that the power iteration
zm =
Amz0
||Amz0||∞
−→± v1
||v1||∞
,
∀z0 ∈Rn.
(b) Consider the following iteration with initial guess x0 = y0 = 1,
xn+1 = xn + yn,
yn+1 = xn+1 + xn.
Show that yn/xn →
√
2 as n →∞.


---

## [2023 | individual | n=4] 2023_Computational_Applied  (chars=706)

Consider the initial value problem
y′ = f(t, y),
0 < t ≤T.
(3)
y(0) = y0.
(4)
Assume f is continuous and Lipschitz in y in [0, T] × (−∞, ∞). Denote yn ≈y(tn),
tn = nh, and h = T/N, with N a positive integer, and consider the one-step method
yn+1 = yn + αhf(tn, yn) + βhf(tn + γh, yn + γhf(tn, yn)),
where α, β and γ are real parameters.
(a) Prove that the method is consistent if and only if α + β = 1, and the order of the
method can not exceed 2.
(b) Suppose that a second-order method of the above form is applied to f(t, y) = −λy
with λ > 0, and the initial condition y0 = 1. Show that the sequence (yn)n≥0 is
bounded if and only if h ≤2
λ. Show further that for such h,
|y(tn) −yn| ≤1
6λ3h2tn,
n ≥0.
2


---

## [2023 | individual | n=5] 2023_Computational_Applied  (chars=687)

Let u(t, x) be the solution of the initial-boundary value problem
ut = Duxx,
0 < x < L,
0 < t ≤T,
(5)
u(0, x) = f(x)
(6)
u(t, 0) = u(t, L) = 0,
(7)
where L > 0 and D > 0. Consider the finite difference scheme
un+1
j
−un
j
∆t
= Dun
j+1 −2un
j + un
j−1
(∆x)2
,
j = 1, . . . , M −1,
n = 0, 1, . . . , N −1
(8)
with un
0 = un
M = 0 for all n and u0
j = f(j∆x), j = 0, . . . , M . Here ∆t = T/N and
∆x = L/M and un
j ≈u(n∆t, j∆x).
(a) Prove that (8) is consistent with (5).
(b) Prove that if ∆t ≤
1
2D(∆x)2 the finite difference scheme (8) is stable under the
l∞norm.
(c) Prove that if ∆t ≤
1
2D(∆x)2 the finite difference scheme (8) converges in the l∞
norm to the exact solution of (5)-(7).


---

## [2023 | individual | n=6] 2023_Computational_Applied  (chars=646)

Let ψε(t, x) be the solution to the following Schr¨odinger equation:
iε∂ψε
∂t = −ε2
2 ∇2
xψε + V (x)ψε,
x = (x1, · · · , xn)T ∈Rn,
where i = √−1, ε ≪1 is a small positive real number (rescaled Planck constant),
∇2
x =
n
X
j=1
∂2
xj, and V (x) ∈C∞(Rn) is the potential function.
Consider the WKB expansion
ψε(t, x) = A(t, x)ei S(t,x)
ε
,
(a) Derive equations for A(t, x) and S(t, x) by asymptotic expansion. (Here both
A(t, x) and S(t, x) are real-valued functions, and do not depend on ε.)
(b) Define u(t, x) = ∇xS(t, x) ∈Rn. Derive an equation for u(t, x). Suppose u(0, x) ∈
C∞(Rn), will u(t, x) always be in C∞(Rn) for all t > 0? Explain why.
3


---

## [2024 | individual | n=1] 2024_2024_Computational_Math  (chars=438)

Let A ∈Rn×n be a non-singular matrix. Let u, v ∈Rn be column vectors. Define the
rank 1 perturbation bA = A + uvT.
(a) Derive a necessary and sufficient condition for bA to be invertible.
(b) Let x, z and b be column vectors in Rn. Suppose one can solve Az = b with
O(n) floating-point operations (flops). Under the conditions derived in(a), design
an algorithm to solve bAx = b with O(n) flops, and provide justification for your
answer.


---

## [2024 | individual | n=2] 2024_2024_Computational_Math  (chars=905)

Consider the integral
Z ∞
0
f(x) dx
where f is continuous, f ′(0) ̸= 0, and f(x) decays like x−1−α with α > 0 in the limit
x →∞.
(a) Suppose you apply the equispaced composite trapezoid rule with n subintervals
to approximate
Z L
0
f(x) dx.
What is the asymptotic error formula for the error in the limit n →∞with L
fixed?
(b) Suppose you consider the quadrature from (a) to be an approximation to the full
integral from 0 to ∞. How should L increase with n to optimize the asymptotic
rate of total error decay? What is the rate of error decrease with this choice of
L? 5
(c) Make the following change of variable x = L(1 + y)
1 −y
, y = x −L
x + L in the original
integral to obtain
Z 1
−1
FL(y) dy.
Suppose you apply the equispaced composite trapezoid rule; what is the asymp-
totic error formula for fixed L?
(d) Depending on α, which method - domain truncation or change-of-variable - is
preferable?
1


---

## [2024 | individual | n=3] 2024_2024_Computational_Math  (chars=495)

Consider the Chebyshev polynomial of the first kind
Tn(x) = cos(nθ),
x = cos(θ),
x ∈[−1, 1].
The Chebyshev polynomials of the second kind are defined as
Un(x) =
1
n + 1T ′(x),
n ≥0.
(a) Derive a recursive formula for computing Un(x) for all n ≥0.
(b) Show that the Chebyshev polynomials of the second kind are orthogonal with
respect to the inner product
⟨f, g⟩=
Z 1
−1
f(x)g(x)
√
1 −x2 dx
(c) Derive the 2-point Gaussian Quadrature rule for the integral
Z 1
−1
f(x)
√
1 −x2 dx =
2
X
j=1
wjf(xj)


---

## [2024 | individual | n=4] 2024_2024_Computational_Math  (chars=897)

Consider the boundary value problem
−d
dx

a(x)du
dx

= f(x),
u(0) = u(1) = 0
where a(x) > δ ≥0 is a bounded differentiable function in [0, 1]. We assume that,
although a(x) is available, an expression for its derivative, da
dx, is not available.
(a) Using finite differences and an equally spaced grid in [0, 1], xl = hl, l = 0, . . . , n
and h = 1/n, we discretize the ODE to obtain a linear system of equations, yield-
ing an O(h2) approximation of the ODE. After the application of the boundary
conditions, the resulting coefficient matrix of the linear system is an (n−1)×(n−1)
tridiagonal matrix.
Provide a derivation and write down the resulting linear system (by giving the
expressions of the elements).
(b) Utilizing all the information provided, find a disc in C, the smaller the better,
that is guaranteed to contain all the eigenvalues of the linear system constructed
in part (a).
2


---

## [2024 | individual | n=5] 2024_2024_Computational_Math  (chars=267)

(a) Verify that the PDE
ut = uxxx
is well posed as an initial value problem.
(b) Consider solving it numerically using the scheme
u(t + k, x) −u(t −k, x)
2k
= −1
2u(x −2h, t) + u(x −h, t) −u(x + h, t) + 1
2u(x + 2h, t)
h
.
Determine this scheme's stability condition.


---

## [2024 | individual | n=6] 2024_2024_Computational_Math  (chars=1156)

Consider the diffusion equation
∂v
∂t = µ∂2v
∂x2,
v(x, 0) = φ(x),
Z b
a
v(x, t) dx = 0
with x ∈[a, b] and periodic boundary conditions. The solution is to be approximated
using the central difference operator L for the 1D Laplacian.
Lvm = vm+1 −2vm + vm−1
h2
,
and the following two finite different approximations, (i) Forward-Euler
vn+1 = vn + µkLvn,
(1)
and (ii) Crank-Nicolson
vn+1 = vn + µk(Lvn + Lvn+1).
(2)
Throughout, consider [a, b] = [0, 2π] and the finite difference stencil to have periodic
boundary conditions on the spatial lattice [0, h, 2h, . . . , (N −1)h] where h = 2π
N and
N is even.
(a) Determine the order of accuracy of the central difference operator Lv in approxi-
mating the second derivative vxx.
(b) Using vn
m =
N−1
X
l=0
ˆvn
l exp

−i2πlm
N

give the updates ˆvn+1
l
in terms of ˆvn
l for each
of the methods, including the case l = 0.
(c) Give the solution for vn
m for each method when the initial condition is φ(m∆x) =
(−1)m.
(d) What are the stability constraints on the time step k for each of the methods,
if any, in equations (1) and (2)? Show there are either no constraints or express
them in the form k ≤F(h, µ).
3


---

## [2025 | individual | n=1] 2025_computational_and_applied_math  (chars=319)

We consider the multipoint iteration method
xk+1 = xk −α
f(xk)
f ′ xk −βf(xk)/f ′(xk)
,
where α and β are arbitrary parameters, for solving the equation f(x) = 0. Determine the val-
ues α and β such that the multipoint method achieves the highest possible order of convergence
for finding ξ, a simple root of f(x) = 0.


---

## [2025 | individual | n=2] 2025_computational_and_applied_math  (chars=214)

Compute the spectral radius of the matrix A−1, where
A =


0
1
0
0
0
0
0
0
1
0
1
0
0
0
0
0
0
1
0
1
0
0
0
0
0
0
1
0
1
0
0
0
0
0
0
1
0
1
0
0
0
0
0
0
1
0
1
0
0
0
0
0
0
1
0
1
0
0
0
0
0
0
1
0


.


---

## [2025 | individual | n=3] 2025_computational_and_applied_math  (chars=908)

Let the ordinary Legendre polynomial of degree k be denoted Pk(x) for k ≥0. The associated
Legendre functions are defined as
P m
k = (−1)m(1 −x2)m/2 dm
dxm Pk(x),
m > 0,
k ≥m.
(Note that despite the name, for odd m they are not actually polynomials.)
(a) Consider the interpolation problem of finding coefficients ak such that
N
X
k=1
akP 1
k (xi) = yi,
i = 1, ..., N.
Prove that this linear system of equations for the unknown coefficients ak is nonsingular
provided that the interpolation points {xi} exclude ±1 and are distinct.
(b) Consider the approximation problem of finding coefficients ak to minimize the squared
approximation error

f(x) −
N
X
k=1
akP 1
k (x)


2
2,
where the L2 norm is taken over x ∈[−1, 1]. Derive the linear system for the coefficients
ak and explain why it is nonsingular.
(c) Let M be the coefficient matrix from part (b). Prove that Mk,j = 0 when k + j is odd.
1


---

## [2025 | individual | n=4] 2025_computational_and_applied_math  (chars=256)

Given a set of column vectors y1, . . . , yn ∈Rm, let V = span{y1, . . . , yn} ⊂Rm. How can we
find ℓ≤dim V orthonormal vectors {ψi}ℓ
i=1 in Rm that minimize
J(ψ1, . . . , ψℓ) =
n
X
j=1

yj −
ℓ
X
i=1
(y⊤
j ψi)ψi

2
,
where ∥y∥=
p
y⊤y is the Euclidean norm?


---

## [2025 | individual | n=5] 2025_computational_and_applied_math  (chars=1110)

Consider the initial-value problem
∂u
∂t + u = ∂2u
∂x2 ,
−∞< x < ∞,
0 < t ≤T,
u(x, 0) = u0(x),
−∞< x < ∞
where T is a fixed positive real number, and u0 is a real-valued continuous function on R.
Consider the θ-scheme
U m+1
j
−U m
j
∆t
+ [θU m+1
j
+ (1 −θ)U m
j ]
= θ
U m+1
j+1 −2U m+1
j
+ U m+1
j−1
(∆x)2
+ (1 −θ)U m
j+1 −2U m
j + U m
j−1
(∆x)2
for j ∈Z, m = 0, ..., M −1, where ∆x > 0 and ∆t = T/M, M ≥1, and U 0
j = u0(j∆t), j ∈Z.
(a) Define the ℓ∞-norm as ||U m||ℓ∞:= maxj∈Z |U m
j |, and assume that ||U 0||ℓ∞is finite. Prove
that for θ ∈[0, 1],
||U m||ℓ∞≤
1 −(1 −θ)∆t
1 + θ∆t
m
||U 0||ℓ∞,
holds for all 1 ≤m ≤M, provided that A(θ)∆t ≤
(∆x)2
2+(∆x)2 , where A(θ) is a constant,
depending on the choice of θ, which you should determine.
(b) Define the ℓ2-norm as ||U m||ℓ2 :=
 ∆x P
j∈Z |U m
j |21/2 and suppose that ||U m||ℓ2 is finite.
• For θ ∈[ 1
2, 1], show that ∥U m∥ℓ2 ≤∥U 0∥ℓ2 holds for any ∆t, ∆x > 0 and all 1 ≤m ≤
M.
• For θ ∈[0, 1
2), prove that ∥U m∥ℓ2 ≤∥U 0∥ℓ2 under the condition B(θ)∆t ≤
2(∆x)2
4+(∆x)2 ,
where B(θ) is a constant, depending on the choice of θ, which you should determine.


---

## [2025 | individual | n=6] 2025_computational_and_applied_math  (chars=559)

Consider the stiffsystem of ordinary differential equations:
dy
dt = f(t, y),
y(0) = y0
where y =

y1
y2

, y0 =

2
1

, and
f(t, y) =
−1000y1 + 999y2
−y2

(a) Find the exact solution y(t) =
y1(t)
y2(t)

.
2

 
(b) For the explicit Euler method:
yn+1 = yn + hf(tn, yn)
determine the absolute stability region and prove divergence when h > 0.002.
(c) For the implicit Euler method:
yn+1 = yn + hf(tn+1, yn+1)
prove unconditional stability for any h > 0.
(d) For the trapezoidal rule:
yn+1 = yn + h
2 [f(tn, yn) + f(tn+1, yn+1)]
analyze its stability.
3


---

## [2026 | individual | n=1] 2026_2026_Computation  (chars=975)

. Consider the equation
(1)
α∂tu(t, x) + β∂xu(t, x) −γ∂xxu(t, x) = f(x),
for (t, x) ∈(0, T) × (0, 1), with f ∈L2(0, 1), T > 0, boundary condition u(t, 0) = u(t, 1) = 0 for
all t > 0 and initial condition u(0, x) = 0. Parameters satisfy α > 0, β ∈R and γ > 0. Let Th be
a uniform mesh partitioning (0, 1), i.e., a collection of intervals [ih, (i + 1)h] with i = 0, 1, . . . , N
and h = 1/(N + 1).
(a). Write the fully discrete variational formulation of (1) using the continuous piecewise
linear finite element method (P1 Lagrange FEM) in space and implicit Euler method in time.
Denoting the time step by τ and ti = iτ for all i ∈N.
(b). Prove the L2 stability estimate ∥un
h∥≤C∥f∥with a constant C > 0 independent of
h, τ, n.
(c). Let {φi}1≤i≤N be the global Lagrange shape functions associated with the nodes xi := ih
for i = 1, . . . , N. Denoting by ui
h := P
1≤j≤N U i
jφj the approximation of u at ti, write the
algebraic linear system solved by (U i
1, . . . , U i
N).


---

## [2026 | individual | n=2] 2026_2026_Computation  (chars=896)

. Let Ω⊂Rd be a bounded domain, d ≤3. Consider the functional J : H1
0(Ω) →R:
J(u) =
Z
Ω
1
2|∇u(x)|2 + 1
4u(x)4 −f(x)u(x)

dx,
where f ∈L2(Ω).
(a). Compute the Fr´echet derivative (gradient) ∇J(u) and the second Fr´echet derivative
(Hessian) ∇2J(u). Prove that J is strictly convex.
(b). Write the Newton's method for finding the minimizer u∗of J(u). Assuming the initial
guess u0 is sufficiently close to the solution u∗, prove the second order convergence of
the Newton's method: there exists C > 0 such that ∥uk+1 −u∗∥H1 ≤C∥uk −u∗∥2
H1.
(c). Let sk = uk+1 −uk and yk = ∇J(uk+1) −∇J(uk). A Quasi-Newton method resorts to
an approximate Hessian Bk+1 satisfying the secant equation: Bk+1sk = yk. A BFGS
update of Bk+1 is
Bk+1v = Bkv −⟨Bksk, v⟩
⟨Bksk, sk⟩Bksk + ⟨yk, v⟩
⟨yk, sk⟩yk,
for any test function v ∈H1
0(Ω). Assuming Bk is positive definite, prove that above
BFGS update is well-defined.


---

## [2026 | individual | n=3] 2026_2026_Computation  (chars=538)

. Consider the initial value problem over RN in the form
x′ = f(t, x)
x(0) = x0 ∈RN,
where f : [0, T] × RN →RN is smooth. Consider the family of one-step methods
(2)
xn+1 = xn + (1 −b)hf(tn, xn) + bhf(tn+1, xn+1),
where h = tn+1 −tn for any n ≥0 is a uniform step size and b ∈[0, 1] is a constant.
(a). Find the value of b so that the local truncation error is O(h3).
1

 
2
(b). Apply the method (2) to x′ = λx, x(0) = x0 ∈R. Find the function g(·) such that
xn = g(hλ)nx0.
(c). Determine the values of b so that this method is A-stable.


---

## [2026 | individual | n=4] 2026_2026_Computation  (chars=615)

. Let A be an invertible N ×N matrix. The shifted QR iteration for a given sequence
of shifts {σn} is defined by
A0 = A,
An −σnIN = QnRn,
An+1 = RnQn + σnIN,
where IN is the N ×N identity matrix, Qn is orthogonal and Rn is upper triangular with positive
diagonal entries.
(a). Prove if no σn is an eigenvalue of A then the sequences {An}, {Qn} and {Rn} are
uniquely defined and satisfy
An+1 = QT
nAnQn,
An+1 = RnAn(Rn)−1.
(b). Suppose A is a symmetric 2 × 2 matrix with eigenvalues λ1 and λ2. Let σ0 = λ1. Find
A1.
(c). Let ˆQn = Q0 . . . Qn−1 and ˆRn = Rn−1 . . . R0 for n ≥1. Prove ˆQk+1 ˆRk+1 = Qk
i=0(A −
σiIN).


---

## [2026 | individual | n=5] 2026_2026_Computation  (chars=450)

. Let A ∈Rn×n be an n by n real matrix and σi(A) be its i-th largest singular value.
A vector x ∈Rn such that Ax = x is called a fixed point of A.
(a). Assume σ1(A) ≤1, show that every fixed point of A is a fixed point of its transpose AT .
(b). Consider A =
1
1
0
0

to verify that the assertion in (a) is not generally true without
assuming σ1(A) ≤1.
(c). Assume AAT = AT A, show that every fixed point of A is a fixed point of its transpose
AT .


---

## [2026 | individual | n=6] 2026_2026_Computation  (chars=751)

. Let the subdifferential of a convex function f : Rn →R ∪{+∞} at a point x be
denoted by ∂f(x). Recall that a vector x∗∈Rn is a subgradient of f at x if it satisfies:
f(z) ≥f(x) + ⟨x∗, z −x⟩,
∀z ∈Rn.
Namely, ∂f(x) = {x∗: f(z) ≥f(x) + ⟨x∗, z −x⟩, ∀z ∈Rn}. Here, ⟨x, y⟩= xT y for any vectors
x and y in Rn. We assume n ≥2 (the n = 1 case is trivial).
(a). Let f : Rn →R be defined by
f(x) =
max
i=1,...,n xi,
x = (x1, . . . , xn)T ∈Rn.
Compute the subdifferential ∂f(0).
(b). Let
g(x) =
max
i=1,...,n xi + δRn
+(x),
where δRn
+ is the indicator function of the non-negative orthant Rn
+ (i.e., δRn
+(x) = 0 if
x ≥0, and +∞otherwise). Show that
∂g(0) = ∂f(0) −Rn
+.
[Here, one may use the fact that ∂g(x) = ∂f(x) + ∂δRn
+(x) for g(x) = f(x) + δRn
+(x).]
