import urllib.request

fhand = urllib.request.urlopen('http://127.0.0.1:9000/?data=value&data1=value1&data3=value3')
for line in fhand:
    print(line.decode().strip())