# ubuntu 삭제하는 법
- rm -rf jssdeploy(프로젝트명)

# 배포 step
- sudo apt-get update
- sudo apt-get install build-essential

#### sudo: 관리자계정으로서 act를 하겠다.

#### 새 컴퓨터에 python을 까는 이치
#### ubuntu 환경에서 새로 까는 것.

- sudo apt-get install virtualenv
#### 파이썬 가상환경을 까는것

- cd jssdeploy
- cd jasoseolprojects
#### 여기에 manage.py에 가상환경을 깔 것

- virtualenv -p python3 venv
- source venv/bin/activate
- cd .. => requirements.txt 위치 확인 후
- pip install -r requirements.txt
#### (install 속도가 겁나 빨라 = king buntu)

#### manage.py있는 경로에서
- python manage.py migrate

- pip install uwsgi
- sudo vi uwsgi.ini
#### i 누른 후 
[uwsgi]
chdir=/home/ubuntu/jssdeploy/jasoseolproject
module=jasoseolproject.wsgi:application
master=True
pidfile=/tmp/project-master.pid
vacuum=True
max-requests=5000
daemonize=/home/ubuntu/jssdeploy/jasoseolproject/django.log
home=/home/ubuntu/jssdeploy/jasoseolproject/venv
virtualenv=/home/ubuntu/jssdeploy/jasoseolproject/venv
socket=/home/ubuntu/jssdeploy/jasoseolproject/uwsgi.sock
chmod-socket=666 
#### 이거 복사하여 cmd창에 우클릭 -> 예쁘게 들어감

- (esc) + (:wq)+(enter)


- uwsgi --ini uwsgi.ini
- sudo apt-get install nginx
- sudo vi /etc/nginx/nginx.conf
#### http 웅앵 써줘야한다
- sudo vi /etc/nginx/sites-enabled/default 
#### 여기서 문서 또 수정해주고(경로)
- python manage.py collectstatic
#### => static 파일들을 모아준것.
- uwsgi --ini uwsgi.ini
- sudo service nginx reload
#### 퍼블릭 dns 복붙
