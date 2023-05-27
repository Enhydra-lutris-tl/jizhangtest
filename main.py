import glob
import os

import pandas as pd
from PySide6.QtCore import QFile, QIODevice
import test


# 获取支付宝账单数据
def getAlipayValue():
    path = open(get_Csv_File() + "/alipay_record_20230331_103351.csv",
                encoding='UTF-8')
    df_alipay = pd.read_csv(path)
    count = df_alipay.shape[0]
    df2 = df_alipay
    for i in range(count):
        # pd.isna(nan) 判断值是否为nan
        if pd.isna(df_alipay.iloc[i]['Unnamed: 1']):
            df2 = df2.drop(labels=i)  # 删除第二列内容为nan的行
    newcol = []
    cl = df2.columns
    for i in range(df2.shape[1]):
        newcol.append(df2.iloc[0][cl[i]].strip())
    df3 = df2.set_axis(newcol, axis=1).reset_index().drop(labels=0).drop(labels="index", axis=1)
    df4 = df3.drop(labels=['对方账号', '商品说明', '商家订单号', '备注'], axis=1)
    df4['金额'] = pd.to_numeric(df4['金额'])  # 列数据类型转换为浮点型
    for i in ['交易时间', '交易分类', '收/支', '收/付款方式', '金额']:
        if i != '金额':
            df4[i] = df4[i].apply(deleltKongge)
    # print('支付宝收支统计:\n', df4.groupby(['收/支']).agg({"金额": "sum"}))
    return df4[['交易时间', '交易分类', '收/支', '收/付款方式', '金额']]


# 返回路径
def get_Csv_File():
    return 'F:\资源'


# 获取微信账单数据
def getWecatValue():
    path = open(get_Csv_File() + "/微信支付账单(20230301-20230331).csv", encoding='UTF-8')
    df_wecat = pd.read_csv(path)
    df_wecat['金额(元)'] = df_wecat['金额(元)'].apply(convert_currency)
    df_wecat['金额(元)'] = pd.to_numeric(df_wecat['金额(元)'])  # 列数据类型转换为浮点型
    # print('微信收支统计:\n', df_wecat.groupby(['收/支']).agg({"金额(元)": "sum"}))
    new_cl = ['交易时间', '交易分类', '收/支', '收/付款方式', '金额']
    return df_wecat[['交易时间', '交易类型', '收/支', '支付方式', '金额(元)']].set_axis(new_cl, axis=1)


# 转换单元格内容
def convert_currency(val):
    new_val = val.replace(',', '').replace('¥', '')
    return float(new_val)


# 清除空格
def deleltKongge(value):
    new_value = value.strip()
    return new_value


# 获取文件夹路径
def getSrc(path, data):
    srcList = glob.glob(path + "*.csv")
    srcList2 = []
    for i in srcList:
        if ('副本' not in i) and (data in i):
            srcList2.append(i)
    if len(srcList2) > 2:
        print('错误')
    # print("输出结果为：", srcList2)
    return srcList2


# pandas输出内容展示
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)
pd.set_option('display.max_colwidth', 1000)
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)


# print(pd.concat([getWecatValue(), getAlipayValue()], ignore_index=True))
# getSrc('/Users/tanglei/life/', '20230331')


def ceshi():
    return pd.concat([getWecatValue(), getAlipayValue()], ignore_index=True)


def getIES():
    IES = ceshi().groupby(['收/支']).agg({"金额": "sum"})
    IES_Json = []
    Index_Value = IES.index.values
    IES_Sum = sum(IES['金额'])
    for i in range(len(Index_Value)):
        if Index_Value[i] == '/':
            label = '其他'
        else:
            label = Index_Value[i]
        IES_Json.append(

            {
                "label": label + '  ' + str(round(IES['金额'].loc[Index_Value[i]] / IES_Sum * 100, 2)) + '%',
                "value": IES['金额'].loc[Index_Value[i]]
            }
        )
    return IES_Json



