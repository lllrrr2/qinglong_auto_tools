# -*- coding: UTF-8 -*-
# 作者仓库:https://github.com/spiritLHL/qinglong_auto_tools
# 觉得不错麻烦点个star谢谢


'''
cron: 1
new Env('二叉树修复脚本依赖文件');
'''


import os,requests
import os.path
# from os import popen

# 版本号 2.10.9 ，其他环境自测
# 只修复依赖文件（jdCookie.js那种）！！不修复环境依赖（pip install aiohttp）！！
# 默认不做任何操作只查询依赖脚本存在与否，有需求请在配置文件中配置对应变量进行操作，更新不会增加缺失文件
# 如果你有发现更多的脚本依赖文件没有新增，欢迎提交issues到https://github.com/spiritLHL/dependence_scripts/issues
# 增加缺失依赖文件(推荐)
# export ec_fix_dep="true"
# 更新老旧依赖文件(慎填，默认的依赖我使用的魔改版本，非必要别选)
# export ec_ref_dep="true"

# 2021.11.27 支持新版本仓库拉取的脚本目录结构，针对各个仓库进行依赖检索
try:
    if os.environ["ec_fix_dep"] == "true":
        print("已配置依赖文件缺失修复\n")
        fix = 1
    else:
        fix = 0
except:
    fix = 0
    print("默认不修复缺失依赖文件，有需求")
    print("请在配置文件中配置 export ec_fix_dep=\"true\" 开启脚本依赖文件缺失修复\n")

try:
    if os.environ["ec_ref_dep"] == "true":
        print("已配置依赖文件老旧更新\n")
        ref = 1
    else:
        ref = 0
except:
    ref = 0
    print("默认不更新老旧依赖文件，有需求")
    print("请在配置文件中配置 export ec_re_dep=\"true\" 开启脚本依赖文件更新\n")


def traversalDir_FirstDir(path):

    list = []
    if (os.path.exists(path)):
        files = os.listdir(path)
        for file in files:
            m = os.path.join(path,file)
            if (os.path.isdir(m)):
                h = os.path.split(m)
                list.append(h[1])
        print("文件夹名字有：")
        print(list)
        return list

