Tugas Analisis 1:
=
• Apa yang terjadi jika kamu mengubah hero1.hp menjadi 500 setelah baris
hero1 = Hero...? Coba lakukan print(hero1.hp).
/=Jika hero1.hp diubah menjadi 500 setelah objek dibuat, maka nilai HP milik objek hero1 akan berubah menjadi 500. Hal ini terjadi karena atribut hp bersifat public sehingga dapat diakses dan diubah langsung dari luar class. Perubahan ini hanya memengaruhi objek hero1, tidak memengaruhi objek hero lainnya.

Tugas Analisis 2:
=
• Perhatikan parameter lawan pada method serang. Parameter tersebut
menerima sebuah objek utuh, bukan hanya string nama. Mengapa ini
penting?
/=Parameter lawan pada method serang() harus berupa objek, bukan hanya string nama, karena method tersebut membutuhkan akses ke atribut dan method milik lawan, seperti lawan.name, lawan.hp, dan method lawan.diserang(). Dengan menggunakan objek, interaksi antar hero dapat berjalan sesuai konsep Object-Oriented Programming (OOP).

Tugas Analisis 3:
=
• Eksperimen Fungsi super(): Pada class Mage, coba hapus (atau jadikan
komentar #) baris kode super().__init__(name, hp, attack_power). Kemudian
jalankan programnya.
• Pertanyaan: Error apa yang muncul saat kamu mencoba melihat info Eudora
(eudora.info())? Mengapa error tersebut mengatakan Mage object has no
attribute 'name', padahal kita sudah mengirim nama "Eudora" saat
pembuatan objek?
• Jelaskan peran fungsi super() dalam menghubungkan data dari class Anak ke
class Induk!
/=Error yang muncul adalah AttributeError: 'Mage' object has no attribute 'name' saat memanggil eudora.info(). Error ini terjadi karena super().__init__() dihapus, sehingga constructor milik class Hero tidak dijalankan dan atribut seperti name, hp, serta attack_power tidak dibuat. Fungsi super() berfungsi untuk menghubungkan class anak dengan class induk agar data dari Hero bisa digunakan oleh Mage.

Tugas Analisis 4:
=
1. Percobaan Hacking: Coba tambahkan baris kode berikut di bagian paling
bawah (luar class):
print(f"Mencoba akses paksa: {hero1._Hero__hp}")
Pertanyaan: Apakah nilai HP muncul atau Error? Jika muncul, diskusikan dengan
temanmy mengapa Python masih mengizinkan akses ini (konsep Name Mangling)
dan mengapa kita tetap tidak boleh melakukannya dalam standar pemrograman
yang baik.
2. Uji Validasi: Hapus logika if dan elif di dalam method set_hp, sehingga isinya
hanya self.__hp = nilai_baru.
Pertanyaan: Kemudian lakukan hero1.set_hp(-100).
Apa yang terjadi pada data HP Hero? Jelaskan mengapa keberadaan method
Setter sangat penting untuk menjaga integritas data dalam game!
/=1. Percobaan Hacking
Nilai HP tetap muncul. Python mengizinkan ini karena name mangling, tapi cara tersebut tidak dianjurkan karena melanggar enkapsulasi dan bisa merusak data objek.

2. Uji Validasi Setter
HP berubah menjadi -100. Ini menunjukkan setter penting untuk membatasi nilai agar data tetap masuk akal dan game berjalan dengan benar.

Tugas Analisis 5:
=
1. Melanggar Kontrak: Pada class Hero, hapus (atau jadikan komentar #) seluruh
blok method def serang(self, target):. Jalankan programnya.
Pertanyaan: Error apa yang muncul? Jelaskan dengan bahasamu sendiri, apa arti
pesan error Can't instantiate abstract class Hero with abstract
method...?
Apa konsekuensinya jika kita lupa membuat method yang sudah dijanjikan di
Interface?
2. Mencetak Cetakan: Coba aktifkan baris kode unit = GameUnit().
Pertanyaan: Mengapa class GameUnit dilarang untuk dibuat menjadi objek?
Apa gunanya ada class GameUnit jika tidak bisa dibuat menjadi objek nyata?
/=1. Melanggar Kontrak

Error yang muncul:
TypeError: Can't instantiate abstract class Hero with abstract method serang

Penjelasan:
Error tersebut muncul karena class Hero tidak membuat method serang() yang sudah diwajibkan oleh abstract class GameUnit. Abstract class berfungsi sebagai kontrak. Jika ada method yang dijanjikan tetapi tidak dibuat, maka class tersebut dianggap belum lengkap dan tidak bisa dibuat objeknya.

Konsekuensi jika lupa membuat method dari Interface:
Program akan error dan objek dari class tersebut tidak bisa dibuat. Hal ini memaksa programmer agar semua aturan dalam interface dipenuhi sehingga struktur program tetap konsisten dan aman.

2. Mencetak Cetakan (GameUnit)

Mengapa GameUnit tidak boleh dibuat objek?
Karena GameUnit adalah abstract class yang hanya berisi aturan dan method kosong. Class ini tidak memiliki implementasi nyata sehingga tidak bisa digunakan langsung sebagai objek.

Apa gunanya GameUnit jika tidak bisa dibuat objek?
GameUnit berfungsi sebagai kerangka atau cetakan agar semua class turunannya memiliki method yang sama. Dengan begitu, kode menjadi lebih terstruktur, rapi, dan mengurangi kesalahan dalam program.

Tugas Analisis 6:
=
1. Uji Skalabilitas (Kemudahan Menambah Fitur): Tanpa mengubah satu huruf
pun pada kode Looping (for pahlawan in pasukan:), buatlah satu class
baru bernama Healer(Hero).
Isi method serang milik Healer dengan: print(f"{self.name} tidak
menyerang, tapi menyembuhkan teman!").
Masukkan objek Healer ke dalam list pasukan.
o Pertanyaan: Apakah program berjalan lancar?
o Kesimpulannya, apa keuntungan Polimorfisme bagi seorang programmer
ketika harus mengupdate game dengan karakter baru di masa depan?
2. Konsistensi Penamaan: Ubah nama method serang pada class Archer
menjadi tembak_panah. Jalankan program.
Pertanyaan: Apa yang terjadi?
Mengapa dalam konsep Polimorfisme, nama method antara Parent Class dan
berbagai Child Class harus persis sama?
/=1. Uji Skalabilitas

Apakah program berjalan lancar?
Ya, program tetap berjalan dengan baik meskipun ditambahkan class Healer, tanpa perlu mengubah kode looping.

Kesimpulan:
Polimorfisme memudahkan programmer menambahkan karakter baru di masa depan tanpa mengubah sistem utama, sehingga kode lebih fleksibel dan mudah dikembangkan.

2. Konsistensi Penamaan Method

Apa yang terjadi?
Program mengalami error karena class Archer tidak lagi memiliki method serang().

Mengapa nama method harus sama?
Karena Polimorfisme bekerja dengan pemanggilan method yang sama. Jika nama method berbeda, program tidak dapat menjalankan perintah yang diberikan.
