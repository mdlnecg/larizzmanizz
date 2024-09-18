# Welcome To larizzmanizz!
## Look at my E-Commerce --> [larizzmanizz](http://madeline-clairine-larizzmanizz.pbp.cs.ui.ac.id/)
Nama: Madeline Clairine Gultom\
NPM: 2306207846\
PBP D

# TUGAS 3 PBP 2024/2025

## 1. Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
Penggunaan data delivery diperlukan dalam pengimplementasian sebuah platform karena berperan sebagai pengiriman dan distribusi data dari satu sistem atau komponen ke sistem lainnya dengan cara yang efisien. Data delivery memastikan keberlangsungan komunikasi dapat berjalan secara tepat waktu dan dengan akurasi tinggi. Dengan memiliki sistem pengiriman data yang baik, platform dapat menangani peningkatan jumlah pengguna atau volume data tanpa menurunkan performa. Oleh karena itu, dengan adanya data delivery yang baik, platform dapat terhindar dari masalah-masalah yang dapat mengganggu kelancaran pelayanan kepada pengguna.

## 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON (JavaScript Object Notation) dan XML (Extensible Markup Language) adalah representasi data yang digunakan dalam melakukan pertukaran data antaraplikasi. XML sudah ada sejak lama dan banyak digunakan di lingkungan perusahaan, sedangkan JSON lebih baru dan lebih populer di kalangan pengembang, terutama yang mencari sintaks sederhana untuk pertukaran data. JSON cenderung lebih simpel dan fleksibel dibandingkan dengan XML. JSON juga memiliki ukuran file yang lebih kecil dibanding XML, serta lebih cepat dalam proses meneruskan data. Dilihat dari strukturnya, JSON lebih simpel sehingga lebih mudah digunakan dan dibaca oleh manusia. Oleh karena itu, JSON lebih baik untuk digunakan dan memang lebih populer dibanding XML.

## 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django berfungsi untuk memeriksa validitas data, yaitu memeriksa apakah data yang dimasukkan ke dalam form sesuai valid atau tidak. Jika semua field valid sesuai dengan aturan yang ditentukan, maka method ini akan mengembalikan True. Sebaliknya, jika ada field yang tidak valid, method ini akan mengembalikan False.

Kita membutuhkan method ini tentunya untuk memvalidasi data sebelum menyimpan atau memproses data dari pengguna. Tanpa validasi, aplikasi rentan terhadap kesalahan, data yang tidak valid, atau bahkan serangan. Selain itu, Django menyediakan proses validasi secara otomatis dengan `is_valid()`, sehingga mudah diimplementasikan.

## 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` adalah token acak yang aman dan digunakan untuk mencegah serangan CSRF (Cross-Site Request Forgery), yaitu salah satu jenis kejahatan mengeksploitasi web. 

Kita membutuhkan `csrf_token` saat membuat form di Django tentunya untuk mencegah serangan CSRF itu sendiri, yaitu dengan memasukkan token csrf, server dapat memastikan bahwa hanya permintaan yang berasal dari sumber yang sah saja yang dapat diproses. Selain itu, csrf token juga dimanfaatkan untuk memverifikasi permintaan yang valid.

Jika kita tidak menambahkan `csrf_token` pada form Django, maka aplikasi Django akan rentan terhadap serangan CSRF, yaitu permintaan yang tidak sah dapat masuk begitu saja tanpa melakukan proses verifikasi terlebih dahulu. Oleh karena itu, eksploitasi oleh penyerang akan lebih mudah dilakukan ketika `csrf_token` tidak ditambahkan pada form Django karena mereka dapat mengambil kendali, seperti mengirimkan permintaan POST ke aplikasi Django korban tanpa sepengetahuan korban. Penyerang juga dapat mengirimkan permintaan palsu bersamaan dengan cookie autentikasi yang sah.

## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step untuk Tugas 3!
1. Membuat `base.html` sebagai kerangka umum untuk halaman web lainnya, serta menambahkan `% extends 'base.html' %` pada tiap file .html.
2. Megubah integer menjadi UUID sebagai primary key untuk mengutamakan sisi keamanan aplikasi.
3. Membuat form input data, yaitu `forms.py` yang berisi kode sebagai berikut.
```
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'rating']
```
Selain itu, perlu untuk mengubah isi `views.py`, `urls.py`, dan juga membuat berkas HTML baru, yaitu `create_product.html`.
4. Menambahkan empat fungsi views baru pada `views.py` untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
```
def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
```

## 6. Mengakses keempat URL di poin 2 menggunakan Postman
* Format XML
![Screenshot (616)(1)(1)](https://github.com/user-attachments/assets/135c2e53-1911-4828-be0c-d0b8352adce4)

* Format JSON
![Screenshot (618)(1)(1)](https://github.com/user-attachments/assets/4aae34ab-7149-4dad-9bc7-58108c0677b3)

* Format XML by ID
![Screenshot (617)(1)(1)](https://github.com/user-attachments/assets/8c4352e5-0757-44bf-851b-405cb8e3f2f1)

* Format JSON by ID
![Screenshot (619)(1)(1)](https://github.com/user-attachments/assets/36c3d412-0d55-4ef8-88ec-8ccc1cf8b248)

---

# TUGAS 2 PBP 2024/2025

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
