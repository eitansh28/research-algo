import re


def reco_ligal_email(file: str):
    """"
    >>> reco_ligal_email("email_example1.txt")
    ['NoMistake1@gmail.com', 'eitan76543@gmail.com', 'evn@gmail.com', 'abc_def@mail.com', 'abc.def@mail-archive.com']
    ['notgood1@bezeq.b', 'Notgood2@bezeq-.int', 'gsgs@fsgsg.v', 'abc#def@mail.com', 'abc..def@mail.com', '.abc@mail.com', 'abc.def@mail#archive.com']
    >>> reco_ligal_email("email_example2.txt")
    ['eitan76543@gmail.com', 'erelsegal_halevi@gmail.com', 'erelsegalhalevi@gmail.com', 'tamar-kar@bezeq.int']
    ['eitan76543-@gmail.com', 'erelsegalhalevi@gmail.c', 'erelsegal..halevi@gmail.com', 'tamar--kar@bezeq.i']
    >>> reco_ligal_email("email_example3.txt")
    ['stam2@bezeq.int', 'eitan@gmail.com']
    ['stam-2@bezeq.i', 'bvcbcbc@gdgdgd--.v', '-e5@h.com']
    """

    with open(file) as f:
        text = f.read()
        bad_adds = []
        good_adds = re.findall("[ \'\n]+[\w]+[\._-]?[\w]+[@]+[\w]+[-]?[\w]+[.]+[\w]{2,}", text)  #Search for suitable addresses according to the rules
        temp_list = re.findall("[ \\n]+[\S]+[@]+[\S]+[.]+[\S]{1,}", text)     #Search of all addresses that looked like an email address
        for i in temp_list:
            if i not in good_adds:   #List only the invalid addresses
                bad_adds.append(i)
        print([x[1:] for x in good_adds])   #Printing the list (without space or /n)
        print([x[1:] for x in bad_adds])    #Printing the list (without space or /n)

# Running examples:
# reco_ligal_email("email_example1.txt")
# reco_ligal_email("email_example2.txt")
# reco_ligal_email("email_example3.txt")


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)