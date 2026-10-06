import sympy as S

t=S.symbols('t')
s=(1+15*t)/16
out={}
for label,k,delta in [('44',S.Rational(7,4),S.Rational(1,2)),('nonsinglet',S.Rational(7,9),S.Rational(1,4))]:
    # sin(pi*t**2/2) >= t**2, pi**2 < 10
    P=S.Poly(S.expand((k*(1-t**4)-S.Rational(512,45)*t*t-delta)*s*s+12*t**4),t)
    n=P.degree()
    b=[S.factor(sum(P.nth(i)*S.binomial(j,i)/S.binomial(n,i) for i in range(j+1))) for j in range(n+1)]
    assert all(x>0 for x in b)
    out[label]={'polynomial':str(P.as_expr()),'bernstein_coefficients':list(map(str,b)),'all_positive':True}
print(out)
