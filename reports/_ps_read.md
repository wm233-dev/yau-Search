
=== [2010] Probability & Statistics | kind=individual | n=1 | paper=2010_Applied_Computational_Probability_and_Statistics_individual | chars=97 ===
Let Z1, · · · , Zn be i.i.d. random variables with Zi ∼N(µ, σ2). Find
E(
n
X
i=1
Zi|Z1 −Z2 + Z3).

=== [2010] Probability & Statistics | kind=individual | n=2 | paper=2010_Applied_Computational_Probability_and_Statistics_individual | chars=156 ===
Let X1, · · · , Xn be pairwise independent.
Further, assume that
EXi = 1 + i−1 and that max1≤i≤n E|Xi|1+ϵ < ∞for some ϵ > 0.
Show that
1
n
n
X
i=1
Xi
P
−→1.

=== [2010] Probability & Statistics | kind=individual | n=3 | paper=2010_Applied_Computational_Probability_and_Statistics_individual | chars=105 ===
Let Z1, · · · , Z6 be i.i.d. random variables with Zi ∼N(0, 1). Set
U 2 = (Z1Z2 + Z3Z4 + Z5Z6)2
Z2
2 + Z2

=== [2010] Probability & Statistics | kind=individual | n=4 | paper=2010_Applied_Computational_Probability_and_Statistics_individual | chars=547 ===
+ Z2
6
,
V 2 = U 2(Z2
2 + Z2
4)
U 2 + Z2
6
.
Find and identify the densities of U 2 and V 2.
4. Suppose that three characteristics in a large propulation can be
observed according to the following frequencies
p1 = θ3,
p2 = 3θ(1 −θ),
p3 = (1 −θ)3,
where θ ∈(0, 1). Let Nj, j = 1, 2, 3 be the observed frequencies of
characteristic j in a random sample of size n.
(a) Construct the approximate level (1 −α) maximum likelihood
confidence set for θ.
(b) Derive the asymptotic distribution for the frequency substitu-
tion estimator ˆθ2 = 1 −(N3/n)1/3.

=== [2010] Probability & Statistics | kind=individual | n=5 | paper=2010_Applied_Computational_Probability_and_Statistics_individual | chars=872 ===
(1) Suppose
S =
·
σ
uT
0
Sc
¸
,
T =
·
τ
vT
0
Tc
¸
,
b =
·
β
bc
¸
,
where σ, τ and β are scalars, Sc and Tc are n-by-n matrices,
and bc is an n-vector. Show that if there exists a vector xc such
that
(ScTc −λI)xc = bc
1

 
2
and wc = Tcxc is available, then
x =
·
γ
xc
¸
,
γ = β −σvTxc −uTwc
στ −λ
solves (ST −λI)x = b.
(2) Hence or otherwise, derive an O(n2) algorithm for solving the
linear system (U1U2 −λI)x = b where U1 and U2 are n-by-
n upper triangular matrices, and (U1U2 −λI) is nonsingular.
Please write down your algorithm and prove that it is indeed of
O(n2) complexity.
(3) Hence or otherwise, derive an O(pn2) algorithm for solving the
linear system (U1U2 · · · Up −λI)x = b where {Ui}p
i=1 are all n-
by-n upper triangular matrices, and (U1U2 · · · Up −λI) is non-
singular. Please write down your algorithm and prove that it is
indeed of O(pn2) complexity.

=== [2010] Probability & Statistics | kind=individual | n=6 | paper=2010_Applied_Computational_Probability_and_Statistics_individual | chars=422 ===
(1) Let A ∈Rm×n, i.e. A is an m-by-n real matrix. Show that
there exists an m-by-m orthogonal matrix U and an n-by-n
orthogonal matrix V such that
U TAV = diag(σ1, σ2, . . . , σp),
where p = min{m, n} and
σ1 ≥σ2 ≥. . . ≥σp ≥0.
(2) Let rank(A)= r. Show that for any positive integer k < r,
min
rank(B)=k∥A −B∥2 = σk+1.
(Hint: Consider the matrix Ak =
k
X
i=1
σiuivT
i , where ui and vi
are columns of U and V respectively.)

=== [2010] Probability & Statistics | kind=team | n=1 | paper=2010_Applied_Computational_Probability_and_Statistics_team | chars=300 ===
Let X1, · · · , Xn be independent and identically distributed random
variables with continuous distribution functions F(x1), · · · , F(xn), re-
spectively. Let Y1 < · · · < Yn be the order statistics of X1, · · · , Xn.
Prove that Zj = F(Yj) has the beta (j, n −j + 1) distribution (j =
1, · · · , n).

=== [2010] Probability & Statistics | kind=team | n=2 | paper=2010_Applied_Computational_Probability_and_Statistics_team | chars=95 ===
Let X1, · · · , Xn be i.i.d. random variable with a continuous density
f at point 0. Let
Yn,i =

=== [2010] Probability & Statistics | kind=team | n=3 | paper=2010_Applied_Computational_Probability_and_Statistics_team | chars=411 ===
4bn
(1 −X2
i /b2
n)I(|Xi| ≤bn).
Show that
Pn
i=1(Yn,i −EYn,i)
(bn
Pn
i=1 Yn,i)1/2
L
−→N(0, 3/5),
provided bn →0 and nbn →∞.
3. Let X1, · · · , Xn be independently and indentically distributed ran-
dom variables with Xi ∼N(θ, 1). Suppose that it is known that |θ| ≤τ,
where τ is given. Show
min
a1,··· ,an+1 sup
|θ|≤τ
E(
n
X
i=1
aiXi + an+1 −θ)2 =
τ 2n−1
τ 2 + n−1.
Hint: Carefully use the sufficiency principle.

=== [2010] Probability & Statistics | kind=team | n=4 | paper=2010_Applied_Computational_Probability_and_Statistics_team | chars=982 ===
The rules for "1 and 1" foul shooting in basketball are as follows.
The shooter gets to try to make a basket from the foul line.
If he
succeeds, he gets another try. More precisely, he make 0 baskets by
missing the first time, 1 basket by making the first shot and xsmissing
the second one, or 2 baskets by making both shots.
Let n be a fixed integer, and suppose a player gets n tries at " 1 and
1" shooting. Let N0, N1, and N2 be the random variables recording
the number of times he makes 0, 1, or 2 baskets, respectively. Note
that N0 + N1 + N2 = n. Suppose that shots are independent Bernoulli
trails with probability p for making a basket.
(a) Write down the likelihood for (N0, N1, N2).
1

 
2
(b) Show that the maximum likelihood estimator of p is
ˆp =
N1 + 2N2
N0 + 2N1 + 2N2
.
(c) Is ˆp an unbiased estimator for p? Prove or disprove. (Hint: Eˆp
is a polynomial in p, whose order is higher than 1 for p ∈(0, 1).)
(d) Find the asymptotic distribution of ˆp as n tends to ∞.

=== [2010] Probability & Statistics | kind=team | n=5 | paper=2010_Applied_Computational_Probability_and_Statistics_team | chars=1527 ===
When considering finite difference schemes approximating partial
differential equations (PDEs), for example, the scheme
(1)
un+1
j
= un
j −λ(un
j −un
j−1)
where λ = ∆t
∆x, approximating the PDE
(2)
ut + ux = 0,
we are often interested in stability, namely
(3)
||un|| ≤C||u0||,
n∆t ≤T
for a constant C = C(T) independent of the time step ∆t and the spa-
tial mesh size ∆x. Here ||·|| is a given norm, for example the L2 norm or
the L∞norm, of the numerical solution vector un = (un
1, un
2, · · · , un
N).
The mesh points are xj = j∆x, tn = n∆t, and the numerical solution
un
j approximates the exact solution u(xj, tn) of the PDE (2) with a
periodic boundary condition.
(i) Prove that the scheme (1) is stable in the sense of (3) for both
the L2 norm and the L∞norm under the time step restriction
λ ≤1.
(ii) Since the numerical solution un is in a finite dimensional space,
Student A argues that the stability (3), once proved for a spe-
cific norm || · ||a, would also automatically hold for any other
norm || · ||b. His argument is based on the equivalency of all
norms in a finite dimensional space, namely for any two norms
|| · ||a and || · ||b on a finite dimensional space W, there exists a
constant δ > 0 such that
δ||u||b ≤||u||a ≤1
δ||u||b.
Do you agree with his argument? If yes, please give a detailed
proof of the following theorem: If a scheme is stable, namely (3)
holds for one particular norm (e.g. the L2 norm), then it is also
stable for any other norm. If not, please explain the mistake
made by Student A.

=== [2010] Probability & Statistics | kind=team | n=6 | paper=2010_Applied_Computational_Probability_and_Statistics_team | chars=1032 ===
We have the following 3 PDEs
(4)
ut + Aux = 0,
(5)
ut + Bux = 0,

 
3
(6)
ut + Cux = 0,
C = A + B.
Here u is a vector of size m and A and B are m × m real matrices.
We assume m ≥2 and both A and B are diagonalizable with only real
eigenvalues. We also assume periodic initial condition for these PDEs.
(i) Prove that (4) and (5) are both well-posed in the L2-norm.
Recall that a PDE is well-posed if its solution satisfies
||u(·, t)|| ≤C(T)||u(·, 0)||,
0 ≤t ≤T
for a constant C(T) which depends only on T.
(ii) Is (6) guaranteed to be well-posed as well? If yes, give a proof;
if not, give a counter example.
(iii) Suppose we have a finite difference scheme
un+1 = Ahun
for approximating (4) and another scheme
un+1 = Bhun
for approximating (5). Suppose both schemes are stable in the
L2-norm, namely (3) holds for both schemes. If we now form
the splitting scheme
un+1 = Bh Ahun
which is a consistent scheme for solving (6), is this scheme guar-
anteed to be L2 stable as well? If yes, give a proof; if not, give
a counter example.

=== [2012] Probability & Statistics | kind=individual | n=1 | paper=2012_Probability2012_individual | chars=309 ===
Solve the following two problems:
1) An urn contains b black balls and r red balls. One of the balls was
drawn at random, and putted back in the urn with a additional balls
of the same color. Now suppose that the second ball drawn at random
is red. What is the probability that the first ball drawn was black?

=== [2012] Probability & Statistics | kind=individual | n=2 | paper=2012_Probability2012_individual | chars=645 ===
Let (Xn) be a sequence of random variables satisfying
lim
a→∞sup
n≥1
P(|Xn| > a) = 0.
Assume that sequence of random variables (Yn) converges to 0 in prob-
ability. Prove that (XnYn) converges to 0 in probability.
2. Solve the following two problems:
1) Let (Ω, F, P) be a probability space, G be a sub-algebra of F.
Assume that X is a non-negative integrable random variable. Set Y =
E[X|G]. Prove that
(a)[X > 0] ⊂[Y > 0],a.s.;
(b)[Y > 0] = ess.inf{A : A ∈G, [X > 0] ⊂A}.
2) Let X and Y have a bivariate normal distribution with zero means,
variances σ2 and τ 2, respectively, and correlation ρ. Find the condi-
tional expectation E(X|X + Y ).

