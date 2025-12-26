# No MCP

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![PyPI version](https://img.shields.io/pypi/v/no-mcp-server.svg)](https://pypi.org/project/no-mcp-server/)

A Model Context Protocol (MCP) server that wraps [NaaS (No as a Service)](https://github.com/hotheadhacker/no-as-a-service).

## Description

This is a joke MCP server that continues the satirical spirit of NaaS. When your AI agent asks any question through this server, it will always respond with "no" along with a creative reason. Perfect for when you want your AI to be consistently negative or just want to add some humor to your MCP setup.

## Installation

```bash
uv pip install no-mcp-server
```

## Usage

### Running with STDIO (Default)

The server runs with stdio transport by default, suitable for MCP clients like Claude Desktop:

```bash
uvx no-mcp-server
```

### Running as HTTP Server

You can run the server as an HTTP endpoint by setting the `MCP_TRANSPORT` environment variable:

```bash
MCP_TRANSPORT=http uvx no-mcp-server
```

The server will start on `http://0.0.0.0:8000/mcp` by default. You can customize the HTTP configuration:

```bash
MCP_HTTP_PATH=mcp uvx no-mcp-server
```

### Configuration

The server can be configured via environment variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `MCP_TRANSPORT` | Transport protocol (`stdio` or `http`) | `stdio` |
| `MCP_HTTP_HOST` | HTTP server host (when using http transport) | `0.0.0.0` |
| `MCP_HTTP_PORT` | HTTP server port (when using http transport) | `8000` |
| `MCP_HTTP_PATH` | HTTP endpoint path (when using http transport) | `/mcp` |
| `NO_BASE_URL` | NaaS API base URL | `https://naas.isalman.dev` |

### Adding to MCP Clients

#### Claude Desktop (STDIO)

Add this configuration to your MCP client settings:

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
      "args": ["no-mcp-server@0.2.1"]
    }
  }
}
```

#### Using HTTP Transport

If you're running the server as HTTP, configure your MCP client to connect to the HTTP endpoint (e.g., `http://localhost:8000/mcp`).

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
