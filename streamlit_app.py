import streamlit as st
import json
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="ClaimStream - Dental Claims Processing System",
    page_icon="🦷",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #007bff, #0056b3);
        color: white;
        padding: 1rem;
        border-radius: 10px;
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .claim-card {
        background: white;
        border: 1px solid #dee2e6;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .status-pending {
        background-color: #fff3cd;
        color: #856404;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-weight: bold;
    }
    
    .status-approved {
        background-color: #d1e7dd;
        color: #0f5132;
        padding: 0.25rem 0.5rem;
        border-radius: 0.25rem;
        font-weight: bold;
    }
    
    .verification-table {
        border: 2px solid #007bff;
        border-radius: 5px;
        overflow: hidden;
    }
    
    .verification-complete {
        background: #28a745;
        color: white;
        padding: 1rem;
        text-align: center;
        font-weight: bold;
        border-radius: 5px;
        margin: 1rem 0;
    }
    
    .recommendation-approve {
        background: #28a745;
        color: white;
        padding: 1rem;
        text-align: center;
        font-size: 1.5rem;
        font-weight: bold;
        border-radius: 10px;
        margin: 1rem 0;
    }
    
    /* Button styling */
    .stButton > button[kind="primary"] {
        background-color: #28a745 !important;
        border-color: #28a745 !important;
        color: white !important;
    }
    
    .stButton > button[kind="secondary"] {
        background-color: #dc3545 !important;
        border-color: #dc3545 !important;
        color: white !important;
    }
    
    .metric-card {
        background: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'claim_data' not in st.session_state:
    st.session_state.claim_data = {
        'claim_id': 'CLM001',
        'provider_name': "Dr. Johnson's Dental Practice",
        'provider_id': 'PRV001',
        'member_name': 'Susan Davis',
        'member_id': 'MBR001',
        'procedure': 'Crown - porcelain fused to high noble metal',
        'procedure_code': 'D2750',
        'amount': 1200,
        'status': 'PENDING'
    }
if 'verification_data' not in st.session_state:
    st.session_state.verification_data = None

# Header
st.markdown("""
<div class="main-header">
    <h1>🦷 ClaimStream - Dental Claims Processing System</h1>
    <h2>Claims Management Center</h2>
</div>
""", unsafe_allow_html=True)

# Step 1: Display Claims
if st.session_state.step >= 1:
    st.markdown("### Cases")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        if st.button("View My Cases", key="view_cases", use_container_width=True):
            st.session_state.step = 2
            st.rerun()
    
    with col2:
        st.markdown("")  # Empty space for balance

# Step 2: Claim Details
if st.session_state.step >= 2:
    st.markdown("---")
    st.markdown("### Dr. Johnson's Practice - Crown Procedure Claim")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("#### Claim Information")
        
        claim_details = f"""
        | Field | Value |
        |-------|-------|
        | **Claim ID** | <span id="claim-id" data-testid="claim-id">{st.session_state.claim_data['claim_id']}</span> |
        | **Provider** | <span data-testid="provider-name-detail">{st.session_state.claim_data['provider_name']}</span> |
        | **Member** | <span data-testid="member-name-detail">{st.session_state.claim_data['member_name']}</span> |
        | **Procedure** | <span data-testid="procedure-desc-detail">{st.session_state.claim_data['procedure_code']}</span> |
        | **Amount** | <span data-testid="claim-amount-detail">${st.session_state.claim_data['amount']:,}</span> |
        | **Status** | <span data-testid="claim-status-detail">{st.session_state.claim_data['status'].lower()}</span> |
        """
        st.markdown(claim_details, unsafe_allow_html=True)
        
        # Verify Data button below claim information
        st.markdown("---")
        if st.button("🔍 Verify Data", key="verify_data", use_container_width=True, type="primary"):
            st.session_state.step = 3
            # Simulate verification process
            st.session_state.verification_data = {
                'submitted_data': {
                    'member_benefits': 1500,
                    'provider_status': 'ACTIVE',
                    'procedure_code': 'D2750',
                    'claim_amount': 1200,
                    'crown_history': 'NONE_REPORTED'
                },
                'pas_data': {
                    'member_benefits': 1500,
                    'provider_status': 'ACTIVE',
                    'procedure_coverage': 'COVERED (80%)',
                    'pricing_benchmark': 'WITHIN_RANGE',
                    'crown_history': 'NONE_FOUND'
                },
                'validation_status': {
                    'member_benefits': 'SUFFICIENT',
                    'provider_network': 'VALID',
                    'procedure_coverage': 'COVERED',
                    'pricing_validation': 'VALID',
                    'crown_history': 'CLEAR'
                },
                'recommendation': 'APPROVE',
                'calculated_benefit': {
                    'coverage_percentage': 80,
                    'covered_amount': 960,
                    'member_responsibility': 240
                }
            }
            st.rerun()
        
        st.markdown("*Click 'Verify Data' to compare submitted information with Policy Administration System*")

# Step 3: Verification Results
if st.session_state.step >= 3 and st.session_state.verification_data:
    st.markdown("---")
    st.markdown("### Claim Verification Results")
    
    # Verification complete indicator
    st.markdown("""
    <div class="verification-complete" id="verification-complete-indicator" data-testid="verification-complete-indicator">
        VERIFICATION COMPLETE - READY FOR DECISION
    </div>
    """, unsafe_allow_html=True)
    
    # Verification table
    st.markdown("#### Data Comparison")
    
    verification_table = f"""
    | Data Field | Submitted Value | PAS System Value | Validation Status |
    |------------|----------------|------------------|-------------------|
    | **Member Remaining Benefits** | <span id="member-benefits-submitted" data-testid="member-benefits-submitted">${st.session_state.verification_data['submitted_data']['member_benefits']:,}</span> | <span id="member-benefits-pas" data-testid="member-benefits-pas">${st.session_state.verification_data['pas_data']['member_benefits']:,}</span> | <span data-testid="member-benefits-status" style="color: #28a745; font-weight: bold;">{st.session_state.verification_data['validation_status']['member_benefits']}</span> |
    | **Provider Network Status** | <span id="provider-status-submitted" data-testid="provider-status-submitted">{st.session_state.verification_data['submitted_data']['provider_status']}</span> | <span id="provider-status-pas" data-testid="provider-status-pas">{st.session_state.verification_data['pas_data']['provider_status']}</span> | <span data-testid="provider-network-status" style="color: #28a745; font-weight: bold;">{st.session_state.verification_data['validation_status']['provider_network']}</span> |
    | **Procedure Coverage** | <span id="procedure-code-submitted" data-testid="procedure-code-submitted">{st.session_state.verification_data['submitted_data']['procedure_code']}</span> | <span id="procedure-coverage-pas" data-testid="procedure-coverage-pas">{st.session_state.verification_data['pas_data']['procedure_coverage']}</span> | <span data-testid="procedure-coverage-status" style="color: #28a745; font-weight: bold;">{st.session_state.verification_data['validation_status']['procedure_coverage']}</span> |
    | **Pricing Validation** | <span id="claim-amount-submitted" data-testid="claim-amount-submitted">${st.session_state.verification_data['submitted_data']['claim_amount']:,}</span> | <span id="pricing-benchmark-pas" data-testid="pricing-benchmark-pas">{st.session_state.verification_data['pas_data']['pricing_benchmark']}</span> | <span data-testid="pricing-validation-status" style="color: #28a745; font-weight: bold;">{st.session_state.verification_data['validation_status']['pricing_validation']}</span> |
    | **Prior Crown Work (5 Years)** | <span id="crown-history-submitted" data-testid="crown-history-submitted">{st.session_state.verification_data['submitted_data']['crown_history']}</span> | <span id="crown-history-pas" data-testid="crown-history-pas">{st.session_state.verification_data['pas_data']['crown_history']}</span> | <span data-testid="crown-history-status" style="color: #28a745; font-weight: bold;">{st.session_state.verification_data['validation_status']['crown_history']}</span> |
    """
    
    st.markdown(verification_table, unsafe_allow_html=True)
    
    # Benefit calculation results
    st.markdown("#### Benefit Calculation Results")
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h4 id="coverage-percentage-value" data-testid="coverage-percentage-value">{st.session_state.verification_data['calculated_benefit']['coverage_percentage']}%</h4>
            <p>Coverage Percentage</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h4 id="covered-amount-value" data-testid="covered-amount-value">${st.session_state.verification_data['calculated_benefit']['covered_amount']:,}</h4>
            <p>Covered Amount</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class="metric-card">
            <h4 id="member-responsibility-value" data-testid="member-responsibility-value">${st.session_state.verification_data['calculated_benefit']['member_responsibility']:,}</h4>
            <p>Member Responsibility</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown(f"""
        <div class="metric-card">
            <h4 id="new-benefit-balance-value" data-testid="new-benefit-balance-value">${1500 - st.session_state.verification_data['calculated_benefit']['covered_amount']:,}</h4>
            <p>New Benefit Balance</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Decision Actions with custom HTML buttons
    st.markdown("#### Decision Actions")
    
    # Create custom HTML buttons that look identical
    st.markdown("""
    <div style="display: flex; gap: 20px; margin: 20px 0;">
        <button id="approve-btn" data-testid="approve-button" 
                onclick="window.parent.postMessage({type: 'approve'}, '*')"
                style="flex: 1; height: 60px; font-size: 16px; font-weight: bold; 
                       background-color: #28a745; color: white; border: none; 
                       border-radius: 8px; cursor: pointer; transition: all 0.2s;">
            ✅ Approve Claim
        </button>
        <button id="deny-btn" data-testid="deny-button"
                onclick="window.parent.postMessage({type: 'deny'}, '*')"
                style="flex: 1; height: 60px; font-size: 16px; font-weight: bold; 
                       background-color: #dc3545; color: white; border: none; 
                       border-radius: 8px; cursor: pointer; transition: all 0.2s;">
            ❌ Deny Claim
        </button>
    </div>
    
    <script>
    window.addEventListener('message', function(event) {
        if (event.data.type === 'approve') {
            // Trigger Streamlit rerun for approve
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'approve'}, '*');
        } else if (event.data.type === 'deny') {
            // Trigger Streamlit rerun for deny
            window.parent.postMessage({type: 'streamlit:setComponentValue', value: 'deny'}, '*');
        }
    });
    </script>
    """, unsafe_allow_html=True)
    
    # Fallback Streamlit buttons (hidden but functional)
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Approve", key="approve_fallback", help="Approve claim"):
            st.session_state.step = 4
            st.session_state.claim_data['status'] = 'APPROVED'
            st.rerun()
    with col2:
        if st.button("Deny", key="deny_fallback", help="Deny claim"):
            st.session_state.step = 4
            st.session_state.claim_data['status'] = 'DENIED'
            st.rerun()
    
    # Hide the fallback buttons with CSS
    st.markdown("""
    <style>
    /* Hide fallback buttons */
    .stButton:has(button[title="Approve claim"]),
    .stButton:has(button[title="Deny claim"]) {
        display: none !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Hidden JSON data for system integration
    verification_json = json.dumps(st.session_state.verification_data, indent=2)
    st.markdown(f"""
    <div id="verification-results-json" data-testid="verification-results-json" style="display: none;">
        {verification_json}
    </div>
    """, unsafe_allow_html=True)

# Step 4: Results
if st.session_state.step >= 4:
    st.markdown("---")
    
    if st.session_state.claim_data['status'] == 'APPROVED':
        st.success("### Claim Approved!")
        st.markdown("""
        - Payment of $960 will be processed to Dr. Johnson's practice within 24 hours
        - Susan Davis's remaining benefits: $540
        - EOB sent to: susan.davis@email.com
        """)
    else:
        st.error("### Claim Denied")
        st.markdown("Claim denied by system. Notification sent to member and provider.")

# Sidebar with system information
with st.sidebar:
    st.markdown("### System Information")
    st.markdown(f"""
    **Current Step:** {st.session_state.step}/4
    
    **Claim ID:** {st.session_state.claim_data['claim_id']}
    
    **Provider:** {st.session_state.claim_data['provider_name']}
    
    **Member:** {st.session_state.claim_data['member_name']}
    
    **Amount:** ${st.session_state.claim_data['amount']:,}
    
    **Status:** {st.session_state.claim_data['status']}
    """)
    
    if st.button("Reset Demo", use_container_width=True):
        st.session_state.step = 1
        st.session_state.claim_data['status'] = 'PENDING'
        st.session_state.verification_data = None
        st.rerun()

# Footer
st.markdown("---")
st.markdown("*ClaimStream - Dental Claims Processing System | Powered by Streamlit*")