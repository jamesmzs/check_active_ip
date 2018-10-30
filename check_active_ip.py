#!/bin/env python
#-*-coding=utf-8-*-
#获取网络内存活ip地址
import subprocess

def address():
  begen='192.168.213.240'
  end='192.168.213.251'
  activefile='/opt/active-iplist.txt'
  unactivefile='/opt/unactive-iplist.txt'

  data=subprocess.Popen(["fping","-g","-a",begen,end],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
  out=data.stdout.readlines()

  result=len(out)
  if result == 0:
       print('网络内无存活主机，请查看脚本是否赋予网络地址参数')
     
  else:
        lists=subprocess.Popen(["fping","-g","-a",begen,end],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
        active=lists.stdout.readlines()
        unactive=lists.stderr.readlines()

        for i in range(len(active)):
          iplist=str(active[i]).replace("b'",'').replace("\\n'",'')
          with open(activefile,'a') as f:
            f.writelines(iplist+'\n')
  
        for err in range(len(unactive)):
          errcontent=str(unactive[err])
          with open(unactivefile,'a') as f:
            f.writelines(errcontent+'\n')
def finish():
    print('检查完成,数据已写入txt文件')


address()

if __name__=="__main__":
   finish()
