import asyncio

import aiotieba

import time

import logging
logging.disable(logging.WARNING)

BDUSS = "输入你的BDUSS"

async def main():
    start_time = time.time()  # 记录程序开始执行的时间
    async with aiotieba.Client(BDUSS) as client:
        uid = 输入待查询用户贴吧id
        user =  await client.tieba_uid2user_info(uid)
        print("查询用户：", user)
        print("查询中...")
        pn = 0
        with open("output.txt", "w", encoding="utf-8") as f:
            while(1):
                user_post = await client.get_user_posts(str(user), pn)
                if user_post.objs == []:
                    f.write("查询完毕, 共查询{}页\n".format(pn - 1))
                    print("查询完毕, 共查询{}页\n".format(pn - 1))
                    break
                
                for x in user_post.objs:
                    tieba_name = await client.get_fname(x.fid)
                    for y in x:
                        f.write("贴吧名: {} 主题帖id: {} 回复贴id: {}\n".format(tieba_name, y.tid, y.pid))
                        f.write("   {:}\n".format(y.text))
                pn += 1
                if (pn % 20 == 0):
                    print("查询页数", pn)
    query_end_time = time.time() - start_time  # 记录查询结束与开始的时间差
    print("总查询时间: {:.2f}秒".format(query_end_time))
asyncio.run(main())
