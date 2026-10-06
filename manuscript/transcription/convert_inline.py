"""Conservative Pandoc inline formula recognition; original expressions recorded."""
import re
from collections import Counter
GREEK = set('alpha beta gamma delta epsilon zeta eta theta iota kappa lambda mu nu xi pi rho sigma tau upsilon phi chi psi omega ell Gamma Delta Theta Lambda Xi Pi Sigma Upsilon Phi Psi Omega'.split())
OPS=set('sum integral sqrt Tr tr Re Im det diag ker Hom min max exp sin cos sign tensor direct_sum grad nabla partial ad binom inf sup product range'.split())
WORDS=set('in outside incident to for and or if where with when every each all at on from the of off block tuple space real part'.split())
SPECIAL = re.compile(r'[_^=<>|+*−±≥≤Γδκ→∂⊗²³∞∑∫α-ωΑ-Ω]')
LITERAL = re.compile(r'(?:\.(?:py|json|md|tex|sh|pdf)$|https?://|[a-z]{3,}_[a-z]{3,}_[a-z]{3,})')
trace=[]

def strval(x):
 t=x.get('t')
 if t=='Str': return x['c']
 if t in ('Space','SoftBreak','LineBreak'):return ' '
 return None

def ismath(s,strict=False):
 s=s.strip('.,;:!?')
 if not s or LITERAL.search(s):return False
 if s in ('(h,xi)','1/sigma','N,kappa,L','(N,kappa,L)'):return True
 if s.strip('()') in ('phi2','rho0','D0','D1','D2','J2','W2','V3','V4','s0','sigma0','chi0','Usigma','E0,total','ZD0','CW2'):return True
 if re.match(r'^[-(]?(?:infinity|pi)(?:[^A-Za-z]|$)',s):return True
 if SPECIAL.search(s):return True
 if re.match(r'(?:O|sqrt|exp|min|max|sin|cos|Hom|Tr|Re|Im|det|diag|ker|binom|sign)\(',s):return True
 if re.fullmatch(r'\([A-Za-z](?:,[A-Za-z])+\)',s):return True
 if re.search(r'\d/\d',s):return True
 if s in GREEK:return True
 if s in OPS:return not strict
 if not strict and re.fullmatch(r'[B-HJ-Zb-hj-z]',s):return True
 if not strict and re.fullmatch(r'[0-9]+(?:\.[0-9]+)?',s):return True
 return False

def imbalance(s):
 # Parentheses and brackets can contain prose support conditions.
 n=0
 for c in s:
  if c in '([{': n+=1
  if c in ')]}': n-=1
 return n

def unclosed_bar(pieces):
 s=''.join(pieces)
 return s.count('||')%2 or s.replace('||','').count('|')%2

def split_affixes(s):
 # Preserve grammatical sentence punctuation outside math.
 prefix=''; suffix=''
 if s.startswith('vanishing-at-'):prefix='vanishing-at-';s=s[len(prefix):]
 while s and s[-1] in '.,;:!?':suffix=s[-1]+suffix;s=s[:-1]
 # apostrophe possession outside the expression.
 if s.endswith("'s"):s=s[:-2];suffix="'s"+suffix
 # Words joined to a mathematical label are prose.
 m=re.match(r'^(.*?)(-(?:or-smaller|dual|bound|term|estimate|norm|coefficient|payment))$',s)
 if m:s=m.group(1);suffix=m.group(2)+suffix
 while s.startswith('(') and imbalance(s)<0:
  prefix+='(';s=s[1:]
 while s.endswith(')') and imbalance(s)<0:
  suffix=')'+suffix;s=s[:-1]
 return prefix,s,suffix

