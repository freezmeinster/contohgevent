# # Contoh Gevent

Kedua script ini adalah contoh penggunana Gevent sebagai green thread management. 

  - test1.py akan membuat file png dengan menggunakan bantuan Pillow sebanyak 1000 buah.
  - test2.py akan memasukan data ke postgresql lewat bantuan psycopg2 dengan ThreadedConnectionPool.
  
### Installasi
buat virtualenv dengan perintah berikut:
```
mkvirtualenv gevent
```

jnstall library pendukung dengan perintah berikut :
```
pip install -r requirements.txt
```
