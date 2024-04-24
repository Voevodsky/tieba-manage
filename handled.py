import asyncio

import aiotieba as tb

STOKEN = "你的stoken"
BDUSS = "你的BDUSS"

from urllib import parse

async def main():
    account = tb.Account(BDUSS, STOKEN)
    async with tb.Client(account=account) as client:
        with open("./output/wuti_delete.txt", "w", encoding="utf-8") as f:
            pn = 1
            while(1):
                user_id = await client.tieba_uid2user_info(待查询人的贴吧主页id)
                # print(user_id)
                result = parse.quote(user_id.user_name)
                bawu_info = await client.get_bawu_postlogs("yy小说吧", search_value=result , search_type=0, pn=pn)
                for x in bawu_info.objs:
                    id = await client.get_user_info(x.post_portrait)
                    f.write("被处理人：{}\n{} \n{} {} {}\n".format(id, x.text, x.op_user_name, x.op_type, x.op_time))
                    f.write("===============\n")
                if bawu_info.has_more == False:
                    pn += 1
                    break
asyncio.run(main())
