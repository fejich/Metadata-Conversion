from xml.sax.saxutils import escape
import os

def remove_extension(filename):
    return os.path.splitext(filename)[0]

# 定义输入输出文件路径
metadata_file = "metadata.pegasus.txt"
gamelist_file = "gamelist.xml"

# 初始化游戏列表和状态变量
games = []
current_game = None
in_files = False

# 读取并解析 metadata.txt
with open(metadata_file, "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip()  # 移除行尾空白和换行符
        if line.startswith("game:"):
            # 保存前一个游戏
            if current_game is not None:
                games.append(current_game)
            # 开始新游戏条目
            current_game = {"name": line[6:].strip()}
            in_files = False
        elif current_game is not None:
            if line.startswith("file:"):
                current_game["file"] = line[5:].strip()
                in_files = False
            elif line.startswith("files:"):
                current_game["files"] = []
                in_files = True
            elif in_files and line.strip():
                # 收集以空白开头的文件行
                if line[0].isspace():
                    current_game["files"].append(line.strip())
                else:
                    in_files = False
            elif line.startswith("description:"):
                current_game["description"] = line[12:].strip()

# 添加最后一个游戏
if current_game is not None:
    games.append(current_game)

# 写入 gamelist.xml 并生成 .m3u 文件
with open(gamelist_file, "w", encoding="utf-8") as f:
    f.write("<gameList>\n")
    for game in games:
        if "file" in game:
            # 单碟游戏
            path = escape("./" + game["file"])
            base = remove_extension(game["file"])
        elif "files" in game:
            # 双碟游戏
            m3u_filename = game["name"] + ".m3u"
            path = escape("./" + m3u_filename)
            # 生成 .m3u 文件
            with open(m3u_filename, "w", encoding="utf-8") as m3u_file:
                for file_path in game["files"]:
                    m3u_file.write(file_path + "\n")
            # 使用文件路径的公共目录作为媒体基础
            common_dir = os.path.basename(os.path.dirname(game["files"][0]))
            base = common_dir
        else:
            continue  # 跳过无文件的游戏

        media_dir = "./media/" + base
        name = escape(game["name"])
        desc = escape(game.get("description", ""))
        image = escape(media_dir + "/boxFront.png")
        image2 = escape(media_dir + "/boxFront.jpg")
        marquee = escape(media_dir + "/logo.png")
        video = escape(media_dir + "/video.mp4")

        # 写入游戏条目
        f.write("  <game>\n")
        f.write(f"    <path>{path}</path>\n")
        f.write(f"    <name>{name}</name>\n")
        f.write(f"    <desc>{desc}</desc>\n")
        f.write(f"    <image>{image}</image>\n")
        #f.write(f"    <image>{image2}</image>\n")
        f.write(f"    <marquee>{marquee}</marquee>\n")
        f.write(f"    <video>{video}</video>\n")
        f.write("  </game>\n")
    f.write("</gameList>\n")