=== [2012] Probability & Statistics | kind=individual | n=3 | paper=2012_Probability2012_individual | chars=416 ===
Suppose that {p(i, j) : i = 1, 2, · · · , m; j = 1, 2, · · · , n} is a finite
bivariate joint probability distribution, that is,
p(i, j) > 0,
m
X
i=1
n
X
j=1
p(i, j) = 1.
(i) Can {p(i, j)} be always expressed as
p(i, j) =
X
k
λkak(i)bk(j)
for some finite λk ≥0, P
k λk = 1, ak(i) ≥0, Pm
i=1 ak(i) = 1, bk(j) ≥
0, Pn
j=1 bk(j) = 1?
1

 
2
(ii) Prove or disprove the above relation by use of conditional prob-
ability.

=== [2012] Probability & Statistics | kind=individual | n=4 | paper=2012_Probability2012_individual | chars=1394 ===
Let X1, · · · , Xm be an independent and identically distributed (i.i.d.)
random sample from a cumulative distribution function (CDF) F, and
Y1, · · · , Yn an i.i.d. random sample from a CDF G. We want to test
H0 : F = G versus H1 : F ̸= G. The total sample size is N = m + n.
Consider the following two nonparametric tests.
• The Wilcoxon rank sum tests. The test proceeds by first rank-
ing the pooled X and Y samples and then taking the sum of the
ranks associated with the Y sample. Let Ry1, · · · , Ryn be the
rankings of the sample y1 < · · · < yn from the pooled sample
in increasing order. The Wilcoxon rank sum statistic is defined
as W = Pn
j=1 Ryj.
• The Mann-Whitney U-test.
Let Uij = 1 if Xi < Yj, and
Uij = 0 otherwise. The Mann-Whitney U-statistic is defined
as U = Pm
i=1
Pn
j=1 Uij. The probability γ = P(X < Y ) can be
estimated as U/(mn). The decision rule is based on assessing
if γ = 0.5.
Assume that there are no tied data values.
(a) Show that W = U + 1
2n(n + 1), which shows that the two test
statistics differ only by a constant and yield exactly the same
p-values.
(b) Using the central limit theorem, the Wilcoxon rank sum statis-
tic W can be converted to a Z-variable, which provides an easy-
to-use approximation. The transformation is
ZW = W −µW
σW
,
where µW and σ2
W are the mean and variance of W under H0.
Show that µW = 1
2n(N + 1) and σ2
W =
1
12mn(N + 1).

=== [2012] Probability & Statistics | kind=individual | n=5 | paper=2012_Probability2012_individual | chars=192 ===
Let X be a random variable with EX2 < ∞, and Y = |X|. Assume
that X has a Lebesgue density symmetric about 0. Show that random
variables X and Y are uncorrelated, but they are not independent.

=== [2012] Probability & Statistics | kind=individual | n=6 | paper=2012_Probability2012_individual | chars=446 ===
Let E1, · · · , En be i.i.d. random variables with Ei ∼Exponential(1).
Let U1, · · · , Un be i.i.d. uniformly (on [0,1]) distributed random vari-
ables. Further, assume that E1, · · · , En and U1, · · · , Un are indepen-
dent.
(a) Find the density of X = (E1 +· · ·+Em)/(E1 +· · ·+En), where
m < n.
(b) Show that Y = (n−m)X
m(1−X) is distributed as the F-distribution with
degrees of freedom (2m, 2(n −m))
(c) Find the density of (U1 · · · Un)−X.

=== [2012] Probability & Statistics | kind=team | n=1 | paper=2012_Probability2012_team | chars=376 ===
Let (Xn) be a sequence of i.i.d. random variables.
1) Assume that each Xn satisfies the exponential distribution with
parameter 1 (i.e. P(Xn ≥x) = e−x, x ≥0). Prove that
(a) P(Xn > α log n, i.o.) = 0, if α > 1; P(Xn > α log n, i.o.) = 1, if
α ≤1.
Here "i.o" stands for "infinitely often", and An, i.o. stands lim supn→∞An.
(b) Let L = lim supn→∞(Xn/ log n), then P(L = 1) = 1.

=== [2012] Probability & Statistics | kind=team | n=2 | paper=2012_Probability2012_team | chars=437 ===
Assume that each Xn satisfies the Poisson distribution with pa-
rameter λ (i.e. P(Xn = k) = λk
k! e−λ, k = 0, 1, 2, · · · .) Put
L = lim sup
n→∞(Xn log log n/ log n).
Prove that P(L = 1) = 1.
2. Let Xi be i.i.d exponential r.v with rate one, i ≥1. Let N be a
geometric random variable with success probability p, 0 < p < 1, i.e.
P(N = k) = (1−p)k−1p, k = 1, 2, · · · , and independent of all Xi, i ≥1.
Find the distribution of PN
i=1 Xi.

=== [2012] Probability & Statistics | kind=team | n=3 | paper=2012_Probability2012_team | chars=84 ===
Let X and Y be i.i.d real valued r.v's. Prove that P(|X +Y | < 1) ≤
3P(|X −Y | < 1).

=== [2012] Probability & Statistics | kind=team | n=4 | paper=2012_Probability2012_team | chars=177 ===
Suppose S = X1 + X2 + · · · + Xn, a sum of independent random
variables with Xi distributed Binomial(1, pi). Show that P(S even) =
1/2 if and only if at least one pi equals 1/2.

=== [2012] Probability & Statistics | kind=team | n=5 | paper=2012_Probability2012_team | chars=234 ===
Let Bθ denote the closed unit ball in R2 with center θ. Suppose
X1, X2, · · · , Xn are independently and uniformly distributed on Bθ,
for an unknown θ in R2. Denote that maximum likelihood estimator
by ˆθ. Show that |ˆθ −θ| = Op(1/n).

=== [2012] Probability & Statistics | kind=team | n=6 | paper=2012_Probability2012_team | chars=603 ===
Suppose that X1, · · · , Xn are a random sample from the Bernoulli
distribution with probability of success p1 and Y1, · · · , Yn be an inde-
pendent random sample from the Bernoulli distribution with probabil-
ity of success p2.
1

 
2
(a) Derive the maximum likelihood ratio test statistic for
H0 : p1 = p2 ←→H1 : p1 ̸= p2.
(Note: No simplification of the resulting test statistic is re-
quired. However, you need to give the asymptotic null.)
(b) Compute the asymptotic power of the test with critical region
|√n(ˆp1 −ˆp2)/
p
2ˆpˆq| ⩾z1−α
when p1 = p and p2 = p + n−1/2∆, where ˆp = 0.5.ˆp1 + 0.5ˆp2.

=== [2013] Probability & Statistics | kind=team | n=1 | paper=2013_TeamProblems2013 | chars=224 ===
. The characteristic function f of a probability distribution function F is
defined by
f(t) =
∫∞
−∞
eitx dF(x).
Show that f1(t) = (cos t)2 is a characteristic function and f2(t) = | cos t| is not a charac-
teristic function.

=== [2013] Probability & Statistics | kind=team | n=2 | paper=2013_TeamProblems2013 | chars=316 ===
. Let I = [0, 1] be the unit interval and B the σ-algebra of Borel sets on I.
Let P be the Lebesgue measure on I. Show that on the probability space (I, B, P) the
set of points of x with the following property has probability 1: for all but finitely many
rational numbers p/q ∈(0, 1),
x −p
q
 ≥
1
(q log q)2.

=== [2013] Probability & Statistics | kind=team | n=3 | paper=2013_TeamProblems2013 | chars=365 ===
. Let X be an integrable random variable, G a σ−algebra, and Y = E[X|G].
Assume that X and Y have the same distribution.
(1) Prove that if X is square-integrable, then X = Y , a.s. (i.e. X must be G measur-
able) ;
(2) Using a) to prove that for any pair of real numbers a, b with a < b, we have
min{max{X, a}, b} = min{max{Y, a}, b}, and consequently, X = Y , a.s.

=== [2013] Probability & Statistics | kind=team | n=4 | paper=2013_TeamProblems2013 | chars=549 ===
. Let X1, · · · , Xn be iid N(θ, σ2), σ2 known, and let θ have a double exponen-
tial distribution, that is, π(θ) = e−|θ|/a/(2a), a known. A Bayesian test of the hypothesis
H0 : θ ≤0 versus H1 : θ > 0 will decide in favor of H1 if its posterior probability is large.
1

 
(a) For a given constant K, calculate the posterior probability that θ > K, that is,
P(θ > K | x1, · · · , xn, a).
(b) Find an expression for lima→∞P(θ > K | x1, · · · , xn, a).
(c) Compare your answer in part (b) to the p-value associated with the classical hypoth-
esis test.

=== [2013] Probability & Statistics | kind=team | n=5 | paper=2013_TeamProblems2013 | chars=1351 ===
. Two sets of interesting ideas emerging in the 1990's are the proposal of
model selection with L1-penalty (e.g., lasso) and the proposal of soft thresholding in
simultaneous inferences. Consider a linear model
Y = Xβ + ε,
where the set up is as usual (i.e., X is a non-random n by p matrix with 1 < p < n,
ε ∼N(0, σ2 · In) with In being the identity matrix). The lasso procedure is to obtain an
estimate of the parameter vector β through minimizing
(L) :
1
2||Y −Xβ||2
2 + λ · ||β||1,
which we denote by β∗
λ; here λ > 0 is a tuning parameter, ||·||2 denote the usual L2 vector
norm, and || · ||1 denotes the usual L1 vector norm.
Denote the ordinary least square estimate of β by ˆβ, we have
1
2||Y −Xβ||2
2 + λ · ||β||1 = 1
2||Y −X ˆβ||2
2 + 1
2||X(β −ˆβ)||2
2 + λ · |β||1.
(0.1)
Furthermore, if X has orthonormal columns, e.g.,
X′X = Ip,
then it can be shown that
β∗
λ,i =















ˆβi −γ,
ˆβi > γ,
0,
|ˆβi| ≤γ,
ˆβi + γ,
βi < −γ.
(0.2)
(0.2) is called the soft thresholding of ˆβi's. This says that with orthonormal design, lasso
solution is equivalent to applying soft thresholding to the ordinary least square solution.
2

 
(a) Prove equation (0.1) without assuming X is orthogonal.
(b) Show that the lasso estimator is obtained by (0.2) under the assumption that X is
orthogonal, and find the relationship between λ and γ.

=== [2013] Probability & Statistics | kind=team | n=6 | paper=2013_TeamProblems2013 | chars=355 ===
. Consider a usual linear model Y = Xβ + ε, where ε ∼N(0, σ2 · In) and
X has n rows and p columns where 1 < p < n. Consider a p-dimensional column vector
a ̸= 0.
(a) Show that, if Xa = 0, then a′β is not estimable.
(b) Prove or disprove that, if a′β is not estimable, then Xa = 0.
(c) Show that X is full rank if and only if a′β are estimable for all a.
3

=== [2013] Probability & Statistics | kind=individual | n=1 | paper=2013_probability2013_individual | chars=226 ===
. Let (Xn) be a sequence of random variables.
(1) Assume that ∑∞
n=0 P(|Xn| > n) < ∞. Prove that lim supn→∞
|Xn|
n
≤1.
(2) Prove that (Xn) converges in probability to 0 if and only if for certain r > 0,
E
[
|Xn|r
1+|Xn|r
]
→0.

