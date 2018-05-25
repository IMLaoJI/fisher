# error code description

## start with 1
means common exception
10000 : parameter exception
10080 : email that used to register has been taken
10081 : nickname that used to register has been taken

## start with 2
means user exceptio

安装教程
pipenv install
安装列表是通过读取pipfile, pipfile.lock文件实现的,
如果没有这两个文件就根据requirements.txt生成pipfile和pipfile.lock并读取.

pipenv lock -r --dev > requirements.txt
用命令生成requirements 文件

只安装在开发环境中
pipenv install --dev requests

通过requirements.txt安装包
pipenv install -r requirements.txt

---> 这样我们可以重用之前的requirement.txt
文件来构建我们新的开发环境，可以把我们的项目顺利的迁到pipenv。

pipenv lock
生成lockfile