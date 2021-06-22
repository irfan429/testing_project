from configparser import RawConfigParser
import sys
sys.path.append('C:/Users/spanidea111/PycharmProjects/nopcommerceApp/Configurations')

config = RawConfigParser()
config.read("C:/Users/spanidea111/PycharmProjects/nopcommerceApp/Configurations/config.ini")


class Readconfig:

    @staticmethod
    def get_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        user_name = config.get('common info', 'username')
        return user_name

    @staticmethod
    def get_password():
        pass_word = config.get('common info', 'password')
        return pass_word





