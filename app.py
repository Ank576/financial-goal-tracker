import streamlit as st
import json
from openai import OpenAI
import re

st.set_page_config(page_title="Financial Goal Tracker", layout="wide", page_icon="💰")

st.title("💰 AI-Powered Financial Goal Tracker")
st.markdown("Get personalized investment recommendations across multiple asset classes using AI.")

# Sidebar for user inputs
with st.sidebar:
    st.header("📊 Your Financial Profile")
    
    # Goal details
    goal_name = st.text_input("Goal Name", value="Retirement Fund", placeholder="e.g., Child Education, Home Purchase")
    target_amount = st.number_input("Target Amount (₹)", min_value=10000.0, value=5000000.0, step=50000.0, format="%.0f")
    current_savings = st.number_input("Current Savings (₹)", min_value=0.0, value=500000.0, step=10000.0, format="%.0f")
    tenure_years = st.slider("Investment Tenure (Years)", 1, 30, 10)
    
    st.markdown("---")
    
    # Risk profile
    st.subheader("Risk Appetite")
    risk_appetite = st.select_slider(
        "Select your risk tolerance",
        options=["Very Conservative", "Conservative", "Moderate", "Aggressive", "Very Aggressive"],
        value="Moderate"
    )
    
    # Age and income
    age = st.slider("Age", 18, 65, 30)
    monthly_income = st.number_input("Monthly Income (₹)", min_value=10000.0, value=100000.0, step=5000.0, format="%.0f")
    monthly_investment = st.number_input("Monthly Investment Capacity (₹)", min_value=1000.0, value=20000.0, step=1000.0, format="%.0f")
    
    st.markdown("---")
    
    # Investment preferences
    st.subheader("Preferences")
    prefer_liquid = st.checkbox("Prefer liquid investments", value=True)
    include_real_estate = st.checkbox("Include Real Estate", value=False)
    tax_saving = st.checkbox("Prioritize tax-saving instruments", value=True)

# Calculate required monthly investment
gap_amount = max(0, target_amount - current_savings)
required_monthly = gap_amount / (tenure_years * 12) if tenure_years > 0 else 0

# Display goal summary
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Target Amount", f"₹{target_amount:,.0f}")
with col2:
    st.metric("Current Savings", f"₹{current_savings:,.0f}")
with col3:
    st.metric("Gap to Cover", f"₹{gap_amount:,.0f}", delta=f"{(gap_amount/target_amount*100):.1f}%")
with col4:
    st.metric("Time Horizon", f"{tenure_years} years")

st.markdown("---")

