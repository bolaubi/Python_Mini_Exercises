
# 1 Right triangle - hollow
def segitiga_kopong():
    nums = abs(int(input("Input the row dimension for the triangle : ")))
    star_container = ''
    if nums <= 1:
        star_container += '*'
    elif nums >= 2:
        star_container += '*'
        star_container += '\n'
        spacer = 0
        if nums == 2:
            star_container += '**'
        if nums >= 3:
            for i in range(nums - 2):
                star_container += '*'
                star_container += (' ' * spacer)
                star_container += '*'
                star_container += '\n'
                spacer += 1
            star_container += ('*' * nums)
    print(star_container)
segitiga_kopong()

# 1 Right triangle - hollow and mirrored
def segitiga_kopong2():
    nums = abs(int(input("Input the row dimension for the triangle : ")))
    star_container = ''
    if nums <= 1:
        star_container += '*'
    elif nums >= 2:
        star_container += '*'
        star_container += '\n'
        spacer = 0
        if nums == 2:
            star_container += '**'
        if nums >= 3:
            for i in range(nums - 2):
                star_container += '*'
                star_container += (' ' * spacer)
                star_container += '*'
                star_container += '\n'
                spacer += 1
            star_container += ('*' * nums)
        star_container += '\n'
        spacer = nums - 3
        for j in range(nums - 2):
            star_container += '*'
            star_container += (' ' * spacer)
            star_container += '*'
            star_container += '\n'
            spacer -= 1
        star_container += '*'
    print(star_container)
segitiga_kopong2()





