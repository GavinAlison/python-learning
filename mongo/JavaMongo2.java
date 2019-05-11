public class MongoDbJDBC2{
	public static void main(String[] args){
		String ip = "127.0.0.1";
		int port = 27017;
		String username = "admin";
		String databaseName = "test";
		String password =  "admin";
		try{
			ServerAddress  serverAddress = new ServerAddress(ip, port);
			List<ServerAddress> addrs = new ArrayList<ServerAddress>();
			addrs.add(serverAddress);

			MongoCredential credential = MongoCredential.createScramSha1Credential(username, databaseName, 
					password.toCharArray());
			List<MongoCredential> credentialList = new ArrayList<MongoCredential>();
			credentialList.add(credential);


			MongoClient mongoClient  = new MongoClient(addrs, credentialList);
			MongoDatabase mongoDatabase  = mongoClient.getDatabase(databaseName);
			mongoDatabase.createCollection("infos");
			System.out.print("create collection is success!")
		}catch(Exception e){
			System.out.println(e.getMessage());
		}
	}

	






}