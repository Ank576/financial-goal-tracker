# 💰 AI-Powered Financial Goal Tracker

An intelligent Streamlit web application that uses LLM (Perplexity Sonar) to analyze your financial goals and recommend optimal asset allocation across multiple investment classes including equity, debt, gold, silver, crude oil/energy, and real estate.

Live demo: [DEMO](https://financial-goal-tracker.streamlit.app/)

> **Note**: This is a prototype for educational and portfolio demonstration purposes. It does NOT provide professional financial advice or replace consultation with a SEBI-registered financial advisor.

---

## 🎯 What This App Does

This AI-powered wealth planning tool helps you:

### **Input Your Financial Profile**
- Set investment goals (Retirement, Child Education, Home Purchase, etc.)
- Define target amount and current savings
- Specify investment tenure (1-30 years)
- Select risk appetite (Very Conservative to Very Aggressive)
- Enter personal details (age, income, monthly investment capacity)
- Choose preferences (liquidity, real estate, tax-saving priority)

### **Get AI-Powered Recommendations**
The app sends your profile to Perplexity's Sonar model which:
- **Searches real-time market data** for 2025 conditions
- **Analyzes 6 asset classes**:
  - 🏦 **Equity**: Large-cap, Mid-cap, Small-cap MFs, Index funds
  - 📊 **Debt**: Corporate bonds, Govt securities, FDs, PPF, EPF
  - 🥇 **Gold**: Physical, Digital, ETFs, Sovereign Gold Bonds
  - 🥈 **Silver**: Physical silver, Silver ETFs
  - ⛽ **Crude/Energy**: Energy sector funds, Commodity ETFs
  - 🏢 **Real Estate**: REITs, direct property investments
- **Generates personalized asset allocation** matching your risk profile
- **Suggests specific instruments** for each asset class
- **Calculates required monthly SIP** and expected corpus
- **Provides tax-saving strategies** (80C, LTCG, STCG)
- **Highlights risk factors** and market outlook

### **Visualize Your Investment Plan**
- Asset allocation breakdown with percentages
- Monthly investment amounts per asset class
- Specific instrument recommendations (mutual funds, bonds, ETFs)
- Expected CAGR and confidence score
- Tax benefits and rebalancing guidance
- Alternative strategies for goal achievement

---

## 🧱 Tech Stack

- **Frontend/UI**: [Streamlit](https://streamlit.io/) - Interactive web interface
- **LLM Backend**: [Perplexity Sonar](https://docs.perplexity.ai/getting-started/models) - Real-time market research AI
- **API Client**: OpenAI-compatible client for Perplexity
- **Language**: Python 3.11
- **Hosting**: Streamlit Community Cloud
- **Configuration**: API keys managed via Streamlit Secrets

---

## 📁 Repository Structure

```
financial-goal-tracker/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .python-version        # Python version (3.11)
└── README.md             # This file
```

---

## 🚀 Quick Start

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Ank576/financial-goal-tracker.git
cd financial-goal-tracker
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Set Up API Key

Create `.streamlit/secrets.toml`:
```toml
PERPLEXITY_API_KEY = "pplx-your-api-key-here"
```

**Get your free API key**: [Perplexity API Settings](https://www.perplexity.ai/settings/api)

### 4️⃣ Run the App
```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` 🎉

---

## 📖 How to Use

### **Step 1: Enter Your Goal**
1. Open the app in your browser
2. In the left sidebar, enter:
   - **Goal Name**: e.g., "Retirement Fund", "Child's Education", "Dream Home"
   - **Target Amount**: Your financial goal in ₹
   - **Current Savings**: How much you've already saved
   - **Investment Tenure**: Years until you need the money (1-30)

### **Step 2: Define Your Profile**
1. **Risk Appetite**: Select from Very Conservative to Very Aggressive
   - Conservative = More debt/gold, less equity
   - Aggressive = Higher equity allocation for growth
2. **Age**: Your current age (affects investment strategy)
3. **Monthly Income**: Your gross monthly income
4. **Monthly Investment Capacity**: How much you can invest monthly

### **Step 3: Set Preferences**
Check boxes for:
- ✅ **Prefer liquid investments** (can be withdrawn easily)
- ✅ **Include Real Estate** (REITs or direct property)
- ✅ **Prioritize tax-saving instruments** (Section 80C benefits)

### **Step 4: Generate Your Plan**
1. Click **"🔍 Generate Investment Plan"**
2. Wait 10-15 seconds while AI analyzes markets
3. Review your personalized recommendations!

### **Step 5: Understand Results**
The app shows:
- ✅ **Goal Achievability**: Can you reach your target?
- 📊 **Asset Allocation**: Percentage breakdown (Equity, Debt, Gold, etc.)
- 💰 **Monthly SIP Required**: How much to invest per month
- 📈 **Expected CAGR**: Projected annual returns
- 📋 **Specific Instruments**: Exact mutual funds, ETFs, bonds to consider
- ⚠️ **Risk Factors**: What could go wrong
- 💡 **Tax Benefits**: How to save on taxes
- 🔄 **Rebalancing Strategy**: When to adjust allocations

---

## 🔬 How It Works

### **Intelligent Prompt Engineering**

The app constructs a detailed prompt for the LLM:

```python
prompt = f"""
You are a SEBI-registered financial advisor for Indian investors.

INVESTOR PROFILE:
- Goal: {goal_name}
- Target: ₹{target_amount}
- Tenure: {tenure_years} years
- Risk: {risk_appetite}
- Age: {age}
...

TASK:
Search 2025 market conditions for:
1. Equity (MFs, Index funds)
2. Debt (Bonds, FDs, PPF)
3. Gold (ETFs, SGBs)
4. Silver (ETFs)
5. Crude/Energy (Commodity funds)
6. Real Estate (REITs)

Provide asset allocation with tax strategies and risk analysis.
"""
```

### **Real-Time Market Research**

Perplexity Sonar model:
1. **Searches** current interest rates, equity valuations, commodity prices
2. **Analyzes** historical returns and risk-adjusted performance
3. **Considers** tax implications (LTCG, STCG, Section 80C)
4. **Generates** optimal mix matching your risk profile

### **Structured JSON Response**

```json
{
  "goal_achievable": true,
  "confidence_score": 85,
  "required_monthly_sip": 25000,
  "expected_return_cagr": "10-12%",
  "asset_allocation": {
    "equity": {
      "percentage": 60,
      "allocation_amount": 15000,
      "instruments": [
        "Nifty 50 Index Fund",
        "Parag Parikh Flexi Cap Fund"
      ]
    },
    "debt": {
      "percentage": 25,
      "allocation_amount": 6250,
      "instruments": ["PPF", "Corporate Bond Funds"]
    },
    "gold": {
      "percentage": 10,
      "allocation_amount": 2500,
      "instruments": ["Sovereign Gold Bonds", "Gold ETF"]
    }
  },
  "recommendations": [
    "Start SIP in Nifty 50 index fund for low-cost equity exposure",
    "Max out PPF for tax benefits under Section 80C"
  ]
}
```

---

## 💡 Sample Use Cases

### **Case 1: Retirement Planning (Age 30)**
- **Goal**: ₹5 Cr retirement corpus
- **Tenure**: 30 years
- **Risk**: Aggressive
- **Result**: 70% Equity, 20% Debt, 10% Gold

### **Case 2: Child Education (Age 40)**
- **Goal**: ₹50 Lakh in 10 years
- **Tenure**: 10 years
- **Risk**: Moderate
- **Result**: 50% Equity, 35% Debt, 10% Gold, 5% Others

### **Case 3: Home Down Payment (Age 28)**
- **Goal**: ₹30 Lakh in 5 years
- **Tenure**: 5 years
- **Risk**: Conservative
- **Result**: 30% Equity, 50% Debt, 15% Gold, 5% Liquid funds

---

## 🎨 Features

- ✅ **Multi-Asset Analysis**: 6 asset classes (Equity, Debt, Gold, Silver, Energy, Real Estate)
- 🤖 **Real-Time AI Research**: Perplexity searches latest market data
- 📊 **Interactive UI**: Sliders, inputs, and metric cards
- 💰 **Tax Optimization**: Section 80C, LTCG, STCG strategies
- 🎯 **Goal-Based Planning**: Tailored to specific financial objectives
- 🔒 **Secure**: API keys managed via Streamlit Secrets
- 📱 **Responsive Design**: Works on desktop and mobile
- 🌐 **India-Focused**: RBI/SEBI compliant recommendations

---

## 🛠️ Deployment on Streamlit Cloud

### **Quick Deploy**

1. **Fork/Push** this repo to your GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io/)
3. Click **"New app"**
4. Select:
   - Repository: `YourUsername/financial-goal-tracker`
   - Branch: `main`
   - Main file path: `app.py`
5. Click **"Deploy"**

### **Add Secrets**

1. In app dashboard, click **"Settings"** → **"Secrets"**
2. Add:
   ```toml
   PERPLEXITY_API_KEY = "pplx-your-key-here"
   ```
3. Save and app restarts automatically ✨

---

## 📚 Asset Classes Explained

### **🏦 Equity (Stocks/Mutual Funds)**
- **Risk**: High
- **Returns**: 12-15% CAGR historically
- **Best For**: Long-term goals (10+ years), aggressive investors
- **Examples**: Nifty 50 Index Fund, Parag Parikh Flexi Cap

### **📊 Debt (Bonds/Fixed Income)**
- **Risk**: Low to Medium
- **Returns**: 6-9% CAGR
- **Best For**: Capital preservation, conservative investors
- **Examples**: PPF, Corporate Bonds, Debt Mutual Funds

### **🥇 Gold**
- **Risk**: Medium
- **Returns**: 8-10% CAGR, inflation hedge
- **Best For**: Portfolio diversification, hedging
- **Examples**: Sovereign Gold Bonds, Gold ETFs

### **🥈 Silver**
- **Risk**: Medium-High
- **Returns**: Volatile, industrial demand-driven
- **Best For**: Tactical allocation (3-5%)
- **Examples**: Physical silver, Silver ETFs

### **⛽ Crude Oil/Energy**
- **Risk**: High (commodity volatility)
- **Returns**: Cyclical, tied to oil prices
- **Best For**: Small tactical bets (2-5%)
- **Examples**: Energy sector mutual funds, Commodity ETFs

### **🏢 Real Estate**
- **Risk**: Medium (illiquid)
- **Returns**: 8-12% including rental yield
- **Best For**: Long-term, high capital investors
- **Examples**: REITs (liquid), Direct property (illiquid)

---

## ⚠️ Risk Disclosure

### **Market Risks**
- Equity markets are subject to volatility
- Past performance doesn't guarantee future returns
- Debt instruments carry interest rate and credit risk
- Commodities (gold, silver, crude) are highly volatile
- Real estate is illiquid and market-dependent

### **AI Limitations**
- LLM recommendations are based on available data, not personalized analysis
- Cannot account for individual tax situations or liabilities
- Market conditions change rapidly; recommendations may become outdated
- Does NOT replace professional financial planning

---

## 🔮 Future Enhancements

- [ ] **PDF Report Generation**: Export investment plan as PDF
- [ ] **Portfolio Tracking**: Track actual vs. planned investments
- [ ] **Rebalancing Alerts**: Notify when to adjust allocations
- [ ] **Multiple Goals**: Plan for retirement + education simultaneously
- [ ] **Expense Ratio Comparison**: Compare fund costs
- [ ] **Historical Backtesting**: See how strategy would've performed
- [ ] **SIP Calculator**: Calculate SIP returns with visualization
- [ ] **Tax Calculator**: Estimate tax liability on investments

---

## 🤝 Contributing

This is a portfolio/learning project. Contributions welcome!

### **How to Contribute**
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License & Disclaimer

**License**: MIT License (open source)

**Disclaimer**:
- ⚠️ **For educational purposes only**
- ❌ **NOT professional financial advice**
- 🚫 **NOT a substitute for SEBI-registered advisors**
- 📊 **AI-generated recommendations may be inaccurate**
- 💼 **Consult certified financial planners before investing**
- 📉 **Past performance ≠ future returns**
- 🔒 **No liability for investment decisions made using this tool**

---

## 👨‍💻 About the Developer

Built with 🧡 by **[Ankit Saxena](https://github.com/Ank576)**

**Product Manager | Fintech Enthusiast | AI/LLM Explorer**

This project demonstrates:
- ✅ **Fintech Domain Knowledge**: Asset allocation, tax strategies, Indian markets
- ✅ **LLM Integration**: Prompt engineering for financial use cases
- ✅ **Product Thinking**: Goal-based wealth planning UX
- ✅ **Rapid Prototyping**: Streamlit for quick MVP development

### **Connect**
- 🔗 [LinkedIn](https://linkedin.com/in/ankitsaxena576)
- 💼 [GitHub Portfolio](https://github.com/Ank576)
- 🌐 [Portfolio Website](https://ank576.github.io/Portfolio/)

---

## 🔗 Related Projects

### **My Fintech Portfolio**
1. 🛒 [BNPL Eligibility Checker](https://github.com/Ank576/bnpl-eligibility-checker) - LLM-powered BNPL approval simulator
2. 🏦 [RBI Fair Practices Auditor](https://github.com/Ank576/fair-practices-auditor) - Loan compliance checker
3. 💰 **Financial Goal Tracker** *(This repo)*

More fintech prototypes coming soon!

---

## 🌟 Show Your Support

If you find this project useful:
- ⭐ **Star this repository**
- 🍴 **Fork for your own experiments**
- 🐦 **Share on social media**
- 💬 **Provide feedback via Issues**

---

**Happy Investing! 💰📈**

*Remember: This is a learning tool. Always do your own research and consult professionals before making financial decisions.*
