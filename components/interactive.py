import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def display_interactive_chart():
    """Display an interactive chart for visualization"""
    st.subheader("Interactive Data Visualization")
    
    # Create sample data
    chart_type = st.selectbox(
        "Select Chart Type", 
        ["Line Chart", "Bar Chart", "Area Chart", "Scatter Plot"]
    )
    
    # Generate random data based on user input
    data_points = st.slider("Number of data points", 5, 50, 20)
    
    # Create random data
    np.random.seed(42)  # For reproducibility
    x = np.arange(data_points)
    y = np.random.randn(data_points).cumsum()
    
    # Display the selected chart
    if chart_type == "Line Chart":
        st.line_chart(pd.DataFrame({"values": y}, index=x))
    elif chart_type == "Bar Chart":
        st.bar_chart(pd.DataFrame({"values": y}, index=x))
    elif chart_type == "Area Chart":
        fig, ax = plt.subplots()
        # 使用更高级的颜色，例如 'viridis' 或 'plasma' 颜色映射
        ax.fill_between(x, y, color='#6A5ACD', alpha=0.7) # SlateBlue
        ax.set_facecolor('#F0F2F6') # Light gray background
        st.pyplot(fig)
    elif chart_type == "Scatter Plot":
        fig, ax = plt.subplots()
        # 使用更高级的颜色
        ax.scatter(x, y, color='#20B2AA') # LightSeaGreen
        ax.set_facecolor('#F0F2F6') # Light gray background
        st.pyplot(fig)
        
    # Add download capability for the data
    df = pd.DataFrame({"x": x, "y": y})
    csv = df.to_csv(index=False)
    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="chart_data.csv",
        mime="text/csv",
    )