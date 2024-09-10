# TUGAS 2 PBP: Membuat E-Commerce 
## Welcome To LaRizzManizz!
Look at my E-Commerce --> [LaRizz Manizz](http://madeline-clairine-larizzmanizz.pbp.cs.ui.ac.id/)\
Nama: Madeline Clairine Gultom\
NPM: 2306207846\
PBP D

## Penjelasan Progress Mengerjakan Tugas 2 PBP

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
<img width="1607" alt="PBP TUGAS 2 (2)" src="https://github.com/user-attachments/assets/1f77bd80-89b4-4b39-9929-98e6f85119f1">

### 9. Jelaskan fungsi git dalam pengembangan perangkat lunak!
GIT merupakan tools yang digunakan developer dan programmer sebagai control system untuk pengembangan software. Adapun fungsi utamanya adalah untuk melacak perubahan pada kode sumber, berkolaborasi antardeveloper, dan menjaga riwayat pengembangan perangkat lunak secara sistematis.

### 10. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Framework Django sering digunakan untuk mengawali pembelajaran pengembangan perangkat lunak karena mudah dipelajari dan dipahami, Django menyediakan banyak fitur bawaan yang meudahkan untuk kepentingan pengembangan. Django juga memiliki dokumentasi yang lengkap serta komunitas yang luas sehingga jika merasa kesulitan, sudah banyak sumber yang menyediakan cara mengatasi masalah yang kita alami. Django juga menggunakan konsep pola desain MT (Model-Template-View), di mana pola ini mengajarkan untnuk memisahkan logika bisnis (model), antarmuka pengguna (template), dan logika tampilan (view). Selain itu semua, Django juga menggunakan bahasa Python, di mana bahasa tersebut merupakan high-level programming language sehingga tetap mudah dipahami dan digunakan bagi pemula.

### 11. Mengapa model pada Django disebut sebagai ORM?
ORM adalah teknik yang memungkinkan developer untuk berinteraksi dengan database menggunakan objek-objek dari bahasa pemrograman. Django ORM (Object-Relational Mapping) adalah bagian dari kerangka kerja Django yang bertanggung jawab untuk memetakan objek Python ke struktur basis data relasional. Disebut ORM karena Django menggunakan mekanisme ORM untuk menghubungkan objek-objek Python dengan database relasional.
