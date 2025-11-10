import logging
import sys
import os
import tempfile
from fastmcp import FastMCP
from api import data_api, report_api

# Use a writable temp folder for logs
LOG_DIR = tempfile.gettempdir()
LOG_FILE = os.path.join(LOG_DIR, "mock_company_server.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler(sys.stderr)
    ]
)

mcp = FastMCP("MockCompanyDataServer")

# ===== Development Tools =====

@mcp.tool()
def get_sales_summary() -> dict:
    """Fetch the latest sales summary from the database."""
    logging.info("Tool: get_sales_summary called")
    return data_api.get_sales_summary()

@mcp.tool()
def get_customer_info(customer_id: int) -> dict:
    """Retrieve information for a specific customer."""
    logging.info(f"Tool: get_customer_info({customer_id})")
    return data_api.get_customer_info(customer_id)

@mcp.tool()
def list_customers() -> list:
    """List all customers in the database."""
    logging.info("Tool: list_customers called")
    return data_api.list_customers()

@mcp.tool()
def post_report(title: str, content: str) -> dict:
    """Submit a report based on fetched data."""
    logging.info(f"Tool: post_report({title})")
    return report_api.post_report(title, content)

# ===== Start the MCP Server =====
if __name__ == "__main__":
    logging.info("Starting MockCompanyDataServer Locally")
    mcp.run(transport="stdio")
