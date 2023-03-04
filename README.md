# bot-statuscode-telegram-codeigniter-dasboard
bot telegram untuk cek jika ada website yang down dengan program python dan dilengkapi dengan dashboardnya menggunakan codeigniter 

# Docker image 
segera hadir

`docker run -it -p 80:80 agungsurya/bot-statuscode:v3 /bin/bash` #dashboard untuk bot

`docker run -it --cap-add=SYS_ADMIN -p 12002:8000 -u agungsurya agungsurya/bot-statuscode:api-server-screenshot-alpine /bin/ash` #note ini api server untuk bot nya yang pertama dengan fitur screnshoot

`docker run -it -p 12002:8000 agungsurya/bot-statuscode:api-server2 /bin/ash`

# segera upload
![image](https://github.com/agungsoboru/bot-statuscode-telegram-codeigniter-dasboard/blob/main/Screenshot%20(538).png)
![image](https://github.com/agungsoboru/bot-statuscode-telegram-codeigniter-dasboard/blob/main/bot-telegram.JPG)
![image](https://github.com/agungsoboru/bot-statuscode-telegram-codeigniter-dasboard/blob/main/bot-telegramm.JPG)
# keunggulan
yang pasti ada dashboard 

bisa tambah dan hapus domain yang akan di cek lewat web

ada server api untuk backup bot nya ketika tidak berhasil ngecek statuscode

ada interface web status api server dan bot nya

bisa tambah user admin atau staf

bot lognya di interface web

app ny punya banyak vulnerability 

ada auth/login

Encrypt and Decrypt Support

# reverensi 
https://github.com/BootsBack/Codeigniter-php-Bootstrap-AdminLTE-Panel-with-user-management

