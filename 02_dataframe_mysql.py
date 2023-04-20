#To create DataFrame from external databases, use sqlContext.read API with jdbc as format and provide the connect string, table name, user id and password as options.  Get into PySpark Shell and execute below commands. 

#Method1
df1 = spark.read.format('jdbc').options(url='jdbc:mysql://192.168.43.60:3306/db_simrs?user=ony&password=rahasia', dbtable='obats').load()
df1.show()

#Method2
df2 = spark.read.format('jdbc').options(url='jdbc:mysql://192.168.43.60:3306/db_simrs', dbtable='dokters', user='ony', password='rahasia').load()
df2.show()