def check_dependence(file_path):
    res = requests.get("https://api.github.com/repos/spiritLHL/dependence_scripts/contents").json()
    dependence_scripts_name = []
    for i in res:
        dependence_scripts_name.append(i["name"])

    dir_list = os.listdir(file_path)

    # 查询
    for i in dependence_scripts_name:
        if i not in dir_list and i != "utils" and i != "function":
            print("缺失文件 {}{}".format(file_path,i))
            # 修补
            try:
                if fix == 1:
                    print("增加文件 {}{}".format(file_path,i))
                    r = requests.get(
                        "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/" + i).text
                    with open(file_path+i, "w", encoding="utf-8") as fe:
                        fe.write(r)
            except:
                temp = 1

    try:
        if temp == 1:
            print("未配置ec_fix_dep，默认不修复增加缺失的依赖文件")
    except:
        pass

    # 更新
    try:
        if ref == 1:
            for i in dependence_scripts_name:
                if i != "utils" and i != "function":
                    with open(i, "r", encoding="utf-8") as f:
                        r = requests.get(
                            "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/" + i).text
                        d = f.read()
                        if r == d:
                            print("无需修改 {}".format(i))
                        else:
                            print("更新文件 {}".format(i))
                            with open(file_path+i, "w", encoding="utf-8") as fe:
                                fe.write(r)
    except:
        print("未配置ec_ref_dep，默认不更新依赖文件")

    #########################################################################################################

    # utils

    res = requests.get("https://api.github.com/repos/spiritLHL/dependence_scripts/contents/utils").json()
    dependence_scripts_utils = []
    for i in res:
        dependence_scripts_utils.append(i["name"])

    try:
        utils_list = os.listdir(file_path+"utils")
    except:
        os.makedirs(file_path+"utils")
        utils_list = os.listdir(file_path+"utils")

    # 查询
    for i in dependence_scripts_utils:
        if i not in utils_list and i != "utils" and i != "function":
            print("缺失文件 {}utils/{}".format(file_path,i))
            # 修补
            try:
                if fix == 1:
                    print("增加文件 {}utils/{}".format(file_path,i))
                    r = requests.get(
                        "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/utils/" + i).text
                    with open(file_path+"utils/" + i, "w", encoding="utf-8") as fe:
                        fe.write(r)
            except:
                temp = 1

    try:
        if temp == 1:
            print("未配置ec_fix_dep，默认不修复增加缺失的依赖文件")
    except:
        pass

    # 更新
    try:
        if ref == 1:
            for i in dependence_scripts_utils:
                if i != "utils" and i != "function":
                    with open(file_path+"utils/" + i, "r", encoding="utf-8") as f:
                        r = requests.get(
                            "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/utils/" + i).text
                        d = f.read()
                        if r == d:
                            print("已存在文件 {}utils/{}".format(file_path,i))
                        else:
                            print("更新文件 {}utils/{}".format(file_path,i))
                            with open(file_path+"utils/" + i, "w", encoding="utf-8") as fe:
                                fe.write(r)
    except:
        print("未配置ec_ref_dep，默认不更新依赖文件")

    ####################################################################################################

    # function

    res = requests.get("https://api.github.com/repos/spiritLHL/dependence_scripts/contents/function").json()
    dependence_scripts_function = []
    for i in res:
        dependence_scripts_function.append(i["name"])

    try:
        function_list = os.listdir(file_path+"function")
    except:
        os.makedirs(file_path+"function")
        function_list = os.listdir(file_path+"function")

    # 查询
    for i in dependence_scripts_function:
        if i not in function_list and i != "utils" and i != "function":
            print("缺失文件 {}function/{}".format(file_path,i))
            # 修补
            try:
                if fix == 1:
                    print("增加文件 {}function/{}".format(file_path,i))
                    r = requests.get(
                        "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/function/" + i).text
                    with open(file_path+"function/" + i, "w", encoding="utf-8") as fe:
                        fe.write(r)
            except:
                temp = 1

    try:
        if temp == 1:
            print("未配置ec_fix_dep，默认不修复增加缺失的依赖文件")
    except:
        pass

    # 更新
    try:
        if ref == 1:
            for i in dependence_scripts_function:
                if i != "utils" and i != "function":
                    with open(file_path+"function/" + i, "r", encoding="utf-8") as f:
                        r = requests.get(
                            "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/function/" + i).text
                        d = f.read()
                        if r == d:
                            print("已存在文件 {}function/{}".format(file_path,i))
                        else:
                            print("更新文件 {}function/{}".format(file_path,i))
                            with open(file_path+"function/" + i, "w", encoding="utf-8") as fe:
                                fe.write(r)
    except:
        print("未配置ec_ref_dep，默认不更新依赖文件")


