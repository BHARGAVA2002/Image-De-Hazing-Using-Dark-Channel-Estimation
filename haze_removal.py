import numpy as np
import skimage.io as io
from gf import guided_filter
import interface

def dark_channel(img,window_size):
    print("Dark channel estimation started...")
    rows,cols,_=img.shape
    tmp=img.min(axis=2)
    dark=np.zeros((rows,cols),dtype=np.double)
    for i in range(rows):
        for j in range(cols):
            patch=tmp[i:i+window_size,j:j+window_size]
            dark[i,j]=np.min(patch)
    io.imsave("Results/dark.jpg",dark)
    return dark


def atmosphere_light(img):
    dark=dark_channel(img,7)
    print("Airlight estimation started...")
    rows,cols,_=img.shape
    airlight=np.zeros((3),dtype=np.double)
    flat=dark.flatten()
    flat.sort()
    num=int(rows*cols*0.001)
    threshold=flat[-num]
    tmp=img[dark>=threshold]
    tmp.sort(axis=0)
    airlight=tmp[-num:,:].mean(axis=0)
    print(airlight)
    return airlight


def transmission_map(img,window_size=7,omega=0.95):
    airlight=atmosphere_light(img)
    print("Transmission map estimation started...")
    rows,cols,_=img.shape
    tran=np.zeros((rows,cols),dtype=np.double)
    for i in range(rows):
        for j in range(cols):
            pixel=(img[i:i+window_size,j:j+window_size]/airlight).min()
            tran[i,j]=1.-omega*pixel
    #tran=tran.astype(np.uint8)
    io.imsave("Results/trans.jpg",tran)
    return [tran,airlight]


def haze_remove(img,t=0.1):
    res=transmission_map(img,7,0.95)
    print("Haze removing started...")
    tran=res[0]
    airlight=res[1]
    gtran=guided_filter(img,tran,20,0.001)  
    gtran[gtran<t]=t
    t=gtran.reshape(*gtran.shape,1).repeat(3,axis=2)
    dest=(img.astype(np.double)-airlight)/t+airlight
    dest*=255
    dest[dest>255]=255
    dest[dest<0]=0
    dest=dest.astype(np.uint8)
    io.imsave("Results/haze_free.jpg",dest)
    return dest


def get_haze_free():
    interface.start()
    img=np.array(interface.img).astype(np.double)/255.
    dest=haze_remove(img)
    interface.start2()
    return dest

get_haze_free()
