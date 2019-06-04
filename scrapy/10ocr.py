from PIL import Image
import tesserocr


def get_bin_table(img, threshold):
    ''' 获取灰度转二值的映射table, 返回灰度图片'''
    table = []
    for i in range(256):
        if i < threshold:
            table.append(0)
        else:
            table.append(1)
    img = img.point(table, '1')
    return img


def sum_9_region(img):
    '''
    9邻域框,以当前点为中心的田字框,黑点个数
    :return:
    '''
    # todo 判断图片的长宽度下限
    img = img.convert('L')
    pixdata = img.load()  # 加载图片数据
    w, h = img.size
    print(w, h)
    for y in range(1, h - 1):
        for x in range(1, w - 1):
            count = 0
            if pixdata[x, y - 1] > 245:
                count = count + 1
            if pixdata[x, y + 1] > 245:
                count = count + 1
            if pixdata[x - 1, y] > 245:
                count = count + 1
            if pixdata[x + 1, y] > 245:
                count = count + 1
            if pixdata[x - 1, y - 1] > 245:
                count = count + 1
            if pixdata[x - 1, y + 1] > 245:
                count = count + 1
            if pixdata[x + 1, y - 1] > 245:
                count = count + 1
            if pixdata[x + 1, y + 1] > 245:
                count = count + 1
            if count > 6:  # 控制领域判定大小
                pixdata[x, y] = 255
    return img
def get_crop_imgs(img):
    """
    按照图片的特点,进行切割,这个要根据具体的验证码来进行工作. # 见原理图
    :param img:
    :return:
    """
    child_img_list = []
    for i in range(4):
        x = 2 + i * (6 + 4)  # 见原理图
        y = 0
        child_img = img.crop((x, y, x + 6, y + 10))
        child_img_list.append(child_img)
    return child_img_list



imagePath = './photo/zao.png'
image = Image.open(imagePath)
imagery = image.convert('L')  # 转化为灰度图
image = get_bin_table(imagery)