=== [2013] Probability & Statistics | kind=individual | n=2 | paper=2013_probability2013_individual | chars=270 ===
. Let X and Y be independent N(0, 1) random variables.
(1) Find E[X + Y |X ≥0, Y ≥0];
(2) Find the distribution function of X + Y given that X ≥0 and Y ≥0.
(Hint: For b) using the fact that U = (X + Y )/
√
2 and V = (X −Y )/
√
2 are
independent and N(0, 1) distributed.)

=== [2013] Probability & Statistics | kind=individual | n=3 | paper=2013_probability2013_individual | chars=483 ===
. Let {Xn} be a sequence of independent and identically distributed con-
tinuous real valued random variables, and regard n as time. Let An be the following
event:
An = {Xn = max{X1, X2, · · · , Xn}}.
We say that a maximum record occurs at n in such an event.
(1) Evaluate the probability P(An).
(2) Denote by Yn the number of maximum records occurred until time n, i.e.,
Yn = the number of {1 ≤k ≤n : Xk = max{X1, X2, · · · , Xk}}.
Evaluate the expectation EYn and the variance DYn.

=== [2013] Probability & Statistics | kind=individual | n=4 | paper=2013_probability2013_individual | chars=523 ===
. Let X = (X1, · · · , Xn) be an iid sample from an exponential density with
mean θ. Consider testing H0 : θ = θ0 vs. H1 : θ > θ0. Let P(X) = your p-value for an
appropriate test.
1

 
(a) What is Eθ0(P(X))? Derive your answer explicitly.
(b) Derive Eθ(P(X)) for θ ̸= θ0. Specifically, assuming only one sample, i.e. n = 1,
calculate Eθ(P(X)) as explicitly as possible for θ ̸= θ0.
(c) When there is only one sample, is Eθ(P(X)) a decreasing function of θ? In general,
can you prove your result for an arbitrary MLR family?

=== [2013] Probability & Statistics | kind=individual | n=5 | paper=2013_probability2013_individual | chars=509 ===
. Let X1, X2 be iid uniform on θ −1
2 to θ + 1
2.
(a) Show that for any given 0 < α < 1, you can find c > 0 such that
Pθ{ ¯X −c < θ < ¯X + c} = 1 −α,
where ¯X is the sample mean.
(b) Show that for ϵ positive and sufficiently small
Pθ{ ¯X −c < θ < ¯X + c
 |X2 −X1| ≥1 −ϵ} = 1
(c) The statement in (a) is used to assert that ¯X ±c is a 100(1−α)% confidence interval
for θ. Does the assertion in (b) contradict this? If your sample observations are
X1 = 1, X2 = 2, would you use the confidence interval in (a)?

=== [2013] Probability & Statistics | kind=individual | n=6 | paper=2013_probability2013_individual | chars=535 ===
. Suppose you want to estimate the total number of enemy tanks in a war on
the basis of the captured tanks. Assume without loss of generality that the tank serial
numbers are 1, 2, · · · , N, where N is the unknown total number of enemy tanks. Also
assume the serial numbers of the n captured tanks are iid uniform on 1, 2, · · · , N. (This
is a simplified assumption which provides a good approximation if n << N).
(a) Find the complete sufficient statistic.
(b) Suggest how you may find the minimum variance unbiased estimate of N.
2

=== [2014] Probability & Statistics | kind=individual | n=1 | paper=2014_probability2014_individual | chars=185 ===
. Let X be a real valued random variable such that for all smooth functions
f : R →R with compact support we have E[Xf(X)] = E[f ′(X)]. Show that X has the
standard normal distribution.

=== [2014] Probability & Statistics | kind=individual | n=2 | paper=2014_probability2014_individual | chars=151 ===
. Let (Xn) be a sequence of uncorrelated random variables of mean zero such
that
∞
X
n=1
nE|Xn|2 < ∞.
Show that Sn = Pn
i=1 Xi converges almost surely.

=== [2014] Probability & Statistics | kind=individual | n=3 | paper=2014_probability2014_individual | chars=387 ===
. Let (Ω, F) be a measurable space and G be a sub-σ-field of F. Let P and
Q be two probabilities which are mutually absolutely continuous on F. We denote by X0
the Radon-Nikodym density of Q with respect to P on F. Show that the following two
properties are satisfied:
(a) 0 < EP[X0|G] < +∞, P-a.s.;
(b) for every F-measurable non-negative random variable f,
EP[fX0|G] = EQ[f|G]EP[X0|G].

=== [2014] Probability & Statistics | kind=individual | n=4 | paper=2014_probability2014_individual | chars=557 ===
.
Suppose X1, . . . , Xn, . . . is a sequence of random numbers drawn from
the uniform distribution U(0, 1). One observes these numbers sequentially. At time n,
one keeps a record of Yn
def
= X(n) = maxn
i=1 Xi = max{Yn−1, Xn} and Zn
def
=
¯Xn =
Pn
i=1 Xi/n = (n −1)/nZn−1 + 1/nXn and discards all previous recordings.
(a) What is the best guess of X1 if one only observes Yn?
(b) What is the best guess of X1 if one only observes Zn?
(c) Comparing the two guesses of X1, which one is better (and in what sense)?
Give good reasoning to justify your answers.

=== [2014] Probability & Statistics | kind=individual | n=5 | paper=2014_probability2014_individual | chars=781 ===
. Suppose we take a random sample of size n from a bag of colored balls
(red, blue and yellow balls) with replacement. Let X1 denote the number of red balls, X2
denote the number of blue balls, and X3 denote the number of yellow balls in the sample.
Assuming we know that the total number of yellow balls is triple the total number of red
balls in the bag. Or in other words, the red, blue and yellow balls occur with probability
p1, p2 and p3 = 3p1, respectively in the bag.
1. Find the aymptotic distribution (after appropriate normalization) for the MLE of
p2.
2. Construct the likelihood ratio test statistic for the null hypothesis that p1 = p2 =
p3/3 (the alternative is that p1 = p2 = p3/3 is not true). What is the asymptotic
distribution of your test statistic under null?

=== [2014] Probability & Statistics | kind=team | n=1 | paper=2014_probability2014_team | chars=188 ===
. Suppose that Xn converges to X in distribution and Yn converges to a
constant c in distribution. Show that
(a) Yn converges to c in probability;
(b) XnYn converges to cX in distribution.

=== [2014] Probability & Statistics | kind=team | n=2 | paper=2014_probability2014_team | chars=319 ===
. Let X and Y be two random variables with |Y | > 0, a.s.. Let Z = X/Y .
(a) Assume the distribution function of (X, Y ) has the density p(x, y). What is the
density function of Z?
(b) Assume X and Y are independent and X is N(0, 1) distributed, Y has the uniform
distribution on (0, 1). Give the density function of Z.

=== [2014] Probability & Statistics | kind=team | n=3 | paper=2014_probability2014_team | chars=410 ===
. Let (Ω, F, P) be a probability space.
(a) Let G be a sub σ-algebra of F, and Γ ∈F. Prove that the following properties
are equivalent:
(i) Γ is independent of G under P,
(ii) for every probability Q on (Ω, F), equivalent to P, with dQ/dP being G measur-
able, we have Q(Γ) = P(Γ).
(b) Let X, Y, Z be random variables and Y is integrable. Show that if (X, Y ) and Z
are independent, then E[Y |X, Z] = E[Y |X].

=== [2014] Probability & Statistics | kind=team | n=4 | paper=2014_probability2014_team | chars=324 ===
. Let X1, ..., Xn be i.i.d. N(0, σ2), and let M be the mean of |X1|, ..., |Xn|.
1. Find c ∈R so that ˆσ = cM is a consistent estimator of σ.
2. Determine the limiting distribution for √n(ˆσ −σ).
3. Identify an approximate (1 −α)% confidence interval for σ.
4. Is ˆσ = cM asymptotically efficient? Please justify your answer.

=== [2014] Probability & Statistics | kind=team | n=5 | paper=2014_probability2014_team | chars=656 ===
. The shifted exponential distribution has the density function
f(y; ϕ, θ) = 1/θ exp{−(u −ϕ)/θ},
y > ϕ, θ > 0.
Let Y1, . . . , Yn be a random sample from this distribution. Find the maximum likelihood
estimator (MLE) of ϕ and θ and the limiting distribution of the MLE.
You may use the following R´enyi representation of the order statistics: Let E1, . . . , En, be
a random sample from the standard exponential distribution (i.e., the above distribution
with ϕ = 0, θ = 1). Let E(r) denote the r-th order statistics. According to the R´enyi
representation,
E(r)
D=
r
∑
j=1
Ej
n + 1 −j ,
r = 1, . . . , n.
Here, the symbol
D= denotes equal in distribution.

=== [2015] Probability & Statistics | kind=individual | n=1 | paper=2015_probability2015_individual | chars=297 ===
. (a) Let X and Y be two random variables with zero means, variance 1,
and correlation ρ. Prove that
E[max{X2, Y 2}] ≤1 +
√
1 −ρ2.
(b) Let X and Y have a bivariate normal distribution with zero means, variances
σ2 and τ 2, respectively, and correlation ρ. Find the conditional expectation E(X|Y ).

=== [2015] Probability & Statistics | kind=individual | n=2 | paper=2015_probability2015_individual | chars=102 ===
. We flip a fair coin until heads turns out twice consecutively. What is the
expected number of flips?

=== [2015] Probability & Statistics | kind=individual | n=3 | paper=2015_probability2015_individual | chars=297 ===
. Let (Xn, n ≥1) be a sequence of independent Gaussian variables, with
respective mean µn, and variance σ2
n.
(a) Prove that if ∑
n X2
n converges in L1, then ∑
n X2
n converges in Lp, for every
p ∈[1, ∞).
(b) Assume that µn = 0, for every n. Prove that if ∑
n σ2
n = ∞, then
P(
∑
n
X2
n = ∞) = 1.

=== [2015] Probability & Statistics | kind=individual | n=4 | paper=2015_probability2015_individual | chars=367 ===
.
Let X1, . . . , Xn be a random sample of size n from the exponential
distribution with pdf f(x; θ) = θ−1 exp(−x/θ) for x, θ > 0, zero elsewhere.
Let
Y1 = min{X1, . . . , Xn}. Consider an estimator nY1.
(a) Show this estimate is unbiased.
(b) Prove or disprove: This estimate is a consistent estimator.
(c) Prove or disprove: This estimate is an efficient estimator.

=== [2015] Probability & Statistics | kind=individual | n=5 | paper=2015_probability2015_individual | chars=418 ===
. Let the independent normal random variables Y1, . . . , Yn have, respec-
tively, the probability density functions N(µ, γ2x2
i ), i = 1, . . . , n, where the given
x1, . . . , xn are not all equal and no one of which is zero.
(a) Construct a confidence interval for γ with significance level 1 −α.
(b) Discuss the test of the hypothesis H0 : γ = 1, µ unspecified, against all alternatives
H1 : γ ̸= 1, µ unspecified.

=== [2015] Probability & Statistics | kind=team | n=1 | paper=2015_team_probability2015 | chars=493 ===
. One hundred passengers board a plane with exactly 100 seats. The first
passenger takes a seat at random. The second passenger takes his own seat if it is
available, otherwise he takes at random a seat among the available ones. The third
passenger takes his own seat if it is available, otherwise he takes at random a seat
among the available ones.
This process continues until all the 100 passengers have
boarded the plane. What is the probability that the last passenger takes his own seat?

