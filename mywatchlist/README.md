JAWABAN TUGAS 2 PBP

link : https://aplikasitugas2.herokuapp.com/mywatchlist/

1. Perbedaan HTML, JSON, XML
    
(JSON)
- fungsi = transfer data
- penyimpanan elemen  = dengan key:value (mapping)
- keamanan = lebih aman
- bahasa = format yang ditulis dalam javascript
- kecepatan = cepat
- pengolahan = tidak melakukan pemrosesan/perhitungan apapun
- eksistensi file = .json
    
(XML)
- fungsi = transfer data
- penyimpanan elemen  = dengan <variable> ... </variable> (tree structure)
- keamanan = rentan terhadap hacking
- bahasa = bahasa markup bukan bahasa pemrograman
- kecepatan = lambat
- pengolahan = dapat melakukan pemrosesan/perhitungan
- eksistensi file = .xml
    
(HTML)
- fungsi = menyajikan/menampilkan data
- penampilan elemen  = dengan <title> ... </title>
- bahasa = bahasa markup bukan bahasa pemrograman
- kecepatan = cepat
- eksistensi file = .html

2. Mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?

Ketika sudah melibatkan data yang besar, pasti membutuhkan data base untuk menyimpan data tersebut. Lalu, ketika ingin menampilkan data-data tersebut, sangat tidak efisien jika menuliskannya satu-satu di HTML. Oleh karena itu, memerlukan data delivery untuk memindahkan data-data tersebut dari satu stack ke stack lainnya sehingga HTML dan data base tersebut dapat terhubung. Selain itu, HTML dan data menjadi dapat dipisah agar lebih terstruktur.

3. Bagaimana cara kamu mengimplementasikan checklist di atas
    1. Membuat aplikasi baru bernama "mywatchlist" dengan menjalankan perintah 'startapp' pada terminal repository
    2. Menambahkan path mywatchlist sehingga pengguna dapat mengakses http://localhost:8000/mywatchlist dengan menambahkan "mywatchlist" di INSTALLED_APPS yang ada pada folder project_django file settings.py dan menambahkan path di file urls.py pada folder project_django
    3. Membuat class WatchList dengan atribut yang terdapat di soal pada file models.py dan menjalankan perintah makemigrations dan migrate
    4. Menambahkan 10 data film dengan membuat folder fixtures dan file initial_data_watchlist.json di dalamnya lalu menulis 10 data tersebut. Lalu, menjalankan perintah loaddata
    5. Mengimplementasikan sebuah fitur untuk menyajikan data dengan format XML,HTML,JSON dengan membuat fungsi baru di file views.py
    6. Membuat routing dengan membuat file urls.py dan menambahkan path XML,HTML,JSON pada file tersebut
    7. Melakukan deployment ke Heroku dengan git add, commit, push perubahan tersebut ke github

4. Screenshot
![Screen Shot 2022-09-22 at 10 30 48 AM](https://user-images.githubusercontent.com/101639653/191652367-40db3f9b-c65d-41e7-b845-461f5139aced.png)
![Screen Shot 2022-09-22 at 10 31 40 AM](https://user-images.githubusercontent.com/101639653/191652391-33ef00b4-0af9-4ed9-bd49-1e02af220fc1.png)
![Screen Shot 2022-09-22 at 10 31 53 AM](https://user-images.githubusercontent.com/101639653/191652402-6ddf425a-53f4-4c05-9d37-0836c6f9a961.png)

