import numpy as np
from PIL import Image
# SVDTest

'''
函数功能： SVD并还原压缩后的数据
参数说明： data代表原始矩阵，percent代表奇异值总和的百分比
'''


def get_approx_svd(data, percent):
    print("Counting sigma...\n")
    u, s, vt = np.linalg.svd(data)
    sigma = np.zeros(np.shape(data))
    sigma[:len(s), :len(s)] = np.diag(s)
    count = int(sum(s)*percent)
    k = -1
    cursum = 0
    while cursum <= count:
        k += 1
        cursum += s[k]
    d = u[:, :k].dot(sigma[:k, :k].dot(vt[:k, :]))
    d[d < 0] = 0
    d[d > 255] = 255
    return np.rint(d).astype("uint8")


'''
函数功能：导入图像，进行SVD压缩，并重构图像
参数说明：filename代表文件名，p代表取值的百分比，get_approx_svd是方法名
'''


def rebuild_image(filename, p, get_approx_svd):
    img = Image.open(filename, 'r')  # openfile
    a = np.array(img)
    r0 = a[:, :, 0]
    g0 = a[:, :, 1]
    b0 = a[:, :, 2]
    r = get_approx_svd(r0, p)

    g = get_approx_svd(g0, p)

    b = get_approx_svd(b0, p)

    i = np.stack((r, g, b), 2)
    Image.fromarray(i).save(str(p*100) + filename)  # save image
    img = Image.open(str(p*100) + filename, 'r')
    img.show()  # show image


filename = "svdtest2.jpg"
t = 1
print("Loading...\n")
rebuild_image(filename, 1.0, get_approx_svd)
print("Done.\n")
