
def maskfiltering(img2d,mask):
    buff2d=img2d.copy()
    #global row, col
    row,col=img2d.shape
    ms=int(len(mask)/2) # mask is square with odd dimension.
    
    for i in range(ms,row-ms):
        for j in range(ms,col-ms):
            sum=0.0
            for p in range(-ms,ms+1):
                for q in range(-ms,ms+1):
                    sum+=buff2d[i+p][j+q]*mask[p+ms][q+ms]
            img2d[i][j]=intlimit(sum)


def maskfiltering2(img2d,maskx,masky):
    buff2d=img2d.copy()
    #global row, col
    row,col=img2d.shape
    ms=int(len(maskx)/2) # maskx and masky must be square with odd dimension.
    
    for i in range(ms,row-ms):
        for j in range(ms,col-ms):
            sumx=sumy=0.0
            for p in range(-ms,ms+1):
                for q in range(-ms,ms+1):
                    sumx+=buff2d[i+p][j+q]*maskx[p+ms][q+ms]
                    sumy+=buff2d[i+p][j+q]*masky[p+ms][q+ms]
            img2d[i][j]=intlimit(abs(sumx)+abs(sumy))


#################### main procedure ###############333

# some lines required

smaskx=[[-1,0,1],[-2,0,2],[-1,0,1]]
smasky=[[-1,-2,-1],[0,0,0],[1,2,1]]
lmask=[[0,1,0],[1,-4,1],[0,1,0]]

maskfiltering(gimg2d,lmask)

maskfiltering2(gimg2d,smaskx,smasky)

# some lines required