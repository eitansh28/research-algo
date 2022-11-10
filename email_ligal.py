import re


def reco_ligal_email(file: str):
    with open(file) as f:
        text = f.read()
        bad_adds = []
        good_adds = re.findall("[ \'\n]+[\w]+[\._-]?[\w]+[@]+[\w]+[-]?[\w]+[.]+[\w]{2,}", text)
        temp_list = re.findall("[ \\n]+[\S]+[@]+[\S]+[.]+[\S]{1,}", text)
        for i in temp_list:
            if i not in good_adds:
                bad_adds.append(i)
        print([x[1:] for x in good_adds])
        print([x[1:] for x in bad_adds])


reco_ligal_email("email_example.txt")