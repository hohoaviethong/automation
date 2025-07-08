import os
import json
from datetime import datetime

class ConfigReader:
    _config = None

    @staticmethod
    def load_config():
        if ConfigReader._config is None:
            config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'testsetting.json')
            with open(config_path, 'r') as config_file:
                ConfigReader._config = json.load(config_file)
        return ConfigReader._config
    
    @staticmethod
    def get_url():
        return ConfigReader.load_config()['login_data']['url']

    @staticmethod
    def get_login():
        return ConfigReader.load_config().get('login_data',{})
    
    @staticmethod
    def get_vacancy_raw():
        return ConfigReader.load_config().get('vacancy_data',{})
    
    # @staticmethod
    # def get_current_user():
    #     return ConfigReader.get_login().get('username','')
    
    @staticmethod
    def get_current_date():
        return datetime.now().strftime("%Y-%m-%d")
    
    @staticmethod
    def process_vacancy_data():
        vacancy = ConfigReader.get_vacancy_raw()
        vacancy_processed = {}
        for k, v in vacancy.items():
            if isinstance(v, str):
                # v = v.replace("{current_user}", ConfigReader.get_current_user())
                v = v.replace("{current_date}", ConfigReader.get_current_date())
            vacancy_processed[k] = v
        return vacancy_processed