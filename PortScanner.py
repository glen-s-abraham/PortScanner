import socket
import optparse
import threading


def firstThousand(host,start,end):

    for port in range(start,end):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(2)
        if not(s.connect_ex((host,port))):
            print('port',port,'is open')
        s.close()
def userPorts(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
    if not (s.connect_ex((host, int(port)))):
        print('port', port, 'is open')
    else:
        print('port', port, 'is closed')
    s.close()

def portScan(host,ports):

    if ports=='default':
        print('Scanning first 1000 well known ports in',host,'...')
        t1=threading.Thread(target=firstThousand,args=(host,1,205))
        t1.start()
        t2 = threading.Thread(target=firstThousand, args=(host, 205, 410))
        t2.start()
        t3 = threading.Thread(target=firstThousand, args=(host, 410, 615))
        t3.start()
        t4 = threading.Thread(target=firstThousand, args=(host, 615, 820))
        t4.start()
        t5 = threading.Thread(target=firstThousand, args=(host, 820, 1025))
        t5.start()

    else:
        print('Scanning user defined ports in', host, '...')
        ports=ports.split(',')

        for port in ports:
            t = threading.Thread(target=userPorts, args=(host,port))
            t.start()


if __name__ == "__main__":
    parser = optparse.OptionParser("usage:program -H <host> -p <ports>")
    parser.add_option("-H",dest='hostname',type='string',help='Enter host name or default host will be taken as 127.0.0.1',default='127.0.0.1')
    parser.add_option("-p",dest='ports',type='string',help='[Optional] Enter ports seperated by commas or first 1000 ports will be Scanned by default',default='default')
    options,arg = parser.parse_args()
    host=options.hostname
    ports=options.ports
    portScan(host,ports)


