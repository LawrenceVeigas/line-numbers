
with open("test.txt", "r") as obj:
    lines = obj.readlines()

    with open("test2.txt", "r+") as obj2:
        to_display = ""
        for n in range(1,len(lines)+1):
            #print(lines[n])
            to_write = ""

            if(n==1):
                string_to_attach = lines[0]
                if "    " in string_to_attach:
                    string_to_attach = string_to_attach.replace("    ", "  ")

            if(n!=1) and (n<=len(lines)):
                string_to_attach = lines[n-1]
                if "    " in string_to_attach:
                    string_to_attach = string_to_attach.replace("    ", "  ")

            #print(string_to_attach)

            count = 0
            number = n
            while (number > 0):
              number = number//10
              count = count + 1

            if(count==1):
                to_write = str(n) + "   " +string_to_attach
                print("m here now")

            if(count==2):
                to_write = str(n) + "  " + string_to_attach
                print("now count is 2")

            if(count==3):
                to_write = str(n) + " " + string_to_attach
                print("now count is 3")

            to_display += to_write
            obj2.write(to_write)
        print(to_display)
