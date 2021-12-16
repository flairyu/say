# 语音播报模块
import pyttsx3
import sys
import os
import shutil
# aiff文件转换成mp3编码文件模块
from pydub import AudioSegment

print(sys.argv, len(sys.argv))

# 模块初始化
engine = pyttsx3.init()

# 语音播报内容
inputFile="input.txt"
contents = []
if len(sys.argv) >= 2:
    inputFile = sys.argv[1]

file = open(inputFile, "r", encoding="utf-8")
contents = file.readlines()
file.close()

# 输出文件格式
outFile = "out/out%d.aiff"
mp3File = "out/out%d.mp3"

print('准备开始语音播报...')
shutil.rmtree("out")
os.mkdir("out")

# 设置要播报的Unicode字符串
for index, content in enumerate(contents):
    print("out%d: %s" % (index, content))
    engine.say(content)
    engine.save_to_file(content, outFile % index)

# 等待任务完成
engine.runAndWait()

# 将文件转换为mp3格式
if len(sys.argv) >= 3 and sys.argv[2] == "mp3":
    for index, content in enumerate(contents):
        AudioSegment.from_file(outFile % index).export(mp3File % index,
                                                       format="mp3")
