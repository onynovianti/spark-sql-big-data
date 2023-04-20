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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/0.1.%20Menjalankan%20Spark%20Daemons.png"></td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/kode%201.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>mylist</td>
    <td>mylist pada kode diatas merujuk pada nama variabel</td>
 </tr>
 <tr>
    <td>myschema</td>
    <td>sama seperti mylist, myschema juga merupakan nama variabel</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/kode%202.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>spark</td>
    <td>Merujuk pada builder spark dengan SparkSession</td>
 </tr>
 <tr>
    <td>createDataFrame</td>
    <td>Membuat data frame manual dan mengambil objek RDD sebagai argumennya</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/kode%203.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>parallelize</td>
    <td>Membuat RDD dari list collection</td>
 </tr>
 <tr>
    <td>toDF</td>
    <td>Membuat data frame dari RDD yang sudah ada</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/4.%20Copy%20File%20people.txt.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>hadoop</td>
    <td>Hadoop Distributed File System (HDFS)</td>
 </tr>
 <tr>
    <td>fs</td>
    <td>Command line untuk memanipulasi file pada HDFS</td>
 </tr>
 <tr>
    <td>put</td>
    <td>Menyalin file dari berkas lokal ke HDFS</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/5.%20Read%20Data%20From%20A%20File%2C%20Infer%20Schema%20And%20Convert%20To%20Dataframe.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>pyspark.sql</td>
    <td>Modul python yang digunakan untuk bekerja dengan Spark SQL</td>
 </tr>
 <tr>
    <td>SQLContext</td>
    <td>Membuat atau mengelola struktur data Spark SQL, seperti DataFrames dan tabel</td>
 </tr>
 <tr>
    <td>createOrReplaceTempView</td>
    <td>Membuat atau mengganti temporary view dari DataFrame</td>
 </tr>
 <tr>
    <td>show</td>
    <td>Menampilkan hasil dari perintah sebelumnya (hasil dari DataFrame) dalam format tabel</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/6.%20Membaca%20Data%20Dari%20File%2C%20Lalu%20Assign%20Schema%20Secara%20Programmatically.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>textFile</td>
    <td>Membaca teks sebagai RDD</td>
 </tr>
 <tr>
    <td>map</td>
    <td>Menerapkan sebuah fungsi pada setiap elemen dan menghasilkan RDD baru</td>
 </tr>
 <tr>
    <td>lambda</td>
    <td>Fungsi tanpa menggunakan kata "def", biasanya dikombinasikan untuk digunakan pada argumen fungsi </td>
 </tr>
 <tr>
    <td>strip</td>
    <td>Menghapus karakter whitespace pada awal dan akhir string</td>
 </tr>
 <tr>
    <td>StructField</td>
    <td>Membuat objek kolom dengan memiliki 3 parameter, yaitu : nama kolom, tipe data, dan opsi tambahan</td>
 </tr>
 <tr>
    <td>StringType</td>
    <td>Mendefinisikan tipe data kolom sebagai String dalam DataFrame</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/7.%20Membuat%20DataFrame%20dari%20Database%20eksternal%20-%20Metode%20Pertama.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>spark.read.format</td>
    <td>Membaca data dari berbagai sumber data seperti json, dan csv, dan lain-lain</td>
 </tr>
 <tr>
    <td>jdbc</td>
    <td>Sumber data berasal dari jdbc (Java Database Connectivity)</td>
 </tr>
 <tr>
    <td>options</td>
    <td>Opsi konfigurasi untuk mengkoneksikan ke JDBC</td>
 </tr>
 <tr>
    <td>load</td>
    <td>Membaca data ke dalam DataFrame</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/8.%20Membuat%20DataFrame%20dari%20Database%20eksternal%20-%20Metode%20Kedua.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>show</td>
    <td>Menampilkan konten, pada kode diatas yaitu menampilkan isi DataFrame df2</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/9.%20Konversi%20dari%20DataFrames%20ke%20RDD.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>collect</td>
    <td>Mengumpulkan baris data dan mereturn list</td>
 </tr>
 <tr>
    <td>rdd</td>
    <td>Pada kode diatas rdd digunakan untuk merubah DataFrame ke dalam RDD</td>
 </tr>
 <tr>
    <td>take</td>
    <td>Mengambil baris dalam RDD. take(2) berarti mengambil 2 baris pertama dan mereturn dalam bentuk list</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/10.%20Membuat%20Dataset%20dan%20DataFrame%20dari%20RDD%20Menggunakan%20Scala.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>makeRDD</td>
    <td>Membuat RDD dari list atau array</td>
 </tr>
 <tr>
    <td>Seq</td>
    <td>Tipe data collection atau urutan dalam Scala</td>
 </tr>
 <tr>
    <td>createDataset</td>
    <td>Membuat dataset baru</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/11.%20Datasets%20RDD.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>filter</td>
    <td>Melakukan filter pada sebuah Dataset dengan kondisi yang diberikan</td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Soal</b></td>
    <td><b style="font-size:30px">Jawab</b></td>
 </tr>
 <tr>
    <td>Pada Kode 11 di baris akhir terjadi error, jelaskan pada laporan praktikum Anda mengapa ini bisa terjadi ?</td>
    <td>Hal tersebut terjadi karena pada struktur Dept yang sudah dilakukan pada kode sebelumnya, tidak menunjukkan adanya kolom bernama dept_location. Yang ada hanya kolom dept_id dan dept_name</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/12.%20Konversi%20ke%20Dataset.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>as</td>
    <td>Memastikan kolom-kolom dalam DataFrame diubah menjadi atribut dari kelas case class Dept</td>
 </tr>
 <tr>
    <td>toDF</td>
    <td>Mengonversi RDD menjadi DataFrame</td>
 </tr>
 <tr>
    <td>first</td>
    <td>Mengembalikan elemen pertama RDD atau DataFrame</td>
 </tr>
