import os
import shutil

print("Starting script execution...")

# 定义目录路径
D_CLASH = "Clash"
d_clash_ruleset = os.path.join(D_CLASH, "Ruleset")
D_MINE = "Mine"
d_mine_tmp = os.path.join(D_MINE, "TMP")

# 创建 TMP 目录
os.makedirs(d_mine_tmp, exist_ok=True)

# 定义输出文件名
F_NAME_OPEN_AI = "OpenAI.list"
F_NAME_CLAUDE = "Claude.list"
F_NAME_TELEGRAM = "Telegram.list"
F_NAME_TWITTER = "Twitter.list"
F_NAME_YOUTUBE = "Youtube.list"
F_NAME_BINANCE = "Binance.list"
F_NAME_GITHUB = "Github.list"
F_NAME_LINE = "Line.list"
F_NAME_LINE_TV = "LineTV.list"
F_NAME_NETFLIX = "Netflix.list"
F_NAME_TIKTOK = "TikTok.list"
F_NAME_REJECT = "Reject.list"
# 这里就顺便定义规则的顺序的，越是小众的规则集越靠前，越是重要的规则集越靠前
rules_file_names = {
    F_NAME_OPEN_AI,
    F_NAME_CLAUDE,
    F_NAME_TELEGRAM,
    F_NAME_TWITTER,
    F_NAME_YOUTUBE,
    F_NAME_BINANCE,
    F_NAME_GITHUB,
    F_NAME_LINE,
    F_NAME_LINE_TV,
    F_NAME_NETFLIX,
    F_NAME_TIKTOK,
    "Google.list",
    "Apple.list",  # Apple 相关的使用 Fastest 节点
    "AppleMedia.list",  # Apple 媒体或存储相关的使用负载均衡节点
    "Facebook.list",
    "Microsoft.list",
    "HKFastest.list",
    "HKBalance.list",
    "JPFastest.list",
    "JPBalance.list",
    "SGFastest.list",
    "SGBalance.list",
    "TWFastest.list",
    "TWBalance.list",
    "UKFastest.list",
    "UkBalance.list",
    "USFastest.list",
    "USBalance.list",
    "Direct.list",  # 直连
    F_NAME_REJECT,  # 禁止
}

# 创建空的输出文件
for filename in rules_file_names:
    open(os.path.join(d_mine_tmp, filename), "w", encoding="UTF-8").close()

# 读取 Clash 和 Clash/Ruleset 目录下的 .list 文件
rules_list_file_paths = []  # 预定义一个数据用于存储 list 文件的路径
for rules_list_file_dirs in [D_CLASH, d_clash_ruleset]:
    print(f"Searching list file in {rules_list_file_dirs}")
    for filename in os.listdir(rules_list_file_dirs):
        print(f"Found the list file {filename}")
        filepath = os.path.join(rules_list_file_dirs, filename)
        if os.path.isfile(filepath) and filename.endswith(".list"):
            rules_list_file_paths.append(filepath)

# 遍历 files 列表并分类写入 TMP 目录
for filepath in rules_list_file_paths:
    filename = os.path.basename(filepath)  # 根据文件路径获取文件名
    OUTPUT = None
    if filename.lower() == F_NAME_OPEN_AI.lower():
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_OPEN_AI)
    elif filename == F_NAME_TELEGRAM:
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_TELEGRAM)
    elif filename == F_NAME_TWITTER:
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_TWITTER)
    elif filename == F_NAME_LINE:
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_LINE)
    elif filename == F_NAME_LINE_TV:
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_LINE_TV)
    elif filename == F_NAME_TIKTOK:
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_TIKTOK)
    elif filename in (F_NAME_BINANCE, "Crypto.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_BINANCE)
    elif filename in (F_NAME_GITHUB, "Developer.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_GITHUB)
    elif filename.startswith("YouTube"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_YOUTUBE)
    elif filename.startswith("Netflix"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_NETFLIX)
    elif filename.startswith("Claude"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_CLAUDE)
    elif filename.startswith("Ban"):  # 如果文件以 Ban 开头则表示是禁止规则
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_REJECT)
    if OUTPUT:
        with open(filepath, "r", encoding="UTF-8") as f:
            content = f.read()
        with open(OUTPUT, "a", encoding="UTF-8") as f:
            f.write(content)

# 自定义多行字符串常量规则
rules = {
    F_NAME_REJECT: [
        "# Custom Reject Rules",
        "DOMAIN-SUFFIX,example.com",
        "DOMAIN,another-example.com",
    ],
    "Direct.list": [
        "# Custom Direct Rules",
        "DOMAIN-SUFFIX,example.net",
        "DOMAIN,another-direct-example.com",
    ],
}

# 将自定义规则写入具体规则文件
for filename, rules in rules.items():
    output_file = os.path.join(d_mine_tmp, filename)
    with open(output_file, "a", encoding="UTF-8") as f:
        f.write("\n".join(rules) + "\n")

# 删除 Mine 目录下的所有规则文件
for filename in os.listdir(D_MINE):
    filepath = os.path.join(D_MINE, filename)
    if os.path.isfile(filepath) and filename.endswith(".list"):
        os.remove(filepath)

# 将 TMP 目录下的文件移动到 Mine 目录
for filename in os.listdir(d_mine_tmp):
    shutil.move(os.path.join(d_mine_tmp, filename), D_MINE)

# 删除 TMP 目录
shutil.rmtree(d_mine_tmp)
print("Script execution completed.")
