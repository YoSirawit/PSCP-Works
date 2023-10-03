"""Remove Tag"""

def main(link):
    """Main Function"""

    tag = ""
    check = 0
    set_tag = set()

    for i in link:
        if i == ">":
            tag += ">"
            check = 0
            set_tag.add(tag)
            print(set_tag)
            tag = ""
        elif i == "<" or check == 1:
            tag += i
            check = 1

    for j in set_tag:
        link = link.replace(j, " ")

    newlink = link.split(" ")
    remem = 0
    for k in range(len(newlink)):
        if newlink[k] == "":
            remem += 1

    for _ in range(remem):
        newlink.remove("")

    print(newlink)

main(input())
