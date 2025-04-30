import configparser


config = configparser.RawConfigParser()
config.read(".//configration/config.ini")


class Readconfig:

    @staticmethod
    def getbase_url():
        url = config.get('url', 'orange_url')
        return url

    @staticmethod
    def getusername():
        username = config.get('login', 'user_name')
        return username

    @staticmethod
    def getpassword():
        password = config.get('login', 'password')
        return password

    @staticmethod
    def gethours():
        hours = config.get('time', 'hours')
        return hours

    @staticmethod
    def getmin():
        mnt = config.get('time', 'minute')
        return mnt

