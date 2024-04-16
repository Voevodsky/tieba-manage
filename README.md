# 基于aiotieba的各种小工具
## block.py 用于封禁用户
```
<2024-04-16 20:28:02.061> [INFO] [block] Suceeded. args=(1532319, 971612416) kwargs={'day': 封禁天数}
是否封禁成功：True/False 被封禁人用户名 
```
## reply_all.py 利用某个帖子的tid(可在网页链接中看到)，爬取该主题帖的所有内容，包括所有楼层和楼中楼，结果输出在文件output.txt中，输出格式如下：
```
贴吧名: xxx

标题: xxxx

发帖人: xxx

回复数： xxx

======================
楼层： 1    用户名: xxx                  回复: xxx

======================
楼层： 2    用户名: xxx                  回复: xxx

楼中楼：             用户名: xxx                回复: xxx

楼中楼：             用户名: xxx                回复: xxx
=====================
..............
```
## box.py 根据用户贴吧id获取某个用户的所有回复，结果输出在文件output.txt中,输出格式如下：
```
贴吧名: xxx 主题帖id: xxxxxx 主题帖: xxx
   回复 xxx :xxx
贴吧名: xxx 主题帖id: xxxxxx 主题帖: xxx
   回复 xxx :xxx
贴吧名: xxx 主题帖id: xxxxxx 主题帖: xxx
   回复 xxx :xxx
........
```
