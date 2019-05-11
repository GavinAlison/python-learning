public class MongoTest{
	private static Mongo mongo = null;
	private static DB db = null;
	private static GridFS fs = null;
	private static oid = null;

	public MongoTest(String ip, int port, String dbName){
		try{
			mongo = new Mongo(ip, port, dbName);
			db = mongo.getDB(dbName);
			fs = new GridFS();
		}catch(Exception e){
			e.printStaticTrace();
		}
	}


	public void queryGridFs(){
		DBCursor cursor = fs.getFileList();
		while(cursor.hasNext()){
			System.out.println(cursor.next());
		}
	}


	public void saveFridFs(String localPath){
		try{
			File f = new File(localPath);
			GridFSInputFile inputFile = fs.createFile(f);
			oid = inputFile.getId().toString();
			System.out.print("save success!");
		}catch(Exceptin e){
			e.printStackTrace();
		}
	}

	pubic void readGridFs(String oid, String localPath){
		try{
			GridFsDBFile inputFile = fs.findOne(new BasicDbObject("_id": new ObjectId(oid)));
			inputFile.writeTo(localPath);
		}catch(Exception e){
			e.printStrackTrace();
		}
	}

	public void readFTPGridFS(String oid, String ip, int port, String username, String password, String destination){
		try{
			GridFsDBFile inputFile = fs.findOne(new BasicDbObject("_id", new ObjectId(oid)));
			InputStream is = inputFile.getInputStream();
			FTPClient fc = new FTPClient()
			fc.connect(ip, port);
			fc.login(username, password);
			fc.setBufferSize(1024);
			fc.setFileType(FTP.BINARY_FILE_TYPE);
			fc.enterLocalPassiveMode();
			if(fc.storeFile(new String(destination.getBytes("GBK"), "iso-8859-1"), is)){
				System.out.println("upload success!");
			}else{
				System.out.println("upload false!");
			}
			is.close();
			fc.logout();
			fc.disconnect();
		}catch(Exception e){
			e.printStatckTrace();
		}
	}


	public void closeMongo(){
		mongo.close();
	}

}