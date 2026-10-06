"""Faithful typesetting of the BFSS notes' compact source math.

Public interface: convert_expr(str) -> LaTeX str. The converter changes notation,
not algebra. ORIGINAL source is retained by build_displays() in JSON and comments.
"""
from __future__ import annotations
import re, json
from pathlib import Path

GREEK='alpha beta gamma delta epsilon varepsilon zeta eta theta vartheta iota kappa lambda mu nu xi pi rho sigma tau upsilon phi varphi chi psi omega Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega'.split()
UNICODE_GREEK=dict(zip('αβγδεζηθικλμνξπρστφχψωΓΔΘΛΞΠΣΦΨΩ', ['alpha','beta','gamma','delta','epsilon','zeta','eta','theta','iota','kappa','lambda','mu','nu','xi','pi','rho','sigma','tau','phi','chi','psi','omega','Gamma','Delta','Theta','Lambda','Xi','Pi','Sigma','Phi','Psi','Omega']))
FUNCTIONS={'Tr':r'\operatorname{Tr}','tr':r'\operatorname{tr}','diag':r'\operatorname{diag}','Hess':r'\operatorname{Hess}','sign':r'\operatorname{sign}','dist':r'\operatorname{dist}','div':r'\operatorname{div}','component':r'\operatorname{component}','average':r'\operatorname{average}','Hom':r'\operatorname{Hom}','range':r'\operatorname{range}','eigenvalues':r'\operatorname{eigenvalues}','ad':r'\operatorname{ad}',**{x:'\\'+x for x in ['det','ker','min','max','inf','sup','log','exp','cos','sin']},'Re':r'\operatorname{Re}','Im':r'\operatorname{Im}'}
SPECIAL={'sum':r'\sum','product':r'\prod','integral':r'\int','partial':r'\partial','nabla':r'\nabla','grad':r'\nabla','tensor':r'\otimes','times':r'\times','pm':r'\pm','dot':r'\cdot','infinity':r'\infty','ell':r'\ell','direct_sum':r'\oplus','in':r'\in','perpendicular':r'\perp'}
LABELS=set('BFSS exc fast slow cent centers center raw full scale total min color derivative active comm Berry kin der orb mix diag op sym density Yukawa'.split())
INDEXES=set('ab ij jk i9 ki Aj Aa F2 H2 1i'.split())|LABELS|set(GREEK)|{'infinity'}
# These attached spellings are unambiguously products in the supplied formulas.
COMPACT = {
 'P_NB_A':'P_N B_A','P_NB_Y':'P_N B_Y','P_IB_Y':'P_I B_Y','P_CB_Y':'P_C B_Y',
 'Y_ep_e':'Y_e p_e','Y_fp_e':'Y_f p_e','Y_fY_gv':'Y_f Y_g v','Y_eY_fY_g':'Y_e Y_f Y_g','Y_fY_g':'Y_f Y_g',
 'r_fr_g':'r_f r_g','r_er_f':'r_e r_f','C_YF':'C_Y F',
 'p_Fv':'p_F v','p_ev':'p_e v','p_gv':'p_g v','Y_ev':'Y_e v','F_jkv':'F_jk v',
 'p_sUf':'p_s U f','p_su':'p_s u','p_sv':'p_s v','beta_jv':'beta_j v','beta_jU':'beta_j U','beta_kv':'beta_k v',
 'c_aU':'c_a U','d_0u':'d_0 u','X_1u':'X_1 u','X_2u':'X_2 u','B_1d_0':'B_1 d_0',
 'n_an_b':'n_a n_b','Q_fv':'Q_f v','Q_eu':'Q_e u','w_at_a':'w_a t_a','P_jv':'P_j v','a_ev':'a_e v','beta_s,av':'beta_(s,a) v',
}

TEXT_PHRASES=[
 'in the off-block tuple space','for every incident pair','for every pair',
 'for every','are pair-block diagonal','with the input-root denominator',
 'is a triangle','higher homogeneous orders','a finite Clifford contraction of',
 'terms of Y-degree','proper union of','pi-blocks','density of','incident',
 'outside','constant','diagonal','mixed','triangle','real','when','with','and',
]

