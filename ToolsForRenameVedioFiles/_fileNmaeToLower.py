import os
# 获取文件夹绝对路径
current_dir = os.path.abspath(os.path.dirname(__file__))
print(current_dir)

fileName = ""
fileNameWithoutPostfix = ""
fileTypeWithPoint = ""
indexOfThePoint = -1
lengthOfTheFileName = 0

# 对目录下的文件进行遍历
for file in os.listdir(current_dir):
    # 判断是否是文件
    if os.path.isfile(os.path.join(current_dir, file)) == True:
        # 0.如果是含有“.py”的python文件，直接跳过替换
        if ".py" in file:
            continue
        elif ".ini" in file:
            continue
        else:
            print(file)
            # 1.准备文件名的字符串
            fileName = file
            # 2.检测字符串中文件扩展名的点“.”的位置
            indexOfThePoint = fileName.find(".")
            # 3.将文件的字符串分为名称和格式两部分
            lengthOfTheFileName = len(fileName)
            # 括号里的整数相当于数组的下标，包前不包后
            fileNameWithoutPostfix = fileName[0:indexOfThePoint]
            fileTypeWithPoint = fileName[indexOfThePoint:lengthOfTheFileName]
            print(indexOfThePoint)
            print(lengthOfTheFileName)
            print(fileNameWithoutPostfix)
            print(fileTypeWithPoint)
            # 4.将名称的部分改成小写
            fileNameWithoutPostfix = fileNameWithoutPostfix.lower()
            # 5.组合字符串
            fileName = fileNameWithoutPostfix+fileTypeWithPoint
            print(fileName)
            # 6.重命名文件
            os.rename(os.path.join(current_dir, file), os.path.join(current_dir, fileName))
# 结束
print("End")