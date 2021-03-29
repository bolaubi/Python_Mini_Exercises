#####  Hourglass Benedict Laiman  #####

numstar_container = ""
int_input_num = int(input("Input the dimension (rows) : ")) // 2
star_counter = 1
space_counter = int_input_num
star_counter = int_input_num + int_input_num - 1
for _ in range(int_input_num - 1):
    numstar_container += (("  ") * (int_input_num - space_counter))
    numstar_container += (" *") * (star_counter)
    numstar_container += "\n"
    space_counter -= 1
    star_counter -= 2

for _ in range(int_input_num):
    numstar_container += (("  ") * (int_input_num - space_counter))
    numstar_container += (" *") * star_counter
    numstar_container += "\n"
    space_counter += 1
    star_counter += 2

# print(numstar_container)
#
#
#
# Input the dimension (rows) : 15
#  * * * * * * * * * * * * *
#    * * * * * * * * * * *
#      * * * * * * * * *
#        * * * * * * *
#          * * * * *
#            * * *
#              *
#            * * *
#          * * * * *
#        * * * * * * *
#      * * * * * * * * *
#    * * * * * * * * * * *
#  * * * * * * * * * * * * *
#
#
# Process finished with exit code 0





















