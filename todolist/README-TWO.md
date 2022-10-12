 1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.
--> Asynchronus programming adalah ketika program bisa menjalankan proses atau event lainnya dalam satu waktu atau serentak. Sedangkan, synchronus programming adalah ketika program hanya bisa menjalankan 1 proses atau event, jadi mengantri atau sequential.

 2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma Event-Driven Programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.
--> Event-Design Programming adalah program yang dijalankan berdasarkan event yang dilakukan oleh user. Contoh penerapan di tugas ini adalah ketika kita memilih ingin menambah task atau delete task, nanti program akan jalan sesuai pilihan kita (user).

 3. Jelaskan penerapan asynchronous programming pada AJAX.
--> Saat melakukan tambah task dengan modal, task yang ditambah akan langsung muncul ke layar tanpa melakukan reload satu halaman.

 4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas.
 --> *AJAX GET
        1. Membuat fungsi baru di views.py bernama "show_json" untuk mengubah data menjadi dalam bentuk file json.

        2. Membuat path baru untuk mengarahkan ke fungsi "show_json", yaitu "path('json/', show_json, name='show_json')"

        3. Mengambil data dari file json diatas lalu data-data tersebut append ke class task_list dengan GET AJAX

    *AJAX POST
        1. Membuat tombol untuk memunculkan modal seperti berikut : <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">Tambah Task</button>
        Lalu menambahkan kode untuk membuat modalnya dengan id exampleModal. Untuk kode modalnya saya mengambil dari bootstrap.

        2. Membuat fungsi baru di views.py bernama "create_task_modal" untuk membuat objek baru berdasarkan data yang disubmit di modal

        3. Membuat path baru untuk mengarahkan ke fungsi "create_task_modal", yaitu path('add/', create_task_modal, name='create_task_modal')

        4. Menampilkan data yang baru ditambahkan dengan POST AJAX dan kembali ke html todolist dengan menambahkan kode "data-bs-dismiss="modal"" pada button tambahkannya.
