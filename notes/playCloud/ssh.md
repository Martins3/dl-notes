`qwe123QWE`
118.89.164.91
# ssh 搭建
1. find out the ip address
2. generate the rsa key
3. paste the public key into the cloud serve .ssh/authorith_key

then you can connneted to it

#  the real build essentils
1. sudo apt-get install gdb
1. zsh(chsh -s $(which zsh))(export PATH="/home/username/miniconda/bin:$PATH")
2. anaconda(wget)
3. pip install wxpy
3. conda install tensorflow
3. conda install theano
4. git set up the remote server
5. mkdir hubachelar
6. on my PC : git remote add qcloud ubuntu@118.89.164.91:/home/ubuntu/hubachelar/All
  on the server: make the  mkdir hubachelar/ALl  and git --bare init
  git push qcloud master
  https://git-scm.com/book/en/v2/Git-on-the-Server-Setting-Up-the-Server
8. fix the console can not show chinese(i have no time)
9. view the image on the terminal
10. digit ocean => java install
11. the shadowsocks
sudo add-apt-repository ppa:max-c-lv/shadowsocks-libev
sudo apt-get update
sudo apt install shadowsocks-libev
12. ssh免去密码登录： sshpass -p 'qwe123QWE' ssh ubuntu@118.89.164.91





1. vpn

# some notes
1. git user
passwords :qwe123QWE
phone: true
room: 12
name: Martin Hu

2. git pull from the cloud server : git pull qcloud master
3.
4. 赋值二维码
scp user@server:/path/to/remotefile.zip /Local/Target/Destination