def _escape_text(s):
 return s.replace('\\',r'\textbackslash{}').replace('{',r'\{').replace('}',r'\}').replace('_',r'\_').replace('#',r'\#').replace('%',r'\%').replace('&',r'\&')

def normalize(s):
 # Source-reviewed named aliases: only typography changes, definitions unchanged.
 for a,b in {'D1':'D_1','D2':'D_2','sigma0':'sigma_0','chi0':'chi_0','Usigma':'U_sigma','phi2':'phi_2','rho0':'rho_0','J2':'J_2','W2':'W_2','V3':'V_3','V4':'V_4','s0':'s_0','E0,total':'E_0,total','σ0':'σ_0','χ0':'χ_0','Uσ':'U_σ'}.items():
  s=s.replace(a,b)
 s=re.sub(r' {2,}', ' SPACEMARK ', s)
 if 'S(U(' in s:
  s=s.replace(')x', ') times ').replace('...x','... times ')
 s=re.sub(r'\bsqrt\s+(J)(?![A-Za-z0-9_])',r'sqrt(\1)',s)
 s=s.replace('±',' pm ').replace('∫',' integral ').replace('∂',' partial ').replace('−','-').replace('≤','<=').replace('≥','>=').replace('≠','!=').replace('→','->').replace('⊗',' tensor ').replace('·',' dot ')
 s=re.sub(r'[⁰¹²³⁴⁵⁶⁷⁸⁹]+',lambda m:'^('+m[0].translate(str.maketrans('⁰¹²³⁴⁵⁶⁷⁸⁹','0123456789'))+')',s)
 s=re.sub(r'\^\(([abc])\)',r'^{(\1)}',s)
 for char,name in UNICODE_GREEK.items(): s=s.replace(char, ' '+name+' ')
 # Whitespace introduced around Unicode Greek must not sever its suffix.
 s=re.sub(r'\b('+'|'.join(GREEK)+r')\s+([_^])',r'\1\2',s)
 s=re.sub(r'([_^])\s+('+ '|'.join(GREEK)+r')\b',r'\1\2',s)
 s=re.sub(r'\bSigma(?=_)','sum',s) # source Σ denotes a sum in Appendix H
 s=s.replace('beta hat','beta_hat').replace('betahat','beta_hat')
 for a,b in sorted(COMPACT.items(),key=lambda ab:-len(ab[0])):s=s.replace(a,b)
 s=re.sub(r'\bbeta_hat(?:,|_)([jk])([vU]?)',lambda m:'HATBETA_'+m[1]+(' '+m[2] if m[2] else ''),s)
 s=s.replace('beta_hat','HATBETA')
 multi_labels=['E_0,ab','E_0,total','E_0,e','H_fast,e','H_B,e','H_F,e','E_B,e','E_F,min,e','W_2,t','W_2,g','h_B,e','U_B,e','R_fast,H2','V_d,2','R_orb,I','R_orb,diag','I_Y,a','c_1,a','beta_s,a']
 for label in sorted(multi_labels,key=len,reverse=True):
  base,sub=label.split('_',1)
  s=re.sub(r'(?<![A-Za-z])'+re.escape(label)+r'(?![A-Za-z0-9])',lambda m:base+'_('+sub+')',s)
 # Source suffix F/op on a norm is a norm label, never a product.
 norm_count=0
 def norm_label(m):
  nonlocal norm_count
  norm_count+=1
  return '||'+(('_' if norm_count%2==0 else '')+(m[1] or '') if m[1] else '')
 s=re.sub(r'\|\|(F|op)?',norm_label,s)
 return re.sub(r'\s+', ' ', s).strip()