=== [2015] Probability & Statistics | kind=team | n=2 | paper=2015_team_probability2015 | chars=287 ===
. Assume a sequence of random variables Xn converges in distribution to a
random variable X. Let {Nt, t ≥0} be a set of positive integer-valued random variables,
which is independent of (Xn) and converges in probability to ∞as t →∞. Prove that
XNt converges in distribution to X as t →∞.

=== [2015] Probability & Statistics | kind=team | n=3 | paper=2015_team_probability2015 | chars=302 ===
. Suppose T1, T2, . . . , Tn is a sequence of independent, identically distributed
random variables with the exponential distribution of the density function
p(x) =
{
e−x,
x ≥0;
0,
x < 0.
Let Sn = T1 + T2 + · · · + Tn. Find the distribution of the random vector
Vn =
{ T1
Sn
, T2
Sn
, · · · , Tn
Sn
}
.

=== [2015] Probability & Statistics | kind=team | n=4 | paper=2015_team_probability2015 | chars=299 ===
. Suppose that X and Z are jointly normal with mean zero and standard
deviation 1.
For a strictly monotonic function f(·), cov(X, Z) = 0 if and only if
cov(X, f(Z)) = 0, provided the latter covariance exists. Hint: Z can be expressed
as Z = ρX + ε where X and ε are independent and ε ∼N(0,
√
1 −ρ2).

=== [2015] Probability & Statistics | kind=team | n=5 | paper=2015_team_probability2015 | chars=390 ===
. Consider the following penalized least-squares problem (Lasso):
1
2∥Y −Xβ∥2 + λ∥β∥1
Let bβ be a minimizer and ∆= bβ −β∗for any given β∗. If λ > 2∥XT(Y −Xβ∗)∥∞,
show that
1. ∥Y −XT bβ∥2 −∥Y −XTβ∗∥2 > −λ∥∆∥1.

 
2. ∥∆Sc∥1 ≤3∥∆S∥1, where S = {j : β∗
j ̸= 0} is the support of the vector β∗, Sc is
its complement set, ∆S is the subvector of ∆restricted on the set S, and ∥∆S∥1
is its L1-norm.

=== [2016] Probability & Statistics | kind=team | n=1 | paper=2016_2016_team | chars=275 ===
. For a random walk process on the complete infinite binary tree (see Fig
1.) starting from root (i.e. level 0), we assume that the object moves to the neighbor
nodes with equal probability. Let Xn denote the level number at time = n. Please
prove that
EXn ≤1/3n + 4/3
Fig 1.

=== [2016] Probability & Statistics | kind=team | n=2 | paper=2016_2016_team | chars=1052 ===
. The goal is to show the concentration inequality for the median of mean
estimator. We divide the problem into three simple steps.
1. Let X be a random variable with EX = µ < ∞and Var(X) = σ2 < ∞. Suppose
we have m i.i.d. random samples {Xi}m
i=1. Let ˆµm =
1
m
Pm
i=1 Xi from X. Show
that
P
 |bµm −µ| ≥2σ
r
1
m

≤1
4.
2. Given k i.i.d. Bernoulli random variables {Bj}k
j=1 with EBj = p < 1
2. Use the
moment generating function of Bj, i.e., E(exp(tBj)), to show that
P
 1
k
k
X
j=1
Bj ≥1
2

≤(4p(1 −p))
k
2 .
3. Suppose we have n i.i.d. random samples {Xi}n
i=1 from a population with mean
µ and variance σ2. For any positive integer k, we randomly and uniformly divide
all the samples into k subsamples, each having size m = n/k (for simplicity,
we assume n is always divisible by k). Let bµj be the sample average of the jth

 
subsample and em be the median of {bµj}k
j=1. Apply the previous two results to
show that
P

| em −µ| ≥2σ
r
k
n

≤
 √
3
2
k.
Hint: Consider the Bernoulli random variable Bj = 1{|bµj −µ| ≥2σ
q
k
n} for
j = 1, ..., k.

=== [2016] Probability & Statistics | kind=team | n=3 | paper=2016_2016_team | chars=588 ===
. (a) Let N ≥2 be an integer, and let X be a random variable taking
values in {0, 1, 2, . . .} such that P{X ≡k (mod N)} =
1
N for all k ∈{0, 1, . . . , N −1}.
Compute E(ei(2πm)X/N) (with i = √−1) for all integers m ≥1.
(b) A game for N players (numbered as 0, 1, 2, . . ., N −1) is as follows: Each player
independently shows a random number of fingers (uniformly chosen from {0, 1, 2, 3, 4, 5});
if S denotes the total number of fingers shown, then the player number S mod N is de-
clared to be the winner of the game.
Find all N such that the players have equal chance to win the game.

=== [2016] Probability & Statistics | kind=team | n=4 | paper=2016_2016_team | chars=178 ===
. Let X1, X2, . . . be independent and identically distributed real-valued
random variables.
Prove or disprove:
If lim supn→∞
|Xn|
n
≤1 almost surely, then
P∞
n=1 P(|Xn| ≥n) < ∞.

=== [2016] Probability & Statistics | kind=team | n=5 | paper=2016_2016_team | chars=271 ===
. Choose, at random, 2016 points on the circle x2 + y2 = 1. Interpret them
as cuts that divide the circle into 2016 arcs. Compute the expected length of the arc
that contains the point (1, 0). How about the variance.

 
S.-T. Yau College Student Mathematics Contests 2016

=== [2016] Probability & Statistics | kind=individual | n=1 | paper=2016_probability2016_individual | chars=402 ===
. A random walker moves on the lattice Z2 according to the following rule:
in the first step it moves to one of its neighbors with probability 1/4, and then in step
n > 1 it moves to one of the neighbors that it didn't visit in the step n −1 with equal
probability. Let T be the time when the random walker steps on a site that it already
visited. Please show that the expectation of T is less than 35.

=== [2016] Probability & Statistics | kind=individual | n=2 | paper=2016_probability2016_individual | chars=221 ===
. Let X be a N × N random matrix with i.i.d. random entries, and
P(X11 = 1) = P(X11 = −1) = 1/2
Define
∥X∥op =
sup
v∈CN:∥v∥2=1
∥Xv∥2
Please show that for any fixed δ > 0,
lim
N→∞P(∥X∥op ≥N 1/2+δ) = 0
Hint: ∥X∥2
op ≤tr|X|2

=== [2016] Probability & Statistics | kind=individual | n=3 | paper=2016_probability2016_individual | chars=254 ===
. Suppose that 2016 balls are put into 2016 boxes with each ball indepen-
dently being put into box i with probability
1
3×1008 for i ≤1008 and
2
3×1008 for i > 1008.
Let T be the number of boxes containing exactly 2 balls. Please find the variance of T.

=== [2016] Probability & Statistics | kind=individual | n=4 | paper=2016_probability2016_individual | chars=160 ===
. Let b > a > 0 be real numbers. Let X be a random variable taking values
in [a, b], and let Y = 1
X . Determine the set of all possible values of E(X) × E(Y ).

=== [2016] Probability & Statistics | kind=individual | n=5 | paper=2016_probability2016_individual | chars=226 ===
. Let X1, X2, . . . be independent and identically distributed real-valued
random variables such that E(X1) = −1. Let Sn = X1 + · · · + Xn for all n ≥1, and let
T be the total number of n ≥1 satisfying Sn ≥0. Compute P(T = ∞).

=== [2017] Probability & Statistics | kind=team | n=1 | paper=2017_2017_team | chars=472 ===
. Let µn be the uniform probability measure on the n-dimensional cube
[−1, 1]n.
Let H ∈Rn be the hyperplane orthogonal to the principal diagonal, i.e.,
H = (1, · · · , 1)⊥. For any r > 0, we further define
AH, r := {x ∈[−1, 1]n, dist(x, H) ≤r},
where dist(x, H) represents the distance from the point x to the hyperplane H. Show
that for any constant ε > 0, the following two estimates hold for all sufficiently large n
1 :
µn¡
AH, nε¢
≥1 −n−2ε,
2 :
µn¡
AH, nε¢
≥1 −e−nε/2

=== [2017] Probability & Statistics | kind=team | n=2 | paper=2017_2017_team | chars=183 ===
.
Let X1, X2, . . . be positive random variables.
We assume that Xn
converges to 0 in probability, and that limn→∞E(Xn) = 2. Prove that limn→∞E(|Xn −
1|) exists and compute its value.

=== [2017] Probability & Statistics | kind=team | n=3 | paper=2017_2017_team | chars=568 ===
. There are n people playing a game. Initially everybody had one dollar at
hand. During each round of the game, we randomly pick two people and they will toss
a fair coin, to decide who wins this round of the game. The loser will submit one dollar
(note: just one, not all of his money) to the winner. Assume that a person who had no
money at hand will be immediately driven out of the game. The game stops until all
money is at the hand of only one person. Calculate the average number of rounds that
the game plays.
Note: In each round only two players are involved.

=== [2017] Probability & Statistics | kind=team | n=4 | paper=2017_2017_team | chars=291 ===
.
Let {Xn}n∈N and {X′
n}n∈N be two independent simple random walks on Zd such
that X0 = X′
0 = 0. Here simple walk means if x, y ∈Zd and ∥x −y∥= 1, then
P(Xn+1 = y|Xn = x) = (2d)−1
Let I = {(s, t) : Xs = X′
t}. Prove that |I| < ∞a.s.
Hint: You can first prove that
P(Xn = 0) = O(n−d/2),
n →∞

=== [2017] Probability & Statistics | kind=team | n=5 | paper=2017_2017_team | chars=534 ===
. Suppose X1, . . . , Xn are i.i.d. Poisson variables with mean λ and we are
interested in estimating p = Pλ(Xi = 0) = e−λ.
1

 
(a) One estimator for p is the proportion of zeros in the sample, ˜p = #{i ≤n : Xi =
0}/n. Determine limiting distribution for √n(˜p −p).
(b) Another estimator would be the maximum likelihood estimator ˆp. Give a formula
for ˆp and determine limiting distribution for √n(ˆp −p).
(c) Find the asymptotic relative efficiency of ˜p with respect to ˆp.
2

 
S.-T. Yau College Student Mathematics Contests 2017

=== [2017] Probability & Statistics | kind=individual | n=1 | paper=2017_probability2017_individual | chars=301 ===
. A box contains 750 red balls and 250 blue balls. Repeatedly pick a ball
uniformly at random from the box and remove it until all remaining balls have a single
color. (Note: no replacement).
Please find integer m such that the expectation value for the total number of the
remaining balls ∈[m, m + 1]

=== [2017] Probability & Statistics | kind=individual | n=2 | paper=2017_probability2017_individual | chars=634 ===
. Suppose a number X0 ∈{1, −1} at the root of a binary tree
is propagated away from the root as follows. The root is the node at level 0. After
obtaining the 2h numbers at the nodes at level h, each number at level h+1 is obtained
from the number adjacent to it (at level h) by flipping its sign with probability p ∈
(0, 1/2) independently.
Let Xh be the average of the 2h values received at the nodes at level h. Define the
signal-to-noise ratio at level h to be
Rh :=
 E[Xh | X0 = 1] −E[Xh | X0 = −1]
2
V ar[Xh|X0 = 1]
.
Find the threshold number pc such that Rh converges to 0 if p ∈(pc , 1/2) and diverges
if p ∈(0, pc), as h →∞.

