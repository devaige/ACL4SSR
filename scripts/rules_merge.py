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
F_NAME_REDDIT = "Reddit.list"
F_NAME_GOOGLE = "Google.list"
F_NAME_APPLE = "Apple.list"
F_NAME_APPLE_MEDIA = "AppleMedia.list"
F_NAME_FACEBOOK = "Facebook.list"
F_NAME_MICROSOFT = "Microsoft.list"
F_NAME_MICROSOFT_MEDIA = "MicrosoftMedia.list"
F_NAME_HK_FASTEST = "HKFastest.list"
F_NAME_HK_BALANCE = "HKBalance.list"
F_NAME_JP_FASTEST = "JPFastest.list"
F_NAME_JP_BALANCE = "JPBalance.list"
F_NAME_SG_FASTEST = "SGFastest.list"
F_NAME_SG_BALANCE = "SGBalance.list"
F_NAME_TW_FASTEST = "TWFastest.list"
F_NAME_TW_BALANCE = "TWBalance.list"
F_NAME_REJECT = "Reject.list"
F_NAME_DIRECT = "Direct.list"
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
    F_NAME_REDDIT,
    F_NAME_GOOGLE,
    F_NAME_APPLE,  # Apple 相关的使用 Fastest 节点
    F_NAME_APPLE_MEDIA,  # Apple 媒体或存储相关的使用负载均衡节点
    F_NAME_FACEBOOK,
    F_NAME_MICROSOFT,
    F_NAME_HK_FASTEST,
    F_NAME_HK_BALANCE,
    F_NAME_JP_FASTEST,
    F_NAME_JP_BALANCE,
    F_NAME_SG_FASTEST,
    F_NAME_SG_BALANCE,
    F_NAME_TW_FASTEST,
    F_NAME_TW_BALANCE,
    F_NAME_DIRECT,  # 直连
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
    elif filename == F_NAME_APPLE:
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_APPLE)
    elif filename == F_NAME_REDDIT:
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_REDDIT)

    elif filename in (F_NAME_BINANCE, "Crypto.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_BINANCE)
    elif filename in (F_NAME_GITHUB, "Developer.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_GITHUB)
    elif filename in ("AppleNews.list", "AppleTV.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_APPLE_MEDIA)
    elif filename in ("Facebook.list", "Instagram.list", "Whatsapp.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_FACEBOOK)
    elif filename in ("Bing.list", "Microsoft.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_MICROSOFT)
    elif filename in ("OneDrive.list", "Xbox.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_MICROSOFT_MEDIA)
    elif filename in ("ProxyGFWlist.list", "ProxyLite.list", "Amazon.list", "AmazonIp.list", "Samsung.list", "Scholar.list", "Spark.list", "TopBlockedSites.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_HK_FASTEST)
    elif filename in ("ProxyMedia.list", "ABC.list", "Adobe.list", "All4.list", "BBC.list", "BBCiPlayer.list", "Blizzard.list", "DAZN.list", "Deezer.list", "Discord.list", "DiscoveryPlus.list", "DisneyPlus.list", "EHGallery.list", "EncoreTVB.list", "Epic.list", "F1.list", "FoxNow.list", "GameDownload.list", "HBO_GO_HKG.list", "HBO.list", "Hulu.list", "HWTV.list", "ITV.list", "JOOX.list", "KakaoTalk.list", "KKBOX.list", "My5.list", "MyTVSuper.list", "Nintendo.list", "NivodTV.list", "Olevod.list", "Origin.list", "Pandora.list", "PBS.list", "Qobuz.list", "SoundCloud.list", "Spotify.list", "Steam.list", "SteamCN.list", "TIDAL.list", "Twitch.list", "ViuTV.list", "Zoom.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_HK_BALANCE)
    elif filename in ("Dmm.list", "Sony.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_JP_FASTEST)
    elif filename in ("AbemaTV.list", "Dubox.list", "HuluJapan.list", "Japonx.list", "Niconico.list", "Pixiv.list", "Porn.list", "Pornhub.list", "TeraBox.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_JP_BALANCE)
    elif filename in ("VikACG.list", "Wikipedia.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_SG_FASTEST)
    elif filename in ("AbemaTV.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_SG_BALANCE)
    # elif filename in ("", ""):
    #     OUTPUT = os.path.join(d_mine_tmp, F_NAME_TW_FASTEST)
    elif filename in ("Bahamut.list", "BilibiliHMT.list", "IqiyiHMT.list", "KKTV.list", "TaiWanGood.list"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_TW_BALANCE)
    elif filename in ("Download.list", "UnBan.list"):  # 不处理
        OUTPUT = None

    elif filename.startswith("Google"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_GOOGLE)
    elif filename.startswith("YouTube"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_YOUTUBE)
    elif filename.startswith("Netflix"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_NETFLIX)
    elif filename.startswith("Claude"):
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_CLAUDE)
    elif filename.startswith("Ban") or filename == "PrivateTracker.list":  # 如果文件以 Ban 开头则表示是禁止规则
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_REJECT)

    else:
        OUTPUT = os.path.join(d_mine_tmp, F_NAME_DIRECT)

    if OUTPUT:
        with open(filepath, "r", encoding="UTF-8") as f:
            content = f.read()
        with open(OUTPUT, "a", encoding="UTF-8") as f:
            f.write(content + "\n")

# 自定义多行字符串常量规则
rules = {
    F_NAME_GOOGLE: [
        "# 从 Clash/Unban.list 中分离出来的 Google 规则",
        "DOMAIN,dl.google.com",
        "DOMAIN-SUFFIX,googletraveladservices.com",
    ],
    F_NAME_HK_BALANCE: [
        "# 从 Clash/Download.list 中分离出来的需要负载均衡的规则",
        "# Mac Download",
        "PROCESS-NAME,aria2c.exe",
        "PROCESS-NAME,fdm.exe",
        "PROCESS-NAME,Folx.exe",
        "PROCESS-NAME,NetTransport.exe",
        "PROCESS-NAME,Transmission.exe",
        "PROCESS-NAME,uTorrent.exe",
        "PROCESS-NAME,WebTorrent.exe",
        "PROCESS-NAME,WebTorrent Helper.exe",
        "PROCESS-NAME,qbittorrent.exe",
        "# bt",
        "DOMAIN-SUFFIX,smtp",
        "DOMAIN-KEYWORD,aria2",
        "URL-REGEX,(Subject|HELO|SMTP)",
    ],
    F_NAME_HK_FASTEST: [
        "# 从 Clash/UnBan.list 中分离出来的需要自动选择的规则",
        "# Epicgames",
        "DOMAIN-SUFFIX,ol.epicgames.com",
        "# Mozilla",
        "DOMAIN-SUFFIX,tracking-protection.cdn.mozilla.net",
        "# Origin",
        "DOMAIN,origin-a.akamaihd.net",
        "# General",
        "DOMAIN,app.adjust.com",
        "# Hypixel Network",
        "DOMAIN,rewards.hypixel.net",
        "# Koodo Mobile",
        "DOMAIN-SUFFIX,koodomobile.com",
        "DOMAIN-SUFFIX,koodomobile.ca",
    ],
    F_NAME_DIRECT: [
        "# 从 Clash/Download.list 中分离出来的需要直连的规则",
        "# Mac Download",
        "PROCESS-NAME,Thunder.exe",
        "# bt",
        "URL-REGEX,(api|ps|sv|offnavi|newvector|ulog.imap|newloc)(.map|).(baidu|n.shifen).com",
        "URL-REGEX,(.+.|^)(360|so|qihoo|360safe|qhimg|360totalsecurity|yunpan).(cn|com)",
        "URL-REGEX,(.+.)?(torrent|announce.php?passkey=|tracker|BitTorrent|bt_key|ed2k|find_node|get_peers|info_hash|magnet:|peer_id=|xunlei)(..+)?",
        "# XunLei",
        "URL-REGEX,(.?)(xunlei|sandai|Thunder|XLLiveUD)(.)",
        "PROCESS-NAME,DownloadService.exe",
        "# 360",
        "URL-REGEX,(.+\\.|^)(360|so)\\.(cn|com)",
        "# Tencent Weiyun",
        "PROCESS-NAME,Weiyun.exe",
        "#Baidu disk",
        "PROCESS-NAME,baidunetdisk.exe",
        "",
        "# 从 Clash/Unban.list 中分离出来的需要直连的规则",
        "# Getui",
        "DOMAIN-SUFFIX,dizhensubao.getui.com",
        "# Tencent",
        "DOMAIN,fairplay.l.qq.com",
        "DOMAIN,livew.l.qq.com",
        "DOMAIN,vd.l.qq.com",
        "# Umeng",
        "DOMAIN,errlog.umeng.com",
        "DOMAIN,msg.umeng.com",
        "DOMAIN,msg.umengcloud.com",
        "# Miui 小米",
        "DOMAIN,tracking.miui.com",
        "# General",
        "DOMAIN,bdtj.tagtic.cn",
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