class Parser:
 def __init__(self,s,prepared=False):
  self.s=s if prepared else normalize(s); self.i=0
 def group(self,op='(',cl=')'):
  assert self.s[self.i]==op
  start=self.i+1; depth=1; self.i+=1
  while self.i<len(self.s):
   c=self.s[self.i]
   if c==op:depth+=1
   elif c==cl:
    depth-=1
    if depth==0:
     ans=self.s[start:self.i];self.i+=1;return ans
   self.i+=1
  return self.s[start:]
 def script(self,kind):
  s=self.s
  while self.i<len(s) and s[self.i].isspace():self.i+=1
  if self.i>=len(s):return ''
  if s[self.i] in '({':
   ch=s[self.i];raw=self.group(ch,')' if ch=='(' else '}')
   if kind=='^' and raw in ('-*','*'):return raw
   rendered=Parser(raw,True).run()
   if kind=='_' and raw=='F,min,e':rendered=rendered.replace(r'\min ',r'\mathrm{min}')
   if kind=='_' and raw=='orb,diag':rendered=rendered.replace(r'\operatorname{diag}',r'\mathrm{diag}')
   return rendered
  if s[self.i]=='*':self.i+=1;return '*'
  if kind=='^':
   m=re.match(r'-?(?:1/2|\d+|\*)',s[self.i:])
   if m:self.i+=len(m[0]);return m[0]
   if s[self.i]=='-':self.i+=1;return '-'+self.script(kind)
   m=re.match(r'[A-Za-z]+',s[self.i:])
   if m:
    raw=m[0]; tok=next((w for w in sorted(set(GREEK)|LABELS|{'infinity'},key=len,reverse=True) if raw.startswith(w)),raw[0])
    self.i+=len(tok);return Parser(tok,True).run()
   c=s[self.i];self.i+=1;return c
  # A subscript may have explicit comma-separated descriptor/index pieces.
  pieces=[]
  while True:
   if self.i>=len(s):break
   m=re.match(r'[A-Za-z0-9]+',s[self.i:])
   if not m:
    if not pieces:pieces.append(self.s[self.i]);self.i+=1
    break
   raw=m[0]
   if s.startswith('fast-density',self.i):
    self.i+=12;pieces.append(r'\mathrm{fast\text{-}density}');break
   candidates=sorted(INDEXES,key=len,reverse=True)
   # A lowercase multi-index such as ab or jk stays intact. Unknown lowercase
   # runs are kept visibly literal and reported by audit, not guessed.
   tok=next((w for w in candidates if raw.startswith(w)),None)
   if tok is None:
    tok=(re.match(r'[a-z]+',raw)[0] if raw[0].islower() else (re.match(r'\d+',raw)[0] if raw[0].isdigit() else raw[0]))
   self.i+=len(tok)
   pieces.append(('\\mathrm{'+tok+'}') if tok in LABELS else Parser(tok,True).run())
   break
  return ''.join(pieces)
 def run(self):
  out=[];s=self.s
  while self.i<len(s):
   c=s[self.i]
   if c.isspace():
    j=self.i
    while self.i<len(s) and s[self.i].isspace():self.i+=1
    out.append(r'\quad ' if self.i-j>=2 else ' ');continue
   phrase=next((w for w in TEXT_PHRASES if s.startswith(w,self.i) and (self.i==0 or not s[self.i-1].isalpha()) and (self.i+len(w)==len(s) or not s[self.i+len(w)].isalpha())),None)
   if phrase=='pi-blocks':
    self.i+=len(phrase);out.append(r'\pi\text{-blocks}');continue
   if phrase:
    self.i+=len(phrase);out.append(r'\text{ '+_escape_text(phrase)+' }');continue
   if s.startswith('fast-density',self.i):self.i+=12;out.append(r'\mathrm{fast\text{-}density}');continue
   if s.startswith('D0',self.i):self.i+=2;out.append(r'\mathrm{D0}');continue
   if s.startswith('SPACEMARK',self.i):self.i+=9;out.append(r'\quad ');continue
   if s.startswith('HATBETA',self.i):self.i+=7;out.append(r'\widehat{\beta}');continue
   if c in '_^':
    self.i+=1;script=self.script(c);out.append(c+'{'+script+'}');continue
   if s.startswith('||',self.i):self.i+=2;out.append(r'\Vert ');continue
   if c=='|':self.i+=1;out.append(r'\vert ');continue
   matched=False
   for a,b in [('!=',r'\ne '),('<=',r'\le '),('>=',r'\ge '),('->',r'\to '),('...',r'\ldots '),('<<',r'\ll '),('>>',r'\gg ')]:
    if s.startswith(a,self.i):self.i+=len(a);out.append(b);matched=True;break
   if matched:continue
   if c=='<':
    end=s.find('>',self.i+1)
    if end>=0 and (not re.match(r'\s*[A-Za-z0-9]',s[end+1:]) or re.match(r'\s*(?:SPACEMARK\b|and\b)',s[end+1:])) and (',' in s[self.i+1:end] or s[end+1:end+3]=='_U') and not any(x in s[self.i+1:end] for x in ['<=','>=','<']):
     inner=s[self.i+1:end];out.append(r'\langle '+Parser(inner,True).run()+r'\rangle ');self.i=end+1;continue
   if c=='*':
    # A bare postfix star is an adjoint in these technical notes.
    out.append('^{*}');self.i+=1;continue
   if c=='#':
    m=re.match(r'#([A-Za-z]+)',s[self.i:])
    if m:out.append(r'\#\text{'+m[1]+'}');self.i+=len(m[0]);continue
   if c=='{':out.append(r'\{');self.i+=1;continue
   if c=='}':out.append(r'\}');self.i+=1;continue
   if c=='&':out.append(r'\&');self.i+=1;continue
   if c=='%':out.append(r'\%');self.i+=1;continue
   if c.isalpha():
    # Longest known name first; remaining adjacent letters are products.
    known=sorted(set(GREEK)|set(FUNCTIONS)|set(SPECIAL)|LABELS|{'sqrt','binom'},key=len,reverse=True)
    word=next((w for w in known if s.startswith(w,self.i) and (self.i+len(w)==len(s) or not s[self.i+len(w)].islower())),None)
    if word:
     self.i+=len(word)
     if word in ('sqrt','binom'):
      saved=self.i
      while self.i<len(s) and s[self.i].isspace():self.i+=1
      if self.i<len(s) and s[self.i]=='(':
       inside=self.group()
       if word=='sqrt':out.append(r'\sqrt{'+Parser(inside,True).run()+'}')
       else:
        parts=split_top(inside,',')
        if len(parts)==2:out.append(r'\binom{'+Parser(parts[0],True).run()+'}{'+Parser(parts[1],True).run()+'}')
        else:out.append(r'\operatorname{binom}('+Parser(inside,True).run()+')')
       continue
      self.i=saved;out.append('\\operatorname{'+word+'}');continue
     if word in GREEK:out.append('\\'+word+' ')
     elif word in FUNCTIONS:out.append(FUNCTIONS[word]+' ')
     elif word in SPECIAL:
      val=SPECIAL[word]
      if word=='direct_sum' and self.i<len(s) and s[self.i]=='_':val=r'\bigoplus'
      out.append(val+' ')
     else:out.append(r'\mathrm{'+word+'}')
     continue
    out.append(c);self.i+=1;continue
   out.append(c);self.i+=1
  return ''.join(out).strip()

