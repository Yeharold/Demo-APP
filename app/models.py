#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-12-13 08:46:30
# @Author  : YeHarold (1174484433@qq.com)
# @Link    : http://example.org

import sqlite3 as db

conn = db.connect('app/database/app.db',check_same_thread = False)
c = conn.cursor()


def createUser():
	'''to create table user in app database
	'''

	sql = 'create table User(\
		userID integer primary key autoincrement,\
		userName varchar(60) not null,\
	    password varchar(60) not null\
	)'

	c.execute(sql)
	conn.commit()
	conn.close()


def sigIn(userName,password):
	''' when user sigin the web site
		form userName and password will be inserted into table User
	'''

	sql = 'insert into User (userName,password) values("%s","%s")'%(userName,password)

	c.execute(sql)
	conn.commit()

	return 'sucessfully sigin'



def loginCheck(userName):
	''' to query data table User by userName
		for login validate 
	''' 

	sql = 'select userName,password from User where userName ="%s"'%(userName)

	c.execute(sql)
	res = c.fetchall()

	return res 

	


