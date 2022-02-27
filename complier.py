# 词法.py
import re
import sys
import logging
import coloredlogs
from const import TOKEN_STYLE, DETAIL_TOKEN_STYLE, keywords, operators, delimiters
coloredlogs.install(level='DEBUG')

# logging.basicConfig(level=logging.DEBUG)


class Token:
    '''记录分析出来的单词'''

    def __init__(self, type_index, value):
        self.type = DETAIL_TOKEN_STYLE[value] if type_index in [
            0, 3, 4] and value in DETAIL_TOKEN_STYLE else TOKEN_STYLE[type_index]
        self.value = value


class Lexer:
    '''词法分析器'''

    def __init__(self, content=None):
        # 用来保存词法分析出来的结果
        self.tokens = []
        self.content = content

    # 判断是否是空白字符
    def is_blank(self, index):
        return self.content[index] in [' ', '\t', '\n', '\r']

    # 跳过空白字符
    def skip_blank(self, index):
        while index < len(self.content) and self.is_blank(index):
            index += 1
        return index

    # 判断是否是关键字
    def is_keyword(self, value):
        for item in keywords:
            if value in item:
                return True
        return False

    # 词法分析主程序
    def main(self):
        i = 0
        while i < len(self.content):
            i = self.skip_blank(i)

            # 如果是字母或者是以下划线开头
            if self.content[i].isalpha() or self.content[i] == '_':
                # 找到该字符串
                temp = ''
                while i < len(self.content) and (self.content[i].isalpha()
                                                 or self.content[i] in ['_', '*', '.']
                                                 or self.content[i].isdigit()):
                    temp += self.content[i]
                    i += 1
                # 判断该字符串
                if self.is_keyword(temp):
                    logging.log(logging.DEBUG, ['关键字', temp])
                    self.tokens.append(Token(0, temp))
                else:
                    logging.log(logging.DEBUG, ['标识符', temp])
                    self.tokens.append(Token(1, temp))
                i = self.skip_blank(i)
            # 如果是数字开头
            elif self.content[i].isdigit():
                temp = ''
                while i < len(self.content):
                    if self.content[i].isdigit() or (self.content[i] == '.' and self.content[i + 1].isdigit()):
                        temp += self.content[i]
                        i += 1
                    elif not self.content[i].isdigit():
                        if self.content[i] == '.':
                            logging.log(logging.ERROR, [
                                        'float number error!', self.content[i]])
                            exit()
                        else:
                            break
                logging.log(logging.DEBUG, ['常量', temp])
                self.tokens.append(Token(2, temp))
                i = self.skip_blank(i)
            # 如果是分隔符
            elif self.content[i] in delimiters:
                logging.log(logging.DEBUG, ['分隔符', self.content[i]])
                self.tokens.append(Token(4, self.content[i]))
                # 如果是字符串常量
                if self.content[i] == '\"':
                    i += 1
                    temp = ''
                    while i < len(self.content):
                        if self.content[i] != '\"':
                            temp += self.content[i]
                            i += 1
                        else:
                            break
                    else:
                        logging.log(logging.ERROR, 'error:lack of \"')
                        exit()
                    logging.log(logging.DEBUG, ['常量', temp])
                    self.tokens.append(Token(5, temp))
                    logging.log(logging.DEBUG, ['分隔符', '\"'])
                    self.tokens.append(Token(4, '\"'))
                i = self.skip_blank(i + 1)
            # 如果是运算符
            elif self.content[i] in operators:
                # 如果是++或者--
                if (self.content[i] in ['+', '-']) and self.content[i + 1] == self.content[i]:
                    logging.log(logging.DEBUG, [
                                '自加自减运算符', self.content[i] * 2])
                    self.tokens.append(Token(3, self.content[i] * 2))
                    i = self.skip_blank(i + 2)
                # 如果是>=或者<=
                elif (self.content[i] in ['>', '<', '!']) and self.content[i + 1] == '=':
                    logging.log(logging.DEBUG, ['运算符', self.content[i] + '='])
                    self.tokens.append(Token(3, self.content[i] + '='))
                    i = self.skip_blank(i + 2)
                # 其他
                else:
                    logging.log(logging.DEBUG, ['一般运算符', self.content[i]])
                    self.tokens.append(Token(3, self.content[i]))
                    i = self.skip_blank(i + 1)
            elif self.skip_blank(i) == i:
                logging.log(logging.ERROR, ['未知符号', self.content[i]])
                i += 1


# 词法辅助函数,结果输出到当前目录的文件下
def output(output_file=False):
    lexer = Lexer()
    lexer.main()
    if output_file:
        output = open('lexer.txt', 'w')
        for token in lexer.tokens:
            output.write('(%s, %s) \r\n' % (token.type, token.value))
        output.close()


if __name__ == '__main__':
    # file_name = sys.argv[1]
    file_name = r'D:\6.Code\Java\divideAndconquer\src\main.java'
    with open(file_name, 'r', encoding="utf-8")as f:
        content = f.read()
    lexer = Lexer(content)
    lexer.main()
    logging.log(logging.INFO, "Completed!")
