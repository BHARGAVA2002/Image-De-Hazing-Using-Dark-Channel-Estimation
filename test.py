from skimage.filters import gaussian
import interface
from PIL import ImageFilter
interface.start()
img=interface.img
temp=img.filter(ImageFilter.GaussianBlur(1))
temp.show()