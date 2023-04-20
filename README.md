# Big-Data
Tugas - Tugas Mata Kuliah Big Data

## Chapter 4
Big Data Analytics with Spark SQL, DataFrames, and Datasets

<hr/>

**0. Persiapan**
<table border="0">
<tr>
    <th colspan="2" align="center"><b>Menjalankan Spark Daemons</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>cd /home/cloudera/spark-2.0.0-bin-hadoop2.7/sbin <br>
sudo ./start-all.sh</td>
    <td><img src=" "></td>
 </tr>
</table><br>

**1. Analitik Dengan DataFrames**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 1 : Membuat DataFrames</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/5be0ff9c4407c5e78a1dd301b06aed51cd4b7518/01_dataframes.py#L1-L4</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>mylist</td>
    <td> </td>
 </tr>
 <tr>
    <td>myschema</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 2 : Membuat DataFrame Dengan Objek List, Schema dan Default Data Types</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/5be0ff9c4407c5e78a1dd301b06aed51cd4b7518/01_dataframes.py#L6-L7</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>spark</td>
    <td> </td>
 </tr>
 <tr>
    <td>createDataFrame</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 3 : Read Data From A File, Infer Schema And Convert To Dataframe </b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/5be0ff9c4407c5e78a1dd301b06aed51cd4b7518/01_dataframes.py#L9-L10</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>parallelize</td>
    <td> </td>
 </tr>
 <tr>
    <td>toDF</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 4 : Copy File people.txt yang Terletak Di Folder Examples/Resources Ke Hdfs</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>hadoop fs -put /home/cloudera/Downloads/examples/resources/people.txt people.txt </td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>hadoop</td>
    <td> </td>
 </tr>
 <tr>
    <td>fs</td>
    <td> </td>
 </tr>
 <tr>
    <td>put</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 5 : Read Data From A File, Infer Schema And Convert To Dataframe</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/5be0ff9c4407c5e78a1dd301b06aed51cd4b7518/01_dataframes.py#L14-L21</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>pyspark.sql</td>
    <td> </td>
 </tr>
 <tr>
    <td>SQLContext</td>
    <td> </td>
 </tr>
 <tr>
    <td>createOrReplaceTempView</td>
    <td> </td>
 </tr>
 <tr>
    <td>show</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 6 : Membaca Data Dari File, Lalu Assign Schema Secara Programmatically</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/5be0ff9c4407c5e78a1dd301b06aed51cd4b7518/01_dataframes.py#L24-L38</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>textFile</td>
    <td> </td>
 </tr>
 <tr>
    <td>map</td>
    <td> </td>
 </tr>
 <tr>
    <td>lambda</td>
    <td> </td>
 </tr>
 <tr>
    <td>strip</td>
    <td> </td>
 </tr>
 <tr>
    <td>StructField</td>
    <td> </td>
 </tr>
 <tr>
    <td>StringType</td>
    <td> </td>
 </tr>
</table><br>

**2. Membuat DataFrame dari Database Eksternal**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 7 : Membuat DataFrame dari Database eksternal - Metode Pertama</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/02_dataframe_mysql.py#L3-L5</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>spark.read.format</td>
    <td> </td>
 </tr>
 <tr>
    <td>jdbc</td>
    <td> </td>
 </tr>
 <tr>
    <td>options</td>
    <td> </td>
 </tr>
 <tr>
    <td>load</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 8 : Membuat DataFrame dari Database eksternal - Metode Kedua</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/02_dataframe_mysql.py#L7-L9</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>show</td>
    <td> </td>
 </tr>
</table><br>

**3. Mengonversi DataFrames ke RDDs**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 9 : Konversi dari DataFrames ke RDD</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/03_convert_df_rdd.py#L1-L12</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>collect</td>
    <td> </td>
 </tr>
 <tr>
    <td>rdd</td>
    <td> </td>
 </tr>
 <tr>
    <td>take</td>
    <td> </td>
 </tr>
