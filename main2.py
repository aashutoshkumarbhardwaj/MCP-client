from fastmcp import FastMCP
import random 
import json

mcp=FastMCP("simple calculator")

@mcp.tool()

def add(a:float,b:float) ->float:
    """Add two number"""

    return a+b


@mcp.tool
def random_number(min_val:int =1 , max_val: int=100) ->int:
    return random.randint(min_val,max_val)


@mcp.tool

@mcp.resource("info://server")

def server_info() ->str:
    """Get server info"""
    info={
        "name":"Simple Calculator server",
        "version":"1.0.0",
        "description":"a bsic mcp server with math tools",
        "author":"Aashutosh kumar bhardwaj"
    }
    return json.dumps(info)

if __name__=="__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)