#mirroring

def mirrorfun(inp,k):
    ori = 'abcdefghijklmnopqrstuvwxyz'
    rev = 'zyxwvutsrqponmlkjihgfedcba'
    dictChars = dict(zip(ori,rev))
    pr = inp[0:k-1]
    suf = inp[k-1:]
    mirror = ''
 
    for i in range(0,len(suf)):
        mirror = mirror + dictChars[suf[i]]
  
    print (pr+mirror)


inp = 'prachi'
k = 2
mirrorfun(inp,k)