</table><br>

**4. Membuat Datasets**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 10 : Membuat Dataset dan DataFrame dari RDD Menggunakan Scala</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/04_datasets.scala#L3-L9</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>makeRDD</td>
    <td> </td>
 </tr>
 <tr>
    <td>Seq</td>
    <td> </td>
 </tr>
 <tr>
    <td>createDataset</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 11 : Datasets RDD</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/04_datasets.scala#L13-L30</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>filter</td>
    <td> </td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Soal</b></td>
    <td><b style="font-size:30px">Jawab</b></td>
 </tr>
 <tr>
    <td>Pada Kode 11 di baris akhir terjadi error, jelaskan pada laporan praktikum Anda mengapa ini bisa terjadi ?</td>
    <td> </td>
 </tr>
</table><br>

**5. Mengonversi DataFrame ke Datasets dan Sebaliknya**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 12 : Konversi ke Dataset</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/05_convert_df_ds.py#L3-L15</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>as</td>
    <td> </td>
 </tr>
 <tr>
    <td>toDF</td>
    <td> </td>
 </tr>
 <tr>
    <td>first</td>
    <td> </td>
 </tr>
</table><br>

**6. Mengakses MetadataMenggunakan Catalog**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 13 : Mengakses informasi metadata tentang tabel Hive dan UDF (Gagal karena tabel/view sample_07 tidak ditemukan)</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/06_access_metadata.py#L3-L9</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>listDatabases</td>
    <td> </td>
 </tr>
 <tr>
    <td>listTables</td>
    <td> </td>
 </tr>
 <tr>
    <td>listFunctions</td>
    <td> </td>
 </tr>
 <tr>
    <td>isCached</td>
    <td> </td>
 </tr>
 <tr>
    <td>select</td>
    <td> </td>
 </tr>
</table><br>

**7. Bekerja Dengan Berkas Teks**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 14 : Memuat Data Dari Berkas Teks</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/07_impor_txt.py#L3-L6</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>Read</td>
    <td> </td>
 </tr>
 <tr>
    <td>text</td>
    <td> </td>
 </tr>
</table><br>

**8. Bekerja dengan JSON**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Copy Dataset people.json</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>hadoop fs -put /home/cloudera/Downloads/examples/resources/people.json people.json </td>
    <td><img src=" "></td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 15 : Memuat Data Dari Berkas JSON</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/08_impor_json.py#L3-L7</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>load</td>
    <td> </td>
 </tr>
 <tr>
    <td>json</td>
    <td> </td>
 </tr>
 <tr>
    <td>format</td>
    <td> </td>
 </tr>
 <tr>
    <td>printSchema</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 16 : Menulis Data ke File JSON Lain</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/08_impor_json.py#L9-L12</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>write</td>
    <td> </td>
 </tr>
 <tr>
    <td>save</td>
    <td> </td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 17 : Menulis Data ke Format Lain</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/08_impor_json.py#L16-L17</td>
    <td><img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>parquet</td>
    <td> </td>
 </tr>
</table><br>

**9. Bekerja dengan CSV**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Unduh Dataset cars.scv</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>wget https://raw.githubusercontent.com/databricks/spark-csv/master/src/test/resources/cars.csv --no-check-certificate <br/> hadoop fs -put cars.csv</td>
    <td><img src=" "></td>
 </tr>
</table><br>

<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 18 : Membuat DataFrame Dari File .csv</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/09_impor_csv.py#L7-L11</td>
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/18.%20Membuat%20DataFrame%20Dari%20File%20.csv.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>Options</td>
    <td> </td>
 </tr>
 <tr>
    <td>inferSchema</td>
    <td> </td>
 </tr>
 <tr>
    <td>csv</td>
    <td> </td>
 </tr>
 <tr>
    <td>header</td>
    <td> </td>
 </tr>
 <tr>
    <td>codec</td>
    <td> </td>
 </tr>
</table><br>