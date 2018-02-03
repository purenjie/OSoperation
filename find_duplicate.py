import os
import hashlib

md5_dict = {}
duplicate_list = []


# 遍历所给目录的所有文件
def walk(dirname):
    if os.path.exists(dirname):
        for name in os.listdir(dirname):
            path = os.path.join(dirname, name)

            if os.path.isdir(path):
                walk(path)
            else:
                md5sum(path, md5_dict, duplicate_list)


# 校验文件md5值
def md5sum(path, md5_dict, duplicate_list):
    md5 = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in read_chunks(f):
            md5.update(chunk)
        if md5.hexdigest() in md5_dict.values():
            duplicate_path = (return_path(md5_dict, md5.hexdigest()), path)
            duplicate_list.append(duplicate_path)
        else:
            md5_dict[path] = md5.hexdigest()


# 每次读取 8k 数据
def read_chunks(fp):
    fp.seek(0)
    chunk = fp.read(8 * 1024)
    while chunk:
        yield chunk
        chunk = fp.read(8 * 1024)
    else:  # 最后要将游标放回文件开头
        fp.seek(0)


# 通过 md5 值寻找文件路径
def return_path(d, value):
    for key in d:
        if d[key] == value:
            return key


# 返回重复的文件列表
def find_duplicate(dirname):
    walk(dirname)
    return duplicate_list

print(find_duplicate('/home/solejay/test'))


