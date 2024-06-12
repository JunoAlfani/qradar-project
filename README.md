![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/cover.png)


# Langkah Awal


Install qradar.iso yang tersedia di web resmi IBM QRadar Comunity yang dapat diunduh. lalu jalankan di virtual mesin.


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/login_system.png)


lalu pada si QRadar yang ada didalam virtual mesin akan memberikan ip web console, paste pada web browser lalu akan muncul halaman login QRadar


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/Dashboard.png)


setelah login berhasil akan masuk kedalam dashboard QRadar yang berisi masih kosong serta ketika click pada menu log activity pun masih kosong.


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/log_activity.png)



# Studi Kasus 

Seorang hacker yang merupakan bagian dari upaya mata-mata dari perusahaan pesaing telah menargetkan sebuah startup. Hacker ini memanfaatkan kelalaian dalam kebijakan keamanan startup target yang belum menerapkan Zero Trust Framework. pada awalnya, hacker melakukan pengumpulan informasi intensif terhadap stratup target. Dalam proses ini, dia mengidentifikasi bahwa startup target belum menerapkan salah satu prinsip kunci dari Zero Trust Framework, yaitu monitoring jaringan secara berkala.


Ketidakmampuan startup target untuk melakukan monitoring berkala pada jaringan mereka menjadi celah yang sangat potensial bagi serangan siber. Dengan informasi yang telah dikumpulkan, hacker mendekati targetnya dengan taktik yang cerdik. dengan menggunakan berbagai metode, hacker berhasil memanfaatkan kelalaian tersebut dan mencoba untuk melakukan data breach ke dalam jaringan startup. Serangan ini dapat mencakup upaya penetrasi jaringan, pencarian celah keamanan yang belum terdeteksi, atau bahkan serangan lain terhadap karyawan startup.


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/port_scan.png)


Pada tahap pertama, hacker melakukan port scanning untuk melihat port port yang terbuka, setelah melakukan port scanning, diketahui bahwa port 22 terbuka pada host target. 


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/hydra.png)


Pada tahap kedua, hacker mencoba untuk mendapatkan hak akses root pada host target dengan menggunakan metode bruteforce. 


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/berhasil_akses_root.png)


Setelah hacker berhasil mendapatkan hak akses root, hacker akan mencari folder/file yang berisi data – data penting yang kemudian data tersebut akan di ambil dengan menggunakan file transfer protocol (sftp, port 22).


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/ddos.png)


Pada tahap terakhir, hacker akan melakukan aksi DDOS untuk menarik perhatian publik dan menjatuhkan reputasi dari startup tersebut.


Jenis – jenis serangan seperti yang ada diatas dapat dideteksi lebih dini dengan melakukan penerapan prinsip zero trust dengan bantuan tools SIEM seperti IBM Qradar SIEM. Berikut adalah tampilan apabila startup ini menggunakan qradar sebagai tools dalam monitoring log jaringan.


Pada tahap pertama, rules yang bernama “Port Scan Detected” akan muncul apabila terdeteksi serangan port scanning pada jaringan yang dimonitor.


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/deteksi_nmap.png)


Dapat dilihat bahwa ada 1 source IP (Attacker || 192.168.1.14) yang mengirimkan paket ke banyak port di 1 destination IP (Target || 192.168.1.35), kemudian terdapat flow type superflow C.


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/log_activity_nmap.png)


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/type%20c.png)


Kemudian pada log activitiy kita dapat melihat bahwa rules yang bernama “Port Scan Detected” akan muncul beserta deskripsi dari serangan nya. Disini kita dapat melihat source ip, destination ip, dan waktu log.


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/source_ip_nmap.png)


Pada tahap kedua, rules yang bernama “Percobaan SSH bruteforce” akan muncul pada log activity. Rules ini akan muncul ketika terjadi event bernama “Root Login Failed” lebih dari 3 kali selama 1 menit pada destination IP yang sama.


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/deteksi_ddos.png)

![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/type%20B.png)


