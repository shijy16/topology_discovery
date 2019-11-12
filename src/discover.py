import os 
import networkx as nx
import subprocess

#166.111
#59.66
#183.172
#183.173
#101.5
def get_ip(cnt):
    return '101.6.' + str(cnt) + '.1'

def ping(cnt):
    ip = get_ip(cnt)
    print('ping',ip)
    popen = subprocess.Popen(['ping','-n', '1','-r','9','-w','500',ip], stdout = subprocess.PIPE)
    popen.wait()
    lines = popen.stdout.readlines()
    res = ''
    for i in range(0,len(lines)):
        line = lines[i].decode('gbk')
        line = line.strip('\n')
        if line == '':
            continue
        if line.find('TTL') != -1:
            print('ALive')
            i+=1
            line = lines[i].decode('gbk')
            line = line.strip('\n')
            while(len(line) > 2):
                res += line
                i+=1
                if i >= len(lines):
                    break
                line = lines[i].decode('gbk')
                line = line.strip('\n')
    return res

if __name__ == '__main__':
    with open('res2.txt','w',encoding='gbk') as f:
        for i in range(0,255):
            try:
                res = ping(i)
                if len(res) > 2:
                    f.write(res + 'END\n')
            except:
                print('ERROR')
