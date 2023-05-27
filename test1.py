import os
from win11toast import toast


class Toast():
    def __init__(self, title, text):
        toast(f'{title}', f'{text}',
              icon=r'F:\资源\KQ001.ico',
              image=r'F:\资源\aa11111.png',
              on_click='https://www.bilibili.com/')


Toast('欢迎', '点击进入B站')

# os.system('osascript -e \'display notification "这是一个通知！！！" with title "你的标题" subtitle "" \'')
