import asyncio

import aiotieba

BDUSS = "输入你的BDUSS"

async def main():
    async with aiotieba.Client(BDUSS) as client:
        # 结果输出到文件output.txt中
        with open("output.txt", "w", encoding="utf-8") as f:
            tid = 待查询的帖子tid
            pn = 1
            while (1):
                posts = await client.get_posts(tid, pn)
                if pn == 1:
                    f.write(f"贴吧名: {posts.thread.fname}\n\n")
                    f.write(f"标题: {posts.thread.title}\n\n")
                    f.write(f"发帖人: {posts.thread.user}\n\n")
                    f.write("回复数： {}\n\n".format(posts.thread.reply_num))
                    f.write("======================\n")
                
                for post in posts:
                    f.write("楼层： {:<5}用户名: {:<20}  回复: {}\n\n".format(post.floor, post.user.user_name, post.text))
                    comments = await client.get_comments(tid, post.pid)
                    for comment in comments:
                        f.write("楼中楼：             用户名: {:<20}   回复: {}\n\n".format(comment.user.user_name, comment.text))
                    f.write("======================\n")
                if posts.has_more:
                    pn += 1
                else:
                    break
                        

asyncio.run(main())
