#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Guoyifan"
__pkuid__  = "1900011755"
__email__  = "guo2001yifan@163.com"
"""

import sys
import urllib
from urllib.request import urlopen


def retrieve_page(m):
    """ Retrieve the contents(bytes) of a web page.
        The contents is decoded to a string before returning it.
    """
    my_socket = urllib.request.urlopen(m[1])
    dta = my_socket.read().decode()
    my_socket.close()
    wcount(dta, int(m[2]))


def wcount(lines, topn):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line.
    """
    stan = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    n_lines = ''
    for i in lines:
        if i in stan:
            i = i.lower()
            n_lines += i
        else:
            n_lines += ' '
    lst = n_lines.split()
    s_lst = sorted(lst)
    n = len(s_lst)
    ans = {}
    for i in range(n):
        if i == 0:
            ans[s_lst[i]] = 1
        else:
            if s_lst[i] != s_lst[i-1]:
                ans[s_lst[i]] = 1
            else:
                ans[s_lst[i]] += 1
    n_ans = sorted(ans.items(), key=lambda x: x[1], reverse=True)
    for i in range(int(topn)):
        print(n_ans[i][0], end='\t')
        print(n_ans[i][1], end='\n')
    pass

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many(words count) to output. If not given,
              will output top 10 words')
        sys.exit(1)
    url = sys.argv[1]
    if len(sys.argv) == 2:
        topn = 10
    else:
        topn = int(sys.argv[2])
    try:
        web_file = urlopen(url)
        lines_byte = web_file.read()
        web_file.close()
        lines = bytes.decode(lines_byte)
        wcount(lines, topn)
    except urllib.request.URLError:
        sys.stdout.write('Web path unexist or denied request!')
    except ValueError:
        sys.stdout.write('Unsupported url format "{}" !'.format(url))
    except Exception:
        sys.stdout.write('Other unpredictable error, please ensure
                         the url starts with "http://" and check your
                         spelling')
