import codecs
import re
from tqdm import trange
from colorama import init, Fore, Style
from default_html import *
init()
print(Style.BRIGHT+Fore.GREEN+"""
                    chate whatsapp         

            baraye dashtane khorogi behtar

            hatman file rahnama ro bekhonin


"""+Fore.MAGENTA)


input1 = input("    name file chate whatsapp ro bedone .txt vared konin: ")+".txt"
input2 = input1[:-4]+".html"


def open_file(file_name, typ):
    return codecs.open(file_name, typ, encoding="utf-8")


file_input = open_file(input1, "r")
file_output = open_file(input2, "w")
file_output.write(head_html)
file_output.close()
file_output = open_file(input2, 'a')

f_read = file_input.readlines()
name = f_read[2].split()[3]

m = 2
user1 = ''
user2 = ''
while 1:
    p = f_read[m].split()
    m += 1
    if name == p[3]:
        user1 = p[3][0]
    elif name != p[3]:
        user2 = p[3][0]
        break


print()
bar = trange(len(f_read)-1, bar_format="{l_bar}{bar}{n_fmt}/{total_fmt} [{elapsed}]")
for i in bar:
    data = f_read[i].split()
    massage = ' '.join(data[4:])
    if data != []:
        if len(data) > 1:
            c6 = re.findall("\d{2}:\d{2}", data[1])
            if c6 != []:
                if data[3][0] == user1:
                    file_output.write(massage_html(user1, data, massage))
                else:
                    file_output.write(massage_html(user2, data, massage))
            else:
                file_output.write(continue_massage(' '.join(data[0:])))
        else:
            file_output.write(continue_massage(' '.join(data[0:])))


print(Fore.YELLOW+"""
            --------------END!--------------
            ---                          ---
            ---by Mohammad Reza Mehrabany---
            ---                          ---
            ---     http://Mrmrm.ir      ---
            --------------------------------
""")


file_input.close()
file_output.close()
input()
