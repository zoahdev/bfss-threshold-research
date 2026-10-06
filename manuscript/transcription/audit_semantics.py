"""Independent flat mathematical token-order audit, plus risk inventories.
This is not a proof of the source derivations. Grouping/scope requires review.
"""
from pathlib import Path
import json,re,collections
D=Path(__file__).parent
GREEK=dict(zip('αβγδεζηθικλμνξπρστφχψωΓΔΘΛΞΠΣΦΨΩ',['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa','lambda','mu','nu','xi','pi','rho','sigma','tau','phi','chi','psi','omega','Gamma','Delta','Theta','Lambda','Xi','Pi','Sigma','Phi','Psi','Omega']))
def flat(s,tex=False):
 if tex:
  s=re.sub(r'\\tag\{[^{}]*\}','',s)
  s=re.sub(r'\\(?:begin|end)\{(?:gather\*?|aligned|bmatrix)\}(?:\[t\])?','',s)
  s=s.replace(r'\widehat{\beta}', 'HATBETA')
  s=s.replace(r'\#', '#')
  s=s.replace(r'\textbackslash{}','')
  for name in ['operatorname','mathrm','text']:
   s=s.replace('\\'+name,'')
  for x,y in {'notag':'','quad':'','langle':'<','rangle':'>','Vert':'||','vert':'|','le':'<=','ge':'>=','ne':'!=','ll':'<<','gg':'>>','to':'->','ldots':'...','int':'integral','otimes':'tensor','times':'x','cdot':'dot','bigoplus':'direct_sum','oplus':'direct_sum','infty':'infinity','perp':'perpendicular','prod':'product','pm':'+-'}.items():
   s=re.sub(r'\\'+x+r'(?![A-Za-z])',lambda m:y,s)
  s=re.sub(r'\\([A-Za-z]+)',r'\1',s)
  s=s.replace(r'\{','{').replace(r'\}','}').replace('\\\\','').replace('&','')
 else:
  s=re.sub(r'\s+\((\d+(?:\.\d+)*)\)\s*[,.;]?\s*$','',s,flags=re.M)
  s=s.replace('−','-').replace('≤','<=').replace('≥','>=').replace('≠','!=').replace('⊗','tensor').replace('·','dot').replace('∫','integral').replace('∂','partial').replace('±','+-')
  s=re.sub(r'[⁰¹²³⁴⁵⁶⁷⁸⁹]+',lambda m:'^('+m[0].translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹','0123456789'))+')',s)
  for x,y in GREEK.items():s=s.replace(x,y)
  s=s.replace('Sigma_','sum_').replace('betahat','beta_hat')
  s=re.sub(r'beta_hat(?:,|_)?','HATBETA',s)
  s=s.replace('sqrt J','sqrt(J)')
  s=re.sub(r'binom\(([^,()]+),([^,()]+)\)',r'binom(\1)(\2)',s)
 s=s.replace('grad','nabla')
 # The source binomial's argument comma is structural and has no TeX token.
 s=re.sub(r'binom\(?1/2[,}]j', 'binom1/2j',s)
 s=re.sub(r'[\s{}()\[\]_^\\]','',s)
 return s
j=json.loads((D/'display_only/display_mapping.json').read_text())
issues=[]
for b in j['blocks']:
 a,c=flat(b['source']),flat(b['latex'],True)
 if a!=c:issues.append({'id':b['id'],'source_flat':a,'tex_flat':c})
print('FLAT TOKEN MISMATCHES',len(issues))
for x in issues:print(x)
(D/'semantic_flat_audit.json').write_text(json.dumps({'scope':'All 366 display blocks, independent flat mathematical-token order check; excludes proof correctness and grouping scope. Mismatches are reviewed manually.','display_count':366,'mismatches':issues},indent=2))

def groups(s,tex=False):
 """Inventory retained explicit parentheses and square/anticommutator brackets.
 Source script grouping and sqrt/binomial argument markers are structural.
 """
 s=re.sub(r'\s+\((\d+(?:\.\d+)*)\)\s*[,.;]?\s*$','',s,flags=re.M) if not tex else re.sub(r'\\tag\{[^{}]*\}','',s)
 out=[];stack=[]
 for i,ch in enumerate(s):
  if ch in '([' or (ch=='{' and (not tex or (i and s[i-1]=='\\'))):
   if tex and ch=='[' and s[max(0,i-14):i].endswith(r'\begin{aligned}'):
    continue
   stack.append((ch,i))
  elif ch in ')]' or (ch=='}' and (not tex or (i and s[i-1]=='\\'))):
   if not stack:continue
   op,st=stack[-1]
   if {'(':')','[':']','{':'}'}[op]!=ch:continue
   stack.pop();inner=s[st+1:i];prefix=s[:st].rstrip()
   if not tex:
    if prefix.endswith(('_','^')) and not (prefix.endswith('^') and inner in ['a','b','c']):continue
    if re.search(r'(sqrt|binom)$',prefix):continue
   out.append((st,op,flat(inner,tex)))
 return [(op,content) for st,op,content in sorted(out)]
group_issues=[]
for b in j['blocks']:
 if b['id']=='a.15':continue # explicit ASCII 2x2 matrix reviewed separately
 a,c=groups(b['source']),groups(b['latex'],True)
 if a!=c:group_issues.append({'id':b['id'],'source_groups':a,'tex_groups':c})
print('EXPLICIT GROUP MISMATCHES',len(group_issues))
for x in group_issues:print(x)
(D/'semantic_group_audit.json').write_text(json.dumps({'scope':'All explicit source grouping parentheses, square brackets and anticommutator braces; source script/sqrt/binomial structural delimiters excluded; 2x2 matrix a.15 manually reviewed.','display_count':366,'mismatches':group_issues},indent=2))
