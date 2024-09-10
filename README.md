# TUGAS 2 PBP: Membuat E-Commerce 
## Welcome To LaRizzManizz!
Look at my E-Commerce --> [LaRizz Manizz](http://madeline-clairine-larizzmanizz.pbp.cs.ui.ac.id/)\
Nama: Madeline Clairine Gultom\
NPM: 2306207846\
PBP D

### Penjelasan Progress Mengerjakan Tugas 2 PBP

### 1. Membuat sebuah proyek Django baru
Membuat direktori lokal dengan nama proyek e-commerce (larizzmanizz), lalu mengaktifkan virtual environment, dan membuat proyek Django baru dengan perintah `django-admin startproject <nama_project> .`, serta mengonfigurasi proyek dengan mengisi ALLOWED_HOSTS di settings.py dan menjalani server.

### 2. Membuat aplikasi dengan nama main pada proyek
Menjalani perintah `python manage.py startapp main` yang akan membuat direktori baru dengan nama main yang akan berisi struktur awal untuk aplikasi Django yang dibuat.

### 3. Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi main
Membuat berkas urls.py pada direktori main, lalu mengisi kode pada file tersebut dengan impor path dari django.urls serta menggunakan fungsi show_main yang nantinya akan muncul ketika URL diakses.

### 4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib, yaitu name, price, dan description
Dengan mengisi berkas models.py dengan nama model Product, serta atributnya, yaitu name, price, dan description. 

### 5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML
Di sinilah fungsi show_main berada yang nantinya akan muncul ketika URL diakses, yaitu nilai-nilai dari atribut name, price, description, dan atribut tambahan lainnya.

### 6. Membuat sebuah _routing_ pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Routing URL pada aplikasi main sudah dilakukan pada (3.), sehingga sekarang dapat melakukan routing url dengan proyek, yaitu dengan membuat berkass urls.py pada direktori lokal utama dan mengimpor fungsi include serta menambahkan rute URL.

### 7. Melakukan deployment ke PWS terhadap aplikasi yang sudah dibuat
Menghubungkan dengan PWS dengan membuat project baru, serta menghubungkan melalui memasukkan url ke ALLOWED_HOSTS di settings.py agar dapat diakses dan melakukan push ke pws setelah proyek berhasil dan jika ke depannya ada _updates_.

### 8. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
