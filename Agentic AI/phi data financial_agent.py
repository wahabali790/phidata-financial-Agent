# import os

# ###############################################################################
# # 1. Set environment variables directly in your code
# ###############################################################################
# os.environ["PHI_API_KEY"] = "phi-Jbgcd3YDSmvsHtfLghV2mo7DTQqV34insempDI_CR6k"
# os.environ["GROQ_API_KEY"] = "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"
# os.environ["OPEN_API_KEY"] = ""

# ###############################################################################
# # 2. Import libraries and classes
# ###############################################################################
# from phi.agent import Agent
# from phi.model.groq import Groq
# from phi.tools.yfinance import YFinanceTools
# from phi.tools.duckduckgo import DuckDuckGo

# ###############################################################################
# # 3. Define the agents
# ###############################################################################

# # Web Search Agent
# web_search_agent = Agent(
#     name="web Search Agent",
#     role="Search the web for the information", 
#     model=Groq(id="llama3-groq-70b-8192-tool-use-preview"), 
#     tools=[DuckDuckGo()],
#     instructions=["Always include sources of references."],
#     show_tool_calls=True,
#     markdown=True
# )

# # Financial Agent
# finance_agent = Agent(
#     name="Finance Agent",
#     model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
#     tools=[
#         YFinanceTools(
#             stock_price=True,
#             stock_fundamentals=True,
#             analyst_recommendations=True,
#             company_news=True
#         )
#     ],
#     instructions=["Always use tables to display the data."],
#     show_tool_calls=True,
#     markdown=True
# )

# # Summary Agent
# summary_agent = Agent(
#     name="Summary Agent",
#     role="provide a concise summary for the data provided by finance",
#     model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
#     instructions=[
#         "Focus on the relevant data from the finance agent (analyst recommendation, latest news).",
#         "Keep the response short but clear."
#     ],
#     show_tool_calls=True,
#     markdown=True
# )

# ###############################################################################
# # 4. Create the multi AI agent that coordinates the other agents
# ###############################################################################
# multi_ai_agent = Agent(
#     team=[web_search_agent, finance_agent, summary_agent],
#     model=Groq(id="llama-3.3-70b-versatile"),
#     instructions=[
#         "Always provide the sources.",
#         "Always use tables to show the data.",
#         "1) First, get the table from the finance agent with the data for TCS.",
#         "2) Then share the latest news for TCS from the finance agent.",
#         "3) Finally, ask the summary agent to provide a short summary."
#     ],
#     show_tool_calls=True,
#     markdown=True
# )

# ###############################################################################
# # 5. Run the multi AI agent to get the summary
# ###############################################################################
# multi_ai_agent.print_response(
#     "What is the current stock price of Apple (AAPL)?",
#     stream=True
# )


## LIbraries
from phi.agent import Agent
from phi.model.openai import OpenAIChat
from phi.tools.googlesearch import GoogleSearch
from phi.tools.yfinance import YFinanceTools

## Put Open AI API key into Python environment
import os
os.environ["OPENAI_API_KEY"] = ''



## Create Agents

# Sentiment Agent
sentiment_agent = Agent(
    name="Sentiment Agent",
    role="Search and interpret news articles.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[GoogleSearch()],
    instructions=[
        "Find relevant news articles for each company and analyze the sentiment.",
        "Provide sentiment scores from 1 (negative) to 10 (positive) with reasoning and sources."
        "Cite your sources. Be specific and provide links."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data and interpret trends.",
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, company_info=True)],
    instructions=[
        "Retrieve stock prices, analyst recommendations, and key financial data.",
        "Focus on trends and present the data in tables with key insights."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Analyst Agent
analyst_agent = Agent(
    name="Analyst Agent",
    role="Ensure thoroughness and draw conclusions.",
    model=OpenAIChat(id="gpt-4o"),
    instructions=[
        "Check outputs for accuracy and completeness.",
        "Synthesize data to provide a final sentiment score (1-10) with justification."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Team of Agents
agent_team = Agent(
    model=OpenAIChat(id="gpt-4o"),
    team=[sentiment_agent, finance_agent, analyst_agent],
    instructions=[
        "Combine the expertise of all agents to provide a cohesive, well-supported response.",
        "Always include references and dates for all data points and sources.",
        "Present all data in structured tables for clarity.",
        "Explain the methodology used to arrive at the sentiment scores."
    ],
    show_tool_calls=True,
    markdown=True,
)

## Run Agent Team

# Final Prompt
agent_team.print_response(
    "Analyze the sentiment for the following companies during the week of December 2nd-6th, 2024: NVDA, MSFT. \n\n"
    "1. **Sentiment Analysis**: Search for relevant news articles and interpret th–e sentiment for each company. Provide sentiment scores on a scale of 1 to 10, explain your reasoning, and cite your sources.\n\n"
    "2. **Financial Data**: Analyze stock price movements, analyst recommendations, and any notable financial data. Highlight key trends or events, and present the data in tables.\n\n"
    "3. **Consolidated Analysis**: Combine the insights from sentiment analysis and financial data to assign a final sentiment score (1-10) for each company. Justify the scores and provide a summary of the most important findings.\n\n"
    "Ensure your response is accurate, comprehensive, and includes references to sources with publication dates.",
    stream=True
)