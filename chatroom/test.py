def cal(R,G,B):
    print('start!')
    maxval = max(R,G,B)
    minval = min(R,G,B)
    print('max = ',maxval)
    print( 'min = ',minval)
    if maxval==minval:
        H = 0
        print( 'no')
    else: 
        if R==maxval:
          H = (G-B)/float(maxval-minval)
        elif G==maxval:
          H=2.0+(B-R)//float(maxval-minval)
        elif B==maxval:
          H=4.0+(R-G)//float(maxval-minval)
        H = H*60.0
    return H

def cal2(R,G,B):
  maxval = max(R,G,B)
  minval = min(R,G,B)
  if maxval == minval:
    H=0
  else:
    if G>=B:
      H=(maxval-R+G-minval+B-minval)/float(maxval-minval)*60
    else:
      H=360-(maxval-R+G-minval+B-minval)/float(maxval-minval)*60
  return H
