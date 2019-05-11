//  使用java 操作 mongo , 上传文件, 下载，查看


public void saveToGridFs(String ip, String port, String path){
	MongoClient mclient = new MongoClient(ip)
	MongoDB db  = mclient.getDB('infos');
	GridFS fs = new GridFS(db);
	File file = new File(path);
	GridFSInputFile gfFile = fs.createFile(file);
	gfFile.save();
}


public void downloadFs(String ip, String port, String path){
	MongoClient mclient = new MongoClient(ip);
	MongoDB db = mclient.getDB();
	GridFS fs = new GridFS(db);
	File file = new File(path);
	FileOutputStream out = new FileOutputStream(file);
	InputStream is = fs.findOne(new BasicDBObject('filename', 'test1.txt'))
						.getInputStream();
	byte[] bytes = new byte[1024];
	while(is.read(bytes)>0){
		out.write(bytes);
	}
	out.flush();
	out.close();
	is.close();
}

public void removeFs(String ip, String port, String path){
	MongoClient mclient = new MongoClient(ip);
	MongoDB db = mclient.getDB();
	GridFS fs = new GridFS(db);
	fs.remove(path);
}

public void listFs(String ip, String port){
	MongoClient mclient = new MongoClient(ip);
	MongoDB db = mclient.getDB();
	GridFS fs = new GridFS(db);
	fs.list();
	fs.search(new BasicDBObject().put("age", 11));
	
}





