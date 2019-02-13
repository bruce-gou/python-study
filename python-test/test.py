# -*- coding: UTF-8 -*-
import mysql.connector

class TransferMoney():
    def __init__(self, db):
        self.db = db
    #转账流程
    def transferMoney(self, id, targetId, money):
        try:
            self.checkTargetUser(targetId) #检查被转账账号是否存在
            self.checkMoney(id, money) #检查余额是否足够
            self.transfer(id, targetId, money) #转账
            self.db.commit() #提交修改
        except Exception as e:
            self.db.rollback() #回滚事物
            raise e
    #检查被转账账号是否存在
    def checkTargetUser(self, id):
        try:
            cursor = self.db.cursor()
            sql_query = 'select * from user where id=%s;' % id
            cursor.execute(sql_query)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('转账账户不存在！')
            else:
               print '转账账户存在!'
        except mysql.connector.Error as e:
            raise Exception('检查被转账账户是否存在出错：' + str(e))
        finally:
            cursor.close()
    #检查转账金额
    def checkMoney(self, id, money):
        try:
            cursor = self.db.cursor()
            sql_query = 'select * from user where id=%s and money > %s;' % (id,money)
            cursor.execute(sql_query)
            rs = cursor.fetchall()
            if len(rs) != 1:
                raise Exception('转账账户余额不足！')
            else:
               print '转账方金额充足!' 
        except mysql.connector.Error as e:
            raise Exception('检查金额出错：：' + str(e))
        finally:
            cursor.close()
    #转账
    def transfer(self, id, targetId, money):
        try:
            cursor = self.db.cursor()
            #自己先减去转账金额
            sql_query = 'update user set money=money-%s where id=%s;' % (money,id)
            rs = cursor.execute(sql_query)
            if cursor.rowcount != 1:
                raise Exception('账号%s减款失败！' % id)
            #目标账户加上转账金额
            sql_query1 = 'update user set money=money+%s where id=%s;' % (money, targetId)
            cursor.execute(sql_query1)
            if cursor.rowcount != 1:
                raise Exception('账号%s加款失败！' % targetId)
            print '成功转账%s元！' %  money
        except mysql.connector.Error as e:
            raise Exception('转账出错：' + str(e))
        finally:
            cursor.close()

def test(n,x):
    num = 1
    for i in range(n):
        num *= x
    print num
if __name__ ==  '__main__':
    db = mysql.connector.connect(host='127.0.0.1',port=3306,user='root',passwd='gou110422',database='test',charset='utf8')
    base = TransferMoney(db)
    test(2,2)
    try:
        id,targetId,money = (1,2,100)
        base.transferMoney(id, targetId, money)
    except Exception as e:
        print '异常：',e
    finally:
        db.close()
#cursor.execute执行sql 语句
#cursor.rowcount 表中受影响数据个数 放在execute()之后
#fetchall() 获取所有数据
#fetchone()  获取一条数据
#fetchmany(3) 获取 3个数据
#db.commit() 数据表内容有更新，必须使用到该语句
#cursor.close() #关闭游标
