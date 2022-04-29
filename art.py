# LIB IMPORTS
import os
import sys
import pywhatkit as py

# FLAG
flag = False

# FETCH SRC
try:
    os.listdir('./src/')[0]
    flag = True
except:
    print('Error: File not found!')
    sys.exit(1)

if(flag):

    # SRC
    SRC_NAME = os.listdir('./src/')[0]
    SRC_PATH = f'./src/{SRC_NAME}'
    SRC_IMGE = SRC_NAME.removesuffix('.jpeg').removesuffix('.png')

    # TAR
    TAR_PATH = './art/'
    TAR_NAME = 'ASCII_ART'
    TAR_EXTN = '.txt'

    # ART
    ART = f'{TAR_PATH}{SRC_IMGE} {TAR_NAME}{TAR_EXTN}'

    # READ
    def read(PATH, MODE):
        f = open(PATH, MODE)
        return f.read()

    # MODE
    def MODE():
        MODE = 'r'
        return MODE

    # READ PROMPTS
    def INIT_RD():
        INIT_PATH = './prompt/initializing.txt'
        return read(INIT_PATH, MODE())

    def SCSS_RD():
        SCSS_PATH = './prompt/success.txt'
        return f'{read(SCSS_PATH, MODE())} at {ART}'

    # print(SCSS_RD())
    # print(INIT_RD())

    # SAVE
    def saveASCII():
        print(INIT_RD())
        py.image_to_ascii_art(SRC_PATH, ART)
        print(SCSS_RD())
