import os
import string

# 获取文件夹绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)

fileName = ""
#对目录下的文件进行遍历
for file in os.listdir(current_dir):
    # 判断是否是文件
    if os.path.isfile(os.path.join(current_dir, file))==True:
        # print(file)
        fileName = file
        # 检查文件名中是否有 ‘add'
        if "add" in fileName:
            if "_add" in fileName:
                continue
            else:
                print('Yes')
                # python3.7 必须在使用 replace 时的写法
                fileName=fileName.replace("add","-")
                print(fileName)
                # 重命名
                os.rename(os.path.join(current_dir, file), os.path.join(current_dir, fileName))
# 结束
print("End")