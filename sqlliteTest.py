"""
sqlite 测试
"""
import sqlite3

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