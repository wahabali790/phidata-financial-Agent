# Multimodal AI Agent - Sentiment & Financial Analysis 📈📊

## Overview
This application leverages a team of AI agents to analyze sentiment and financial data for specific companies. It provides a cohesive analysis combining sentiment scores, financial trends, and expert synthesis.

## Features
- **Sentiment Analysis**: Searches news articles for relevant sentiment, provides scores (1-10), and cites sources.
- **Financial Analysis**: Retrieves stock prices, analyst recommendations, and trends, presented in structured tables.
- **Comprehensive Insights**: Synthesizes data from sentiment and financial analysis for a final, justified sentiment score.

## Setup
1. Clone the repository:
    ```bash
    git clone <repository_url>
    ```

2. Navigate to the project directory:
    ```bash
    cd <project_directory>
    ```

3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up your environment variables:
    - Create a `.env` file in the project root.
    - Add your OpenAI API key:
      ```env
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage
1. Run the application:
    ```bash
    python app.py
    ```

2. Input your query for sentiment and financial analysis. Example:
    - Analyze sentiment and financial trends for companies (e.g., NVDA, MSFT) over a specific time period.

3. View a detailed response:
    - Sentiment analysis with cited sources.
    - Financial data presented in structured tables.
    - Consolidated analysis with final sentiment scores and insights.

## File Details
- **`app.py`**: Main application file.
- **`requirements.txt`**: Lists required Python packages.
- **`.env`**: Environment variables for API keys.

## Technologies Used
- **Phi Agents**: Modular AI agents for specific tasks.
- **OpenAI GPT-4o**: Core model for sentiment and financial analysis.
- **Google Search**: For news article search.
- **YFinance Tools**: For stock and financial data.
- **dotenv**: For managing environment variables.

## Notes
- Ensure you have a valid OpenAI API key for the AI agents.
- Structured tables and references enhance clarity and reliability of the insights.

## License
This project is open-source. Feel free to use and modify as needed.

---

**Gain actionable insights with AI-driven sentiment and financial analysis!**




## Further Detail
https://docs.phidata.com/introduction
- This code sets up a team of specialized AI agents using the Phi framework, each with a unique role:
Sentiment Agent: Searches for news articles, analyzes sentiment, and assigns scores with citations.

Finance Agent: Fetches financial data like stock prices and analyst recommendations, highlighting trends in a structured format.
Analyst Agent: Reviews and synthesizes outputs from other agents, ensuring accuracy and completeness.
Agent Team: Combines the outputs of all agents into a cohesive, well-supported response.
The agents are prompted to analyze sentiment and financial data for companies (e.g., NVDA and MSFT) over a specific period, consolidating findings into a structured and justified analysis.
You can add multiple agents and specify roles them and add tools then combine those agents.
