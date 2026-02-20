# 🛠️ SnowToolBox使用教程
## 🚀 快速开始
### 📋 环境要求
- Python 3.6+
- 无需安装额外依赖（只用标准库）
- Windows/Linux/MacOS操作系统
### 📁 文件结构

```
你的项目文件夹/  
├── launcher.py # 主启动程序  
├── config.txt # 配置文件（可自定义）  
└── ... # 其他文件（会被整理功能分类）
```
## ## ⚙️ 配置文件 (config.txt) 规范

config.txt:

```
max = 1 # 最大选项数值
min = 1 # 最低选项数值
--- # 分割线，方便launcher.py解析
code :
1. 整理文件 - 自动分类整理当前目录文件 # 声明选项一的用处
--- # 分割线，方便launcher.py解析
import time
time.sleep(2)
...
# 上面是选项一，这里填写选项一的代码
--- # 分割线，方便launcher.py解析
code :
2. 系统信息 - 显示电脑基本配置 # 声明选项二的用处
---
# 上面是选项二，这里填写选项二的代码
...
--- # 最后以分割线结束
```

## ▶️ 运行你的代码
### 在写完config.txt后，你可以打开launcher.py，如果没有错误，那么大功告成！🎉

> [!IMPORTANT]
> 如果你的代码运行不正常，请检查是否保存config.txt或**仔细**地检查你的代码或config.txt语法是否存在错误
> 如果以上办法不能解决，请到github上提出issue或pr，提交前请先**确认**没有其他人提出这个错误

>[!TIP]
>你可以先编写Python代码，然后再将代码复制到config.txt中

## 📜 许可证
- 本项目（ToolBox）使用GNU3.0许可证

## 👥 贡献者

项目创建者：SnowCodeDev
优化：DeepSeek

## 🤝 致谢
- 如果你喜欢这个项目，请点个star，为此项目支持。
- 欢迎提出PR或issue
- 如果你认为此说明文件存在错误，请提交issue或PR

最后编辑时间：2026/2/20
编辑人：SnowCodeDev
