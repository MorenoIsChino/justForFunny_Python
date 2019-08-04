import os
# 获取文件夹绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)

fileName = ""

# 对目录下的文件进行遍历
for file in os.listdir(current_dir):
    # 判断是否是文件
    if os.path.isfile(os.path.join(current_dir, file)) == True:
        # 0.如果是含有“.py”或者 “.ini”的python文件，直接跳过替换
        if ".py" in file:
            continue
        elif ".ini" in file:
            continue
        else:
            print(file)
            # 文件名首字母大写
            fileName = file
            fileName = fileName.capitalize()
            # 重命名文件
            os.rename(os.path.join(current_dir, file), os.path.join(current_dir, fileName))
# 结束
print("End")