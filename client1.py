import asyncio

from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, ToolMessage
from langchain_mcp_adapters.client import MultiServerMCPClient
import os
from langchain_openai import ChatOpenAI

load_dotenv()

SERVERS = {
    # "math": {
    #     "transport": "stdio",
    #     "command": "/Users/aashutoshkumarbhardwaj/.local/bin/uv",
    #     "args": [
    #         "run",
    #         "fastmcp",
    #         "run",
    #         "/Users/aashutoshkumarbhardwaj/MCPCLIENT/main2.py",
    #     ],
    # },
    "expense": {
        "transport": "streamable_http",
        "url": "https://gullakai.fastmcp.app/mcp",
    },
}


async def main():
    # Create MCP client
    client = MultiServerMCPClient(SERVERS)

    # Get all available tools
    tools = await client.get_tools()

    # Dictionary for quick lookup
    named_tools = {tool.name: tool for tool in tools}

    print("\nAvailable Tools:")
    for tool in tools:
        print(f"• {tool.name}")

    # Create LLM
    llm = ChatOpenAI(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
    )

    # Bind MCP tools
    llm_with_tools = llm.bind_tools(tools)

    prompt = "What is the product of 12 and 5?"

    # First LLM call
    response = await llm_with_tools.ainvoke(
        [HumanMessage(content=prompt)]
    )

    print("\n========== AI RESPONSE ==========")
    print(response)

    # If no tool was selected
    if not response.tool_calls:
        print("\nNo tool call made.")
        print(response.content)
        return

    # Extract tool information
    tool_call = response.tool_calls[0]

    tool_name = tool_call["name"]
    tool_args = tool_call["args"]
    tool_call_id = tool_call["id"]

    print(f"\nSelected Tool : {tool_name}")
    print(f"Tool Args     : {tool_args}")

    # Execute tool
    tool_result = await named_tools[tool_name].ainvoke(tool_args)

    print("\n========== TOOL RESULT ==========")
    print(tool_result)

    # Create ToolMessage
    tool_message = ToolMessage(
        content=str(tool_result),
        tool_call_id=tool_call_id,
    )

    # Final LLM response
    final_response = await llm_with_tools.ainvoke(
        [
            HumanMessage(content=prompt),
            response,
            tool_message,
        ]
    )

    print("\n========== FINAL ANSWER ==========")
    print(final_response.content)


if __name__ == "__main__":
    asyncio.run(main())