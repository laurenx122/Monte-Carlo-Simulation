import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="Monte Carlo Explorer", layout="wide")

tab1, tab2 = st.tabs(["🎯 Estimate Pi", "📅 Project Timeline"])

# --- TAB 1: PI ESTIMATION ---
with tab1:
    st.header("Estimating π (The Basics)")
    num_samples = st.slider("Number of 'Darts' to Throw", 100, 10000, 1000)
    
    if st.button("Run Pi Simulation"):
        x, y = np.random.uniform(-1, 1, num_samples), np.random.uniform(-1, 1, num_samples)
        inside = x**2 + y**2 <= 1
        pi_est = (np.sum(inside) / num_samples) * 4
        
        st.metric("Estimated π", f"{pi_est:.4f}")
        fig, ax = plt.subplots()
        ax.scatter(x[inside], y[inside], color='blue', s=1)
        ax.scatter(x[~inside], y[~inside], color='red', s=1)
        st.pyplot(fig)

# --- TAB 2: PROJECT TIMELINE ---
with tab2:
    st.header("Thesis Project Risk Simulator")
    st.write("Input the estimated days for your main thesis phases:")

    col1, col2, col3 = st.columns(3)
    with col1:
        min_d = st.number_input("Best Case (Days)", value=20)
    with col2:
        mode_d = st.number_input("Most Likely (Days)", value=30)
    with col3:
        max_d = st.number_input("Worst Case (Days)", value=60)

    deadline = st.slider("Your Deadline (Total Days)", 20, 100, 45)

    if st.button("Simulate Project Risks"):
        # We use a 'Triangular Distribution' because it mimics human estimation
        simulations = np.random.triangular(min_d, mode_d, max_d, 10000)
        
        prob_on_time = np.mean(simulations <= deadline) * 100
        
        st.subheader(f"Chance of finishing by day {deadline}: {prob_on_time:.1f}%")
        
        fig2, ax2 = plt.subplots()
        ax2.hist(simulations, bins=50, color='skyblue', edgecolor='black', alpha=0.7)
        ax2.axvline(deadline, color='red', linestyle='--', label='Your Deadline')
        ax2.set_xlabel("Total Days to Complete")
        ax2.set_ylabel("Frequency")
        ax2.legend()
        st.pyplot(fig2)