import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from datetime import datetime, timedelta

# Page configuration
st.set_page_config(
    page_title="Docker Streamlit App",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    .sidebar .sidebar-content {
        background-color: #f8f9fa;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<h1 class="main-header">🚀 Docker Streamlit App</h1>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.selectbox(
    "Choose a page",
    ["Dashboard", "Data Visualization", "Interactive Demo", "About"]
)

if page == "Dashboard":
    st.header("📊 Dashboard")
    
    # Create some sample data
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Total Users",
            value="1,234",
            delta="12%"
        )
    
    with col2:
        st.metric(
            label="Revenue",
            value="$45,678",
            delta="8%"
        )
    
    with col3:
        st.metric(
            label="Active Sessions",
            value="567",
            delta="-3%"
        )
    
    with col4:
        st.metric(
            label="Conversion Rate",
            value="2.4%",
            delta="0.5%"
        )
    
    # Sample chart
    st.subheader("📈 Sample Data Visualization")
    
    # Generate sample data
    dates = pd.date_range(start='2024-01-01', end='2024-12-31', freq='D')
    values = np.random.randn(len(dates)).cumsum() + 100
    
    df = pd.DataFrame({
        'Date': dates,
        'Value': values
    })
    
    fig = px.line(df, x='Date', y='Value', title='Sample Time Series Data')
    st.plotly_chart(fig, use_container_width=True)

elif page == "Data Visualization":
    st.header("📊 Data Visualization")
    
    # File uploader
    uploaded_file = st.file_uploader(
        "Choose a CSV file",
        type=['csv'],
        help="Upload a CSV file to visualize the data"
    )
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
            
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
            st.subheader("Data Statistics")
            st.dataframe(df.describe())
            
            # Column selection for visualization
            numeric_columns = df.select_dtypes(include=[np.number]).columns.tolist()
            
            if len(numeric_columns) >= 2:
                col1, col2 = st.columns(2)
                
                with col1:
                    x_col = st.selectbox("Select X-axis column", numeric_columns)
                
                with col2:
                    y_col = st.selectbox("Select Y-axis column", numeric_columns)
                
                if x_col and y_col:
                    fig = px.scatter(df, x=x_col, y=y_col, title=f'{x_col} vs {y_col}')
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.warning("Need at least 2 numeric columns for visualization")
                
        except Exception as e:
            st.error(f"Error reading file: {str(e)}")
    else:
        st.info("👆 Upload a CSV file to get started")

elif page == "Interactive Demo":
    st.header("🎮 Interactive Demo")
    
    # Interactive widgets
    st.subheader("Slider Demo")
    slider_value = st.slider("Select a value", 0, 100, 50)
    st.write(f"You selected: {slider_value}")
    
    st.subheader("Selectbox Demo")
    option = st.selectbox(
        "Choose an option",
        ["Option 1", "Option 2", "Option 3", "Option 4"]
    )
    st.write(f"You chose: {option}")
    
    st.subheader("Checkbox Demo")
    if st.checkbox("Show advanced options"):
        st.write("Advanced options are enabled!")
        
        # Nested controls
        advanced_option = st.radio(
            "Select advanced option",
            ["Option A", "Option B", "Option C"]
        )
        st.write(f"Advanced option selected: {advanced_option}")
    
    st.subheader("Text Input Demo")
    user_input = st.text_input("Enter your name", "Anonymous")
    st.write(f"Hello, {user_input}!")
    
    st.subheader("Number Input Demo")
    number = st.number_input("Enter a number", min_value=0, max_value=1000, value=100)
    st.write(f"Number entered: {number}")

elif page == "About":
    st.header("ℹ️ About")
    
    st.markdown("""
    ## Docker Streamlit App
    
    This is a sample Streamlit application running in a Docker container.
    
    ### Features:
    - 📊 Interactive dashboard
    - 📈 Data visualization
    - 🎮 Interactive demos
    - 📁 File upload capabilities
    - 🎨 Modern UI design
    
    ### Technology Stack:
    - **Streamlit**: Web app framework
    - **Docker**: Containerization
    - **Python**: Backend language
    - **Plotly**: Interactive charts
    - **Pandas**: Data manipulation
    
    ### Getting Started:
    1. Build the Docker image: `docker build -t streamlit-app .`
    2. Run the container: `docker run -p 8501:8501 streamlit-app`
    3. Open your browser: `http://localhost:8501`
    
    ### Docker Commands:
    ```bash
    # Build image
    docker build -t streamlit-app .
    
    # Run container
    docker run -p 8501:8501 streamlit-app
    
    # Run with docker-compose
    docker-compose up
    ```
    """)
    
    # System information
    st.subheader("System Information")
    st.code(f"""
    Python Version: {st.__version__}
    Streamlit Version: {st.__version__}
    Pandas Version: {pd.__version__}
    Numpy Version: {np.__version__}
    """)

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: #666;'>Built with ❤️ using Streamlit and Docker</div>",
    unsafe_allow_html=True
) 