def split_top(s,sep=','):
 parts=[];last=0;depth=0
 for i,c in enumerate(s):
  if c in '({[':depth+=1
  elif c in ')}]':depth-=1
  elif c==sep and depth==0:parts.append(s[last:i]);last=i+1
 parts.append(s[last:]);return parts

def convert_expr(s:str, appendix:str|None=None)->str:
 """Convert a source expression to TeX math without adding delimiters."""
 if appendix=='d':s=s.replace('D0','D_0')
 result=Parser(s).run()
 result=result.replace(r'-\text{ density of } ',r'\text{-density of }')
 result=re.sub(r"([A-Za-z])'(_\{[^{}]*\})?\^\{([^{}]*)\}",lambda m: '{'+m[1]+"'"+(m[2] or '')+'}^{'+m[3]+'}',result)
 return result

BLOCK_RE=re.compile(r'\\begin\{verbatim\}\n(.*?)\\end\{verbatim\}',re.S)
TAG_RE=re.compile(r'\s+\((\d+(?:\.\d+)*)\)\s*[,.;]?\s*$')

def convert_display(source,block_id=''):
 original=source
 # The sole source ASCII block matrix has a faithful explicit matrix rendering.
 if block_id=='a.15':
  latex=r'\[T=\begin{bmatrix}I_H&O_H\\K&E^{*}O\end{bmatrix}.\]'
  return {'id':block_id,'source':original,'latex':latex,'tags':[],'flags':[],'rows':[]}
 groups=[];rows=[];tags=[];flags=[]
 for line in source.strip().splitlines():
  if not line.strip():
   if rows:groups.append((rows,None));rows=[]
   continue
  tag=None;m=TAG_RE.search(line)
  if m:tag=m[1];tags.append(tag);line=line[:m.start()]
  if line.strip():rows.append(convert_expr(line.strip(), appendix=block_id.split('.')[0]))
  if tag:groups.append((rows,tag));rows=[]
 if rows:groups.append((rows,None))
 if 'D0' in source:flags.append({'kind':'distinct_named_symbol','source':'D0','action':r'preserved as upright \mathrm{D0}; Appendix H defines it with the opposite sign from Appendix D D_0, so the symbols are not identified'})
 if 'density of f' in source:flags.append({'kind':'verbal_density','source':'[H_a-density of f]','action':'retained literal source annotation; not replaced by an invented density'})
 if 'average_alpha' in source:flags.append({'kind':'average_operator','source':'average_alpha','action':'operator name retained; no normalization inferred'})
 if 'a finite Clifford contraction' in source:flags.append({'kind':'verbal_term','source':'a finite Clifford contraction of F_A','action':'retained in text within math'})
 if block_id=='j.5':flags.append({'kind':'verbal_product_range','source':'B proper union of >=2 pi-blocks','action':'verbal range retained without set-theoretic reinterpretation'})
 if block_id=='i.71':flags.append({'kind':'block_vector_separator','source':'[C_Y F^(-1)+K^* ; I_Y F^(-1)]','action':'semicolon retained, no matrix orientation inferred'})
 rendered=[]
 for rs,tag in groups:
  env='\\begin{aligned}\n'+' \\\\\n'.join('& '+r for r in rs)+'\n\\end{aligned}'
  if tag:env+='\\tag{'+tag+'}'
  else:env+=r'\notag'
  rendered.append(env)
 # gather supports each original local tag; align blocks retain deliberate lines.
 latex='\\begin{gather*}\n'+' \\\\\n'.join(rendered)+'\n\\end{gather*}'
 return {'id':block_id,'source':original,'latex':latex,'tags':tags,'flags':flags,'notation_changes':[a for a in ['J2','W2','V3','V4','s0','phi2','rho0','E0,total','σ0','χ0','Uσ'] if a in original],'rows':[r for rs,t in groups for r in rs]}

