import os
import hashlib


# 每次读取 8k 字节数据
def read_chunks(fp):
    fp.seek(0)
    chunk = fp.read(8 * 1024)
    while chunk:
        yield chunk
        chunk = fp.read(8 * 1024)
    else:  # 最后要将游标放回文件开头
        fp.seek(0)


# 校验文件 md5 值
def md5sum(filename):
    md5 = hashlib.md5()
    cwd = os.getcwd()
    file_name = os.path.join(cwd, filename)
    with open(file_name, 'rb') as f:
        print(file_name)
        for chunk in read_chunks(f):
            md5.update(chunk)
    return md5.hexdigest()

