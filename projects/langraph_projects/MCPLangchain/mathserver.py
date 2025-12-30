from mcp.server.fastmcp import FastMCP

# server initialization and naming
mcp = FastMCP("Math")

@mcp.tool()
def addition(first_number: int, second_number: int) -> int:
    """
        __summary__
        Add two numbers
    """
    return first_number + second_number


@mcp.tool()
def multiplication(first_number: int, second_number: int) -> int:
    """
        __summary__
        Add two numbers
    """
    return first_number * second_number


if __name__ == "__main__":
    """
        The transport = "stdio" argument tells the server to:
        Use standard input/output (stdin and stdout) to receive and response to tool function calls.
    """
    mcp.run(transport = "stdio")