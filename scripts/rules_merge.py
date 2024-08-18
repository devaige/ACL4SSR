import os
import shutil

# 定义目录路径
d_clash = "Clash"
d_clash_ruleset = os.path.join(d_clash, "Ruleset")
d_mine = "Mine"
d_mine_tmp = os.path.join(d_mine, "TMP")

# 创建 TMP 目录
os.makedirs(d_mine_tmp, exist_ok=True)

# 定义输出文件名
F_NAME_OPEN_AI = "OpenAI.list"
F_NAME_REJECT = "Reject.list"
# 这里就顺便定义规则的顺序的，越是小众的规则集越靠前，越是重要的规则集越靠前
rules_file_names = {
    F_NAME_OPEN_AI,
    "Claude.list",
    "Telegram.list",
    "Twitter.list",
    "Youtube.list",
    "Binance.list",
    "Github.list",
    "Line.list",
    "Netflix.list",
    "TikTok.list",
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
    open(os.path.join(d_mine_tmp, filename), "w").close()

# 读取 Clash 和 Clash/Ruleset 目录下的 .list 文件
rules_list_file_paths = []  # 预定义一个数据用于存储 list 文件的路径
for rules_list_file_dirs in [d_clash, d_clash_ruleset]:
    for dirpath, dirnames, filenames in os.walk(rules_list_file_dirs):  # 遍历指定目录得到文件夹路径、文件夹名字、文件名的三元组
        for filename in filenames:  # 遍历文件名
            if filename.endswith(".list"):  # 根据文件名判断文件是否所需
                rules_list_file_paths.append(
                    os.path.join(dirpath, filename)
                )  # 将 list 文件路径存入数组

# 遍历 files 列表并分类写入 TMP 目录
for filepath in rules_list_file_paths:
    filename = os.path.basename(filepath)  # 根据文件路径获取文件名
    output = None
    if filename.startswith("Ban"):  # 如果文件以 Ban 开头则表示是禁止规则
        output_file = os.path.join(d_mine_tmp, F_NAME_REJECT)
    if output:
        with open(filepath, "r") as f:
            content = f.read()
        with open(output, "a") as f:
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
    with open(output_file, "a") as f:
        f.write("\n".join(rules) + "\n")

# 删除 Mine 目录下的所有规则文件
for filename in os.listdir(d_mine):
    filepath = os.path.join(d_mine, filename)
    if os.path.isfile(filepath) and filename.endswith(".list"):
        os.remove(filepath)

# 将 TMP 目录下的文件移动到 Mine 目录
for filename in os.listdir(d_mine_tmp):
    shutil.move(os.path.join(d_mine_tmp, filename), d_mine)

# 删除 TMP 目录
shutil.rmtree(d_mine_tmp)
