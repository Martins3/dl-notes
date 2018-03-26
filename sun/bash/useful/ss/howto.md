注册新的机器:
不可以第一次使用 sshpass, 添加了ssh key之后才可以添加
in vultr
1. sudo apt-get install python-setuptools
2. export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
**and enters**
3. apt install python-pip 
pip install shadowsocks


ssserver -p 443 -k qwerdafewrswqr -m aes-256-cfb --user nobody -d start