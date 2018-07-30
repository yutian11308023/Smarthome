# encoding:utf-8
from flask import Flask,request
import json
import time
import sys
import sqlite3
import os

app=Flask(__name__)
####回复文本格式##########
re={}
result={}
result["type"]="text"
result["content"]=""
re["error_code"]=0
re["error_msg"]=""
re["result"]=result
dic={'温度':'temperature','湿度':'humidity','光照':'light','二氧化碳':'co2_simulation','声音':'noise'}
class Response:
	def __init__(self,intent,nom_word):
		self.re=re
		self.intent=intent
		self.nom_word=nom_word
	def json_resp(self,intent,nom_word):
		if intent=="OPEN_AIRCONDITIONER":
			re["result"]["content"]="请稍等，正在为您打开空调"
		elif intent=="CLOSE_AIRCONDITIONER":
			re["result"]["content"]="请稍等，正在为您关闭空调"
		elif intent=="CHANGE_TEMP_UP":
			re["result"]["content"]="正在帮您升高空调温度，请稍等"
		elif intent=="CHANGE_TEMP_DOWN":
			re["result"]["content"]="正在帮您降低空调温度，请稍等"
		elif intent=="CHANGE_TEMP_TO":
			re["result"]["content"]="好的，正在为您将空调设置为该温度，请稍等"
		elif intent=="W_SPEED_UP":
			re["result"]["content"]="正在帮您提高空调风速，请稍等"
		elif intent=="W_SPEED_DOWN":
			re["result"]["content"]="正在帮您降低空调风速，请稍等"
		elif intent=="CHANGE_W_SPEED":
			re["result"]["content"]="好的，正在为您调节风速，请稍等"
		elif intent=="OPEN_SLEEP":
			re["result"]["content"]="好的，正在为您打开睡眠模式，请稍等"
		elif intent=="CLOSE_SLEEP":
			re["result"]["content"]="好的，正在为您关闭睡眠模式，请稍等"
		elif intent=="TIMER_SET":
			re["result"]["content"]="好的，正在为您设置定时关闭，请稍等"
		elif intent=="TIMER_CLOSE":
			re["result"]["content"]="好的，正在为您取消空调定时，请稍等"
		elif intent=="CHANGE_COM_MOD":
			re["result"]["content"]="好的，正在为您调节到该模式，请稍等"
		elif intent=="CHANGE_SMART_MOD":
			re["result"]["content"]="好的，正在为您调节到该模式，请稍等"
		elif intent=="ENV_INFO_QUERY":
			conn = sqlite3.connect("db.sqlite3")
			c = conn.cursor()
			############选择查询信息的最新值#########
			c.execute('SELECT '+dic[nom_word]+' FROM myhome_nodedata ORDER BY id desc')
			#########取出查询项对应字段对应数据######
			query_result=c.fetchone()[0]					
			re["result"]["content"]="您当前的室内"+nom_word+"为"+str(query_result)
		else:
			re["result"]["content"]="请求失败，请重试"
		return re
		
@app.route("/unit/callback",methods=['POST'])
def callback():
	#print(request.headers)
	#print(request.data)
	dic=json.loads(str(request.data,encoding='utf-8'))
	intent=dic["response"]["schema"]["intent"]
	nom_word=dic["response"]["schema"]["slots"][0]["normalized_word"]
	exp1=Response(intent,nom_word)
	
	if os.path.exists("db.sqlite3"):
		conn = sqlite3.connect("db.sqlite3")
		c = conn.cursor()
	else:
		conn = sqlite3.connect("db.sqlite3")
		c = conn.cursor()		
		c.execute('''CREATE TABLE myhome_commands(ID integer NOT NULL PRIMARY KEY AUTOINCREMENT,INTENT
		text NOT NULL ,SLOTS text NOT NULL)''')
		c.execute('INSERT INTO myhome_commands VALUES(1,"0","0")')				#插入意图和归一化词槽
	c.execute("UPDATE myhome_commands SET INTENT=?,SLOTS=? where ID=1",(intent,normal[nom_word]))
	conn.commit()
	conn.close()
	json_re=exp1.json_resp(intent,nom_word)#获得答复数据
	json_re=json.dumps(re)
	#print(json_re)
	return json_re
	
	
	
if __name__=='__main__':
	app.run(host='172.20.10.12',port=9999,debug=True)
	
