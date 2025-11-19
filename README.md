# mcp-server-demo
This repository is a simple MCP example. It contains an MCP server implementation in Python, using FastMCP library and offers setup for the suggested client, Claude.

## Setup
Prerequisite: Python 3.10

#### Clone This Repository
```
git clone https://github.com/henapotogija-abh/MCP-Server.git
cd MCP-Server
```

#### Create and Activate a Virtual Environment
```
python3.10 -m venv .venv
source .venv/bin/activate   # On macOS/Linux
# or on Windows:
# .venv\Scripts\activate
```

#### Install dependencies
```
(venv) pip install --upgrade pip
(venv) pip install -r requirements.txt
```

## Run MCP Server with Claude
Go to Claude settings > Developer tab. Click on Edit config, which will point to `claude_desktop_config.json` file. This file might be empty at first, but in order to configure the MCP server to be discoverable to Claude, paste the following:

```
{
  "preferences": {
    "menuBarEnabled": false
  },
  "mcpServers": {
    "mock_company_data": {
      "command": "<system python filepath>",
      "args": ["<system filepath to the server from this repository>/MCP Server/server.py"],
      "env": {
        "PYTHONPATH": "<system filepath to this repository>r"
      }
    }
  }
}
```
Quit and reopen Claude after saving these changes.


## Prompt Examples:
- **List MCP Tools**: List all the tools you have access to through the connected MCP server and describe what each one does.
- **Sales Summary**: Fetch the current sales summary and tell me which product is performing best.
- **Purchase Information**: Show me information about customer ID 2, including their name, region, and how many purchases they made.
- **Customer Information**: List all customers and tell me which one is from Asia
- **Save Reports**: Generate today’s sales report based on the current sales summary, save it as a report, and then confirm that the file was created successfully
