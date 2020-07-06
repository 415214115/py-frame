import configparser
config = configparser.ConfigParser()
file_path = 'AppConfig/config.ini'
class configFile():
    def __init__(self):
        pass

    def __get_file(self):
        with open(file_path,'r') as files:
            config.read_file(files)

    def __set_file(self):
        with open(file_path,'w+') as files:
            config.write(files)

    def get_config(self, section):
        self.__get_file()
        data = {}
        for i in config.items(section):
            data[i[0]] = i[1]
            # print (config.items('db'))
        return data
        
    def set_config(self, section, key, value):
        config.read(file_path)
        config.set(section, key, value)
        self.__set_file()
        
cfg = configFile()

print(cfg.get_config('run'))