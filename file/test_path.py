files = list()
default_upload_path = '/mnt/default'
# for path in '/mnt/default'.split('/'):

file_info = [None for _ in range(2)]
file_info[0] = 'd'
file_info[1] = default_upload_path.split('/')[1]
files.append(file_info)
print(files)