def convert_inlines(items, convert_expr, appendix):
 # Work only Str/Space runs. Inline Code is math in these technical sources.
 out=[];i=0
 while i<len(items):
  x=items[i];t=x['t']
  if t=='Code':
   s=x['c'][1]
   if not LITERAL.search(s):
    tex=convert_expr(s)
    out.append({'t':'Math','c':[{'t':'InlineMath'},tex]});trace.append({'appendix':appendix,'source':s,'tex':tex,'kind':'code'})
   else:out.append(x)
   i+=1;continue
  if t=='Str' and ismath(x['c']) and x['c'].strip('.,;:!?') != 'product' and (x['c'].strip('.,;:!?') not in OPS or (i+2<len(items) and items[i+1]['t'] in ('Space','SoftBreak') and strval(items[i+2]) is not None and ismath(strval(items[i+2]),strict=True))):
   # Most math is one token; extend through math tokens and explicit grouped annotations.
   j=i;pieces=[];depth=0;last=i
   while j<len(items):
    v=strval(items[j])
    if v is None:break
    if v==' ':
     # Retain whitespace only if the next token remains mathematical.
     if j+1>=len(items):break
     nv=strval(items[j+1])
     if nv is None:break
     if depth<=0 and not unclosed_bar(pieces) and nv.strip('.,;:!?')=='product':break
     if depth<=0 and not unclosed_bar(pieces) and not ismath(nv) and nv not in ('A','I','i','dot'):break
     pieces.append(' ');j+=1;continue
    if j>i and depth<=0 and not unclosed_bar(pieces) and v.strip('.,;:!?')=='product':break
    if j>i and depth<=0 and not unclosed_bar(pieces) and not ismath(v) and v not in ('A','I','i','dot'):break
    pieces.append(v);depth+=imbalance(v);last=j
    j+=1
    # Sentence punctuation ends a formula expression.
    if depth<=0 and not unclosed_bar(pieces) and re.search(r'[.;:]$',v):break
   raw=''.join(pieces).strip()
   prefix,s,suffix=split_affixes(raw)
   # Do not consume unmatched groups: single-token conversion can safely preserve delimiters.
   if imbalance(s) or unclosed_bar([s]):raise ValueError('Unbalanced inline expression: '+repr(s))
   tex=convert_expr(s)
   if prefix:out.append({'t':'Str','c':prefix})
   out.append({'t':'Math','c':[{'t':'InlineMath'},tex]})
   if suffix:out.append({'t':'Str','c':suffix})
   trace.append({'appendix':appendix,'source':s,'tex':tex,'kind':'plain'})
   i=j;continue
  if t in ('Emph','Strong','Strikeout','Underline','SmallCaps','Superscript','Subscript'):
   x={'t':t,'c':convert_inlines(x['c'],convert_expr,appendix)}
  elif t=='Link':
   x=dict(x);x['c']=[x['c'][0],convert_inlines(x['c'][1],convert_expr,appendix),x['c'][2]]
  out.append(x);i+=1
 return out

def walk_blocks(blocks,convert_expr,display_blocks,appendix):
 out=[]
 for x in blocks:
  t=x['t'];c=x.get('c')
  if t in ('Para','Plain'):
   x={'t':t,'c':convert_inlines(c,convert_expr,appendix)}
  elif t=='CodeBlock':
   block=next(display_blocks)
   x={'t':'RawBlock','c':['latex',block]}
  elif t=='Header':
   # Preserve source headings including historical local numbers.
   c[1][0]=appendix+'-'+c[1][0]
   c[2]=[part for node in c[2] for part in (convert_inlines([node],convert_expr,appendix) if node.get('t')=='Str' and re.search(r'[_^]',node.get('c','')) else [node])]
   x={'t':t,'c':c}
  elif t=='BulletList':
   x={'t':t,'c':[walk_blocks(b,convert_expr,display_blocks,appendix) for b in c]}
  elif t=='OrderedList':
   x={'t':t,'c':[c[0],[walk_blocks(b,convert_expr,display_blocks,appendix) for b in c[1]]]}
  elif t=='BlockQuote':
   x={'t':t,'c':walk_blocks(c,convert_expr,display_blocks,appendix)}
  out.append(x)
 return out
