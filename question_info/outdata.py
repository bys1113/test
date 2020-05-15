import json, os



def jsonLoad(filepath):
    '''
    读取指定路径下的JSON文件
    支持传入目录，会查找目录下的.json文件读取
    :param filepath: 文件路径
    :return: 返回解码的JSON数据 或者 None
    '''

    _path = ''
    if os.path.isdir(filepath):    # 目录的处理
        for file in os.listdir(filepath):
            if file.endswith('json'):
                _path = os.path.join(filepath, file)
    elif os.path.isfile(filepath) and filepath.endswith('json'):# 文件的处理
        _path = filepath

    # 无JSON文件返回None
    if _path == '':
        print("未发现JSON结尾的文件，无法解码")
        return None
    # 解码Json
    try:
        with open(_path, 'r', encoding='utf-8') as fp:
                return json.load(fp)
    except Exception as e:
        print(e)

def getOption(id):
    '''
    返回试题的选项信息
    :param id:  试题编号
    :return: option：{'A': '北京', 'B': '西安', 'C': '深圳', 'D': '上海'}
    '''
    return (content['选项'][0]['Question-001'])

path = r'E:\UI\question_info'
print(jsonLoad(path))


