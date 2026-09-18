#!/usr/bin/env python3
"""MCP Server: 获取今天的日期"""

import asyncio
from datetime import date
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    ListToolsResult,
    CallToolResult,
    CallToolRequestParams,
    PaginatedRequestParams,
)

async def my_list_tools(ctx, params: PaginatedRequestParams | None) -> ListToolsResult:
    return ListToolsResult(
        tools=[
            Tool(
                name="get_today_date",
                description="获取今天的日期，返回格式为 YYYY-MM-DD",
                inputSchema={
                    "type": "object",
                    "properties": {},
                },
            )
        ]
    )

async def my_call_tool(ctx, params: CallToolRequestParams) -> CallToolResult:
    if params.name == "get_today_date":
        today = date.today().isoformat()
        return CallToolResult(
            content=[TextContent(type="text", text=f"今天的日期是：{today}")]
        )
    return CallToolResult(
        content=[TextContent(type="text", text=f"未知工具: {params.name}")]
    )

server = Server(
    "today-date",
    on_list_tools=my_list_tools,
    on_call_tool=my_call_tool,
)

async def main():
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())

if __name__ == "__main__":
    asyncio.run(main())
