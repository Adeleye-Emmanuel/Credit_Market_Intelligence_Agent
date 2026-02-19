# Credit_Market_Intelligence_Agent
An AI-powered agent system that synthesizes multi-source financial data to answer credit market questions in real-time. The agent autonomously reasons about which data sources to query, fetches information in parallel, and generates institutional-quality market analysis.

## Quick Start

1. **Install dependencies:**
```bash
   pip install -r requirements.txt
```

2. **Set up environment variables:**
   Copy `.env.example` to `.env` and add your API keys.

3. **Start MongoDB:**
```bash
   # Using Docker (recommended)
   docker run -d -p 27017:27017 --name mongodb mongo:latest
   
   # Or install locally
   brew install mongodb-community  # macOS
```

4. **Run the agent:**
```bash
   python -m agent.core
```

5. **Launch dashboard:**
```bash
   streamlit run dashboard/app.py
```

## Architecture

- **Agent Core**: Anthropic Claude with tool-use capabilities
- **Data Sources**: FRED, Yahoo Finance, Alpha Vantage
- **Storage**: MongoDB for caching and metrics
- **Dashboard**: Streamlit for performance visualization

## Example Queries

- "What's driving credit spreads today?"
- "Analyze the current yield curve shape"
- "Is the VIX signaling risk-off sentiment?"