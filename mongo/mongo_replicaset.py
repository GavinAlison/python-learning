# 开启shell
# 
mongo --nodb
# 创建一个包含三个服务器的副本集, 1 primary ndoe, 2 slave node
replicaSet = new ReplSetTest('nodes', 3)
# 启动3个mongod进程
replicaSet.startSet()
replicaSet.initiate()


conn1 = new Mongo('localhost:31000')
primaryDB = conn1.getDB('test')
primaryDB.isMaster()
for(i=0; i< 10000; i++){primaryDB.coll.insert({count: i})}
primaryDB.coll.count()


# 另一个shell
conn2 = new Mongo('localhost:31001')
secondDB = conn2.getDB('test')
secondDB.coll.find()
# 设置从备份节点读取数据没问题
secondDB.setSlaveOK()
secondDB.coll.find()
# 备份节点不可执行写操作
# 自动故障转移
# primary node shell
primaryDB.addCommand({'shutdown', 1})
# second node shell
secondDB.isMaster()