def build_displays(src:Path,dst:Path):
 dst.mkdir(parents=True,exist_ok=True);allblocks=[];counts={}
 for letter in 'abcdefghij':
  text=(src/(letter+'.tex')).read_text();n=0
  def repl(m):
   nonlocal n
   n+=1;b=convert_display(m[1],f'{letter}.{n}');allblocks.append(b)
   comments='\n'.join('% ORIGINAL '+line for line in m[1].strip().splitlines())
   return '% DISPLAY '+b['id']+'\n'+comments+'\n'+b['latex']
  text=BLOCK_RE.sub(repl,text);(dst/(letter+'.tex')).write_text(text);counts[letter]=n
 (dst/'display_mapping.json').write_text(json.dumps({'counts':counts,'total':len(allblocks),'blocks':allblocks},indent=2,ensure_ascii=False))
 return allblocks

if __name__=='__main__':
 import argparse
 p=argparse.ArgumentParser();p.add_argument('--src',default='output/bfss_review_v2_recovered_20261005/appendices');p.add_argument('--dst',default='tmp/bfss_formula_conversion/display_only');a=p.parse_args()
 bs=build_displays(Path(a.src),Path(a.dst));print('Converted',len(bs),'blocks; flagged',sum(bool(b['flags']) for b in bs))
