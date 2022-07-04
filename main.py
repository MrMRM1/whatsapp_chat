import codecs
import re
import sys

from default_html import *

input1 = sys.argv[1]
output = input1[:-4] + ".html"


def open_file(file_name, typ):
    return codecs.open(file_name, typ, encoding="utf-8")


def progressbar(it, prefix="", size=60, out=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size * j / count)
        print(f"{prefix}[{u'█' * x}{('.' * (size - x))}] {j}/{count}", end='\r', file=out, flush=True)

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    print("\n", flush=True, file=out)


with open_file(output, "w") as f:
    f.write(head_html)

with open_file(input1, "r") as f:
    f_read = f.readlines().copy()

file_output = open_file(output, 'a')

for i in progressbar(range(len(f_read)-1)):
    data = f_read[i]
    if data:
        try:
            time = re.findall(r"\d{2}:\d{2}", data)[0]
            datatime = re.findall(r'^.*,', data)[0][:-1]
        except:
            file_output.write(continue_message(data))
            continue

        try:
            user = re.findall(r'\d{2}.-.*: ', data)[0][5:][:-1]
        except:
            file_output.write(message_service(data))
            continue

        massage = re.findall(r': .*', data)[0][1:]

        if user:
            file_output.write(message_html(user, datatime, time, massage))
        else:
            file_output.write(continue_message(data))

file_output.close()

