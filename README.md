# # Contoh Gevent

Kedua script ini adalah contoh penggunan Gevent sebagai green thread management. 

  - test1.py akan membuat file png dengan menggunakan bantuan Pillow sebanyak 1000 buah.
  - test2.py akan memasukan data ke postgresql lewat bantuan psycopg2 dengan ThreadedConnectionPool.
  
### Installasi
buat virtualenv dengan perintah berikut:
```
mkvirtualenv gevent
```

install library pendukung dengan perintah berikut :
```
pip install -r requirements.txt
```

Buat direktori "hasil" sebagai tempat menampung hasil png dengan perintah
```
mkdir hasil
```

### Penggunaan

Untuk membuat file png jalankan script
```
python test1.py
```

Untuk mencoba insert ke postgresql jalankan script
```
python test2.py
```
