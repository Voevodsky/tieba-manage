import asyncio

import aiotieba

import logging
logging.disable(logging.WARNING)

BDUSS = "你的BDUSS"

async def main():
    async with aiotieba.Client(BDUSS) as client:
        uid = 待用户贴吧id
        user =  await client.tieba_uid2user_info(uid)
        print("查询用户：", user)
        print("查询中...")
        pn = 0
        with open("./output/wuti1.txt", "w", encoding="utf-8") as f:
            while(1):
                user_post = await client.get_user_posts(str(user), pn)
                if user_post.objs == []:
                    f.write("查询完毕, 共查询{}页\n".format(pn))
                    print("查询完毕, 共查询{}页\n".format(pn))
                    break
                
                for x in user_post.objs:
                    tieba_name = await client.get_fname(x.fid)
                    for y in x:
                        f.write("贴吧名: {} 主题帖id: {} 回复贴id: {}\n".format(tieba_name, y.tid, y.pid))
                        f.write("   {:}\n".format(y.text))
                pn += 1
                if (pn % 20 == 0):
                    print("查询页数", pn)
asyncio.run(main())
