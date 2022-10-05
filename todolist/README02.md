1. Apa perbedaan dari Inline, Internal, dan External CSS? Apa saja kelebihan dan kekurangan dari masing-masing style?
--> *Inline CSS adalah model styling dimana penulisannya berada pada body dan pada elemetnnya langsung.
    Contoh : <p style = "color:#009900; font-size:50px;font-style:italic; text-align:center;">Halo</p>
    Kelebihan : Lebih prioritas dari tipe lainnya, cocok untuk quickfix, request HTTP lebih kecil
    Kekurangan : Kode menjadi kurang rapih, harus diterapkan satu-persatu

    *Internal CSS adalah model styling dimana penulisannya berada pada head dan pada <style>.
    Contoh : <head>
        <style>
            .main {
                text-align:center; 
            }
        </style>
        </head>
    Kelebihan : Dapat menggunakan Class dan ID, lebih mudah karena dalam satu file, kode lebih rapih
    Kekurangan : Prioritas kedua, waktu akses website bertambah, tidak efisien jika ingin dipakai di banyak file

    *External CSS adalah model styling dimana penulisannya seperti internal css namun berada di file yang berbeda, lalu di input di file html dengan <link>.
    Contoh: <link rel="stylesheet" href="filecss.css"/>
    Kelebihan : Dapat digunakan dibanyak halaman, tidak menambah size html, kode terpisah dengan html sehingga lebih mudah dirawat
    Kekurangan : Prioritas terakhir

2. Jelaskan tag HTML5 yang kamu ketahui !
--> <body> : Mendefinisikan konten dari suatu dokumen
    <button> : Membuat tombol yang bisa di klik
    <div> : Menspesifikasi suatu bagian di dalam dokumen
    <head> : Mendifisikan bagian head dari dokumen (contohnya title,style)
    <h1> sampai <h6> : Untuk heading html
    <p> : Untuk paragraf
    <table> : Untuk membuat tabel
    <style> : Memasukkan informasi style

3. Jelaskan tipe-tipe CSS selector yang kamu ketahui !
--> *Element Selector
    Menggunakan tag HTML sebagai selector untuk mengubah properti yang terdapat dalam tag tersebut.
    Contoh : h1 {
            color: #fca205;
            font-family: "Monospace";
            font-style: italic;
            }

    *ID Selector
    Menggunakan ID pada tag sebagai selector-nya. Pada body diberi 'id="nama id"', lalu di style diberi #nama id.
    Contoh : <div id="header"> , lalu 
            #header {
                background-color: #f0f0f0;
                margin-top: 0;
                padding: 20px 20px 20px 40px;
                }

    *Class Selector
    Menambahkan beberapa class pada tag HTML. Pada body diberi 'class="nama clss"', lalu di style diberi .nama class.
    Contoh : <div class="content_section">, lalu
            .content_section {
            background-color: #3696e1;
            margin-bottom: 30px;
            color: #000000;
            font-family: cursive;
            padding: 20px 20px 20px 40px;
            }

4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas !
--> *Kustomisasi templat untuk halaman login, register, dan create-task semenarik mungkin.
    Menambahkan "<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-iYQeCzEYFbKjA/T2uDLTpkwGzCiq6soy8tYaI1GyVh/UjpbCx/TYkiZhlZB6+fzT" crossorigin="anonymous">" dan "<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-u1OknCvxWvY5kfmNBILK2hRnQC3Pr17a+RTT6rIHI7NnikvbZlHgTPOOmMi466C8" crossorigin="anonymous"></script>" pada base.html lalu extend base.html dan mulai design dengan bootstrap.

    * Kustomisasi halaman utama todo list menggunakan cards. (Satu card mengandung satu task).
    Menambahkan <div class="card" style="width: 18rem;"> dan <div class="card-body"> untuk membuat card pada setiap task. Lalu, agar rapih saya menambahkan container agar cardnya tersusun rapih. 
            .grid-container {
            display: grid;
            grid-template-columns: auto auto auto auto;
            gap: 10px;
            padding: 10px;
            }

    *Membuat keempat halaman yang dikustomisasi menjadi responsive.
    Sebenarnya sudah bawaan dari bootstrap, namun karena beberapa element tidak responsive sehingga agar aman saya menambahkan <meta name="viewport", content="width=device-width, initial-scale=1.0"> pada head.