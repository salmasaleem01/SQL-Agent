"""
Simple Agent Demo - Agent Framework Without Tools

This script demonstrates the most basic usage of LangChain's agent framework
without any tools. It creates an agent that can only talk to the LLM for
conversational AI, showing the agent structure before adding tool capabilities.

Educational Purpose:
- Understand the agent framework structure without tool complexity
- See how agents work at their core (just LLM conversation)
- Learn the foundation before adding SQL tools and capabilities
- Compare agent vs direct LLM usage

Key Concepts:
- Agent framework with zero tools
- Conversational agent pattern
- Agent initialization and invocation
- System message configuration for agents
"""

# Load environment variables first (including OPENAI_API_KEY)
from dotenv import load_dotenv, find_dotenv; load_dotenv(find_dotenv())

# Import LangChain components for agent creation
from langchain_google_genai import ChatGoogleGenerativeAI  # Google Gemini language model integration
from langchain.agents import initialize_agent, AgentType  # Agent framework
from langchain.schema import SystemMessage  # System message configuration
from langchain.tools import BaseTool  # Base class for creating dummy tools
from pydantic import BaseModel, Field  # Data validation for tool inputs
from typing import Type  # Type hinting
import os

class DummyInput(BaseModel):
    """
    Pydantic model for dummy tool input - not actually used.

    This exists only to satisfy the tool framework requirements.
    """
    query: str = Field(description="Any input - this tool does nothing")

class DummyTool(BaseTool):
    """
    Dummy Tool - Does Nothing But Allows Agent Creation

    This tool exists only to satisfy LangChain's requirement that agents
    must have at least one tool. It doesn't actually do anything useful,
    allowing us to demonstrate pure conversational agent behavior.

    Educational Purpose:
    - Shows that agents require tools (even dummy ones)
    - Demonstrates the tool interface without functionality
    - Allows focus on agent conversation patterns
    """

    name: str = "dummy_tool"
    description: str = "A dummy tool that does nothing - used only for agent framework demo"
    args_schema: Type[BaseModel] = DummyInput

    def _run(self, query: str) -> str:
        """
        Dummy tool execution - returns a message explaining it does nothing.

        Args:
            query (str): Any input (ignored)

        Returns:
            str: Message explaining this is a dummy tool
        """
        return "This is a dummy tool that does nothing. I can only provide information through conversation."

    def _arun(self, *args, **kwargs):
        """Async version - not implemented."""
        raise NotImplementedError

def main():
    """
    Main function demonstrating simple agent usage without tools.

    This function shows how to create and use a LangChain agent without any tools:
    1. Initialize the LLM
    2. Create an agent with zero tools
    3. Configure the agent with a system message
    4. Demonstrate agent invocation vs direct LLM usage

    Key difference: Agent framework structure without tool complexity.
    """

    # Initialize the Language Model
    # ChatGoogleGenerativeAI: Creates connection to Google's Gemini models for the agent
    # Parameters:
    #   - model: Specify which Gemini model to use
    #   - temperature: Controls response randomness (0 = deterministic)
    print("🤖 Initializing language model for agent...")
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash",
        temperature=0,
        transport="rest",
        api_key=os.environ.get("GOOGLE_API_KEY")
    )

    # Define System Message for Agent
    # This sets the agent's personality and behavior
    system_message = SystemMessage(
        content="""You are a helpful AI assistant specializing in explaining technology concepts.
        You provide clear, concise explanations and are always friendly and professional.
        You have access to one dummy tool, but you should prefer to answer questions directly through conversation."""
    )

    # Create Dummy Tool Instance
    # This tool does nothing but allows the agent to be created
    dummy_tool = DummyTool()

    # Create Agent with Dummy Tool
    # initialize_agent: Creates an agent executor using the agent framework
    # Parameters:
    #   - tools: List with one dummy tool (required by framework)
    #   - llm: Language model for reasoning and responses
    #   - agent: Agent type (ZERO_SHOT_REACT_DESCRIPTION for simple reasoning)
    #   - verbose: Show execution steps for educational purposes
    #   - agent_kwargs: Additional configuration including system message
    print("🎯 Creating agent with dummy tool (conversational focus)...")
    agent = initialize_agent(
        tools=[dummy_tool],          # Dummy tool to satisfy framework requirements
        llm=llm,                     # Language model for conversation
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Simple reasoning agent type
        verbose=True,                # Show agent reasoning process
        agent_kwargs={
            "system_message": system_message  # Set agent personality
        }
    )

    # Interactive CLI Interface for Simple Agent Demo
    print("🤖 Simple Agent Demo - Agent Framework Without Tools")
    print("This agent demonstrates basic conversation without SQL tools.")
    print("Type 'quit' or 'exit' to stop.\n")
    
    # Show Agent Properties
    print("🔍 Agent configuration:")
    print("=" * 60)
    print(f"Agent type: {type(agent)}")
    print(f"Available tools: {len(agent.tools)} (dummy tool only)")
    try:
        print(f"LLM model: {getattr(llm, 'model', getattr(llm, 'model_name', 'unknown'))}")
    except Exception:
        pass
    print(f"Agent verbose mode: {agent.verbose}")
    print("=" * 60)
    
    while True:
        try:
            # Get user input
            user_input = input("\n💬 Your question: ").strip()
            
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
            print(f"\n🤖 Agent Response: {result['output']}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}\n")

# Error Handling Wrapper
# This ensures graceful handling of common issues like missing API keys
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("\n🔧 Troubleshooting tips:")
        print("1. Make sure your .env file contains GOOGLE_API_KEY")
        print("2. Verify your virtual environment is activated")
        print("3. Check that you've installed requirements: pip install -r requirements.txt")
        print("4. Ensure you have internet connection for API calls")