def check_root():
    res = requests.get("https://api.github.com/repos/spiritLHL/dependence_scripts/contents").json()
    dependence_scripts_name = []
    for i in res:
        dependence_scripts_name.append(i["name"])

    dir_list = os.listdir("./")

    # 查询
    for i in dependence_scripts_name:
        if i not in dir_list and i != "utils" and i != "function":
            print("缺失文件 {}".format(i))
            # 修补
            try:
                if fix == 1:
                    print("增加文件 {}".format(i))
                    r = requests.get(
                        "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/" + i).text
                    with open(i, "w", encoding="utf-8") as fe:
                        fe.write(r)
            except:
                temp = 1

    try:
        if temp == 1:
            print("未配置ec_fix_dep，默认不修复增加缺失的依赖文件")
    except:
        pass

    # 更新
    try:
        if ref == 1:
            for i in dependence_scripts_name:
                if i != "utils" and i != "function":
                    with open(i, "r", encoding="utf-8") as f:
                        r = requests.get(
                            "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/" + i).text
                        d = f.read()
                        if r == d:
                            print("无需修改 {}".format(i))
                        else:
                            print("更新文件 {}".format(i))
                            with open(i, "w", encoding="utf-8") as fe:
                                fe.write(r)
    except:
        print("未配置ec_ref_dep，默认不更新依赖文件")

    #########################################################################################################

    # utils

    res = requests.get("https://api.github.com/repos/spiritLHL/dependence_scripts/contents/utils").json()
    dependence_scripts_utils = []
    for i in res:
        dependence_scripts_utils.append(i["name"])

    try:
        utils_list = os.listdir("./utils")
    except:
        os.makedirs("utils")
        utils_list = os.listdir("./utils")

    # 查询
    for i in dependence_scripts_utils:
        if i not in utils_list and i != "utils" and i != "function":
            print("缺失文件 utils/{}".format(i))
            # 修补
            try:
                if fix == 1:
                    print("增加文件 utils/{}".format(i))
                    r = requests.get(
                        "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/utils/" + i).text
                    with open("./utils/" + i, "w", encoding="utf-8") as fe:
                        fe.write(r)
            except:
                temp = 1

    try:
        if temp == 1:
            print("未配置ec_fix_dep，默认不修复增加缺失的依赖文件")
    except:
        pass

    # 更新
    try:
        if ref == 1:
            for i in dependence_scripts_utils:
                if i != "utils" and i != "function":
                    with open("./utils/" + i, "r", encoding="utf-8") as f:
                        r = requests.get(
                            "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/utils/" + i).text
                        d = f.read()
                        if r == d:
                            print("已存在文件 utils/{}".format(i))
                        else:
                            print("更新文件 utils/{}".format(i))
                            with open("./utils/" + i, "w", encoding="utf-8") as fe:
                                fe.write(r)
    except:
        print("未配置ec_ref_dep，默认不更新依赖文件")

    ####################################################################################################

    # function

    res = requests.get("https://api.github.com/repos/spiritLHL/dependence_scripts/contents/function").json()
    dependence_scripts_function = []
    for i in res:
        dependence_scripts_function.append(i["name"])

    try:
        function_list = os.listdir("./function")
    except:
        os.makedirs("function")
        function_list = os.listdir("./function")

    # 查询
    for i in dependence_scripts_function:
        if i not in function_list and i != "utils" and i != "function":
            print("缺失文件 function/{}".format(i))
            # 修补
            try:
                if fix == 1:
                    print("增加文件 function/{}".format(i))
                    r = requests.get(
                        "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/function/" + i).text
                    with open("./function/" + i, "w", encoding="utf-8") as fe:
                        fe.write(r)
            except:
                temp = 1

    try:
        if temp == 1:
            print("未配置ec_fix_dep，默认不修复增加缺失的依赖文件")
    except:
        pass

    # 更新
    try:
        if ref == 1:
            for i in dependence_scripts_function:
                if i != "utils" and i != "function":
                    with open("./function/" + i, "r", encoding="utf-8") as f:
                        r = requests.get(
                            "https://ghproxy.com/https://raw.githubusercontent.com/spiritLHL/dependence_scripts/master/function/" + i).text
                        d = f.read()
                        if r == d:
                            print("已存在文件 function/{}".format(i))
                        else:
                            print("更新文件 function/{}".format(i))
                            with open("./function/" + i, "w", encoding="utf-8") as fe:
                                fe.write(r)
    except:
        print("未配置ec_ref_dep，默认不更新依赖文件")




if __name__ == '__main__':

    # 针对青龙拉取仓库后单个仓库单个文件夹的情况对每个文件夹进行检测，不需要可以注释掉  开始到结束的部分

    ### 开始

    dirs_ls = traversalDir_FirstDir("./")

    # script根目录默认存在的文件夹，放入其中的名字不再检索依赖完整性
    or_list = ['node_modules', '__pycache__', 'utils', '.pnpm-store', 'function', 'tools']

    print()
    for i in dirs_ls:
        if i not in or_list:
            file_path = "./" + i + "/"
            print("检测依赖文件是否完整路径  {}".format(file_path))
            check_dependence(file_path)
            print()

    ### 结束


    # 检测根目录，不需要可以注释掉下面这行，旧版本只需要保留下面这行
    check_root()


    print("检测完毕")









# 待开发
# 修复依赖环境
# export ec_add_dep="true"
# docker exec -it qinglong bash -c "$(curl -fsSL https://ghproxy.com/https://raw.githubusercontent.com/FlechazoPh/QLDependency/main/Shell/QLOneKeyDependency.sh | sh)"
# try:
#     if os.environ["ec_add_dep"] == "true":
#         pass
# except:
#     pass
# text = os.popen("$(curl -fsSL https://ghproxy.com/https://raw.githubusercontent.com/FlechazoPh/QLDependency/main/Shell/QLOneKeyDependency.sh | sh)").read()
# print(text)
