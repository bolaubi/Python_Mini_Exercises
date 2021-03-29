#####  Time Converter Benedict Laiman  #####

# First Method
def timeConverter(seconds):
    secs = abs(int(seconds))
    if secs > 359999:
        return 'Invalid Input'
    hh = secs // 3600
    mm = (secs % 3600) // 60
    ss = (secs % 3600) % 60
    time_list = [hh, mm, ss]
    time_disp = ['0', '0', ':', '0', '0', ':', '0', '0']

    if hh < 10:
        time_disp[1] = str(hh)
    else:
        time_disp[0] = str(hh // 10)
        time_disp[1] = str(hh % 10)
    if mm < 10:
        time_disp[4] = str(mm)
    else:
        time_disp[3] = str(mm // 10)
        time_disp[4] = str(mm % 10)
    if ss < 10:
        time_disp[7] = str(ss)
    else:
        time_disp[6] = str(ss // 10)
        time_disp[7] = str(ss % 10)

    return f"\"{''.join(time_disp)}\""

print(timeConverter(-3600))

# # Second Method
# def timeConverter(seconds):
#     secs = abs(int(seconds))
#     if secs > 359999:
#         return 'Invalid Input'
#     hh = secs // 3600
#     mm = (secs % 3600) // 60
#     ss = (secs % 3600) % 60
#     return '"%02d:%02d:%02d"' % (hh, mm, ss)
# print(timeConverter(-3600))






