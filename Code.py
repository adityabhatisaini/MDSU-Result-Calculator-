# define all codes in the particular function
def bsc_3(obt_mks):
    total_mks=2025
    cal_per= round(obt_mks/(total_mks/100),2)
    return f'Final percentage is:{cal_per}'

user_input=int(input('Enter your obtained marks'))
print(bsc_3(user_input))