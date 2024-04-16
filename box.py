import asyncio

import aiotieba

import logging
logging.disable(logging.WARNING)

BDUSS = "输入你的BDUSS"

async def main():
    async with aiotieba.Client(BDUSS) as client:
        uid = 待查询的用户贴吧id
        user =  await client.tieba_uid2user_info(uid)
        print("查询用户：", user)
        print("查询中...")
        pn = 0
        with open("./output/wuti.txt", "w", encoding="utf-8") as f:
            while(1):
                user_post = await client.get_user_posts(str(user), pn)
                if user_post.objs == []:
                    f.write("查询完毕\n")
                    break
                
                for x in user_post.objs:
                    for y in x:
                        tieba_name = await client.get_fname(y.fid)
                        post_info = await client.get_posts(y.tid)
                        f.write("贴吧名: {} 主题帖id: {} 主题帖: {}\n".format(tieba_name, y.tid, post_info.thread.title))
                        f.write("   {:}\n".format(y.text))
                pn += 1
            # 终端输出ending表示查询完毕
            print("ending")
asyncio.run(main())