=== [2017] Probability & Statistics | kind=individual | n=3 | paper=2017_probability2017_individual | chars=503 ===
. Consider the space representing an infinite sequence of coin flips, namely
Ω:= {H, T}∞, (H: head, T: tail) with the associated σ-field F generated by finite
dimensional rectangles. For 0 ≤p ≤1, denote by Pp the probability measure on (Ω, F)
corresponding to flipping a coin an infinite number of times with probability of H being
p and probability of T being q = 1 −p at each flip.
Show that for each p ∈[0, 1], there exists Ap such that
Pp(Ap) > 1/2
1

 
and for any p′ ̸= p, p′ ∈[0, 1]
Pp′(Ap) < 1/2

=== [2017] Probability & Statistics | kind=individual | n=4 | paper=2017_probability2017_individual | chars=597 ===
. Let G := G(n, p) be a random graph with n vertices where each possible
edge has probability p of existing. The existence of the edges are independent to each
other. With G, we say A ⊂{1, 2, · · · , n} is a fully connected set if and only if
i, j ∈A =⇒i −th and j −th vertices are (directly) connected with an edge in G
Define T as the size of the largest fully connected set
T := max{|A| : A is a fully connected set}
Let's fix p ∈(0, 1), please prove that
lim
n→∞P
 
T
2 log 1
p n ≤1 + ϵ
!
= 1,
∀ϵ > 0,
and
lim
n→∞P


T
q
2 log 1
p n
≥1 −ϵ

= 1,
∀ϵ > 0,
Hint:
P (T = n) = p(n
2) = pn(n−1)/2

=== [2017] Probability & Statistics | kind=individual | n=5 | paper=2017_probability2017_individual | chars=451 ===
. Consider a population of constant size N + 1 that is suffering from an
infectious disease. We can model that spread of the disease as Markov process. Let
X(t) be the number of healthy individuals at time t and suppose that X(0) = N. We
assume that if X(t)
lim
h→0
1
hP (X(t + h) = n −1|X(t) = n)) = λn (N + 1 −n)
For 0 ≤s ≤1, 0 ≤t, define
G(s, t) := E(sX(t))
Please find a non-trivial partial differential equation for G(s, t), which involves ∂tG.
2

=== [2018] Probability & Statistics | kind=team | n=1 | paper=2018_2018_team | chars=414 ===
. Let Xi, 1 ≤i ≤N be i.i.d. random variables. Here X1 is uniformly
distributed on [0, 1]. We reorder them as
e
X1 ≤e
X2 ≤· · · e
XN
a) Let N = 2m −1, and Y = e
Xm, please find the A and B such that
Y −A
N B
has nontrivial distribution, and please find this distribution.
b) Let N = 2m, and Y = e
Xm −e
Xm−1, please find the A and B such that
Y −A
N B
has nontrivial distribution, and please find this distribution.

=== [2018] Probability & Statistics | kind=team | n=2 | paper=2018_2018_team | chars=502 ===
. Let X = (Z2)N, i.e., X = (X1, X2 · · · , XN · · · ), Xi ∈(0, 1). It can be
considered as countable lightbulbs. 0 means off, 1 means on. We start with X0 =
0. Keep generating independent geometric random variables, whose distribution are
geom(1/2). Denote them as K1, K2 · · · . Now let Xm (for m ≥1) be as follows
(Xm −Xm−1)k = 1(k = Km),
Z2
i.e, in the m −th turn, we only change the status of the Km−th light bulb. Then what
is the probability of all lights being offagain, i.e.,
P (∃m > 1,
Xm = 0)

=== [2018] Probability & Statistics | kind=team | n=3 | paper=2018_2018_team | chars=513 ===
. Let x1, x2, . . . , xn be d-dimensional vectors of real numbers with n suffi-
ciently large but the exact value is not of importance.
A function of µ is defined to be
ℓ(µ) = sup{
n
X
i=1
log pi :
n
X
i=1
pixi = µ;
n
X
i=1
pi = 1, p1 > 0, . . . , pn > 0}
on the space of the interior of the convex hull of x1, . . . , xn.
(a) Show that this is a concave function of µ on the convex hull.
(b) Let ¯x = n−1 Pn
i=1 xi. Let a be a vector of length d. Prove that ℓ(¯x + ta) is a
decreasing function of t when t > 0.
1

=== [2018] Probability & Statistics | kind=team | n=4 | paper=2018_2018_team | chars=719 ===
. Consider the histogram estimator, defined as follows. We observe iid
random variables X1, . . . , Xn, taking values in [0, 1] according to the distribution with
PDF f (assuming it is sufficiently smooth). Define bins
B1 =
·
0, 1
m
¶
, B2 =
· 1
m, 2
m
¶
, . . . , Bm =
·m −1
m
, 1
¸
Let h = 1/m, vj be the number of observations in bin Bj, and define ˆpj = vj/n and
pj =
R
Bj f(u)du. Then the histogram estimator of the density f is
ˆfn(x) =
m
X
j=1
ˆpj
h I{x ∈Bj}
1. Find the (exact) mean and variance of ˆfn(x).
2. Explain why increasing the number of bins decreases the bias of ˆfn(x).
3. If our goal is to minimize the mean-squared error
MSE = E
·Z
(f(x) −ˆfn(x))2dx
¸
,
please give some advice on how to choose m.

=== [2018] Probability & Statistics | kind=team | n=5 | paper=2018_2018_team | chars=632 ===
. Let Xi ∼N(θi, 1) independently for i = 1, . . . , k. We are interested in
estimating τ = θ2
1 + · · · + θ2
k given observations X1, . . . , Xk.
1. A possible estimator of τ is ˜τ = Pk
i=1 X2
i −k. Show that it is unbiased and
compute its sampling variance.
2. Now assume the proper prior θi ∼N(0, A), independently for i = 1, . . . , k and
a given A > 0. Since A is unknown, please provide an estimator ˆA of A and
also derive the empirical Bayes estimator of τ, denoted as ˆτB. (Hint: ˆτB = E(τ |
X1, . . . , Xk, ˆA)).
3. How do you compare the two estimators, ˜τ and ˆτB?
2

 
S.-T. Yau College Student Mathematics Contests 2018

=== [2018] Probability & Statistics | kind=individual | n=1 | paper=2018_probability2018_individual | chars=483 ===
. A submarine is lost in some ocean. There are two (and only two) possible
regions: A and B. Experts estimate the probability of being lost in A is 70%. On the
other hand, for each search, the probability of finding this submarine is 40% if it is lost
in A. This number is 80% for region B. Now we have independently searched region A
4 times and region B once, but still have not found the submarine yet. Now based on
these informations, which region we should search next? And why?

=== [2018] Probability & Statistics | kind=individual | n=2 | paper=2018_probability2018_individual | chars=475 ===
. A teacher and 12 students sit around a circle. In the beginning the teach
holds a gift, he will randomly pass it to the left person or right person next to him, so
as the other students each time. (For the gift, It is like a random walk between these
people) The rule is that the gift will be eventually given to some student (not teacher)
if he/she
is the last student who ever touches the gift.
Which student(s) have the highest probability to get this gift (i.e., win) ?

=== [2018] Probability & Statistics | kind=individual | n=3 | paper=2018_probability2018_individual | chars=253 ===
. In a party, N people attend, each of them brings k gifts. When they
leave, each of them randomly picks k gifts. Let X be the total number of gifts which
are taken back by their owners. Let's fix k, please find the limiting distribution of X
when N →∞.

=== [2018] Probability & Statistics | kind=individual | n=4 | paper=2018_probability2018_individual | chars=458 ===
. Suppose that a random vector x = (x1, ..., xn)′ ∈Rn(n ≥2) is distributed
as a multivariate normal distribution N(0, Σ) with the following joint probability den-
sity function
f(x) =
1
(2π)
n
2 det(Σ)
1
2 exp
½
−1
2x′Σ−1x
¾
, x ∈Rn,
where Σ is an n × n positive definite matrix. Let the (i, j) element of Ω= Σ−1 be ωij
(1 ≤i, j ≤n). For 1 ≤i ̸= j ≤n, show that if ωij = 0, then xi and xj are conditionally
independent when the other elements of x are given.

=== [2018] Probability & Statistics | kind=individual | n=5 | paper=2018_probability2018_individual | chars=585 ===
. Letx, y be two independent random vectors in Rn (n ≥3). Assume that
P(y = 0) = 0 and x has a standard multivariate normal distribution, i.e., x ∼N(0, In).
(a) For any nonzero constant vector a ∈Rn satisfying ||a|| = (a′a)1/2 = 1, prove that
√
n −1
a′x
p
||x||2 −(a′x)2 ∼tn−1,
here tn−1 stands for a t distribution with n −1 degrees of freedom.
(b) The sample correlation coefficient between x = (x1, ..., xn)′ and y = (y1, ..., yn)′ is
defined as
r =
Pn
i=1(xi −¯x)(yi −¯y)
pPn
i=1(xi −¯x)2pPn
i=1(yi −¯y)2.
where ¯x = Pn
i=1 xi/n, ¯y = Pn
i=1 yi/n. Show that √n −2
r
√
1−r2 ∼tn−2.
1

=== [2019] Probability & Statistics | kind=individual | n=1 | paper=2019_ProbaStat2019_individual | chars=170 ===
Suppose (Xn)n≥1 is a sequence of positive random variables. There exists a constant C > 0 such that,
E[Xn] ≤C,
E[max{0, −log Xn}] ≤C,
∀n.
Show that
lim sup
n→∞X1/n
n
= 1.

=== [2019] Probability & Statistics | kind=individual | n=2 | paper=2019_ProbaStat2019_individual | chars=329 ===
Suppose γ is a probability measure on {0, 1, 2} such that γ(0) > γ(2) > 0. Let (ξn)n≥1 be a sequence
of i.i.d. random variables with common law γ. Define the sequence
Y0 = 0,
Yn+1 = max{0, Yn + ξn+1 −1},
∀n ≥0.
Show that (Yn)n≥0 is an irreducible Markov chain on the state space N = {0, 1, 2, . . .} and it is positive
recurrent.

=== [2019] Probability & Statistics | kind=individual | n=3 | paper=2019_ProbaStat2019_individual | chars=257 ===
Suppose (ϵn)n≥1 is a sequence of i.i.d. random variables and the common law is Bernoulli:
P[ϵ1 = 1] = P[ϵ1 = −1] = 1/2.
Consider the random series f(x) = P∞
n=1 ϵnxn. Show that the random series attains zero infinitely
many times on x ∈[0, 1) almost surely.

