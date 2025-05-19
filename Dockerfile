
# 使用官方 Python 运行环境基础镜像
FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 复制当前目录所有文件到工作目录
COPY . /app

# 安装依赖（如果你有 requirements.txt，可以把依赖写进去）
RUN pip install requests

# 运行签到脚本
CMD ["python", "glados_checkin.py"]
