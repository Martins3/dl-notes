import random

def wulishanghai(yuanshiwuli, hujia):
    assert yuanshiwuli > 0
    return yuanshiwuli * (100 / (100 + hujia))

def hujia(yuanshi_hujia, hujia_chuantou):
    assert yuanshi_hujia >= 0
    return yuanshi_hujia * ( 100 / (100 + hujia_chuantou))

def shanghai(wuli, muofa):
    return wuli + muofa


def after_attack(life, shanghai):
    after_life = life - shanghai
    return max(after_life, 0)


def baoji(rate):
    assert rate <=1
    assert rate >=0
    seed = random.randint(0, 101)
    rate = rate * 100
    if(seed < rate):
        return 1
    else:
        return 0

def muofanshanghai(yuanshi_muofa, muofa_kangxin):
    return yuanshi_muofa / (100 / (100 + muofa_kangxin))




class hero(object):
    def __init__(self,
                 name,
                 life,
                 wulishanghai,
                 muofashanghai,
                 hujia,
                 muokang,
                 yidongsudu,
                 q,
                 w,
                 e,
                 r):
        self.name = name
        self.life = life
        self.wulishanghai = wulishanghai

    def set_df(self, d, f):
        self.d = d
        self.f = f
