import unittest, re, json
from pathlib import Path
from convert_math import convert_expr, build_displays, BLOCK_RE, TAG_RE

class ConversionTests(unittest.TestCase):
 def same(self,source,expected):
  self.assertEqual(re.sub(r'\s+','',convert_expr(source)),re.sub(r'\s+','',expected),source)
 def test_exact_semantic_regressions(self):
  cases={
   '0<kappa<1/20, L>1':r'0<\kappa<1/20,L>1','2/R_BFSS':r'2/R_{\mathrm{BFSS}}','<d_0,F^-1 J_2* d_0>':r'\langle d_{0},F^{-1}J_{2}^{*}d_{0}\rangle','<d_0,X>':r'\langle d_{0},X\rangle','D0':r'\mathrm{D0}','J2':r'J_2','W2':r'W_2','V4':r'V_4','σ0':r'\sigma_0','χ0':r'\chi_0','Uσ':r'U_{\sigma}','phi2':r'\phi_2','rho0':r'\rho_0','s0':r's_0','±lambda':r'\pm\lambda','d=sqrt J':r'd=\sqrt{J}','z_1i':r'z_{1i}','delta_i9':r'\delta_{i9}',
   'rho_F2':r'\rho_{F2}','R_fast,H2':r'R_{\mathrm{fast},H2}',
   'A_i^(a)':r'A_{i}^{(a)}','A_n^(b)':r'A_{n}^{(b)}',
   'M^(-*)':r'M^{-*}',"K'_e²":r"{K'_{e}}^{2}",
   'N^4/2':r'N^{4}/2','r_e^-1/2':r'r_{e}^{-1/2}',
   '(r_e r_f)^-1/2':r'(r_{e}r_{f})^{-1/2}',
   '||F^(-1)L||<=2s/(1-kappa)':r'\Vert F^{-1}L\Vert\le2s/(1-\kappa)',
   '||P F^-1||+||F^-1 P*||':r'\Vert PF^{-1}\Vert+\Vert F^{-1}P^{*}\Vert',
   '||S||F²':r'\Vert S\Vert_{F}^{2}',
   'beta_s,av':r'\beta_{s,a}v','P_jv':r'P_j v','Q_fv':r'Q_f v','Q_eu':r'Q_e u','w_at_a':r'w_a t_a',
   'U_B,e=constant':r'U_{B,e}=\text{ constant }',
   '[H_a-density of f]':r'[H_a\text{-density of }f]',
  }
  # Braced TeX scripts and their single-token equivalents mean the same thing.
  for src,tgt in cases.items():
   tgt=re.sub(r'_([A-Za-z0-9])',r'_{\1}',tgt)
   with self.subTest(source=src):self.same(src,tgt)
 def test_contextual_aliases(self):
  self.assertEqual(convert_expr('D0',appendix='d'),r'D_{0}')
  self.assertEqual(convert_expr('D0',appendix='h'),r'\mathrm{D0}')
  self.assertEqual(convert_expr('H1'),r'H1')
 def test_no_unconverted_math_unicode(self):
  p=Path(__file__).parent/'display_only/display_mapping.json'
  j=json.loads(p.read_text())
  self.assertEqual(j['total'],366)
  self.assertEqual(j['counts'],{'a':36,'b':38,'c':45,'d':33,'e':37,'f':11,'g':32,'h':26,'i':78,'j':30})
  for b in j['blocks']:
   with self.subTest(block=b['id']):
    self.assertNotRegex(b['latex'],r'[∫∂Σ≤≥≠−⊗²³]')
    self.assertNotIn(r'^{-^{*}}',b['latex'])
    self.assertNotIn('SPACEMARK',b['latex'])
    self.assertNotIn('HATBETA',b['latex'])
    source_tags=[m[1] for l in b['source'].splitlines() if (m:=TAG_RE.search(l))]
    self.assertEqual(b['tags'],source_tags)

if __name__=='__main__':unittest.main()
