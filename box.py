import asyncio

import aiotieba

import time

import logging
logging.disable(logging.WARNING)


import time

BDUSS = "输入BDUSS"


async def main():
    start_time = time.time()  # 记录程序开始执行的时间
    async with aiotieba.Client(BDUSS) as client:
        uid = 输入用户贴吧主页id
        user =  await client.tieba_uid2user_info(uid)
        print("查询用户：", user)
        print("查询中...")
        pn = 1
        with open("./output.txt", "w", encoding="utf-8") as f:
            while(1):
                user_post = await client.get_user_posts(str(user), pn)
                if user_post.objs == []:
                    right = await client.get_user_posts(str(user), pn + 1)
                    if right.objs == []:
                        f.write("查询完毕, 共查询{}页\n".format(pn - 1))
                        print("查询完毕, 共查询{}页\n".format(pn - 1))
                        break
                
                for x in user_post.objs:
                    tieba_name = await client.get_fname(x.fid)
                    for y in x:
                        timeArray = time.localtime(y.create_time)
                        otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
                        link = "https://tieba.baidu.com/p/{}?pid={}&cid=0#{}".format(y.tid, y.pid, y.pid)
                        f.write("贴吧名: {} 链接: {} 回复时间: {}\n".format(tieba_name, link, otherStyleTime))
                        f.write("   {:}\n".format(y.text))
                pn += 1
                if (pn % 20 == 0):
                    print("查询页数", pn)
    query_end_time = time.time() - start_time  # 记录查询结束与开始的时间差
    print("总查询时间: {:.2f}秒".format(query_end_time))
asyncio.run(main())
