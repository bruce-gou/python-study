from django.urls import path

# 私有模块
import admin.view.sqlInit as sqlInit

import admin.view.dict as dict
import admin.view.menu as menu
import admin.view.power as power
import admin.view.article as article
import admin.view.resources as resources
import admin.view.speech as speech
import admin.view.user as user



urlpatterns = [
    # 数据库初始化添加数据
    path('/sqlInit', sqlInit.SqlInit),

    # 用户管理
    path('/user/list', user.List),
    path('/user/add', user.Add),
    path('/user/editPwd', user.EditPwd),
    path('/user/edit', user.Edit),
    path('/user/del', user.Del),
    
    # 字典
    path('/getDict', dict.AllDict),
    path('/dict/typeList', dict.TypeList),
    path('/dict/addType', dict.AddType),
    path('/dict/delType', dict.DelType),
    path('/dict/list', dict.List),
    path('/dict/add', dict.Add),
    path('/dict/edit', dict.Edit),
    path('/dict/del', dict.Del),



    #菜单
    path('/getMenu', menu.getMenu),
    path('/menu/list', menu.List),
    path('/menu/add', menu.Add),
    path('/menu/enable', menu.Enable),
    path('/menu/edit', menu.Edit),
    path('/menu/del', menu.Del),

    #权限
    path('/getAllPower', power.getAllPower),
    path('/power/list', power.List),
    path('/power/edit', power.Edit),

    # 文章
    path('/article/list', article.List),
    path('/article/add', article.Add),
    path('/article/detail', article.Detail),
    path('/article/edit', article.Edit),
    path('/article/del', article.Del),

    # 资源
    path('/resources/list', resources.List),
    path('/resources/add', resources.Add),
    path('/resources/edit', resources.Edit),
    path('/resources/del', resources.Del),

    # 评论
    path('/speech/list', speech.List),
    path('/speech/assess', speech.Assess),
    path('/speech/del', speech.Del)
]