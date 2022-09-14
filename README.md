link menuju aplikasi Heroku : https://aplikasitugas2.herokuapp.com/katalog/

2. Virtual Environtment digunakan sebagai sebuah tempat untuk mengotak-atik sebuah projek seperti menginstall sesuatu untuk sebuah projek sehingga projek satu dengan projek yang lainnya terpisah environmentnya dan tidak saling mengganggu. Jadi sebagai sebuah sekat antara projek-projek, ketika satu projek sedang menginstall sesuatu maka projek lainnya tidak terpengaruh karena dibatasi oleh virtual environment tersebut. Sebenarnya tanpa virtual environment pun sebuah aplikasi tetap dapat berjalan namun menjadi tidak aman karena dapat memengaruhi aplikasi atau projek lainnya jika tidak memakai virtual environment.

3. 1). menambahkan kode dibawah ini pada views.py sebagai pengambilan data dari model dan dikembalikan ke dalam sebuah HTML.

    def show_catalog(request):                          #memberi nama fungsi dengan show_catalog
    data_barang_katalog = CatalogItem.objects.all()     #memanggil semua data yang ada di CatalogItem, models.py
    context = {
    'nama': 'Syarifah Nur Amalia',
    'NPM' : '2106751272',                               #membuat dictionary yang berisi data yang akan dipakai di HTML
    'list_barang': data_barang_katalog,
    }
    return render(request, "katalog.html", context)     #memasukan data yang ada di dictionary context ke katalog.html

    2). menambahkan kode dibawah ini pada urls.py sebagai routing terhadap fungsi show_catalog di views.py sehingga nantinya halaman HTML dapat ditampilkan di browser.

    from katalog.views import show_catalog
    app_name = 'katalog'
    urlpatterns = [
    path('', show_catalog, name='show_catalog'),
    ]

    dan menambahkan kode dibawah ini pada variable urlpattern yang ada di file urls.py, project_django agar aplikasinya terdaftar.
    path('katalog/', include('katalog.urls')),

    3). menambahkan data yang ada pada dictionary context ke dalam file katalog.html dengan mengisi {{ key }} diantara <p>.

      <h5>Name: </h5>
      <p>{{ nama }}</p>

      <h5>Student ID: </h5>
      <p>{{ NPM }}</p>

      dan mengiterasikan list_barang lalu menuliskan data barang tersebut di tabel dengan mengisi {{ barang.sesuatu }}.

      {% for barang in list_barang %}
    <tr>
        <th>{{ barang.item_name }}</th>
        <th>{{ barang.item_price }}</th>
        <th>{{ barang.item_stock }}</th>
        <th>{{ barang.rating }}</th>
        <th>{{ barang.description }}</th>
        <th>{{ barang.item_url }}</th>
    </tr>
      {% endfor %}

    4). create new app di heroku lalu menyimpan API Key di repositori github dengan key HEROKU_API_KEY dan menyimpan nama app dengan key HEROKU_APP_NAME.