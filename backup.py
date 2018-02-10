import os
import sys
import time
import zipfile


# 接收待压缩文件路径并解压到指定位置
def multi_compress(folder_list, zippath):
    for dire in folder_list:
        zip_dir(dire, zippath)
    unZip(zippath + add_time(), zippath)


# 压缩文件
def zip_dir(dire, zippath):
    filelist = []
    if os.path.isfile(dire):
        filelist.append(dire)
    else:
        for root, dir_list, filename in os.walk(dire):
            for name in filename:
                filelist.append(os.path.join(root, name))

    zipFile = zipfile.ZipFile(zippath + add_time(), 'a')
    for zip_file in filelist:
        zipFile.write(zip_file, remove_path(dire, zip_file))
    zipFile.close()


# 移除压缩文件多余目录前缀
def remove_path(dirpath, zippath):
    d_list = dirpath.split(os.sep)
    z_list = zippath.split(os.sep)
    length = len(z_list) - len(d_list) + 1
    z_path = z_list[-length:]
    zip_name = os.sep.join(z_path)
    return zip_name


# 添加压缩时间信息
def add_time():
    return time.strftime('%Y%m%d')


# 解压文件
def unZip(filepath, unzipPath):
    zf = zipfile.ZipFile(filepath)
    zf.extractall(unzipPath)
    zf.close()


if __name__ == '__main__':
    back_folder = sys.argv[1:len(sys.argv)-1]
    zippath = sys.argv[-1]
    multi_compress(back_folder, zippath)

