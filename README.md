OS:centos 7
python 版本：3.5


运行方式：

1.执行执行main脚本，会调用check_active_ip.py  excel.py（excel依赖于check_active_ip.py的执行）

2.本脚本已制作成“包”的形式，可在上级目录执行： python  check_active_ip （为方便以后使用该环境，制作成包）


3.借鉴该脚本，可修改check_active_ip.py文件中的网段地址范围


注意：该脚本依赖于fping命令，系统需要安装fping命令，而python 某些版本有fping的库，使用特定版本python开发该脚本，可直接使用fping库。

 

