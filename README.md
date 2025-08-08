# Metadata-Conversion
天马G（Pegasus）元数据转换为 EmulationStation 格式，适用于Batocera/RetroBat/EmuELEC 等复古游戏系统

Python 脚本使用AI编写，简单测试过可行。后续有发现问题再修改，使用时请注意备份数据。

用于将国内 跳坑者联盟 制作的 天马G metadata数据列表 `metadata.pegasus.txt`

转换为 Batocera 、RetroBat 、EmuELEC 等系统可识别的 EmulationStation 数据列表 `gamelist.xml`
> 包含游戏简介、封面图片与视频

### 运行环境与用法

+ Python 3
  
确保已安装 Pillow 库，用于处理图片格式转换

`pip install Pillow`

.py 与 .bat 文件复制至游戏 roms 目录下，运行相应 bat 脚本即可批量处理

> 9）批量生成空白游戏文件.bat 与 generate_files_same_dir.py  仅用于做测试，会生成空白的游戏文件！！！
>> 不要在实际游戏文件夹中使用

---

### 文件结构
![文件结构](https://github.com/fejich/Metadata-Conversion/blob/45d83dfc054c12348ebcddc9a27226cedfcc719a/%E6%96%87%E4%BB%B6%E7%BB%93%E6%9E%84.png)

### RetroBat 演示

![](https://github.com/fejich/Metadata-Conversion/blob/45d83dfc054c12348ebcddc9a27226cedfcc719a/%E6%95%88%E6%9E%9C1.png)
![](https://github.com/fejich/Metadata-Conversion/blob/45d83dfc054c12348ebcddc9a27226cedfcc719a/%E6%95%88%E6%9E%9C2.png)
