#!/bin/sh


# NOTE: This is an example that sets up SSH authorization. To use it, you'd need to replace "ssh-rsa AA... youremail@example.com" with your SSH public.
# You can replace this entire script with anything you'd like, there is no need to keep it


mkdir -p /root/.ssh
chmod 600 /root/.ssh
echo ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQD14mzv49lZp1qSLF+vGRawHSgJ3Q5v8IKa3RRsflcp6IogQCjPyHupQzzMkDtyJRNGY97aNcBUzidIuG1qM08++CqAH+tw2E9p64cCOEWEwT+5URajUk7ZwEZKGG1WbLGV2i43l+zvYmBsqNP7kUo4F57aPcrn0exBt7rkz/lQdz7SYycyEeLOGcqWGaCBabW/hZfqC4VD1pzOTOHRmLA/6Lz4YftPIb4H8NCQblObWRV7LdEo/ljXvWiSCOgiAQCp3Kg3XZuBpQm1+T+1n0aCsQwzHtjpzLTgs7NyJ/olh/Q2KG9dR4Oz773gVABUPOFkmLeVzWMa3REomaUsIZkt hubachelar@gmail.com > /root/.ssh/authorized_keys
chmod 700 /root/.ssh/authorized_keys
