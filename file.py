import os

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

if __name__ == '__main__':
    # get_file_list()
    create_file()
    # create_file_link()
