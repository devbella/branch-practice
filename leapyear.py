for i in range(1, 3000+1):	
    if (i%4==0 and i%100!=0) or (i%400==0):
        print('LEAP YEAR!')
    else:
        print('NOT a LEAP YEAR!')
