# No MCP

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

A Model Context Protocol (MCP) server that wraps [NaaS (No as a Service)](https://github.com/hotheadhacker/no-as-a-service).

## Description

This is a joke MCP server that continues the satirical spirit of NaaS. When your AI agent asks any question through this server, it will always respond with "no" along with a creative reason. Perfect for when you want your AI to be consistently negative or just want to add some humor to your MCP setup.

## Installation

```bash
uv pip install no-mcp-server
```

## Usage

### Running with uvx

```bash
uvx no-mcp-server
```

### Adding to MCP Servers

Add this configuration to your MCP client settings (e.g., Claude Desktop config):

```json
{
  "mcpServers": {
    "no-mcp": {
      "command": "uvx",
      "args": ["no-mcp-server"]
    }
  }
}
```

Or with a specific version:

```json
{
  "mcpServers": {
    "no-mcp": {
      "command": "uvx",
      "args": ["no-mcp-server@0.0.1"]
    }
  }
}
```

Once configured, your AI agent will have access to the `query` tool, which will respond to any question with "no" and a creative explanation.

## Development

This project uses uv for package management:

```bash
# Install dependencies
uv sync

# Run tests
uv run poe test

# Run linting
uv run poe lint

# Format code
uv run poe format
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details.