=== [2019] Probability & Statistics | kind=individual | n=4 | paper=2019_ProbaStat2019_individual | chars=3226 ===
Consider a randomized experiment with 2N units, half to be randomly assigned an active treatment,
and the other half to be assigned the control treatment; the objective is to measure the effect of the
active versus control treatments on an outcome, called Y . For example, the units could be people with
high blood pressure, where Y is blood pressure one week after receiving the active drug or an inactive
drug, a placebo, where the patient is blinded to which drug is being given.
The estimand, the goal of the experiment, is the average value of Y if all 2N units received active
minus the average value of Y if all 2N units received control. Assume that these 2 × 2N numbers
are fixed quantities (in the statistical literature this assumption is known as SUTVA the stable-unit-
treatment-value assumption), which means that the outcome Y for the i-th unit receiving a particular
treatment is a proper function of that unit and the treatment that unit i received.
Derive the following results in this simple situation.
a) Find the expectation of the estimator, the difference in the observed sample means (between those
assigned treatment and those assigned control), in terms of the estimand (defined above), where
expectation in this context refers to averaging over all possible random allocations.
b) The variance of the estimator described in part a) (again, with variance defined as averaging over
all possible random allocations).
c) Find an unbiased estimator of the variance in part b), assuming additive treatment effects, that is,
the treatment minus control values of Y are constant across the 2N units, so that the treatment
versus control condition adds a constant value for all 2N units.
d) Find the bias of the estimator in part c) when the treatment effects are non-additive.
e) Generalize the results in parts a),b), c) and d) to the situation where 2N is replaced by Nt + Nc,
with Nt units getting active treatment and Nc units getting control, where these sample sizes are
unequal.
f) Argue that the estimator in part c), when the sample sizes are large, will look gaussian, and
conduct a small simulation to indicate that this often happens with relatively small sample sizes.
1

 
g) Modify the first four parts to consider a different randomized experiment, but still with 2N units,
half to be allocated to active and half to be allocated to control, but now we have a covariate, X, a
background variable that is suspected to be related to Y . For example, X could be blood pressure
today, pre-treatment. In this experiment, many randomized allocations are considered, but all
allocations are rejected if the sample X means of the treated and controls are too different for
example more than a standard deviation apart. Be careful here to note which results generalize
and which do not.
h) Finally, consider the randomized experiment in part g) when Nt units are treated and Nc are
control, where Nt and Nc are not equal: Which results in parts a),b),c) and d) generalize without
modification? In particular, describe how the conclusion in part f) changes. Note that this is an
interesting situation where the asymptotic distributions of sample means are not gaussian. What
are these distributions?
2

=== [2019] Probability & Statistics | kind=team | n=1 | paper=2019_ProbaStat2019_team | chars=156 ===
Suppose (Xn)n≥1 is a sequence of i.i.d. random variables and the common law is exponential with
parameter one. Show that
P
·
lim sup
n→∞
Xn
log n = 1
¸
= 1.

=== [2019] Probability & Statistics | kind=team | n=2 | paper=2019_ProbaStat2019_team | chars=204 ===
Let (Xn)n≥1 be i.i.d. real random variables and set Sn = Pn
i=1 Xi for n ≥1. Suppose that for some
constant c ∈R we have Sn/n →c as n →∞almost surely. Show that X1 has a finite first moment
and E[X1] = c.

=== [2019] Probability & Statistics | kind=team | n=3 | paper=2019_ProbaStat2019_team | chars=199 ===
Consider uniform permutation of {1, 2, . . . , n} and denote by Xn the number of cycles in the permu-
tation. Find a sequence of reals (an)n≥1 such that
lim
n→∞
E[Xn]
an
= 1,
and justify your answer.

=== [2019] Probability & Statistics | kind=team | n=4 | paper=2019_ProbaStat2019_team | chars=438 ===
The Erd¨os-R´enyi random graph G(n, p) with parameters n ≥1 and p ∈[0, 1] is the random graph
whose vertex set is V = {1, 2, . . . , n} and where for each pair i ̸= j ∈V the edge i ↔j is present with
probability p independently of all the other pairs.
(a) For ϵ > 0, if pn ≥(1 + ϵ) log n
n , then
P[G(n, pn) has an isolated vertex] →0,
as n →∞.
(b) For ϵ > 0, if pn ≤(1 −ϵ) log n
n , then
P[G(n, pn) has an isolated vertex] →1,
as n →∞.
1

=== [2020] Probability & Statistics | kind=individual | n=1 | paper=2020_Prob_Stat_probability_and_statistics_20 | chars=150 ===
. Let X be an essentially bounded random variable with mean zero. Show that
EeX ≤cosh ∥X∥∞,
where cosh x = ex+e−x
2
is the hyperbolic cosine function.

=== [2020] Probability & Statistics | kind=individual | n=2 | paper=2020_Prob_Stat_probability_and_statistics_20 | chars=206 ===
.
Let λ be a positive number. Suppose that X is a random variable with E|X| < ∞.
Suppose that
λE f (X + 1) = E{X f (X)}
for all bounded smooth functions. Show that X has the Poisson distribution Poisson(λ).

=== [2020] Probability & Statistics | kind=individual | n=3 | paper=2020_Prob_Stat_probability_and_statistics_20 | chars=409 ===
. Consider the random walk
Sn = a + X1 + X2 + · · · + Xn,
where a is a positive integer and {Xi} are independent and identically distributed random variables
with a common distribution
P{Xi = 1} = p,
P{Xi = −1} = 1 −p.
Let τ0 = inf{n : Sn = 0} be the first time the random walk reaches the state x = 0. For all p ∈[0,1]
find the probability Pa{τ0 < ∞} that the random walk will eventually hit the state x = 0.

=== [2020] Probability & Statistics | kind=individual | n=4 | paper=2020_Prob_Stat_probability_and_statistics_20 | chars=1545 ===
. Let Z = (X,Y) be an R2-valued random variable such that (1) X andY are independent;
(2) both X and Y have mean zero and finite (nonvanishing) second moments; (3) the distribution of
Z is invariant under the rotation counter-clockwise around the origin by an angle θ not a multiple of
90 degrees. Show that X and Y must be normal random variables with the same variance.
Part II: Statistics
The following collection of questions concerns the design of a randomized experiment where the
N units to be randomized to drug A or drug B are people, for whom we have a large number
of background covariates, collectively labelled X (e.g., age, sex, blood pressure, height, weight,
occupational status, history of heart disease, family history of heart disease). The objective is to
assign approximately half to drug A and half to drug B where the means of each of the X variables
(and means of non-linear functions of them, such as squares or products) are close to equal in the
two groups. Instead of using classical methods of design, such as blocking or stratification, the plan
is to use modern computers to try many random allocations and discard those allocations that are
considered unacceptable according to a pre-determined criterion for balanced X means, in particular

 
an affinely invariant measure such as the Mahalanobis distance between the means of X in the two
groups. After an acceptable allocation is found, outcome variables will be measured, and their
means will be compared in group A and group B to estimate a treatment effect.

=== [2020] Probability & Statistics | kind=individual | n=5 | paper=2020_Prob_Stat_probability_and_statistics_20 | chars=238 ===
.
Prove that if the two groups are of the same size (i.e., N/2 for even N), this plan
will result in unbiased estimates of the A versus B casual effect based on the sample means of Y in
groups A and B, where Y is any linear function of X.

=== [2020] Probability & Statistics | kind=individual | n=6 | paper=2020_Prob_Stat_probability_and_statistics_20 | chars=96 ===
.
Provide a counter-example to the assertion that Problem 5 is true in small samples
with odd N.

=== [2021] Probability & Statistics | kind=individual | n=1 | paper=2021_ExamPaper_21S_probability_and_statistics_21s | chars=216 ===
.
Suppose that a sequence {Xn} of real-valued random variables converges to X in distribution
and there are positive constants r and C such that E|Xn|r ≤C for all n. Show that
lim
n→∞E|Xn|s = E|X|s
for all 0 < s < r.

=== [2021] Probability & Statistics | kind=individual | n=2 | paper=2021_ExamPaper_21S_probability_and_statistics_21s | chars=263 ===
.
Let p(x, y) be the (one-step) transition function of a Markov chain on a discrete state space S
and pn(x, y) be the n-step transition function. Show that for any positive integers L and N and any two states
x and y we have
N+L
Õ
n=L
pn(x, y) ≤
N
Õ
n=0
pn(y, y).

=== [2021] Probability & Statistics | kind=individual | n=3 | paper=2021_ExamPaper_21S_probability_and_statistics_21s | chars=250 ===
.
Let {Xn} be an independent, identically distributed sequence of random variables with the
symmetric Bernoulli distribution
P {X = 1} = P {X = −1} = 1
2.
Let Sn =
N
Õ
i=1
Xi be the partial sum. Show that for all α > 1
2,
P

lim
n→∞
Sn
nα = 0

= 1.

=== [2021] Probability & Statistics | kind=individual | n=4 | paper=2021_ExamPaper_21S_probability_and_statistics_21s | chars=263 ===
.
Let Xn =

Xij
 
be an n × n random matrix whose entries are independent and identically
distributed random variables with the symmetric Bernoulli distribution
P {X = 0} = P {X = 1} = 1
2.
Let pn = P {det XN is odd}. Show that lim
n→∞pn > 0.
Part II: Statistics

=== [2021] Probability & Statistics | kind=individual | n=5 | paper=2021_ExamPaper_21S_probability_and_statistics_21s | chars=1468 ===
. You have been asked to help design a randomized trial of a new drug, call it drug A, to be used
in place of the current drug, call it drug B, for a particular medical condition. The budget is fixed to have
1000 patients treated with A and 1000 treated with drug B. The issue is how to do the allocation of patients,
because we have many pre-randomization measurements on each patient, roughly 200, such as blood pressure

 
recordings, age, sex, and a large collection of genetics measurements. Obviously it is desirable to have the
A group similar to the B group with respect to all pre-treatment covariates and non-linear functions of them
that are expected to influence the effectiveness of the drugs with respect to the outcome variables.
Complete (or simple) randomization does this in expectation, but with many covariates, some covariates will
not be balanced between the A and B groups in any one single randomized allocation. Standard blocking
used in traditional experimental design can force balance on a few covariates, but the designer of drug A
wants to have an experimental design that creates balance on many covariates, and feels that you, as a modern
applied mathematician/statistician, should be able to do this.
Describe a class of methods that achieves this goal where each patient has a positive probability of receiving
drug A and a positive probability of receiving drug B. Provide enough detail that you are describing an
explicit algorithm.

=== [2021] Probability & Statistics | kind=individual | n=6 | paper=2021_ExamPaper_21S_probability_and_statistics_21s | chars=796 ===
. You are given the results of a randomized experiment of two drugs, A and B. The experiment
was not conducted in the usual way, however, but rather by allocating patients by a machine-learning
algorithm under which each patient has a positive probability of receiving A and of receiving B; moreover
the algorithm is completely specified and is built to create better than random balance on the covariates.
(a) Can unbiased estimates of the causal effect of drug A versus B be found, and if so, show why.
(b) Can exact small sample, non-parametric inferences for the causal effect in part (a) be derived, based
solely on the randomization distribution of some statistic? For example, can we find exact significance
levels under a sharp null hypothesis? If so, outline how to accomplish this goal.

=== [2022] Probability & Statistics | kind=individual | n=1 | paper=2022_ExamPaper_2022_probability_and_statistics_22s | chars=229 ===
.
Let {𝑋𝑛} be a sequence of Gaussian random variables. Suppose that 𝑋is a random variable such
that 𝑋𝑛converges to 𝑋in distribution as 𝑛→∞. Show that 𝑋is also a (possibly degenerate, i.e., variance zero)
Gaussian random variable.

