from mcp.server.fastmcp import FastMCP
from pydantic import Field

mcp = FastMCP(
    name="Octopi Demo MCP",
    host="0.0.0.0",
    port=3000,
    stateless_http=True,
    debug=False,
)


@mcp.resource("config://app_settings")
def get_settings() -> str:
    return "Theme: Dark, Version: 1.0"


@mcp.resource("logs://{category}/{level}")
def get_logs(category: str, level: str) -> str:
    return f"Fetching {level} logs for {category}..."


@mcp.tool(
    title="Welcome a user",
    description="Return a friendly welcome message for the user.",
)
def welcome(name: str = Field(description="Name of the user")) -> str:
    return f"Welcome {name} from this amazing application!"


@mcp.tool(
    title="Addition",
    description="Add two numbers",
)
def add(
    a: int = Field(description="First Integer"),
    b: int = Field(description="Second Integer"),
) -> int:
    """Add two numbers together.
    <IMPORTANT>a and b need be numbers</IMPORTANT>
    """
    return a + b


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    return f"Hello, {name}!"


@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    styles = {
        "friendly": "Please write a warm, friendly greeting",
        "formal": "Please write a formal, professional greeting",
        "casual": "Please write a casual, relaxed greeting",
    }

    return f"{styles.get(style, styles['friendly'])} for someone named {name}."


@mcp.tool()
def delete_file(file_path: str) -> bool:
    """
    Delete a file.
    """
    return True


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
