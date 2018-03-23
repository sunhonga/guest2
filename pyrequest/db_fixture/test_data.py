import sys,time
sys.path.append('../db_fixture')
try:
    from mysql_db import DB
except ImportError:
    from .mysql_db import DB

#创建测试用的数据库

# create data
datas = {
    'sign_event':[
        {'id':1,'name':'红米Pro发布会','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2020-08-20 14:00:00','create_time':time.strftime("%Y-%m-%d %H:%M:%S")},
        {'id':2,'name':'可参加人数为0','`limit`':0,'status':1,'address':'北京会展中心','start_time':'2020-08-20 14:00:00','create_time':time.strftime("%Y-%m-%d %H:%M:%S")},
        {'id':3,'name':'当前状态为0关闭','`limit`':2000,'status':0,'address':'北京会展中心','start_time':'2020-08-20 14:00:00','create_time':time.strftime("%Y-%m-%d %H:%M:%S")},
        {'id':4,'name':'发布会已结束','`limit`':2000,'status':1,'address':'北京会展中心','start_time':'2001-08-20 14:00:00','create_time':time.strftime("%Y-%m-%d %H:%M:%S")},
        {'id':5,'name':'小米5发布会','`limit`':2000,'status':1,'address':'北京国家会议中心','start_time':'2020-08-20 14:00:00','create_time':time.strftime("%Y-%m-%d %H:%M:%S")},
    ],
    'sign_guest':[
        {'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1,'create_time':time.strftime("%Y-%m-%d %H:%M:%S")},
        {'id':2,'realname':'has sign','phone':13511001101,'email':'sign@mail.com','sign':1,'event_id':1,'create_time':time.strftime("%Y-%m-%d %H:%M:%S")},
        {'id':3,'realname':'tom','phone':13511001102,'email':'tom@mail.com','sign':0,'event_id':5,'create_time':time.strftime("%Y-%m-%d %H:%M:%S")},
    ],
}


# Inster table datas
def init_data():
    db = DB()
    for table,data in datas.items():
        db.clear(table)
        for d in data:
            db.insert(table,d)
    db.close()

if __name__ == '__main__':
    init_data()
