fh = open('Prac-3.txt','w')
import random
length = 10
password_list='QWERTYUIOPLKJHGFDSAZXCVBNMqwertyuioplkjhgfdsazxcvbnm0123456789!@#$%^&*()<>~=+-_*/'
password=''
i=1
while i<=length:
    password = password + random.choice(password_list)
    i+=1
fh.write(str(password))
fh.close()
