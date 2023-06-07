"""
sqlite 测试
"""
import sqlite3

# 创建表
def chuangj():
    conn = sqlite3.connect('sqlliteTest.db')

    c = conn.cursor()
    # 使用SQL语句
    c.execute("""CREATE TABLE test (
    name TEXT,
    age INTEGER,
    height REAL
    )""")

    conn.commit()
    conn.close()


# 加入新行
def tianjiahang(tableNmae, name, age, height):
    conn = sqlite3.connect('sqlliteTest.db')

    c = conn.cursor()
    # 使用SQL语句
    c.execute(f"INSERT INTO {tableNmae} values ({name}, {age}, {height})")

    conn.commit()
    conn.close()


# 修改行
def setData(ID, listData):
    for i in listData:
        print(ID, i, listData[i])


# 获取数据
def getData():
    conn = sqlite3.connect('sqlliteTest.db')

    c = conn.cursor()
    # 使用SQL语句
    c.execute(f"select * from test")
    res = c.fetchall()
    print(res)
    conn.commit()
    conn.close()