if st.button("🔍 Generate Investment Plan", type="primary", use_container_width=True):
    # Check for API key
    api_key = st.secrets.get("PERPLEXITY_API_KEY", None)
    
    if not api_key:
        st.error("⚠️ PERPLEXITY_API_KEY not found in Streamlit secrets!")
        st.info("""**Setup Instructions:**
        1. Go to your Streamlit Cloud app settings
        2. Navigate to 'Secrets' section
        3. Add: `PERPLEXITY_API_KEY = "pplx-your-key-here"`
        4. Get your key from: https://www.perplexity.ai/settings/api
        """)
        st.stop()
    
    # Initialize client
    client = OpenAI(
        api_key=api_key,
        base_url="https://api.perplexity.ai"
    )
    
    with st.spinner("🤖 AI is analyzing your profile and searching for best investment options..."):
        prompt = f"""You are a SEBI-registered financial advisor specializing in goal-based wealth planning for Indian investors.

INVESTOR PROFILE:
- Goal: {goal_name}
- Target Amount: ₹{target_amount:,.0f}
- Current Savings: ₹{current_savings:,.0f}
- Gap Amount: ₹{gap_amount:,.0f}
- Investment Tenure: {tenure_years} years
- Risk Appetite: {risk_appetite}
- Age: {age} years
- Monthly Income: ₹{monthly_income:,.0f}
- Monthly Investment Capacity: ₹{monthly_investment:,.0f}
- Liquidity Preference: {"High" if prefer_liquid else "Medium"}
- Real Estate Interest: {"Yes" if include_real_estate else "No"}
- Tax Saving Priority: {"Yes" if tax_saving else "No"}

TASK:
Search and analyze current market conditions (2025) for these asset classes:
1. Equity (Large-cap, Mid-cap, Small-cap mutual funds, Index funds)
2. Debt (Corporate bonds, Government securities, Fixed deposits, PPF, EPF)
3. Gold (Physical, Digital Gold, Gold ETFs, Sovereign Gold Bonds)
4. Silver (Physical, Silver ETFs)
5. Crude Oil (Energy sector funds, Commodity ETFs)
6. Real Estate (REITs, direct property - if applicable)

Provide asset allocation considering:
- Current Indian market conditions and interest rates
- Historical returns for each asset class
- Risk-adjusted returns matching investor's risk profile
- Tax implications (Section 80C, LTCG, STCG)
- Liquidity requirements
- Inflation hedge

Return ONLY valid JSON (no markdown, no code blocks):

{{
  "goal_achievable": boolean,
  "confidence_score": "number 0-100",
  "required_monthly_sip": number,
  "expected_corpus": number,
  "expected_return_cagr": "string percentage",
  "asset_allocation": {{
    "equity": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "debt": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "gold": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "silver": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "crude_energy": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}},
    "real_estate": {{"percentage": number, "allocation_amount": number, "instruments": ["instrument1", "instrument2"]}}
  }},
  "recommendations": ["recommendation1", "recommendation2", "recommendation3"],
  "risk_factors": ["risk1", "risk2"],
  "tax_benefits": ["benefit1", "benefit2"],
  "rebalancing_frequency": "string",
  "alternative_strategies": ["strategy1", "strategy2"],
  "market_outlook_2025": "string summary",
  "disclaimer": "string"
}}

Ensure asset allocation percentages sum to 100%. Base recommendations on current 2025 market data."""

        try:
            response = client.chat.completions.create(
                model="sonar-pro",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.2
            )
            
            raw = response.choices[0].message.content.strip()
            
            # Clean markdown
            raw = re.sub(r'``````', '', raw)
            
            # Extract JSON
            json_match = re.search(r'\{.*\}', raw, re.DOTALL)
            if not json_match:
                st.error("No JSON found in LLM response")
                st.code(raw)
                st.stop()
            
            json_str = json_match.group(0)
            result = json.loads(json_str)
            
            # Display results
            st.success("✅ Investment Plan Generated Successfully!")
            
            # Key metrics
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Goal Achievable", "✅ YES" if result["goal_achievable"] else "⚠️ NEEDS ADJUSTMENT")
            with col2:
                st.metric("Confidence Score", f"{result['confidence_score']}%")
            with col3:
                st.metric("Required Monthly SIP", f"₹{result['required_monthly_sip']:,.0f}")
            with col4:
                st.metric("Expected CAGR", result['expected_return_cagr'])
            
            st.markdown("---")
            
            # Asset Allocation Pie Chart
            st.subheader("📊 Recommended Asset Allocation")
            
            allocation = result['asset_allocation']
            
            # Create columns for asset breakdown
            col1, col2 = st.columns([1, 1])
            
            with col1:
                st.markdown("### Allocation Breakdown")
                for asset_class, details in allocation.items():
                    if details['percentage'] > 0:
                        st.markdown(f"""
                        **{asset_class.replace('_', ' ').title()}**: {details['percentage']}%
                        - Monthly: ₹{details['allocation_amount']:,.0f}
                        """)
            
            with col2:
                st.markdown("### Recommended Instruments")
                for asset_class, details in allocation.items():
                    if details['percentage'] > 0 and details['instruments']:
                        st.markdown(f"**{asset_class.replace('_', ' ').title()}**")
                        for instrument in details['instruments']:
                            st.write(f"• {instrument}")
            
            st.markdown("---")
            
            # Recommendations
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("💡 Key Recommendations")
                for rec in result['recommendations']:
                    st.success(f"✓ {rec}")
            
            with col2:
                st.subheader("⚠️ Risk Factors")
                for risk in result['risk_factors']:
                    st.warning(f"⚠ {risk}")
            
            # Tax benefits
            if result.get('tax_benefits'):
                st.subheader("💰 Tax Benefits")
                for benefit in result['tax_benefits']:
                    st.info(f"🏦 {benefit}")
            
            # Additional insights
            with st.expander("📈 Market Outlook & Strategy"):
                st.write("**Rebalancing Frequency:**", result.get('rebalancing_frequency', 'Quarterly'))
                st.write("**Market Outlook 2025:**", result.get('market_outlook_2025', 'N/A'))
                
                st.markdown("**Alternative Strategies:**")
                for strategy in result.get('alternative_strategies', []):
                    st.write(f"• {strategy}")
            
            # Full JSON
            with st.expander("🔍 View Complete Analysis (JSON)"):
                st.json(result)
            
            # Disclaimer
            st.markdown("---")
            st.warning(f"**Disclaimer:** {result.get('disclaimer', 'This is an AI-generated recommendation for educational purposes only. Consult a SEBI-registered financial advisor before making investment decisions.')}")

        except json.JSONDecodeError as e:
            st.error(f"JSON Parse Error: {e}")
            st.code(json_str if 'json_str' in locals() else raw)
        except Exception as e:
            st.error(f"API Error: {str(e)}")
            st.info("Set PERPLEXITY_API_KEY in Streamlit secrets")

st.markdown("---")
st.caption("**Built with 🧡 by Ankit Saxena** | AI-Powered Wealth Planning | Demo Only - Not Financial Advice")
