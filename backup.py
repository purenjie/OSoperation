import os
import sys
import time
import zipfile


# 压缩文件
def zip_dir(dir):
    filelist = []
    if os.path.isfile(dir):
        filelist.append(dir)
    else:
        for root, dir_list, filename in os.walk(dir):# https://docs.python.org/3/library/os.html
            for name in filename:
                filelist.append(os.path.join(root, name))

    zipFile = zipfile.ZipFile(dir+'.zip', 'a')
    for zip_file in filelist:
        zipFile.write(zip_file, add_time() + remove_path(dir, zip_file))
    zipFile.close()


# 移除压缩文件多余目录前缀
def remove_path(dirpath, zippath):
    d_list = dirpath.split('/')
    z_list = zippath.split('/')
    length = len(z_list) - len(d_list) + 1
    z_path = z_list[-length:]
    zip_name = '/'.join(z_path)
    return zip_name


# 添加压缩时间信息
def add_time():
    today = time.strftime('%Y%m%d')
    now = time.strftime('%H%M%S')
    backup_time = today + '-' + now
    return backup_time


# 解压文件
def unZip(filepath, unzipPath):
    zf = zipfile.ZipFile(filepath)
    zf.extractall(unzipPath)
    zf.close()


if __name__ == '__main__':
    zip_dir(sys.argv[1])
    unZip(sys.argv[1] + '.zip', sys.argv[2])



















