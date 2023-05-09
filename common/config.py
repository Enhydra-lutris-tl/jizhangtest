import yaml


def get_yaml_data():
    getvalue = yaml.safe_load(open('../config.yaml', encoding='UTF-8'))
    return getvalue


def set_yaml_data(data, key, value):
    data[key] = value
    # 将修改的配置保存到配置文件中
    with open('../config.yaml', 'w') as f:
        yaml.safe_dump(data, f)

    # 删除文件
    # os.remove('apollo.yaml')
