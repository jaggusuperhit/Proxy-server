from fastmcp import FastMCP

# Create a proxy to your remote FastMcp cloud server
# FastMcp Cloud uses Streamable HTTP (default), so just use the /mcp URL
mcp = FastMCP.as_proxy(
    "https://increasing-cyan-meerkat.fastmcp.app/mcp", # Standard FastMCP Cloud URL
    name = "Suraj Server Proxy"
)



if __name__ == "__main__":
    # This runs via STDIO, which Claude Desktop can connect to
    mcp.run()
