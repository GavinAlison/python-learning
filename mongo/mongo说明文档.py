# 配置分片
mongo -nodb
cluster  = new ShardingTest({'shards': 3, 'chunksize': 1})
db = (new Mongo('localhost:30999')).getDB('test')
# 启动分片
sh.enableSharding('test')

use test
db.users.ensureIndex({'username': 1})
sh.shardCollection({'test.users', {'username': 1}})
sh.status()


# 启动分片步骤
# server-config-1
mongod --configsvr --dbpath /var/lib/mongodb -f 
	/var/lib/config/mongod.conf
# server-config-2
mongod --configsvr --dbpath /var/lib/mongod -f
	/var/lib/config/mongod.conf
# server-config-3
mongo --configsvr --dbpath /var/lib/mongod -f
	/var/lib/config/mongod.conf

mongos --configdb config-1:27019,config-2:27019,config-3:27019
	-f /var/lib/mongos.conf






