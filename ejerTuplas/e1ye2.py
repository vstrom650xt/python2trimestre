import operator
import re
if __name__ == '__main__':
    result_list = []
    diccionario1 = dict()
    diccionario2 = dict()
    tuple = tuple()
    patron_regex = re.compile( r"\b\w+@\w+\.\w+\b")
    email_regex = re.compile(r"[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*@[a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*[.][a-zA-Z]{2,5}")
    with open('mbox-short.txt', 'r') as archivo:
        for line in archivo:
            if line.startswith("From:") and email_regex.search(line):
                line2 = line.replace("From: ","")
                result_list.append(line.strip())
                #print(line2.strip())
                diccionario1[line2] = diccionario1.get(line2, 0) + 1
                indice = line2.find('@')
                indice2 = line2.find(' ',indice)
                patron = line2[indice:indice2]
                diccionario2[patron] = diccionario2.get(patron, 0) + 1

    tuple = diccionario2.items()
    print(tuple)
    a=sorted(tuple,key=operator.itemgetter(1),reverse=True)
    print(a[0])
    # print(diccionario1)
    print(tuple)




    # for l in result_list:
    #     while(result_list.count(l)>1):
    #         result_list.remove(l)
    # print(len(result_list))
    #






    #print(result_list)
