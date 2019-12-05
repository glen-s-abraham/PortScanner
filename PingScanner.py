
import pexpect
ipstart=str(input("Enetr starting ip:"))
ipstart=ipstart[0:ipstart.rindex('.',1)]
lim=int(input('Enter limit'))
livehost=[]
print('scanning hosts...')
for i in range(1,lim):
        ip=ipstart+"."+str(i)
        cmd='ping -c 1 '+ip
        child=pexpect.run(cmd)
        if not(child.find('Host Unreachable')>0):
                livehost.append(ip)
print('live hosts')
for host in livehost:
        print(host)

