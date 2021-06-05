# f = open('passdict.txt', 'w')
# for id in range(1000000):
#     password = str(id).zfill(6)+'\n'
#     f.write(password)
# f.close()

from unrar import rarfile


def extractFile(zipFile, password):
    try:
        zipFile.extractall(pwd=bytes(password, "utf8"))
        print("password:" + password)  # 破解成功
    except:
        pass  # 失败，就跳过


def main():
    rarFile = rarfile.RarFile('D:\BaiduNetdiskDownload\whwdjx.rar')
    PwdLists = open('passdict.txt')  # 读入所有密码
    for line in PwdLists.readlines():  # 挨个挨个的写入密码
        Pwd = line.strip('\n')
        guess = extractFile(rarFile, Pwd)


if __name__ == '__main__':
    main()