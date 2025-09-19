"""
Simple SQL Agent Demo

This script demonstrates the basic usage of LangChain's SQL agent capabilities.
It creates a simple agent that can execute SQL queries against a SQLite database
without any safety restrictions.

Key Components:
- ChatOpenAI: The language model that powers the agent
- SQLDatabase: Wrapper for database connection and operations
- SQLDatabaseToolkit: Pre-built tools for SQL operations
- create_sql_agent: Factory function to create a SQL-capable agent

Safety Note: This agent has NO restrictions and can execute any SQL including
DELETE, DROP, INSERT, etc. It's meant for demonstration purposes only.
"""

# Import necessary LangChain components for SQL agent functionality
from langchain_google_genai import ChatGoogleGenerativeAI  # Google Gemini chat model
from langchain_community.utilities import SQLDatabase  # Database connection wrapper
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit  # Updated import path
from langchain_community.agent_toolkits.sql.base import create_sql_agent  # Updated import path
from dotenv import load_dotenv, find_dotenv  # Load environment variables from nearest .env
import os
from pathlib import Path

# Ensure we load a .env placed alongside this script (works regardless of CWD)
_here = Path(__file__).resolve().parent
load_dotenv(_here / ".env")
# Fallback: also try to load the nearest parent .env if present
load_dotenv(find_dotenv())

# Initialize the Language Model
# ChatGoogleGenerativeAI: Creates a Google Gemini model instance for the agent
# Parameters:
#   - model: Specifies which Gemini model to use
#   - temperature: Controls randomness (0 = deterministic, 1 = more creative)
api_key = os.environ.get("GOOGLE_API_KEY")
if not api_key:
    raise RuntimeError("GOOGLE_API_KEY is not set. Add it to scripts/.env or export it in your shell.")

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-pro",
    temperature=0,
    api_key=api_key,
    transport="rest",
)

# Create Database Connection
# SQLDatabase.from_uri: Creates a database wrapper from a connection string
# Parameters:
#   - uri: SQLite database file path (creates file if it doesn't exist)
# Returns: SQLDatabase object that handles connection management and query execution
db = SQLDatabase.from_uri("sqlite:///SQLAgent/sql_agent_class.db")

# Create SQL Agent
# create_sql_agent: Factory function that creates a complete SQL-capable agent
# Parameters:
#   - llm: The language model instance to use for reasoning
#   - toolkit: SQLDatabaseToolkit provides pre-built tools for SQL operations
#     - db: Database connection object
#     - llm: Language model for query generation and result interpretation
#   - agent_type: Specifies the agent architecture ("openai-tools" uses function calling)
#   - verbose: If True, prints detailed execution steps for debugging
# Returns: AgentExecutor that can process natural language requests and execute SQL
agent = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    agent_type="zero-shot-react-description",
    verbose=True
)

# Interactive CLI Interface
# Get user input for SQL queries instead of hardcoded prompts
def main():
    print("🤖 SQL Agent Ready! Ask me anything about the database.")
    print("Type 'quit' or 'exit' to stop.\n")
    
    while True:
        try:
            # Get user input
            user_input = input("💬 Your question: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
            
            # Skip empty inputs
            if not user_input:
                continue
            
            # Execute the agent with user input
            print("\n🔄 Processing your request...")
            result = agent.invoke({"input": user_input})
            print(f"\n📊 Result: {result['output']}\n")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")

if __name__ == "__main__":
    main()