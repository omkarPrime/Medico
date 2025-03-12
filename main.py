import streamlit as st

# Load CSS for styling
with open('assets/styles.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Title and Introduction
st.title("Health Metrics Monitor")

st.markdown("""
<div class="gradient-header">
    <h1>Health Metrics Monitor</h1>
    <p>Your personal health tracking companion</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="text-align: center; padding: 1rem;">
    Welcome to your personal Health Metrics Monitor! Track and understand your vital health metrics
    with our interactive dashboard. Select a metric from the sidebar to get started.
</div>
""", unsafe_allow_html=True)

# Sidebar for metric selection
st.sidebar.markdown("""
<div style="text-align: center; padding: 1rem 0;">
    <h2>Health Metrics</h2>
</div>
""", unsafe_allow_html=True)

metric = st.sidebar.radio(
    "Choose a health metric to monitor:",
    ["Heart Rate", "Blood Pressure", "Body Temperature", "Respiratory Rate", "BMI"],
    key="metric_selector"
)

# Display main dashboard content
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="metric-container">
        <div style="text-align: center;">
            <h3>Your Vitals</h3>
            <img src="data:image/svg+xml;base64,YOUR_IMAGE_HERE" class="medical-icon"/>
            <p class="metric-description">Monitor your health metrics in real-time with interactive visualizations.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-container">
        <div style="text-align: center;">
            <h3>Insights</h3>
            <img src="data:image/svg+xml;base64,YOUR_IMAGE_HERE" class="medical-icon"/>
            <p class="metric-description">Understand your health data with personalized recommendations and trends.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Display Key Health Indicators
st.markdown("<h3 style='text-align: center; margin: 2rem 0;'>Key Health Indicators</h3>", unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">60-100</div>
        <div class="stats-label">Heart Rate (bpm)</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">120/80</div>
        <div class="stats-label">Blood Pressure (mmHg)</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">98.6°F</div>
        <div class="stats-label">Body Temperature</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="stats-card">
        <div class="stats-number">12-20</div>
        <div class="stats-label">Respiratory Rate (bpm)</div>
    </div>
    """, unsafe_allow_html=True)

# Display selected metric details
if metric == "Heart Rate":
    st.markdown("<h4>Heart Rate Details...</h4>", unsafe_allow_html=True)
elif metric == "Blood Pressure":
    st.markdown("<h4>Blood Pressure Details...</h4>", unsafe_allow_html=True)
elif metric == "Body Temperature":
    st.markdown("<h4>Body Temperature Details...</h4>", unsafe_allow_html=True)
elif metric == "Respiratory Rate":
    st.markdown("<h4>Respiratory Rate Details...</h4>", unsafe_allow_html=True)
elif metric == "BMI":
    st.markdown("<h4>BMI Details...</h4>", unsafe_allow_html=True)

# Footer Disclaimer
st.markdown("""
<div style="text-align: center; padding: 1rem; color: #666666;">
    <strong>Disclaimer:</strong> This tool is for educational purposes only and should not be used
    as a substitute for professional medical advice, diagnosis, or treatment.
</div>
""", unsafe_allow_html=True)