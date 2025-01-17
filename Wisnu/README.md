[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/P7ZdhZuT)
# UG 9 PRIORITY QUEUE
## UNTUK MEMPERMUDAH HIDUP KALIAN, KERJAKAN DI main.py
Pada UG ini, kalian akan menyimulasikan penanganan darurat korban bencana alam dengan memanfaatkan priority queue. Dengan memanfaatkan priority queue, tentukan setiap prioritas korban bencana untuk ditangani, dan masukkan ke dalamnya.


Untuk melakukan penentuan prioritas pada pasien, bisa dilakukan Triase. Triase adalah metode untuk menentukan prioritas penanganan pasien dengan menegecek respirasi, denyut nadi, dan status mental. Setelah melalui tahap ini, pasien akan diberi prioritas berupa status. Status hitam artinya tidak tertolong lagi, merah artinya kritis, kuning artinya tidak membahayakan jiwa. Prioritas yang paling tinggi ke rendah: hitam, merah, kuning. Tahap Triase dibagi dalam 3 tahap:

### Pengecekan Respirasi 
Mengecek kecepatan bernapas pasien per menit
- jika kecepatan pernapasan pasien 0 / menit (mati), maka status pasien adalah ***STATUS HITAM***
- jika kecepatan pernapasan lebih dari 30 atau kurang dari 10 kali per menit, maka status pasien menjadi ***STATUS MERAH***.
- jika kecepatan bernapas pasien normal (antara 10-30 kali per menit), bisa dilanjutkan ke pengecekan denyut nadi

### Pengecekan Denyut Nadi
Pengecekan denyut nadi jantung.
- jika denyut nadi lemah atau tidak teraba, maka status pasien menjadi ***STATUS MERAH***
- selain itu, bisa dilanjutkan ke pengecekan status mental

### Pengecekan Status Mental
Pengecekan apakah pasien bisa diberi perintah
- jika pasien bisa diberi perintah, statusnya menjadi ***STATUS KUNING***
- jika tidak bisa diberi perintah, statusnya menjadi ***STATUS MERAH***

Perlu diperhatikan apabila pasien sudah mendapatkan status (misal, status hitam), maka pengecekan selanjutnya tidak perlu. Contoh, jika Budi sudah diberikan status hitam saat Pengecekan Respirasi, maka budi tidak perlu melakukan pengecekan denyut nadi dan status mental. Bisa dilihat di hasil akhir.


Melalui ketentuan di atas, buatlah sebuah program yang meminta input dari pengguna sebanyak 3 pasien, kemudian tentukan status mereka. Prioritas yang paling tinggi ke rendah: hitam, merah, kuning. kemudian, masukkan semua data pasien ke dalam sebuah priority queue. Terakhir, tampilkan semua data pasien sesuai dengan status mereka.

Kalian sudah diberikan class PriorityQueue yang merupakan sorted priority queue. method - methodnya bisa kalian lihat sendiri. Priority Queue ini akan menerima bentuk prioritas sebagai angka. misal, untuk melakukan method enqueue(prioritas, data), kalian menggunakannya seperti ini: enqueue(3, "Asep"). Parameter pertama adalah prioritas, yang kedua adalah datanya. Nah untuk mempermudah hidup kalian, maka kita sepakati saja bahwa:

- ***Status Hitam*** mempunyai prioritas 3
- ***Status Merah*** mempunyai prioritas 2
- ***Status Kuning*** mempunyai prioritas 1

Nah, satu lagi, kalian sudah diberikan sebuah fungsi bernama print_pasien(pq). Fungsi ini akan menerima parameter berupa sebuah objek PriorityQueue. Fungsi ini berfungsi untuk menampilkan seluruh data dari pasien. Jadi, kalian tidak perlu repot - repot membuat algoritma menampilkan data pasien, cukup panggil saja fungsi ini dan masukkan priority queue yang sudah kalian isi sebagai parameter nya.
## Hasil Akhir
```
    Masukkan 3 pasien
    Nama pasien: Asep
    Kecepatan Respirasi per menit: 0


    Nama pasien: Budi
    Kecepatan Respirasi per menit: 30
    Denyut lemah/tidak terasa (y/n): y


    Nama pasien: Hanafi
    Kecepatan Respirasi per menit: 30
    Denyut lemah/tidak terasa (y/n): n
    Apakah bisa diperintah? (y/n): y

    === HASIL DATA PASIEN ===
    1. Asep, status: Sudah meninggal
    2. Budi, status: Merah
    3. Hanafi, status: Kuning
```
