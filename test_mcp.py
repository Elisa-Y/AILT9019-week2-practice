#!/usr/bin/env python3
"""测试脚本：通过 stdio 调用 get_today_date 工具"""

import asyncio
import json
from mcp.client.session import ClientSession
from mcp.client.stdio import stdio_client, StdioServerParameters

async def main():
    params = StdioServerParameters(
        command="python3",
        args=["/Users/elisa.yu/Desktop/mySkill_9019/mcp_server.py"],
    )
    async with stdio_client(params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            result = await session.call_tool("get_today_date", {})
            print(result.content[0].text)

asyncio.run(main())
