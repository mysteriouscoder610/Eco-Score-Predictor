import streamlit as st
import joblib
import pandas as pd

# Configure page
st.set_page_config(
    page_title="Eco Score Predictor",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for enhanced styling
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #4CAF50, #2E7D32);
        padding: 2rem;
        border-radius: 10px;
        text-align: center;
        color: white;
        margin-bottom: 2rem;
    }
    
    .section-header {
        background: linear-gradient(90deg, #E8F5E8, #C8E6C9);
        padding: 1rem;
        border-radius: 8px;
        border-left: 4px solid #4CAF50;
        margin: 1rem 0;
    }
    
    .metric-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        border: 1px solid #E0E0E0;
        text-align: center;
    }
    
    .score-excellent {
        background: linear-gradient(135deg, #4CAF50, #8BC34A);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(76, 175, 80, 0.3);
    }
    
    .score-good {
        background: linear-gradient(135deg, #FF9800, #FFC107);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(255, 152, 0, 0.3);
    }
    
    .score-poor {
        background: linear-gradient(135deg, #F44336, #E57373);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 20px rgba(244, 67, 54, 0.3);
    }
    
    .info-box {
        background: #E3F2FD;
        border: 1px solid #2196F3;
        border-radius: 8px;
        padding: 1rem;
        margin: 1rem 0;
    }
    
    .stButton > button {
        background: linear-gradient(90deg, #4CAF50, #45a049);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        border-radius: 25px;
        font-size: 1.1rem;
        font-weight: bold;
        transition: all 0.3s ease;
        width: 100%;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 15px rgba(76, 175, 80, 0.4);
    }
</style>
""", unsafe_allow_html=True)

# Load the trained model
@st.cache_resource
def load_model():
    try:
        model = joblib.load('xgboost_model.pkl')
        return model
    except FileNotFoundError:
        st.error("Model file 'xgboost_model.pkl' not found. Please make sure it's in the same directory.")
        return None

model = load_model()

# Main header
st.markdown("""
<div class="main-header">
    <h1>🌱 Eco Score Predictor</h1>
    <p>Predict the environmental impact of your product using AI</p>
</div>
""", unsafe_allow_html=True)

# Sidebar for information
with st.sidebar:
    st.markdown("### 📊 About Eco Score")
    st.markdown("""
    **Eco Score Range:** 0-100
    - **80-100:** Excellent 🌟
    - **60-79:** Good ✅
    - **40-59:** Fair ⚠️
    - **Below 40:** Needs Improvement ❌
    """)
    
    st.markdown("### 🎯 How to Use")
    st.markdown("""
    1. Enter basic product information
    2. Select relevant categories
    3. Choose packaging materials
    4. Select transport modes
    5. Click 'Predict Eco Score'
    """)
    
    st.markdown("### 🌍 Environmental Impact")
    st.markdown("""
    This tool helps assess:
    - Carbon footprint
    - Water usage
    - Packaging sustainability
    - Transportation efficiency
    """)

if model is not None:
    # Create main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Basic Information Section
        st.markdown("""
        <div class="section-header">
            <h3>🔧 Basic Product Information</h3>
        </div>
        """, unsafe_allow_html=True)
        
        basic_col1, basic_col2 = st.columns(2)
        
        with basic_col1:
            carbon = st.number_input('🔥 Carbon Footprint (kg)', min_value=0.0, format="%.2f", 
                                   help="Carbon emissions during production")
            animal_based = st.selectbox('🐄 Animal-Based Product', [0, 1], 
                                      format_func=lambda x: '🐄 Yes' if x == 1 else '🌱 No')
        
        with basic_col2:
            water = st.number_input('💧 Water Usage (L)', min_value=0.0, format="%.2f",
                                  help="Water consumption during production")
            imported = st.selectbox('🌍 Imported Product', [0, 1], 
                                  format_func=lambda x: '✈️ Yes' if x == 1 else '🏠 Local')
        
        # Category Section
        st.markdown("""
        <div class="section-header">
            <h3>📦 Product Category</h3>
        </div>
        """, unsafe_allow_html=True)
        
        cat_col1, cat_col2 = st.columns(2)
        
        with cat_col1:
            category_accessories = st.checkbox('👜 Accessories')
            category_beverage = st.checkbox('🥤 Beverage')
        
        with cat_col2:
            category_food = st.checkbox('🍎 Food')
            category_personal_care = st.checkbox('🧴 Personal Care')
        
        # Packaging Section
        st.markdown("""
        <div class="section-header">
            <h3>📦 Packaging Materials</h3>
        </div>
        """, unsafe_allow_html=True)
        
        pack_col1, pack_col2, pack_col3 = st.columns(3)
        
        with pack_col1:
            packaging_cardboard = st.checkbox('📦 Cardboard')
            packaging_compost = st.checkbox('🌱 Compostable')
            packaging_foil = st.checkbox('🔸 Foil')
        
        with pack_col2:
            packaging_glass = st.checkbox('🍶 Glass')
            packaging_paper = st.checkbox('📄 Paper')
            packaging_plastic = st.checkbox('🛍️ Plastic')
        
        with pack_col3:
            packaging_tetra_pak = st.checkbox('📦 TetraPak')
            packaging_no_packing = st.checkbox('🚫 No Packaging')
        
        # Transport Section
        st.markdown("""
        <div class="section-header">
            <h3>🚛 Transportation Mode</h3>
        </div>
        """, unsafe_allow_html=True)
        
        trans_col1, trans_col2, trans_col3 = st.columns(3)
        
        with trans_col1:
            transport_mode_air = st.checkbox('✈️ Air Transport')
        
        with trans_col2:
            transport_mode_ship = st.checkbox('🚢 Ship Transport')
        
        with trans_col3:
            transport_mode_truck = st.checkbox('🚛 Truck Transport')
        
        # Prediction Button
        st.markdown("<br>", unsafe_allow_html=True)
        predict_button = st.button('🔮 Predict Eco Score', type="primary")
    
    with col2:
        # Information panel
        st.markdown("""
        <div class="info-box">
            <h4>💡 Tips for Better Eco Score</h4>
            <ul>
                <li>Choose local products</li>
                <li>Minimize packaging</li>
                <li>Prefer plant-based options</li>
                <li>Select sustainable transport</li>
                <li>Use recyclable materials</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
        # Environmental impact indicators
        st.markdown("### 🌍 Impact Indicators")
        if carbon > 0:
            st.metric("Carbon Impact", f"{carbon} kg", delta=f"{carbon*2.2:.1f} lbs CO2")
        if water > 0:
            st.metric("Water Usage", f"{water} L", delta=f"{water*0.26:.1f} gallons")

    # Prediction Logic
    if predict_button:
        # Create a DataFrame from the input values
        input_data = pd.DataFrame({
            'Carbon (kg)': [carbon],
            'Water (L)': [water],
            'Animal-Based': [animal_based],
            'Imported': [imported],
            'Category_Accessories': [int(category_accessories)],
            'Category_Beverage': [int(category_beverage)],
            'Category_Food': [int(category_food)],
            'Category_Personal Care': [int(category_personal_care)],
            'Packaging_Cardboard': [int(packaging_cardboard)],
            'Packaging_Compost': [int(packaging_compost)],
            'Packaging_Foil': [int(packaging_foil)],
            'Packaging_Glass': [int(packaging_glass)],
            'Packaging_Paper': [int(packaging_paper)],
            'Packaging_Plastic': [int(packaging_plastic)],
            'Packaging_TetraPak': [int(packaging_tetra_pak)],
            'Packaging_no packing': [int(packaging_no_packing)],
            'Transport Mode_Air': [int(transport_mode_air)],
            'Transport Mode_Ship': [int(transport_mode_ship)],
            'Transport Mode_Truck': [int(transport_mode_truck)],
        })

        # Make prediction
        try:
            predicted_eco_score = model.predict(input_data)[0]
            
            # Convert to Python float to avoid type issues
            predicted_eco_score = float(predicted_eco_score)
            
            # Display result with enhanced styling
            st.markdown("<br>", unsafe_allow_html=True)
            
            # Determine score category and styling
            if predicted_eco_score >= 80:
                score_class = "score-excellent"
                emoji = "🌟"
                message = "Excellent Environmental Performance!"
                recommendation = "Your product has minimal environmental impact. Keep up the great work!"
            elif predicted_eco_score >= 60:
                score_class = "score-good"
                emoji = "✅"
                message = "Good Environmental Performance"
                recommendation = "Your product is environmentally friendly with room for minor improvements."
            elif predicted_eco_score >= 40:
                score_class = "score-good"
                emoji = "⚠️"
                message = "Fair Environmental Performance"
                recommendation = "Consider reducing packaging or choosing more sustainable materials."
            else:
                score_class = "score-poor"
                emoji = "❌"
                message = "Needs Environmental Improvement"
                recommendation = "Focus on reducing carbon footprint, using sustainable packaging, and local sourcing."
            
            st.markdown(f"""
            <div class="{score_class}">
                <h2>{emoji} {message}</h2>
                <h1 style="font-size: 3rem; margin: 1rem 0;">{predicted_eco_score:.1f}/100</h1>
                <p style="font-size: 1.2rem;">{recommendation}</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Progress bar (fixed to handle float conversion)
            progress_value = max(0.0, min(1.0, predicted_eco_score / 100.0))
            st.progress(progress_value)
            
            # Additional metrics
            col_met1, col_met2, col_met3 = st.columns(3)
            
            with col_met1:
                st.metric("Eco Score", f"{predicted_eco_score:.1f}", 
                         delta=f"{predicted_eco_score-50:.1f} vs avg")
            
            with col_met2:
                category = "Excellent" if predicted_eco_score >= 80 else "Good" if predicted_eco_score >= 60 else "Fair" if predicted_eco_score >= 40 else "Poor"
                st.metric("Category", category)
            
            with col_met3:
                percentile = min(99, int(predicted_eco_score * 1.2))
                st.metric("Percentile", f"{percentile}%")
            
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")
            st.error("Please check your model file and input data.")

else:
    st.error("⚠️ Model could not be loaded. Please ensure 'xgboost_model.pkl' is in the correct directory.")
    st.info("📁 Expected file location: Same directory as this script")