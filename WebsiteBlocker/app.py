import time
from datetime import datetime as dt
temp_path='hosts'
hosts_path='\/etc\/hosts'
redirect='127.0.0.1'
websites=['www.reddit.com','www.facebook.com','www.pornhub.com','www.xhamster.com','www.myfreecams.com']
cy = dt.now().year
cm = dt.now().month
cd = dt.now().day

while True:
    if dt(cy,cm,cd,8) < dt.now() < dt(cy,cm,cd,12):
        print('test')
        with open(temp_path,'r+') as f:
            content = f.read()
            for website in websites:
                if website in content:
                    pass
                else: 
                    f.write(redirect + ' ' + website + '\n')
    else:
        with open(temp_path, 'r+') as f:
            content = f.readlines()
            f.seek(0)
            for ln in content:
                if not any(website in ln for website in websites):
                    f.write(ln)
            f.truncate()

    time.sleep(5)
