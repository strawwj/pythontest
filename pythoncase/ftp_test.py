from ftplib import FTP
host = input("请输入你的ip：")
#username = input("请输入你的用户名")
#mima = input("请输入你的密码：")
ftp = FTP('{}'.format(host))
#ftp.login(username,mina)
ftp.login()
while True:
    mingling = input("请输入你的命令：")
    if mingling == 'cd':
        c = input("请输入要到的路径：")
        ftp.cwd('{}'.format(c))
    if mingling == 'ls':
        ftp.retrlines('LIST')
    if mingling == 'put':
        d = input('请输入你要上传的文件')
        ftp.storbinary('STOR {}'.format(d),open('{}'.format(d),"rb"))
    if mingling == 'q':
        ftp.quit()
        break
#print(ftp)
#print(my_Ftp())    
