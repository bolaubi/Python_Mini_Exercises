#####  Seven Segment  #####

def seven_segment():
    logo_seven = ['''
            
        ██████╗ ███████╗███╗   ██╗███████╗    ███████╗███████╗██╗   ██╗███████╗███╗   ██╗    ███████╗███████╗ ██████╗ ███╗   ███╗███████╗███╗   ██╗████████╗
        ██╔══██╗██╔════╝████╗  ██║██╔════╝    ██╔════╝██╔════╝██║   ██║██╔════╝████╗  ██║    ██╔════╝██╔════╝██╔════╝ ████╗ ████║██╔════╝████╗  ██║╚══██╔══╝
        ██████╔╝█████╗  ██╔██╗ ██║███████╗    ███████╗█████╗  ██║   ██║█████╗  ██╔██╗ ██║    ███████╗█████╗  ██║  ███╗██╔████╔██║█████╗  ██╔██╗ ██║   ██║   
        ██╔══██╗██╔══╝  ██║╚██╗██║╚════██║    ╚════██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║╚██╗██║    ╚════██║██╔══╝  ██║   ██║██║╚██╔╝██║██╔══╝  ██║╚██╗██║   ██║   
        ██████╔╝███████╗██║ ╚████║███████║    ███████║███████╗ ╚████╔╝ ███████╗██║ ╚████║    ███████║███████╗╚██████╔╝██║ ╚═╝ ██║███████╗██║ ╚████║   ██║   
        ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝    ╚══════╝╚══════╝  ╚═══╝  ╚══════╝╚═╝  ╚═══╝    ╚══════╝╚══════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝   ╚═╝   
                                                                                                                                                            
        ''']
    number_ = {
        '0': [' __ ', '|  |', '|__|'],
        '1': ['    ', '   |', '   |'],
        '2': [' __ ', ' __|', '|__ '],
        '3': [' __ ', ' __|', ' __|'],
        '4': ['    ', '|__|', '   |'],
        '5': [' __ ', '|__ ', ' __|'],
        '6': [' __ ', '|__ ', '|__|'],
        '7': [' __ ', '   |', '   |'],
        '8': [' __ ', '|__|', '|__|'],
        '9': [' __ ', '|__|', ' __|']
    }
    while True:
        print(logo_seven[0])
        print()
        num_input = input("Input your number : ")
        abstract_ = [number_[k] for k in num_input]

        for l in range(3):  # Creating each single row
            container = list()  # Creating a temporary container
            for part in abstract_:
                # Append each part of the number starting from the top row to the bottom row, there are 3 rows in total
                container.append(part[l])
            print(' '.join(container))  # butuh d join kalo ga ada petiknya
        askuser = input('Do you want to play again? (y/n) : ')
        if askuser == 'y':
            continue
        elif askuser == 'n':
            print('Game Over, Starting over... ')
            break


seven_segment()
