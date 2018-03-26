
#  login
# ssh huxueshi@115.156.197.252 -p 42022

# copy data form local to server
# scp -P 42022 /home/martin/X-Brain/SVD/mnist.pkl.gz huxueshi@115.156.197.252:/home/huxueshi/SVD

# copy expreiment res

scp -r -P 42022 huxueshi@115.156.197.252:/home/huxueshi/SVD/showResFc   /home/martin/X-Brain/SVD/showResFc


# 复制代码
# scp -r -P 42022 /home/martin/AllWorkStation/dynamic/python huxueshi@115.156.197.252:/home/huxueshi/AllWorkStation/dynamic/pytho