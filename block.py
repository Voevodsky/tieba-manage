import asyncio

import aiotieba

BDUSS = "在此处输入你的BDUSS"

async def main():
    async with aiotieba.Client(BDUSS) as client:
        user_info = await client.tieba_uid2user_info("输入用户主页额贴吧id")
        block_fid = await client.get_fid("输入贴吧名")
        # 结果
        com = await client.block(block_fid, user_info.user_id, day="输入封禁天数")
        print("是否封禁成功：{:}".format(com))

asyncio.run(main())
