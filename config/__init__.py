import yaml
import os
# yml的文件路径
yml_file = os.path.join(os.path.dirname(__file__),'config.yaml')
with open(yml_file,encoding="utf8") as file:
    # 解析yaml文件为字典类型
    config_data = yaml.safe_load(file)
    print(config_data)

# TODO 将yml文件序列化为类