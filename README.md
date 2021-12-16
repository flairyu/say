# 文本转语音

默认从input.txt输入，每行转换为一个语音文件

## 环境：

```bash
# 创建虚拟环境
python3 -m venv venv
venv/Script/activate

# 安装依赖包
pip install -r require.txt
```

## 使用：

```bash
python say.py

# 生成mp3格式的音频
python say.py input.txt mp3
```

执行上述命令，就会在当前目录生成一批：out/outxx.aiff 每行对应一个文件。如果指定了mp3，还会生成mp3文件。