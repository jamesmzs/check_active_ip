#!/bin/env python
#-*-coding=utf-8-*-
#活跃ip地址写入excel
import xlwt
from xlwt import Workbook
#import check_active_ip

def excel():
  iplist=Workbook(encoding='utf-8')
  sheet1=iplist.add_sheet('活跃的地址',cell_overwrite_ok=True)
  styleBlueBkg=xlwt.easyxf('pattern: pattern solid, fore_colour ocean_blue; font: bold on')
  first_col=sheet1.col(0)
  first_col.width=256*20
  firstline='ip address'
  i=1

  activefile='/opt/active-iplist.txt'
  with open(activefile,'r') as f:
    lines=f.readlines()
    for line in lines:
      sheet1.write(0, 0,firstline,  styleBlueBkg)
      sheet1.write(i,0,line)
      i=i+1
  iplist.save('/opt/result.xls')

def finish():
    print('数据已生成excel表格')

excel()
finish()
