# scheduler 定时发送消息

import itchat
import json
from apscheduler.scheduler.blocking import BlockingScheduler

toUser = None
msg = '晚安'

def auto_send(toUser, msg):
	itchat.send(toUserName= toUser, msg = msg)

def login():
	itchat.auto_login(hotReload =True)
	friends = itchat.get_friends()
	friendsStr = json.dumps(friends)
	print(friendsStr)
	
	try:
		for item in friendsStr:
			if(item['NickName'] == '亲'):
				global toUser
				toUser = item['toUserName']
				scheduler = BlockingScheduler()
				scheduler.add_job(auto_send, 'cron', day_of_week='0-6', hour=22, minute=00, args=[msg, toUser])
				scheduler.start()
				itchat.run()
	except Exception as e:
		itchat.logout()
		print(e)

if __name__ =='__main__':
	itchat.auto_login(hotReload =True)
	friends = itchat.get_friends()
	print(friends)

