from captcha.image import ImageCaptcha  # pip install captcha
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import random,time

# 验证码中的字符
number = ['0','1','2','3','4','5','6','7','8','9']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


IMAGE_HEIGHT = 40
IMAGE_WIDTH = 132
MAX_CAPTCHA = 4
CHAR_SET_LEN = 62

def random_captcha_text(char_set=number+alphabet+ALPHABET, captcha_size=4):
    captcha_text = []
    for i in range(captcha_size):
        c = random.choice(char_set)
        captcha_text.append(c)
    return captcha_text

# 生成字符对应的验证码
def gen_captcha_text_and_image():
    image = ImageCaptcha(width=IMAGE_WIDTH, height=IMAGE_HEIGHT, font_sizes=(16, 28, 40))

    captcha_text = random_captcha_text()
    captcha_text = ''.join(captcha_text)

    captcha = image.generate(captcha_text)
    image.write(captcha_text, captcha_text + '.jpg')  # 写到文件

    captcha_image = Image.open(captcha)
    captcha_image = np.array(captcha_image)
    return captcha_text, captcha_image

if __name__ == '__main__':
    # 测试
    while(1):
        text, image = gen_captcha_text_and_image()
        print('begin ', time.ctime(), type(image))
        f = plt.figure()
        ax = f.add_subplot(111)
        ax.text(0.1, 0.9,text, ha='center', va='center', transform=ax.transAxes)
        plt.imshow(image)


        #plt.show()
        print('end ', time.ctime())