=== [2022] Probability & Statistics | kind=individual | n=2 | paper=2022_ExamPaper_2022_probability_and_statistics_22s | chars=617 ===
.
For two probability measures 𝜇and 𝜈on the real line 𝐑, the total variation distance ‖𝜇−𝜈‖𝑇𝑉is
defined as
‖𝜇−𝜈‖𝑇𝑉= sup {𝜇(𝐶) −𝜈(𝐶) ∶𝐶∈ℬ(𝐑)} ,
where ℬ(𝐑) is the 𝜎-algebra of Borel sets on 𝐑. Let 𝒞(𝜇, 𝜈) be the space of couplings of the probability measures
𝜇and 𝜈, i.e., the space of 𝐑2 valued random variables (𝑋, 𝑌) defined on some (not necessarily same) probability
space (Ω, ℱ, ℙ) such that the marginal distributions of 𝑋and 𝑌are 𝜇and 𝜈, respectively. Show that
‖𝜇−𝜈‖𝑇𝑉= inf {ℙ(𝑋≠𝑌) ∶(𝑋, 𝑌) ∈𝒞(𝜇, 𝜈)} .
For simplicity you may assume that 𝜇and 𝜈are absolutely continuous with respect to the Lebesgue measure on
𝐑.

=== [2022] Probability & Statistics | kind=individual | n=3 | paper=2022_ExamPaper_2022_probability_and_statistics_22s | chars=373 ===
.
We throw a fair die repeatedly and independently. Let 𝜏11 be the first time the pattern 11 (two
consecutive 1's) appears and 𝜏12 the first time the pattern 12 (1 followed by 2) appears.
(a) Calculate the expected value 𝔼𝜏11.
(b) Which is larger, 𝔼𝜏11 or 𝔼𝜏12? It is sufficient to give an intuitive argument to justify your answer. You can
also calculate 𝔼𝜏12 if you wish.

=== [2022] Probability & Statistics | kind=individual | n=4 | paper=2022_ExamPaper_2022_probability_and_statistics_22s | chars=443 ===
.
Let {𝑋𝑛} be a Markov chain on a discrete state space 𝑆with transition function 𝑝(𝑥, 𝑦), 𝑥, 𝑦∈𝑆.
Suppose that there is a state 𝑦0 ∈𝑆and a positive number 𝜃such that 𝑝(𝑥, 𝑦0) ≥𝜃for all 𝑥∈𝑆.
(a) Show that is a positive constant 𝜆< 1 such that for any two initial distribution 𝜇and 𝜈,
∑
𝑦∈𝑆
||ℙ𝜇{𝑋1 = 𝑦} −ℙ𝜈{𝑋1 = 𝑦}|| ≤𝜆∑
𝑦∈𝑆
|𝜇(𝑦) −𝜈(𝑦)| .
(b) Show that the Markov chain has a unique stationary distribution 𝜋and
∑
𝑦∈𝑆
||ℙ𝜇{𝑋𝑛= 𝑦} −𝜋(𝑦)|| ≤2𝜆𝑛.

=== [2022] Probability & Statistics | kind=individual | n=5 | paper=2022_ExamPaper_2022_probability_and_statistics_22s | chars=542 ===
. Consider a linear regression model with 𝑝predictors and 𝑛observations:
𝐘= 𝑋𝛽+ 𝐞,
where 𝑋𝑛×𝑝is the design matrix, 𝛽is the unknown coefficient vector, and the random error vector 𝐞has a mul-
tivariate normal distribution with mean zero and Var(𝐞) = 𝜎2𝐼𝑛(𝜎2 > 0 unknown and 𝐼𝑛is the identity matrix).

 
Here rank(𝑋) = 𝑘≤𝑝, 𝑝may or may not be greater than 𝑛, but we assume 𝑛−𝑘> 1. Let 𝐱1 = (𝑥1,1, … , 𝑥1,𝑝) be
the first row of 𝑋and define
𝛾= 𝐱1𝛽
𝜎.
Find the uniformly minimum variance unbiased estimator (UMVUE) of 𝛾or prove it does not exist.

=== [2022] Probability & Statistics | kind=individual | n=6 | paper=2022_ExamPaper_2022_probability_and_statistics_22s | chars=354 ===
. Let 𝑋1, … , 𝑋2022 be independent random variables with 𝑋𝑖∼ 𝑁( 𝜃𝑖, 𝑖2), 1 ≤𝑖≤2022. For estimating
the unknown mean vector 𝜽∈𝑅2022, consider the loss function 𝐿(𝜽, 𝐝) = ∑
2022
𝑖=1 (𝑑𝑖−𝜃𝑖)2/𝑖2. Prove that 𝐗=
(𝑋1, … , 𝑋2022) is a minimax estimator of 𝜽.
Recall: If 𝑌|𝜇  ∼𝑁(𝜇, 𝜎2) and 𝜇∼ 𝑁(𝜇0, 𝜎2
0) then 𝜇|𝑌= 𝑦∼𝑁(
𝜇0/𝜍2
0+𝑦/𝜍2
1/𝜍2
0+1/𝜍2 ,
1
1/𝜍2
0+1/𝜍2).

=== [2023] Probability & Statistics | kind=individual | n=1 | paper=2023_probability_statistics | chars=639 ===
The sequence (X1, X2, . . . , Xn, . . .) is a Dirichlet process with base distribution G0 and
concentration parameter α0 > 0 if G0 is a probability distribution on R and satisfies:
• X1 ∼G0
• Conditional on X1, X2, . . . , Xn, the distribution of Xn+1 is α0G0+Pn
i=1 δXi, appro-
priately normalized, where δx is the Dirac measure with probability 1 on singleton
{x}.
Assume that G0 has finite first and second moments.
(a) Derive the distribution of Xn, n ≥1.
(b) Let Yn = I(Xn > 0). Prove or disprove (Yn)n≥1 forms a Dirichlet Process. If
(Yn)n≥1 forms a Dirichlet Process, determine its concentration parameter and its
base distribution.

=== [2023] Probability & Statistics | kind=individual | n=2 | paper=2023_probability_statistics | chars=491 ===
Suppose X and Y are non-negative random variables on a probability space (Ω, F, P).
Let H(x, y) be a function on [0, ∞)2 such that E(|H(X, Y )|) < ∞. Define function
φ(u) = u/(1 + u) for u ≥0. For integer n = 0, 1, 2, . . ., let
Un =
2n
X
j=1
j −1
2n I
j −1
2n
≤φ(X) < j
2n

,
Vn = E(H(X, Y )|Un).
Prove or disprove that there exists a random variable Z such that as n →∞, Vn
converges to Z almost surely. If there exists such a Z, show the expression of Z (in
the sense of almost surely).

=== [2023] Probability & Statistics | kind=individual | n=3 | paper=2023_probability_statistics | chars=331 ===
Let X1, X2, . . . , Xn be a sequence of i.i.d. random variables with a uniform distribution
on (0, 1). Define the events A1, A2, . . . by
An = {Xn = max(X1, . . . , Xn)}.
Define Rn = Pn
k=1 I(Ak).
Let (mn) be a sequence of positive numbers such that
limn→∞mn = ∞. Compute the following limit
lim
n→∞P

|Rn −log n| > mn
p
log n

1

=== [2023] Probability & Statistics | kind=individual | n=4 | paper=2023_probability_statistics | chars=599 ===
Denote by B the Borel sigma field on the real line R, and let (Ω, F) be a measurable
space. Define a mapping Q(t, A) for t ∈R and A ∈F such that Q(t, ·) is a probability
measure on (Ω, F) for each t ∈R, and Q(·, A) is a Borel function for each A ∈F.
Denote by Π a probability measure on (R, B), P a probability measure on (Ω, F), and
T a random variable on (Ω, F, P). Assume that Π, P and T satisfy Π = P ◦T −1, and
for A ∈F,
P(A) =
Z
R
Q(t, A)Π(dt),
where P ◦T −1 denotes the induced probability measure by T. Prove or disprove the
following statement:
For any A ∈F,
P(A|T) = Q(T, A) almost surely.

=== [2023] Probability & Statistics | kind=individual | n=5 | paper=2023_probability_statistics | chars=752 ===
Four statisticians I, II, III and IV play a sequence of games. For each game, the winning
probabilities of I, II, III and IV are (1 −θ)/2, (1 −θ)/2, θ/2 and θ/2, respectively,
where 0 < θ < 1. There is only one winner in each game and no tie is allowed. Assume
that outcomes of games are independent of each other. For a fixed integer r ≥2, the
stopping rule is to terminate as soon as one of the following conditions hold: (1) I
and II together win r games; (2) III and IV together win r + 1 games. At the time of
termination, let X1, X2, X3 and X4 denote the numbers of games won by I, II, III and
IV, respectively.
(a) Prove or disprove the statistic T = (X1 + X2, X3 + X4) is complete.
(b) Find a uniformly minimum variance unbiased estimator of θ.

=== [2023] Probability & Statistics | kind=individual | n=6 | paper=2023_probability_statistics | chars=748 ===
A system of interest involves three random variables, X, Y , and S, where S has a
Poisson distribution with mean 2λ, for a parameter λ > 0, and where X and Y are
conditionally independent Bernoulli variables, given S = s, with
P(X = 1|S = s) =
1
2s+1 and P(Y = 1|S = s) = θ
2s,
where θ ∈(0, 1) is a second parameter. The random variable S is unobservable.
We have n i.i.d. copies (Xi, Yi) of (X, Y ).
(a) An intuitive estimator for θ is ˆθn = ¯Yn/(2 ¯Xn), where ¯Xn = 1
n
Pn
i=1 Xi and ¯Yn =
1
n
Pn
i=1 Yi. Derive its asymptotic distribution.
(b) Consider the hypothesis testing problem
H0 : θ = 1/2
versus
H1 : θ ̸= 1/2.
Construct an exact test statistic. As θ moves away from 1/2, describe all sources
of increasing power that you can think of.
2

=== [2024] Probability & Statistics | kind=individual | n=1 | paper=2024_2024_statistics | chars=927 ===
There are r players, with player i initially having ni units, ni > 0, i =
1, . . . , r. At each stage, two of the players are chosen to play a game, with
the winner of the game receiving 1 unit from the loser. Any player whose
fortune drops to 0 is eliminated, and this continues until a single player
has all n = Pr
i=1 ni units, with that player designated as the winner. Note
that the mechanism to choose two players at each stage is unknown. It can
be either deterministic or random. Assume that the results of successive
games are independent and that each game is equally likely to be won by
either of its two players.
For any set of players S ⊆{1, . . . , r}, let X(S) denote the number of
games involving only members of S. Does E(X(S)) depend on the player
selection mechanism? If you think it doesn't depend, calculate the expec-
tation. If you think it depends, give two mechanisms leading to different
expectations.

=== [2024] Probability & Statistics | kind=individual | n=2 | paper=2024_2024_statistics | chars=352 ===
Let X1, X2, . . . be independent Bernoulli random variables satisfying P(Xi =
1) = p and P(Xi = −1) = q = 1 −p for some p ∈(0, 1). Let Sn =
X1 + . . . + Xn and M = supn≥1(Sn/n).
(a) Calculate P(M = 0).
(b) Show that P(p −q < M ≤1) = 1. For any rational number x ∈
(p −q, 1], is P(M = x) > 0? If so, prove it. If not, find a point with
zero probability.

=== [2024] Probability & Statistics | kind=individual | n=3 | paper=2024_2024_statistics | chars=375 ===
Let X have a uniform distribution on the interval [0,1] and let Nm,k be
the digit in the mth place to the right of the decimal point in Xk.
(a) Find limm→∞P(Nm,m = i) for i = 0, 1, 2, . . . , 9.
(b) Let k(m) be a function of m, taking values greater than 1. Find a nec-
essary and sufficient condition on k(m) such that limm→∞P(Nm,k(m) =
i) =
1
10 for i = 0, 1, 2, . . . , 9.

=== [2024] Probability & Statistics | kind=individual | n=4 | paper=2024_2024_statistics | chars=1551 ===
Assume we have n observations: (Yi, xi), i = 1, . . . , n, where Yi is the
random response and xi = (xi1, · · · , xip)T is a vector of p fixed covariates
for the ith observation. Denote β = (β1, · · · , βp) be a unknown p-length
vector of regression coefficients. Let θi = Pp
j=1 xijβj, µi = E(Yi) and σ2
i =
V ar(Yi). Assume the density of Yi belongs to the following exponential
family:
f(yi; θi) = exp{θiyi −b(θi)},
(1)
where b′(θi) = µi, b
′′(θi) = σ2
i . Suppose that all θi's are contained in a
compact subset of a space Θ. Let ℓn(β) be the log-likelihood function of
the data, and let Hn(β) = −∂2ℓn(β)
∂β∂βT .
1

 
Let X be the set of all p covariates under consideration. Let α0 ⊂X be
the subset that contains and only contains all the important covariates
affecting Y (the corresponding βj's are nonzero). Let α be any subset of
X, and let β(α) be the vector of the components in β that correspond to
the covariates in α. Let A = {α : α0 ⊂α} be the collection of models that
including all important covariates. We assume:
(I) There exist positive constants C1, C2 such that for all sufficiently
large n,
C1 < λmin
n 1
nHn(β)
o
< λmax
n 1
nHn(β)
o
< C2,
where λmin
n
1
nHn(β)
o
and λmax
n
1
nHn(β)
o
are the smallest and largest
eigenvalues of 1
nHn(β).
(II) For any given ϵ > 0, there exists a constant δ > 0 such that, when n
is sufficiently large,
(1 −ϵ)Hn(β(α)) ≤Hn( ˜β) ≤(1 + ϵ)Hn(β(α))
for all α ∈A and ˜β satisfying ∥˜β −β(α)∥≤δ.
For any model α, let ˆβα be the MLE of β(α) based on this model. Show
that
max
α∈A ∥ˆβα −β(α)∥= Op(n−1/3).

=== [2024] Probability & Statistics | kind=individual | n=5 | paper=2024_2024_statistics | chars=663 ===
Consider a random sample of size n, and write the data as an r = rn by
c = cn matrix, {Xij : i = 1, . . . , rn; j = 1, . . . , cn} with n = rncn. To
specify notation, {Xij} are i.i.d. with c.d.f. F(x) and continuous density
f(x). Let β denote the median, i.e., F(β) = 0.5. Define an estimator by
ˆβn = min
j
n
max
i {Xij}
o
.
(a) What is the condition on rn when n →∞for median-unbiasedness,
i.e., β is also the median for the distribution of ˆβn?
(b) We further assume F is differentiable in an open neighborhood of β
and has a positive derivative at β. For rn in (a), show that rn(ˆβn−β)
converges in distribution, and find the limiting distribution function.
2

=== [2025] Probability & Statistics | kind=individual | n=1 | paper=2025_statistics | chars=865 ===
.
Consider a single observation X ∼N(µ, σ2) with both µ and σ2 unknown. We are interested in
constructing confidence interval (CI) for µ.
1. Consider the following CI:
CI(X; c1, c2) =
(
c1X ≤µ ≤c2X
if X > 0
c2X ≤µ ≤c1X
if X < 0 .
What is the coverage probability of this CI?
2. Let F(x; b1, b2) be a function that is measurable in x and is a distribution function on b1 < b2,
and which generates a randomized confidence interval whose lower and upper endpoints are
random variables b1 < b2 with distribution function F(x; b1, b2). Then, there is a randomized
confidence interval given by a distribution function G(c1, c2) randomly choosing a interval of
the form CI(x; c1, c2) with (C1, C2) ∼G and satisfying the following "minimax" property:
inf
µ,σ Eµ,σPG{µ ∈CI(X; c1, c2)} ≥sup
F
inf
µ,σ Eµ,σPF (X;·){µ ∈(b1, b2)}
Eµ,σEG [(c2 −c1)|X|] = Eµ,σEF (X;·) [(b2 −b1)] .

=== [2025] Probability & Statistics | kind=individual | n=2 | paper=2025_statistics | chars=1334 ===
.
Consider a joint distribution of the random variable pair {X, Y }, and let P1 and P2 be the two
marginal distributions on the real line (that is, for X and Y , respectively). Let p1(x) and p2(y)
be the respective densities for P1 and P2 with respect to a dominating measure µ. Let ν(·) be any
function such that ν(X) and ν(Y ) are not bounded and their expectations E1(ν(X)) and E2(ν(Y ))
are both finite under P1 and P2, respectively. Suppose a single observation r comes from population
1 with probability 1/2 and from population 2 with probability 1/2. The problem is to choose the
population, i, for which the expectation is greater, based on the single observation r.
Consider a randomized decision rule (or selection rule) to be given by a function
φ : R →[0, 1]
such that φ(r) is the probability of choosing population 1 based on the observation r. Assume φ(r)
is a one-to-one function.
For any given decision function φ(r), for any two densities p1(x) and p2(y) (with respect to
the Lebesgue measure) such that E1(ν(X)) > E2(ν(Y )), is the probability of correctly selecting
population 1 always greater than or equal to 1/2? If so, prove it. If not, for any given decision
function φ(r), construct a p1(x) and a p2(y) such that E1(ν(X)) > E2(ν(Y )) but the probability of
correctly selecting population 1 is less than 1/2.
1

=== [2025] Probability & Statistics | kind=individual | n=3 | paper=2025_statistics | chars=173 ===
.
Let n ≥2 be a natural number. Prove that there exist independent random variables X1, X2, . . . , Xn =
X0 such that
P
 Xk−1 < Xk

= 1 −
1
4 cos2 π
n+2
,
for all 1 ≤k ≤n.

=== [2025] Probability & Statistics | kind=individual | n=4 | paper=2025_statistics | chars=557 ===
.
Consider a one-way ANOVA with p cells and n/p observations per cell:
Yij = βj + Rij,
i = 1, . . . , n/p,
j = 1, . . . , p,
where {Rij} are i.i.d. Assume the true values βj = 0.
Let ψ be a given function and let ˆβj denote the solution of the equation
0 =
n/p
X
i=1
ψ
 Yij −ˆβj

.
Let ψ be a bounded function such that ψ′ is bounded and continuous near zero.
Suppose
Eψ(R) = 0 and Eψ′(R) = d ̸= 0. Assume p(log p)/n →0. Prove that there are solutions {ˆβj} of
the equation and a constant B > 0 such that
P
(
max
j
|ˆβj| ≥
 1
B
p log n
n
1/2)
≤2p
n →0.
2

=== [2026] Probability & Statistics | kind=individual | n=1 | paper=2026_2026_statistics | chars=1380 ===
. A copula is a multivariate cumulative distribution function with uniform marginals on
[0, 1]. By Sklar's Theorem, any joint distribution can be decomposed into its marginal distributions and
a copula that captures the dependence structure between variables. That is, for random variables U and
V with marginal CDFs FU and FV , their joint CDF can be written as H(u, v) = C{FU(u), FV (v)} for
some copula C. The copula parameter ρ indexes the strength and shape of dependence, independently
of the marginals.
Let Ya ∈{0, 1, . . . , L −1} be an ordinal outcome observed in treatment group a ∈{0, 1}.
(1). Define ψ = Pr(Y1 > Y0) as the probability that the outcome in the treatment group exceeds that
in the control group. Suppose the joint CDF satisfies Pr(Y1 ≤k, Y0 ≤j) = C{F1(k), F0(j)} with
the convention Fa(−1) = 0, where C is a pre-specified copula. Derive a closed-form expression for
ψ in terms of C, F1, and F0.
(2). Suppose Ya arises from a latent continuous variable Y ∗
a through the threshold model
Y ∗
a = µa + εa,
Ya = ℓ⇐⇒τℓ−1 < Y ∗
a ≤τℓ,
with shared thresholds −∞= τ−1 < τ0 < · · · < τL−2 < τL−1 = +∞and µa a constant for group
a. Also, suppose the joint distribution of the latent residuals satisfies
Pr(ε1 ≤e1, ε0 ≤e0) = C{Fε1(e1), Fε0(e0)} ,
where C is a pre-specified copula and Fεa(e) = Pr(εa ≤e). Prove that this implies
Pr(Y1 ≤k, Y0 ≤j) = C{F1(k), F0(j)} .

=== [2026] Probability & Statistics | kind=individual | n=2 | paper=2026_2026_statistics | chars=582 ===
. Consider the partitioned linear regression model
Y = X1β1 + X2β2 + ε,
where Y ∈Rn, X1 ∈Rn×k1, X2 ∈Rn×k2, k1, k2 ≥1, and [X1 X2] have full column rank. Define the
annihilator matrix
M1 = In −X1(X⊤
1 X1)−1X⊤
1 ,
which projects onto the orthogonal complement of the column space of X1. Recall that for a generic
regression of a response ˜Y on a predictor matrix ˜X with full column rank, the OLS estimator is
ˆβ = ( ˜X⊤˜X)−1 ˜X⊤˜Y .
Prove: the OLS estimator ˆβ2 obtained from the full regression of Y on [X1 X2] is identical to the OLS
estimator obtained from regressing M1Y on M1X2.

=== [2026] Probability & Statistics | kind=individual | n=3 | paper=2026_2026_statistics | chars=213 ===
. Let φ and Φ be the density and distribution functions of the standard normal, and a > 0
is a constant.
(a) Show that f(x) = 2φ(x)Φ(ax) is the density of some random variable (denoted by Y ).
(b) Calculate E(Y ).

=== [2026] Probability & Statistics | kind=individual | n=4 | paper=2026_2026_statistics | chars=159 ===
. Let {Bt, t ≥0} be a standard Brownian motion. For a > 0, define the first exit time from
the interval (−a, a):
τa = inf{t ≥0 : |Bt| = a}.
Compute E[τ 2
a].
1

=== [2026] Probability & Statistics | kind=individual | n=5 | paper=2026_2026_statistics | chars=417 ===
. Let X1, X2, . . . be i.i.d. random variables. Suppose that for some integer n ≥2, there exist
constants a > 0 and b ∈R such that
X1 + · · · + Xn
d= aX1 + b.
(U1)
Let α = ln n
ln a.
(a). Prove: In the case α = 1 and b = 0, the characteristic function of Xk is
φ(t) = exp{iµt −γ|t|}.
(b). Prove: If we additionally assume E|X1| < ∞, prove that excluding the degenerate case, it is
impossible to satisfy (U1) and α ≤1.

=== [2026] Probability & Statistics | kind=individual | n=6 | paper=2026_2026_statistics | chars=166 ===
. Let ξ and η be independent random variables. If the sum S = ξ + η and the difference
D = ξ −η are also independent, then ξ and η must follow normal distributions.
2