</table><br>

**6. Mengakses MetadataMenggunakan Catalog**
<table border="0">
 <tr>
    <th colspan="2" align="center"><b>Kode 13 : Mengakses informasi metadata tentang tabel Hive dan UDF <br>(Gagal karena tabel/view sample_07 tidak ditemukan)</b></th>
 </tr>
 <tr>
    <td><b style="font-size:30px">Code</b></td>
    <td><b style="font-size:30px">Output</b></td>
 </tr>
 <tr>
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/06_access_metadata.py#L3-L9</td>
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/13.%20Mengakses%20informasi%20metadata%20tentang%20tabel%20Hive%20dan%20UDF.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>listDatabases</td>
    <td>Mendapatkan daftar dari semua database yang tersedia pada cluster Spark</td>
 </tr>
 <tr>
    <td>listTables</td>
    <td>Mendapatkan daftar dari semua table yang tersedia pada cluster Spark</td>
 </tr>
 <tr>
    <td>listFunctions</td>
    <td>Mendapatkan daftar dari semua function yang tersedia pada cluster Spark</td>
 </tr>
 <tr>
    <td>isCached</td>
    <td>Mengecek apakah tabel sudah di cache atau belum, nilai kembalian berupa true/false</td>
 </tr>
 <tr>
    <td>select</td>
    <td>Memilih kolom, pada contoh diatas yang dipilih adalah kolom name</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/14.%20Memuat%20Data%20Dari%20Berkas%20Teks.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>Read</td>
    <td>Membaca data dari sumber eksternal</td>
 </tr>
 <tr>
    <td>text</td>
    <td>Format teks dan dimuat menjadi RDD</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/0.2.%20Copy%20Dataset%20people.json.png"></td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/15.%20Memuat%20Data%20Dari%20Berkas%20JSON.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>load</td>
    <td>Membaca data ke dalam DataFrame</td>
 </tr>
 <tr>
    <td>json</td>
    <td>Format json dimuat dalam DataFrame</td>
 </tr>
 <tr>
    <td>format</td>
    <td>Membaca file dalam format tertentu seperti pada parameter atau argumen</td>
 </tr>
 <tr>
    <td>printSchema</td>
    <td>Menampilkan schema DataFrame</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/16.%20Menulis%20Data%20ke%20File%20JSON%20Lain.png"></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>write</td>
    <td>Menulis DataFrame ke format JSON</td>
 </tr>
 <tr>
    <td>save</td>
    <td>Menulis DataFrame ke dalam format tertentu</td>
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
    <td>https://github.com/onynovianti/spark-sql-big-data/blob/b130c4f9f24a422157ab882c8922a95564620841/00_images/17.%20Menulis%20Data%20ke%20Format%20Lain.png<img src=" "></td>
 </tr>
 <tr>
    <td><b style="font-size:30px">Kode</b></td>
    <td><b style="font-size:30px">Keterangan</b></td>
 </tr>
 <tr>
    <td>parquet</td>
    <td>Format file untuk menyimpan data terstruktur di hdfs</td>
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
    <td><img src="https://github.com/onynovianti/spark-sql-big-data/blob/master/00_images/0.3.%20Unduh%20Dataset%20cars.scv.png"></td>
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
    <td>Opsi konfigurasi</td>
 </tr>
 <tr>
    <td>inferSchema</td>
    <td>Menentukan tipe data dari setiap kolom secara otomatis</td>
 </tr>
 <tr>
    <td>csv</td>
    <td>Membaca file csv dan mereturn sebagai DataFrame</td>
 </tr>
 <tr>
    <td>header</td>
    <td>Argumen untuk membaca file dengan header</td>
 </tr>
 <tr>
    <td>codec</td>
    <td>Mengompresi data yang disimpan di HDFS</td>
 </tr>
</table><br>