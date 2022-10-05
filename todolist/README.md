link : https://aplikasitugas2.herokuapp.com/todolist/login/?next=/todolist/

1. Csrf token merupakan sebuah random string yang di-generate setiap kali halaman form muncul. Gunanya untuk sebagai pengaman agar mencegah CSRF attack dengan mengirimkan informasi tambahan pada setiap pengiriman data ke server. Informasi tersebut berisi nilai acak yang sudah diatur parameternya oleh aplikasi web. Nilai acak tersebut berfungsi untuk menentukan apakah permintaan tersebut berasal dari pengguna yang memiliki otoritas atau bukan. 

2. Kita dapat membuat elemen form sendiri secara manual. Secara garis besar, caranya buat file forms.py dahulu, lagu di dalem file tersebut import library form dan class yang ada di model yang ingin dihidupkan objeknya. Lalu di file tersebut mendefinisikan modelnya sebagai class yang objeknya ingin dihidupkan dari models.py. Lalu dibuat formnya berdasarkan atribut yang dimiliki modelnya.

3. Ketika user memasukkan data dan memencet tombol submit, browser akan memberi response POST request lalu diarahkan ke views.py dengan fungsi yang sesuai. Lalu, data tersebut dicek terlebih dahulu apakah sesuai aturan atau tidak, jika sesuai aturan maka data tersebut akan masuk ke database, lalu views nge redirect ke views sebelumnya.

4.  1). Membuat aplikasi todolist dengan menjalankan perintah python3 manage.py startapp todolist
    2). Menambahkan "todolist" ke dalam INSTALLED_APPS yang terdapat pada file settings.py folder project django
    3). Membuat class Task dengan atribut user, date, title, description

    class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()

    Lalu jalankan perintah makemigrations dan migrate

    4). Membuat fungsi-fungsi untuk login, logout, dan registrasi di views.py dan membuat html nya untuk login dan registrasi

    5). Membuat fungsi todolist untuk menampilkan semua data yang ingin ditampilkan dengan memakai variable context

    def todolist(request):
    tasklist = Task.objects.filter(user=request.user)
    context = {
    'tasks' : tasklist,
    'username' : request.user,
    'last_login' : request.COOKIES['last_login'],
    }
    return render(request, "todolist.html", context)

    6). Membuat fungsi create_task sebagai fungsi untuk menambahkan task

    7). Menambahkan path-path yang dibutuhkan dan appname pada file urls.py folder todolist

    app_name = "todolist"

    urlpatterns = [
        path('', todolist, name='todolist'),
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
        path('create-task/', create_task, name='create_task'),
    ]

    8). commit dan push
