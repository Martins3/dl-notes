import sys
from urllib.request import urlopen
from html.parser import HTMLParser


def get_result(word):
    url = 'http://fanyi.youdao.com/openapi.do?keyfrom=majunzhe&key=27448872&type=data&doctype=xml&version=1.1&q='
    query_url = url + word
    result = urlopen(query_url).read().decode('utf-8')
    return result


class WordResultParser(HTMLParser):
    bHandled = False
    bExplain = False
    data_meaning = ''
    output = ''
    tags = ('phonetic', 'ex', 'key')
    def parse_data(self, data):
        beg_pos = data.rfind('[') + 1
        end_pos = data.find(']', beg_pos, len(data))
        if end_pos == -1:
            end_pos = len(data)
        self.data_meaning = data[beg_pos:end_pos]   
    def handle_starttag(self, tag, attrs):
        if 'basic' == tag:
            self.output += '基本释义：\n'
        elif 'web' == tag:
            self.output += '网络释义：\n'
        elif 'explain' == tag:
            self.bExplain = True
        if tag in self.tags:
            self.bHandled = True

    def handle_endtag(self, tag):
        if 'explain' == tag:
            self.output += '\n'
            self.bExplain = False   
    def unknown_decl(self, data):
        if self.bHandled != True:
            return
        self.parse_data(data)
        endstr = '\n'
        if self.bExplain:
            endstr = ' '
        self.output += self.data_meaning + endstr
        self.bHandled = False   




def test():
    """
    测试文件的格式
    """
    print(get_result("apple"))



if __name__ == "__main__":
    test()