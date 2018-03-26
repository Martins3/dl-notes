https://en.wikipedia.org/wiki/Virtual_private_server
Nginx是一款轻量级的Web 服务器/反向代理服务器及电子邮件(IMAP/POP3)代理服务器

1、http服务器。Nginx是一个http服务可以独立提供http服务。可以做网页静态服务器。
2、虚拟主机。可以实现在一台服务器虚拟出多个网站，例如个人网站使用的虚拟机。
3、反向代理，负载均衡。当网站的访问量达到一定程度后，单台服务器不能满足用户的请求时，需要用多台服务器集群可以使用nginx做反向代理。并且堕胎服务器可以平均分担负载，不会应为某台服务器负载高宕机而某台服务器闲置的情况。
nginx七层load balance结构图：
