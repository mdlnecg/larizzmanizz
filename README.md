# Welcome To larizzmanizz!
## [🍪 larizzmanizz 🍪](http://madeline-clairine-larizzmanizz.pbp.cs.ui.ac.id/)
Nama: Madeline Clairine Gultom\
NPM: 2306207846\
PBP D

## TUGAS 5 PBP 2024/2025

### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Dalam CSS, terdapar urutan prioritas untuk menentukan gaya mana yang perlu diterapkan. Urutan prirotias tersebut sebagai berikut.
* **Inline styles**, yaitu gaya yang ditulis lansung di elemen HTML dengan menggunakan atribut `style` menempati prioritas tertinggi.
* **ID Selectors**, yaitu selektor ID yang biasa digunakan seperti `#header`.
* **Class, pseudo-class, dan attribute selectors**, yaitu selector class (`.lexend-body`), pseudo-class (`:hover`), dan attribut selector (`[type="text"]`).
* **Type selectors dan pseudo-elements**, selector elemen HTML seperti `p, div`, dan pseudo-element seperti `::after`.
* **Universal selector, combinators, dan inheritance**, selector universal seperti `*` dan combinator seperti `+, >, ~`.

### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design penting dalam pengembangan aplikasi web karena dengan adanya responsive design akan memberikan pengalaman pengguna yang optimal terlepas dari perangkat apapun yang sedang digunakan. Jika pengguna merasa nyaman, maka akan terjadi peningkatan akses pada aplikasi web yang dikembangkan. Dengan menggunakan responsive design juga akan menghemat biaya dan waktu, dibanding membuat versi yang terpisah untuk tiap perangkat. **Adapun contoh aplikasi yang sudah responsif, yaitu X (dulunya adalah Twitter) dan webtoon**, karena kedua aplikasi tersebut dapat digunakan dengan nyaman dan baik di berbagai perangkat. **Aplikasi yang belum responsif salah satunya adalah TIX ID**, karena ketika ingin menggunakan di table atau iPad, tampilannya akan sama dengan di ponsel, tentunya lebih nyaman menggunakan aplikasi web yang sudah responsif. Tampilan TIX ID pada iPad sebagai berikut.
![WhatsApp Image 2024-10-02 at 11 46 19_3cd8f86b](https://github.com/user-attachments/assets/52343eb2-832d-43ff-823c-fe079d8ab298)

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
* **Margin**: Ruang di luar batas elemen yang berfungsi untuk jarak antara elemen dan elemen lainnya di sekitarannya, sifatnya transparan dan sering digunakan untuk mengatur jarak antarelemen dalam tata letak. Cara implementasinya sebagai berikut.
```css
.element {
    margin: 20px; /* Mengatur margin semua sisi menjadi 20px */
}
```
* **Border**: Garis yang mengelilingi elemen dan dapat memiliki warna, ketebalan, dan gaya. Biasa digunakan untuk memberikan batasan visual pada elemen, seperti kotak teks atau tombol. Cara implementasinya sebagai berikut.
```css
.element {
    border: 2px solid black; /* Mengatur border dengan ketebalan 2px, tipe solid, dan warna hitam */
}
```
* **Padding**: Ruang di dalam batas elemen antara konten dan border untuk membuat jarak antara konten elemen dengan tepi elemen itu sendiri. Biasa digunakan agar konten lebih mudah dibaca dan terlihat lebih rapih. Cara implementasinya sebagai berikut.
```css
.element {
    padding: 15px; /* Mengatur padding semua sisi menjadi 15px */
}
```

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
* **Flexbos (Flexible Box Layout)**: dirancang untuk tata letak suatu dimensi, yaitu mengatur elemen secara horizontal atau vertikal di dalam sebuah *flexbox*. Flexbox memudahkan pengaturan elemen dalam satu arah dan memungkinkan elemen di dalamnya untuk diperluas atau menyusut sesuai ruang yang tersedia. Flexbox sangat berguna untuk mengatur elemen seperti menu navigasi, toolbar, kartu produk, atau tata letak yang bergantung pada elemen berukuran dinamis. Contoh penerapannya sebagai berikut.
```html
<div class="flex-container">
  <div class="box">Item 1</div>
  <div class="box">Item 2</div>
</div>
```
```css
.flex-container {
  display: flex;
  justify-content: space-between; /* Mengatur item agar tersebar merata */
  align-items: center; /* Menyelaraskan item di tengah secara vertikal */
}

.box {
  flex-grow: 1; /* Item dapat tumbuh untuk mengisi ruang yang tersedia */
  padding: 10px;
  background-color: lightblue;
}
```
* **Grid Layout**: dirancang untuk tata letak dua dimensi yang memungkinkan pengaturan elemen dalam baris dan kolom secara bersamaan karena grid layout memungkinkan pembagian area konten menjadi sel, sehingga kita dapat mengatur elemen untuk memenuhi beberapa kolom atau baris. Cocok untuk mengatur tata letak yang lebih kompleks, seperti membuat tata letak halaman web secara keseluruhan. Contoh penerapannya sebagai berikut.
```html
<div class="grid-container">
  <div class="header">Header</div>
  <div class="menu">Menu</div>
  <div class="content">Content</div>
  <div class="footer">Footer</div>
</div>
```
```css
.grid-container {
  display: grid;
  grid-template-columns: 1fr 3fr; /* 2 kolom, satu kecil dan satu lebih besar */
  grid-template-rows: auto auto auto; /* 3 baris */
  grid-template-areas:
    "header header"
    "menu content"
    "footer footer"; /* Penempatan item pada grid area */
}

.header { grid-area: header; }
.menu { grid-area: menu; }
.content { grid-area: content; }
.footer { grid-area: footer; }
```

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
1. Implementasi fungsi untuk menghapus dan mengedit product
Membuat fungsi edit_product dan delete_product pada views.py kemudian routing ke urls.py serta membuat edit_product.html karena mengedit suatu produk membutuhkan halaman baru. 
Fungsi edit_product dan delete_product pada views.py
```python
...
def edit_product(request, id):
    # Mendapatkan product entry berdasarkan id
    product = Product.objects.get(pk = id)

    # Set product entry sebagai instance dari form
    form = ProductEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_model'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Mendapatkan product berdasarkan id
    product = Product.objects.get(pk = id)

    # Hapus product
    product.delete()

    # Kembali ke halaman awal 
    return HttpResponseRedirect(reverse('main:show_model'))
```

Routing ke urls.py 
```python
...
from main.views import ..., edit_product, delete_product
...
urlpatterns = [
    ...,
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product')
]
```

Isi dari edit_product.html
```html
{% extends 'base.html' %}
{% load static %}
{% block meta %}
<title>Edit Product</title>
{% endblock meta %}

{% block content %}
{% include 'navbar.html' %}
<div class="flex flex-col min-h-screen bg-[#FFF1DB]">
  <div class="container mx-auto px-4 py-8 mt-16 max-w-xl">
    <h1 class="text-3xl font-bold text-center mb-8 text-black">Edit Product Entry</h1>
  
    <div class="bg-[#FFF8F3] rounded-lg p-6 form-style">
      <form method="POST" class="space-y-6">
          {% csrf_token %}
          {% for field in form %}
              <div class="flex flex-col">
                  <label for="{{ field.id_for_label }}" class="mb-2 font-semibold text-gray-700">
                      {{ field.label }}
                  </label>
                  <div class="w-full">
                      {{ field }}
                  </div>
                  {% if field.help_text %}
                      <p class="mt-1 text-sm text-gray-500">{{ field.help_text }}</p>
                  {% endif %}
                  {% for error in field.errors %}
                      <p class="mt-1 text-sm text-red-600">{{ error }}</p>
                  {% endfor %}
              </div>
          {% endfor %}
          <div class="flex justify-center mt-6">
              <button type="submit" class="bg-[#B5C18E] text-white font-semibold px-6 py-3 rounded-lg hover:bg-[#809671] transition duration-300 ease-in-out w-full">
                  Edit Product Entry
              </button>
          </div>
      </form>
  </div>
  </div>
</div>
{% endblock %}
```

2. Kustomisasi desain pada template HTML yang telah dibuat pada tugas-tugas sebelumnya menggunakan CSS framework, yaitu Tailwind
    1. Halaman login
![Screenshot 2024-10-02 114303](https://github.com/user-attachments/assets/cb5726b2-ec6f-4c3c-87c3-3c56a2422527)

    2. Halaman register
![Screenshot 2024-10-02 114419](https://github.com/user-attachments/assets/d1e3f1f2-f673-4ea2-8de8-c6d0d528eb98)

    3. Halaman daftar produk
        * jika belum ada produk
![Screenshot 2024-10-02 114438](https://github.com/user-attachments/assets/e8a0948b-4be6-476a-b83e-f254f4d9e66d)
        * ⁠jika sudah ada produk
![Screenshot 2024-10-02 114528](https://github.com/user-attachments/assets/53a9817c-50d4-4304-80ba-b98537360547)

    4. Halaman menambahn produk
![Screenshot 2024-10-02 114505](https://github.com/user-attachments/assets/067a9c27-dfed-401a-8db2-1fea53710d9b)

    5. Halaman mengedit produk
![Screenshot 2024-10-02 114539](https://github.com/user-attachments/assets/273c3fd7-b11f-4cf3-8b24-78dae3ae0c64)

    6. Navigation bar
        * versi mobile
![WhatsApp Image 2024-10-02 at 11 50 48_c0c2d960](https://github.com/user-attachments/assets/3aa5a7da-7d01-4305-89b7-85de7fad5df2)

        * ⁠versi desktop
![Screenshot 2024-10-02 115123](https://github.com/user-attachments/assets/fe13a408-5221-48b1-ae54-834df6ff920d)

---
# Archive Tugas

## TUGAS 4 PBP 2024/2025

### 1. Apa perbedaan antara `HttpResponseRedirect()` dan `redirect()`?
Perbedaan yang paling jelas terletak pada argumennya, di mana `HttpResponseRedirect()` mewajibkan argumennya berupa URL Lengkap, contohnya sebagai berikut.
```python
def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
```
Sedangkan, untuk `redirect()`, argumennya dapat berupa model, view, atau url, serta `redirect()` ini akan mengembalikan `HttpResponseRedirect` jika default `permanent=False`. Contoh penggunaannya sebagai berikut.
```python
def create_product_form(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_model')
    ...
```
Tujuan dari kedua fungsi ini sama, yaitu digunakan untuk mengarahkan pengguna ke URL lain yang pada umumnya menggunakan status kode 302 (Found). Namun, `redirect()` lebih fleksibel dan merupakan _shortcut_ dari `HttpResponseRedirect()`.

### 2. Jelaskan cara kerja penghubungan model `Product` dengan `User`!
Kita dapat menghubungkan model `Product` dengan `User` dengan menggunakan `ForeignKey`, yang bertujuan untuk mengaitkan tiap satu pengguna dengan produk yang terdefinisi, sehingga satu pengguna dapat memiliki banyak produk dan setiap produk dimiliki oleh satu pengguna. Berikut contoh implementasi penghubungannya.
```python
...
from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
`ForeignKey` tersebut menghubungkan model `Product` ke `User` dan `on_delete=models.CASCADE` bertujuan agar ketika pengguna dihapus, maka setiap model yang terikat dengan user tersebut juga akan ikut terhapus.

### 3. Apa perbedaan antara _authentication_ dan _authorization_, apakah yang dilakukan saat pengguna login?
Keduanya sama-sama penting dalam hal sekuriti untuk menjaga sistem dan informasi pengguna. _Authentication_ adalah proses untuk memverifikasi pengguna sebelum diberi izin dan hak dalam menggunakan suatu website, sedangkan _authorization_ merujuk kepada penentuan level akses yang dapat diberikan kepada pengguna. Proses _authentication_ biasanya terdapat pada halaman awal, seperti login yang meminta username dan password, sedangkan _authorization_ pada saat user sudah berhasil masuk, maka akan terlihat izin yang diberikan kepada pengguna, misalnya jika pada sebuah web terdapat admin dan user biasa, maka user biasa tidak dapat mengakses halaman yang direstriksi khusus untuk admin. Pengimplementasian pada Django dapat dilakukan sebagai berikut.
```python
...
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

@login_required(login_url='/login')

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_model"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)
   ...
   ```
_Authenticate_ dengan import `from django.contrib.auth import authenticate, login, logout`, sedangkan _authorization_ dengan dekorator `@login_required(login_url='/login')`.

### 4. Bagaimana Django mengingat pengguna yang telah login? Jelaskan kegunaan lain dari cookies dan apakah semua cookies aman digunakan!
Django menggunakan _session_ dan disimpan dalam _cookies_, Django akan membuat _session ID_ setiap kali pengguna berhasil login, lalu ketika pengguna mengirim request, Django akan membaca _session ID_ dari _cookie_ tersebut dan mencocokkannya dengan data sesi yang telah disimpan di server atau database. Dengan begitu, pengguna tidak perlu login ulang kembali setiap mengirim request. Kegunaan lain dari _cookies_ adalah melacak preferensi pengguna, menyimpan keranjang belanja (pada e-commerce), melacak aktivitas pengguna, juga untuk menampilkan iklan sesuai dengan riwayat browsing pengguna (biasa disebut _third-party cookies_). Tidak semua cookies aman digunakan, terdapat beberapa kemungkinan serangan pada saat menggunakan _cookies_, seperti session hijacking (menyamar sebagai pengguna yang sah) dan CSRF (Cross-Site Request Forgery). Namun, Django juga tentunya sudah menyiapkan berbagai langkah keamanan, seperti penggunaan cookies yang aman (HttpOnly, Secure, dan SameSite), serta perlindungan CSRF.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara _step-by-step_
#### 1. Mengimplementasikan fungsi registrasi, login, dan logout
Membuat fungsi register ke `views.py`yang berguna untuk menghasilkan formulir registrasi dan menghasilkan akun pengguna ketika data disubmit dari form. Lalu, membuat `register.html` untuk menjadi halaman ketika user ingin mengisi formulir registrasi. Kemudian, membuat fungsi login_user untuk ke `views.py` untuk memproses login. Selanjutnya, membuat `login.html` yang akan menjadi tampilan pada saat melakukan login. Untuk logout, mirip dengan proses sebelumnya, tetapi tidak perlu membuat `.html`-nya. Semua fungsi yang telah dibuat, diimpor ke `urls.py` dan memasukkan path url ke dalam _urlpatterns_.

#### 2. Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
Setelah fungsi-fungsi di nomor (1) sudah berjalan dengan baik, saya melakukan _register_ untuk dua akun berbeda, lalu menambahkan tiga produk berbeda untuk tiap _user_.

#### 3. Menghubungkan model Product dengan User
Mengimpor _User_ ke `models.py`, lalu menambahkan atribut baru pada `Product` di `models.py`, yaitu sebagai berikut.
```python
...
from django.contrib.auth.models import User

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ...
```
Lalu, membaharui `create_product_form` yang ada di `views.py` agar mencegah tidak langsung menyimpan objek dan melakukan otorisasi agar memastikan objek dimiliki oleh pengguna yang sedang _login_ saja. Selain itu, memperbarui `show_model` agar dapat menampilkan objek yang terasosiasikan dengan pengguna yang sedang login. Selain itu, perlu juga untuk memperbarui `settings.py`, yaitu mengimpor os dan mengatur `DEBUG = no PRODUCTION`.

#### 4. Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi
Mengimpor HttpResponseRedirect, reverse, dan datetime pada `views.py`. Memodifikasi fungsi `login_user` dengan menambahkan cookie yang bernama `last_login` untuk melihat riwayat loginnya. Perlu juga untuk menambahkan potongan kode last_login pada `show_model` juga `.delete_cookie` pada fungsi `logout_user`. Setelah itu, tambahkan potongan kode pada `main.html` agar dapat menampilkan data last login.

---
## TUGAS 3 PBP 2024/2025

### 1. Jelaskan mengapa kita memerlukan _data delivery_ dalam pengimplementasian sebuah platform?
Penggunaan data delivery diperlukan dalam pengimplementasian sebuah platform karena berperan sebagai pengiriman dan distribusi data dari satu sistem atau komponen ke sistem lainnya dengan cara yang efisien. Data delivery memastikan keberlangsungan komunikasi dapat berjalan secara tepat waktu dan dengan akurasi tinggi. Dengan memiliki sistem pengiriman data yang baik, platform dapat menangani peningkatan jumlah pengguna atau volume data tanpa menurunkan performa. Oleh karena itu, dengan adanya data delivery yang baik, platform dapat terhindar dari masalah-masalah yang dapat mengganggu kelancaran pelayanan kepada pengguna.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
JSON (JavaScript Object Notation) dan XML (Extensible Markup Language) adalah representasi data yang digunakan dalam melakukan pertukaran data antaraplikasi. XML sudah ada sejak lama dan banyak digunakan di lingkungan perusahaan, sedangkan JSON lebih baru dan lebih populer di kalangan pengembang, terutama yang mencari sintaks sederhana untuk pertukaran data. JSON cenderung lebih simpel dan fleksibel dibandingkan dengan XML. JSON juga memiliki ukuran file yang lebih kecil dibanding XML, serta lebih cepat dalam proses meneruskan data. Dilihat dari strukturnya, JSON lebih simpel sehingga lebih mudah digunakan dan dibaca oleh manusia. Oleh karena itu, JSON lebih baik untuk digunakan dan memang lebih populer dibanding XML.

### 3. Jelaskan fungsi dari method `is_valid()` pada form Django dan mengapa kita membutuhkan method tersebut?
Method `is_valid()` pada form Django berfungsi untuk memeriksa validitas data, yaitu memeriksa apakah data yang dimasukkan ke dalam form sesuai valid atau tidak. Jika semua field valid sesuai dengan aturan yang ditentukan, maka method ini akan mengembalikan True. Sebaliknya, jika ada field yang tidak valid, method ini akan mengembalikan False.

Kita membutuhkan method ini tentunya untuk memvalidasi data sebelum menyimpan atau memproses data dari pengguna. Tanpa validasi, aplikasi rentan terhadap kesalahan, data yang tidak valid, atau bahkan serangan. Selain itu, Django menyediakan proses validasi secara otomatis dengan `is_valid()`, sehingga mudah diimplementasikan.

### 4. Mengapa kita membutuhkan `csrf_token` saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan `csrf_token` pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
`csrf_token` adalah token acak yang aman dan digunakan untuk mencegah serangan CSRF (Cross-Site Request Forgery), yaitu salah satu jenis kejahatan mengeksploitasi web. 

Kita membutuhkan `csrf_token` saat membuat form di Django tentunya untuk mencegah serangan CSRF itu sendiri, yaitu dengan memasukkan token csrf, server dapat memastikan bahwa hanya permintaan yang berasal dari sumber yang sah saja yang dapat diproses. Selain itu, csrf token juga dimanfaatkan untuk memverifikasi permintaan yang valid.

Jika kita tidak menambahkan `csrf_token` pada form Django, maka aplikasi Django akan rentan terhadap serangan CSRF, yaitu permintaan yang tidak sah dapat masuk begitu saja tanpa melakukan proses verifikasi terlebih dahulu. Oleh karena itu, eksploitasi oleh penyerang akan lebih mudah dilakukan ketika `csrf_token` tidak ditambahkan pada form Django karena mereka dapat mengambil kendali, seperti mengirimkan permintaan POST ke aplikasi Django korban tanpa sepengetahuan korban. Penyerang juga dapat mengirimkan permintaan palsu bersamaan dengan cookie autentikasi yang sah.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step untuk Tugas 3!
1. Membuat `base.html` sebagai kerangka umum untuk halaman web lainnya, serta menambahkan `% extends 'base.html' %` pada tiap file .html.
2. Megubah integer menjadi UUID sebagai primary key untuk mengutamakan sisi keamanan aplikasi.
3. Membuat form input data, yaitu `forms.py` yang berisi kode sebagai berikut.
```python
from django.forms import ModelForm
from main.models import Product

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description', 'rating']
```
Selain itu, perlu untuk mengubah isi `views.py`, `urls.py`, dan juga membuat berkas HTML baru, yaitu `create_product.html`.\
4. Menambahkan empat fungsi views baru pada `views.py` untuk melihat objek yang sudah ditambahkan dalam format XML, JSON, XML by ID, dan JSON by ID.
```python
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

### 6. Mengakses keempat URL di poin 2 menggunakan Postman
* Format XML
![Screenshot 2024-09-18 112248](https://github.com/user-attachments/assets/089bb5ea-70e0-465e-a411-c3fc15cfbd3b)

* Format JSON
![Screenshot 2024-09-18 112341](https://github.com/user-attachments/assets/2a723a77-7018-4f74-9677-2a5ae72b9f06)

* Format XML by ID
![Screenshot 2024-09-18 112311](https://github.com/user-attachments/assets/6ccb3f48-75a6-4553-8643-45bfc6d2758f)

* Format JSON by ID
![Screenshot 2024-09-18 112401](https://github.com/user-attachments/assets/9a9ae767-e4bd-44b7-bdf7-ac0fae0b9870)

---
## TUGAS 2 PBP 2024/2025

### 1. Membuat sebuah proyek Django baru
Membuat direktori lokal dengan nama proyek e-commerce (larizzmanizz), lalu mengaktifkan virtual environment, dan membuat proyek Django baru dengan perintah `django-admin startproject <nama_project> .`, serta mengonfigurasi proyek dengan mengisi ALLOWED_HOSTS di settings.py dan menjalani server.

### 2. Membuat aplikasi dengan nama main pada proyek
Menjalani perintah `python manage.py startapp main` yang akan membuat direktori baru dengan nama main yang akan berisi struktur awal untuk aplikasi Django yang dibuat.

### 3. Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi main
Membuat berkas urls.py pada direktori main, lalu mengisi kode pada file tersebut dengan impor path dari django.urls serta menggunakan fungsi show_model yang nantinya akan muncul ketika URL diakses.

### 4. Membuat model pada aplikasi main dengan nama Product dan memiliki atribut wajib, yaitu name, price, dan description
Dengan mengisi berkas models.py dengan nama model Product, serta atributnya, yaitu name, price, dan description. 

### 5. Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML
Di sinilah fungsi show_model berada yang nantinya akan muncul ketika URL diakses, yaitu nilai-nilai dari atribut name, price, description, dan atribut tambahan lainnya.

### 6. Membuat sebuah _routing_ pada urls.py aplikasi main untuk memetakan fungsi yang telah dibuat pada views.py
Routing URL pada aplikasi main sudah dilakukan pada (3.), sehingga sekarang dapat melakukan routing url dengan proyek, yaitu dengan membuat berkas urls.py pada direktori lokal utama dan mengimpor fungsi include serta menambahkan rute URL.

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
