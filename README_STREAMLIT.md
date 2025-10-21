# 🦷 ClaimStream - Dental Claims Processing System

A Streamlit web application for intelligent dental claims processing with automated verification and decision workflows.

## 🚀 Live Demo

**Streamlit Cloud:** [Your App URL will be here]

## 📋 Features

- **Claims Management Center** - Professional interface for claims processing
- **Intelligent Verification** - Automated comparison of submitted vs PAS data
- **System Recommendations** - AI-powered approve/deny recommendations
- **Real-time Processing** - Interactive workflow simulation
- **Audit-Ready Elements** - All elements tagged for external system integration

## 🎯 Use Case Demo

This application demonstrates processing a routine dental claim:

- **Provider:** Dr. Johnson's Dental Practice
- **Member:** Susan Davis (Premium Plan, $1,500 remaining benefits)
- **Procedure:** Crown D2750 ($1,200 claim)
- **Coverage:** 80% ($960 approved, $240 member responsibility)
- **Result:** $540 remaining benefits after processing

## 🔧 Local Development

### Prerequisites
- Python 3.8+
- pip

### Installation
```bash
# Clone the repository
git clone https://github.com/rashrrush/claimstream-dental
cd claimstream-dental

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run streamlit_app.py
```

### Access
- **Local URL:** http://localhost:8501
- **Network URL:** Will be displayed in terminal

## 🌐 Deploy to Streamlit Cloud

### Step 1: Push to GitHub
```bash
# Initialize git repository (if not already done)
git init
git add .
git commit -m "Initial commit: ClaimStream Dental Claims Processing System"

# Add your GitHub repository
git remote add origin https://github.com/rashrrush/claimstream-dental.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click "New app"
4. Select your repository: `rashrrush/claimstream-dental`
5. Set main file path: `streamlit_app.py`
6. Click "Deploy!"

### Step 3: Your App Will Be Live
- **URL Format:** `https://rashrrush-claimstream-dental-streamlit-app-[hash].streamlit.app/`
- **Custom Domain:** Available with Streamlit Cloud Pro

## 🤖 System Integration Elements

The application includes specific HTML elements for external system integration:

### Key Elements for Automation
```python
# Member benefits comparison
member-benefits-submitted  # $1,500
member-benefits-pas       # $1,500

# Provider status verification  
provider-status-submitted # ACTIVE
provider-status-pas      # ACTIVE

# Final system recommendation
final-recommendation     # APPROVE

# Decision buttons
approve-btn             # Approve button
deny-btn               # Deny button
```

### JSON Data Access
```python
# Complete verification data available in:
verification-results-json  # Hidden div with full JSON data
```

## 📊 Workflow Steps

1. **View Cases** - Display pending claims
2. **Claim Details** - Show comprehensive claim information
3. **Verify Data** - Compare submitted vs PAS system data
4. **System Decision** - Automated recommendation with manual override
5. **Process Result** - Complete workflow with audit trail

## 🎨 UI Features

- **Responsive Design** - Works on desktop and mobile
- **Professional Styling** - Clean, business-appropriate interface
- **Interactive Elements** - Step-by-step workflow progression
- **Real-time Updates** - Dynamic status and calculation updates
- **Audit Trail** - Complete transaction logging

## 🔒 Security & Compliance

- **Data Validation** - All inputs validated and sanitized
- **Audit Logging** - Complete transaction trails
- **Error Handling** - Comprehensive error management
- **PII Protection** - Sensitive data properly handled

## 📈 Performance

- **Fast Loading** - Optimized for quick response times
- **Efficient Processing** - Streamlined verification workflow
- **Scalable Architecture** - Ready for production deployment

## 🛠️ Customization

### Modify Claim Data
Edit the `claim_data` in `streamlit_app.py`:
```python
st.session_state.claim_data = {
    'provider_name': 'Your Provider Name',
    'member_name': 'Your Member Name',
    'amount': 1500,  # Your claim amount
    # ... other fields
}
```

### Update Styling
Modify the CSS in the `st.markdown()` style section:
```python
st.markdown("""
<style>
    .main-header {
        background: your-color;
        # ... your styles
    }
</style>
""", unsafe_allow_html=True)
```

## 📞 Support

For questions or issues:
- **GitHub Issues:** [Create an issue](https://github.com/rashrrush/claimstream-dental/issues)
- **Documentation:** See this README
- **Streamlit Docs:** [docs.streamlit.io](https://docs.streamlit.io)

## 📄 License

MIT License - See LICENSE file for details

---

**Built with ❤️ using Streamlit | ClaimStream Dental Claims Processing System**