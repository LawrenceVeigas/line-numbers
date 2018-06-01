
# Open the file in which your original code exists
with open("test.txt", "r") as obj:
    # Read the contents as a line so that each line is a value in a list
    lines = obj.readlines()

    # While the test file is open, open the test2 file where you'd want to save the code along with line numbers.
    # You can do it in the same file too if you like.
    with open("test2.txt", "r+") as obj2:
        # to_display is basically to output our file code block on the terminal
        to_display = ""

        for n in range(1,len(lines)+1):
            # The actual string we want to write in the test2 file.
            to_write = ""

            # Things get a bit tricky because the values in the list start with index 0, however, we want the line number to begin with 1. Can you grasp what I've done in the next few lines of code?
            if(n==1):
                string_to_attach = lines[0]
                # Just some minor logic to indent the file in a convention accepted at my workplace
                if "    " in string_to_attach:
                    string_to_attach = string_to_attach.replace("    ", "  ")

            if(n!=1) and (n<=len(lines)):
                string_to_attach = lines[n-1]
                if "    " in string_to_attach:
                    string_to_attach = string_to_attach.replace("    ", "  ")

            # So another tricky situation arises because the line numbers 1, 10, 100 will cause the code to be indented differently, we need to handle the spaces according to the digits in the line numbers
            count = 0
            number = n
            while (number > 0):
              number = number//10
              count = count + 1

            if(count==1):
                # If line number is a single digit number, add 3 spaces
                to_write = str(n) + "   " +string_to_attach

            if(count==2):
                # If line number is a double digit number, add 2 spaces
                to_write = str(n) + "  " + string_to_attach

            if(count==3):
                # If line number is a triple digit number, add 1 space
                to_write = str(n) + " " + string_to_attach

            to_display += to_write
            obj2.write(to_write)
        print(to_display)
