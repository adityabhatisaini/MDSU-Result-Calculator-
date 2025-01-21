# define all codes in the particular function
def bsc_3(obt_mks):
    total_mks=2025
    cal_per= round(obt_mks/(total_mks/100),2)
    print(f'Final percentage is:{cal_per}')
    return total_mks

user_input=int(input('Enter your obtained marks'))
bsc_3(user_input)