import re
import sys
import pandas as pd

SETS = ["A.", "B.", "C.", "D.", "E."]
def no_option(ans):
    if ans[:2] in SETS:
        return ans[2:]
    return ans

# 文件读取
if len(sys.argv) > 1:
    path = sys.argv[1]
else:
    print("Please use \'python csv2md.py xxx.csv\'")

df = pd.read_csv(path)

# 列名改变
col_now = list(df)
col_names = ["编号","开始时间","结束时间","自定义字段","申请年份","申请年份填空","昵称","本科专业","申请方向:CS","申请方向:DS","申请方向:Stat/Biostat","申请方向:MFE/Fin/FinMath","申请方向:其他","申请方向:其他填空","申请类型","最终决定","录取","拒绝","未出","绩点","排名","TOEFL/IELTS","GRE","实习经历","研究经历","论文发表","海外交流","重要奖项","邮箱","微信","分享", "NAN"]
df = df.rename(index=str, columns={key:val for key, val in zip(col_now, col_names)})
df.fillna("无", inplace=True)

# 昵称和本科专业
df_md = df.loc[:, ["昵称", "本科专业"]]

# 申请年份
df_md = pd.concat([df["申请年份"].apply(no_option), df_md], axis=1)

# 申请专业
def concat(major_list):
    majors = []
    for i in major_list:
        if i == "无":
            continue
        else:
           i = no_option(i)
        majors.append(i)
    if len(majors) == 0:
        return "无"
    else:
        return "; ".join(majors)

majors = []
for i, row in df.loc[:, ["申请方向:CS","申请方向:DS","申请方向:Stat/Biostat","申请方向:MFE/Fin/FinMath","申请方向:其他填空"]].iterrows():
    majors.append(concat(list(row)))
df["申请方向"] = majors
df_md = pd.concat([df_md, df["申请方向"]], axis=1)

# 申请类型
df_md = pd.concat([df_md, df["申请类型"].apply(no_option)], axis=1)

# 除联系方式之外的其他
for col in ["最终决定","录取","拒绝","未出","绩点","排名","TOEFL/IELTS","GRE","实习经历","研究经历","论文发表","海外交流","重要奖项"]:
    df_md = pd.concat([df_md, df[col]], axis=1)

df_md.to_csv("sample.csv", index=None)





