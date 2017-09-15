# coding:utf-8

from fabric.api import env, run
from fabric.operations import sudo

GIT_REPO = "https://github.com/xuepengs/blogproject.git"

env.user = 'ubuntu'
env.password = '3879245'

# 填写你自己的主机对应的域名
env.hosts = ['34.214.32.58']

# 一般情况下为 22 端口，如果非 22 端口请查看你的主机服务提供商提供的信息
env.port = '22'


def deploy():
    source_folder = '/home/xuepeng/sites/swordman.wang/blogproject'
    
    sudo('cd %s && git pull' % source_folder)
    sudo("""
        cd {} &&
        ../env/bin/pip install -r requirements.txt &&
        ../env/bin/python3 manage.py collectstatic --noinput &&
        ../env/bin/python3 manage.py migrate
        """.format(source_folder))
    sudo('systemctl start xuepeng')
    sudo('service nginx reload')