Dapat dilihat bahwa ada banyak source IP yang mengirimkan data ke 1 destination IP (Target || 192.168.1.35), kemudian terdapat flow type superflow B.


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/ddos_rules.png)


Rules yang telah dibuat, yaitu “DDOS detected” akan muncul pada halaman log activity karena pada network activity terdeteksi flow type superflow C.
Dengan menggunakan qradar, kita dapat memonitoring jaringan dengan lebih mudah. Kita juga dapat melakukan konfigurasi ataupun menambahkan rules – rules baru sesuai dengan kebutuhan kita. Qradar membantu kita dalam mengidentifikasi aktivitas tidak wajar dalam jaringan. Rules – rules yang telah dibuat dapat membantu dalam mendeteksi serangan siber secara dini sehingga dapat meminimalisir kerusakan.


# Work Flow


![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/workflow.png)


# Topologi


a. Port Scan (NMAP)

![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/port_scan_workflow.png)


b. SSH Brute Force

![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/workflow_bruteforce.png)


a. Distributed denial-of-service (DDOS) 

![alt text](https://github.com/JunoAlfani/qradar-project/blob/main/dokumentasi/ddos_workflow.png)



# Analisis

Setelah mengidentifikasi serangan yang terjadi dalam jaringan, hal yang perlu dilakukan selanjutnya adalah melakukan mitigasi terhadap serangan yang terjadi pada jaringan, berikut adalah langkah – langkah yang dapat dilakukan :

a. Port Scanning
Port scanning adalah metode yang dilakukan oleh cybercriminal untuk mengidentifikasi port port yang terbuka pada komputer target. 
Metode Pencegahan :

- Melakukan konfigurasi firewall, hanya buka port yang diperlukan
- Port terbuka hanya pada kurun waktu tertentu, setelah itu port akan tertutup
- Menggunakan firewall tarpit untuk mengelabuhi hacker seolah port yang di scan terbuka
    

b. SSH Brute Force
SSH bruteforce adalah serangan yang dilakukan dengan cara memasukkan segala kombinasi username dan password pada port SSH yang terbuka.
Metode Pencegahan :

- Gunakan password yang kuat, sehingga tidak mudah di bruteforce
- Batasi percobaan login
- Gunakan Public key authentication
- Konfigurasi firewall untuk membatasi akses ssh server ke ip yang terpercaya
- Monitoring log SSH, amati apabila terjadi aktivitas mencurigakan seperti login gagal berulang kali dari ip yang tidak diketahui
- menganalisis pola percobaan login yang mencurigakan. Ini melibatkan mengidentifikasi alamat IP yang mencoba login berulang kali dengan nama pengguna yang berbeda atau mencoba kombinasi kata sandi yang salah.
    

c. Distributed Denial-Of-Services (DDOS)
Serangan DDoS adalah salah satu ancaman siber yang dapat sangat merusak, terutama pada startup yang mungkin tidak memiliki infrastruktur keamanan yang kuat. Dalam skenario ini, startup mungkin rentan terhadap serangan DDoS karena mereka baru mulai mengembangkan kebijakan keamanan yang ketat, termasuk implementasi pendekatan Zero Trust.

- Identifikasi Serangan DDoS: Penting untuk mengenali serangan DDoS secepat mungkin. Hal ini dapat dilakukan dengan memonitor lalu lintas jaringan dan mencari tanda-tanda peningkatan lalu lintas yang tidak biasa.
- Gunakan Firewall dan Filter: Menggunakan firewall yang kuat dan filter lalu lintas dapat membantu membatasi lalu lintas yang masuk ke server. Ini dapat membantu dalam menghentikan lalu lintas DDoS yang tidak diinginkan.
- Blokir semua URL dan IP berdasarkan IoC (Indicator of Compromise) pada firewall, IDS, web gateway, router, dan lain – lain.
- SIEM akan mengumpulkan data dari berbagai sumber, termasuk log jaringan, peristiwa keamanan, dan aktivitas pengguna. Data ini akan memberikan wawasan tentang serangan yang sedang terjadi.




