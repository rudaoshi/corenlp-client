#coding=utf8
__author__ = 'Sun'


from client import CoreNLPClient

if __name__ == "__main__":

    client = CoreNLPClient('localhost', 5900)

    result = client.analysis("1982年初涉影坛，相继主演《投奔怒海》、《法外情》、《天若有情》、《暗战》、《无间道》、《盲探》等电影[2]  。至2014年已获3届香港电影金像奖最佳男主角奖、2届台湾电影金马奖最佳男主角奖[3]  ，2005年获颁香港院线“1985-2005年全港最高累积票房香港男演员”奖[4]  ，2006年被授予香港演艺学院荣誉院士[5]  。")
    print result