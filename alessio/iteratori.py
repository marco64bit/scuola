
def foo():
    yield 'prima chiamata'
    yield 'seconda chiamata'


for x in foo():
    print(x)

# ===============================================
print("\n"*5)

text = """
Titolo

sottotitolo

testo libero
con accapi e punti.
linea troppo lunga mi va a capo da sola

ciao.
"""


def line_splitter(line, max_length):
    """
    Torna una stringa con a capi ogni volta che la linea supera la lunghezza `max_length` di caratteri
    """
    chunked_line = "\n    ".join([line[i:i + max_length]
                                 for i in range(0, len(line), max_length)])
    return chunked_line


def text_to_line(text, max_length=None):
    """
    Divide un testo in linee basandosi sugli a capi.\n
    Se max_length è definito andrà a capo anche quando 
    una linee supera max_length in caratteri
    """
    lines = text.split('\n')
    for line_number, line in enumerate(lines):
        if max_length:
            line = line_splitter(line, max_length)
        yield line


# uso l'iteratore aggiungendoci un pò di grafica prima
for line_num, line_text in enumerate(text_to_line(text, max_length=20)):
    print(f"[{line_num}] {line_text}")


print("\n"*5)


long_text = """
Titolo

Sottotitolo

sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj.

asdas oiaj asij aasdasd
sadasdasdasd.

sdasdkasidjasj asoi 
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj.

sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasjsad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj
sad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasjsad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasjsad oasidj aosijdoisaj das
asdas doaisj doiajs dioasj oid
asdjaosijd aosij doais jaos
sad iojasj doiasjd ioasj


fine.

"""


def text_to_pages(text, page_line_num):
    """
    Suddivide un testo in pagine in base al page_line_num
    che è il numero massimo di linee per pagina
    """
    lines = text.split("\n")
    for x in range(0, len(lines), page_line_num):
        yield "\n".join(lines[x: x + page_line_num])


max_line_length = 30

prefix_len = 5
print(f'{"=" * (max_line_length + prefix_len + 1)}+')

# uso i due iteratori, prima divido in pagine, e poi in linee aggiungendo un pò di grafica con le print
for page_num, text in enumerate(text_to_pages(long_text, page_line_num=15)):

    page_text = f"[Pag {page_num + 1}]"
    print(f"{' ' * (max_line_length + len(page_text)- 2)} |")

    for line_num, line_text in enumerate(text_to_line(text, max_length=max_line_length)):
        prefix = f"[{str(line_num + 1).zfill(2)}]"
        print(f"{prefix} {line_text} {' ' * (max_line_length  - len(line_text))}|")

    print(f"{' ' * (max_line_length + len(page_text)- 2)} |")
    print(f"{' ' * (max_line_length + len(page_text)- 2)} |")
    print(f"{' ' * (max_line_length - 2)}{page_text} |")
    print(f"{'=' * (max_line_length + len(page_text)-1)}+")

# ===============================================
print("\n"*5)


def piramide(size, char):
    space_count = 1
    for char_multiplier in range(0, size, 2):
        pad = (round(size/2) - space_count)
        space_count += 1
        yield f'{" " * pad }{char}{char * char_multiplier}'


for char in piramide(10, '*'):
    print(char)

# ===============================================
print("\n"*5)


def albero(size, char, msg):
    space_count = 1
    for char_multiplier in range(0, size, 2):
        pad = (round(size/2) - space_count)
        space_count += 1
        yield f'{" " * pad }{char}{char * char_multiplier}'

    wood_width = round(size / 3)
    for x in range(2):
        pad = round((size) / 2 - wood_width / 2)
        yield f"{' ' * pad}{char * round(size / 3)}"

    yield " " * 10
    yield f"{' ' * (round(size/2) - round(len(msg) / 2))}{msg}"


for char in albero(30, '*', "Buon Natale!"):
    print(char)
