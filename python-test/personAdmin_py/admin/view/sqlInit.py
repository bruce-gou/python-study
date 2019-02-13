from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.

#私有模块
import login.models as login
import admin.model.dict as dict
import admin.model.menu as menu
import admin.model.power as power
import admin.model.article as article
import admin.model.resources as resources
import admin.model.speech as speech

import admin.model.speech as models #创建数据库表的模块
from common.base import resBack, valuesFun

# 数据库初始化
def SqlInit(req):
    # 用户
    login.Users.objects.create(user='admin',pwd='MTIzNDU2',name='张三',role=1,roleName='超级管理员',isEnable=1,tel='17348052001',mailbox='qcnh1920@163.com')
    
    # 字典
    dict.Dict.objects.create(name='html', code='1', typeId=1)
    dict.Dict.objects.create(name='js', code='2', typeId=1)
    dict.Dict.objects.create(name='css', code='3', typeId=1)

    dict.Dict.objects.create(name='前端资料', code='1', typeId=2)
    dict.Dict.objects.create(name='技术刊物', code='2', typeId=2)
    dict.Dict.objects.create(name='工具插件', code='3', typeId=2)
    dict.Dict.objects.create(name='博客', code='4', typeId=2)
    dict.Dict.objects.create(name='网上教程', code='5', typeId=2)

    dict.Dict.objects.create(name='超级管理员', code='1', typeId=3)
    dict.Dict.objects.create(name='管理员', code='2', typeId=3)
    dict.Dict.objects.create(name='普通用户', code='3', typeId=3)

    dict.Dict.objects.create(name='系统管理', code='setting', typeId=4)
    dict.Dict.objects.create(name='随笔管理', code='bars', typeId=4)
    dict.Dict.objects.create(name='资源管理', code='database', typeId=4)

    dict.Dict.objects.create(name='查询', code='search', typeId=5)
    dict.Dict.objects.create(name='编辑', code='edit', typeId=5)
    dict.Dict.objects.create(name='删除', code='del', typeId=5)
    dict.Dict.objects.create(name='新增', code='add', typeId=5)

    # 字典类型
    dict.DictType.objects.create(name='随笔类型', code=1)
    dict.DictType.objects.create(name='资源类型', code=2)
    dict.DictType.objects.create(name='用户角色', code=3)
    dict.DictType.objects.create(name='菜单图标', code=3)
    dict.DictType.objects.create(name='菜单权限', code=4)

    # 菜单
    menu.Menu.objects.create(name='随笔管理', icon='bars', path='essay', orderNumber='1', isEnable=1, parentId=0, allPower='search')
    menu.Menu.objects.create(name='随笔列表', icon='', path='essayList', orderNumber='1.1', isEnable=1, parentId=1, allPower='search,edit,del,add')
    
    menu.Menu.objects.create(name='资源管理', icon='database', path='resources', orderNumber='2', isEnable=1, parentId=0, allPower='search')
    menu.Menu.objects.create(name='资源列表', icon='', path='list', orderNumber='2.1', isEnable=1, parentId=3, allPower='search,edit,del,add')

    menu.Menu.objects.create(name='系统管理', icon='setting', path='sys', orderNumber='3', isEnable=1, parentId=0, allPower='search')
    menu.Menu.objects.create(name='用户管理', icon='', path='user', orderNumber='3.1', isEnable=1, parentId=5, allPower='search,edit,del,add')
    menu.Menu.objects.create(name='菜单管理', icon='', path='menu', orderNumber='3.2', isEnable=1, parentId=5, allPower='search,edit,del,add')
    menu.Menu.objects.create(name='权限管理', icon='', path='power', orderNumber='3.3', isEnable=1, parentId=5, allPower='search,edit')
    menu.Menu.objects.create(name='数据字典', icon='', path='dict', orderNumber='3.4', isEnable=1, parentId=5, allPower='search,edit,del,add')

    # 权限
    power.Power.objects.create(userTypeId=1, menuId=1, menuName='随笔管理', power='查询')
    power.Power.objects.create(userTypeId=1, menuId=2, menuName='随笔列表', power='查询,新增,删除,编辑')
    power.Power.objects.create(userTypeId=1, menuId=3, menuName='资源管理', power='查询')
    power.Power.objects.create(userTypeId=1, menuId=4, menuName='资源列表', power='查询,新增,删除,编辑')
    power.Power.objects.create(userTypeId=1, menuId=5, menuName='系统管理', power='查询')
    power.Power.objects.create(userTypeId=1, menuId=6, menuName='用户管理', power='查询,新增,删除,编辑')
    power.Power.objects.create(userTypeId=1, menuId=7, menuName='菜单管理', power='查询,新增,删除,编辑')
    power.Power.objects.create(userTypeId=1, menuId=8, menuName='权限管理', power='查询,编辑')
    power.Power.objects.create(userTypeId=1, menuId=9, menuName='数据字典', power='查询,新增,删除,编辑')

    # 文章
    article.Article.objects.create(title='JS获取最终样式', content='11111', typeId=1, typeIdName='html', time='1470817725737', readNum=117, commentNum=1, isPublish=0)

    # 资源
    resources.Resources.objects.create(typeId=1, typeIdName='前端资料', name='菜鸟教程', url='http://www.runoob.com/')

    # 评论
    speech.Speech.objects.create(author='张三', content='测试', essayId=1, time='1479019567673', isCheck=1)
    return HttpResponse('数据初始化成功！')