import os
from os import path

def get_file_list():
    """
    디렉토리의 파일 목록을 가져오는 예제
    """
    path_dir = 'Y:/지어소프트_전달데이터/200602_front/20200602_133422/20200602_133422'

    file_list = os.listdir(path_dir)
    bin_file_list = []
    for file_name in file_list:
        if not file_name.startswith('CAN') and file_name.endswith('.bin'):
            bin_file_list.append(file_name)

    print(bin_file_list)

def create_file():
    os.mkdir('Y:/지어소프트_전달데이터/200602_front/20200602_133422/20200602_133422/1_20200602_133422/ann_img')

def create_file_link():
    """
    파일의 링크파일을 만드는 예제
    """
    src = 'C:/Users/hshwang/Desktop/test/123.txt'
    dst = 'C:/Users/hshwang/Desktop/test/123_link.txt'

    # This creates a symbolic link on python in tmp directory
    # 윈도우에서는 동작안함
    os.symlink(src, dst)

    print("symlink created")

def is_exist():
    print(__file__)
    print(path.exists('e:/ho/dev/IDE/VSCode-win32-x64/workspace/practice-python/file/sample.txt'))
    print(path.exists('sample.txt'))
    print(path.exists('./sample.txt'))
    print(path.exists('file/sample.txt'))
    print(os.getcwd())
    print(path.exists(os.getcwd() + '/file/sample.txt'))

def read_line_enumerate(line_number):
    with open('file/sample.txt', 'r') as file:
        for i, line in enumerate(file):
            if i == line_number:
                print(line)

def read_line_readlines(line_number):
    with open('file/sample.txt', 'r') as file:
        row = file.readlines()[line_number]
        print(row)


if __name__ == '__main__':
    # get_file_list()
    # create_file()
    # create_file_link()
    # is_exist()
    read_line_readlines(9)