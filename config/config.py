import os

import yaml


def get_yaml_data(yaml_path):
    getvalue = yaml.safe_load(open(yaml_path, encoding='UTF-8'))
    return getvalue


def set_yaml_data(data, key, value):
    data[key] = value
    # 将修改的配置保存到配置文件中
    with open('../config.yaml', 'w') as f:
        yaml.safe_dump(data, f)


# 添加内容
'''
    data : 源数据
    add_key : 要添加的内容的键
    add_value : 要添加的内容数据
'''


def add_yaml_data(data, add_key, add_value):
    yaml_data = data
    # 判断是否存在该键
    if add_key in yaml_data:
        print('已存在的key，添加失败，请使用「set_yaml_data」方法进行修改')
    else:
        yaml_data[add_key] = add_value
        with open('../config.yaml', 'w') as f:
            yaml.safe_dump(yaml_data, f)


# 删除文件
def remove_yaml(yaml_path):
    os.remove(yaml_path)
