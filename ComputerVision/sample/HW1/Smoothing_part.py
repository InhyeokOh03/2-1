
def maskfiltering(img2d,mask):
    buff2d=img2d.copy()
    row,col=img2d.shape
    ms=int(len(mask)/2) # mask must be square with odd dimension.
    
    for i in range(ms,row-ms):
        for j in range(ms,col-ms):
            sum=0.0
            for p in range(-ms,ms+1):
                for q in range(-ms,ms+1):
                    sum+=buff2d[i+p][j+q]*mask[p+ms][q+ms]
            img2d[i][j]=intlimit(sum)

def medianfiltering(img2d,ms):
    buff2d=img2d.copy()
    row,col=img2d.shape
    hs=int(ms/2) # mask must be square with odd dimension.
    
    for i in range(hs,row-hs):
        for j in range(hs,col-hs):
            temp = []
            for p in range(-hs,hs+1):
                for q in range(-hs,hs+1):
                    temp.append(buff2d[i+p][j+q])
            temp.sort()
            img2d[i][j]=temp[int(ms*ms/2)]

#################### main procedure ###############333

# some lines required

std = 2.0
hs=int(msize/2) # msize must be odd number
for i in range(-hs,hs+1):
    for j in range(-hs,hs+1):
        mask[i+hs][j+hs] = (1.5/hs)*(1.0/(2*3.1416*std))*np.exp(-1.0*(i*i+j*j)/(2*std*std))

#(1.5/hs) is an arbitaray constant for better visualizaiotion.


maskfiltering(gimg2d,mask)

medianfiltering(gimg2d,msize)

# some lines required