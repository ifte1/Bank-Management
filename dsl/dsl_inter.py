import sys

if len(sys.argv) != 2:
    sys.exit(1)
    

functions = {'added': lambda a, b: a + b,
             'out': lambda a, b: a - b}
with open(sys.argv[1]) as file:
    #define empty basket
    basket_situation = {"apple": 0,
               "banana": 0,
               "mango": 0,
               "orange": 0
               }




    for each_line in file:
        each_line = each_line.strip()
        if not each_line or each_line[0] == '~':
            continue
        qus_part = each_line.split()
        if qus_part[0] == 'How':
            print("There are " + str(basket_situation[qus_part[2]]) + " " + qus_part[2] + " in the basket.")


        else:
            a = basket_situation[qus_part[1]]
            b = int(qus_part[0])
            basket_situation[qus_part[1]] = functions[qus_part[2]](a, b)