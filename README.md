# 🌱 Eco Score Predictor

A machine learning-powered web application that predicts the environmental impact of products using various sustainability factors. Built with Streamlit and XGBoost, this tool helps users assess and improve their product's eco-friendliness.

## 🌟 Features

- **Interactive Web Interface**: User-friendly Streamlit dashboard with modern styling
- **ML-Powered Predictions**: XGBoost model for accurate eco score predictions
- **Comprehensive Input Parameters**: 
  - Basic product information (carbon footprint, water usage)
  - Product categories (food, beverage, accessories, personal care)
  - Packaging materials (plastic, glass, cardboard, compostable, etc.)
  - Transportation modes (air, ship, truck)
- **Real-time Scoring**: Instant eco score calculation (0-100 scale)
- **Visual Feedback**: Color-coded results with recommendations
- **Responsive Design**: Mobile-friendly interface with gradient styling

## 🎯 Eco Score Categories

| Score Range | Category | Description |
|-------------|----------|-------------|
| 80-100 | 🌟 Excellent | Minimal environmental impact |
| 60-79 | ✅ Good | Environmentally friendly with minor improvements needed |
| 40-59 | ⚠️ Fair | Moderate impact, consider sustainable alternatives |
| Below 40 | ❌ Needs Improvement | High environmental impact, significant changes required |

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/eco-score-predictor.git
   cd eco-score-predictor
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Add your trained model**
   
   Place your trained XGBoost model file as `xgboost_model.pkl` in the root directory.

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the app**
   
   Open your browser and navigate to `http://localhost:8501`

## 📁 Project Structure

```
eco-score-predictor/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── xgboost_model.pkl     # Trained ML model (not included)
├── README.md             # Project documentation
└── assets/               # Images and static files (optional)
```

## 🔧 Model Requirements

The application expects a trained XGBoost model saved as `xgboost_model.pkl` with the following input features:

### Input Features (19 total)
- `Carbon (kg)`: Carbon footprint in kilograms
- `Water (L)`: Water usage in liters
- `Animal-Based`: Binary indicator (0/1)
- `Imported`: Binary indicator (0/1)
- **Categories** (4 binary features):
  - `Category_Accessories`
  - `Category_Beverage`
  - `Category_Food`
  - `Category_Personal Care`
- **Packaging Types** (8 binary features):
  - `Packaging_Cardboard`
  - `Packaging_Compost`
  - `Packaging_Foil`
  - `Packaging_Glass`
  - `Packaging_Paper`
  - `Packaging_Plastic`
  - `Packaging_TetraPak`
  - `Packaging_no packing`
- **Transport Modes** (3 binary features):
  - `Transport Mode_Air`
  - `Transport Mode_Ship`
  - `Transport Mode_Truck`

## 🎨 User Interface

The application features a modern, responsive design with:

- **Gradient backgrounds** and smooth animations
- **Interactive forms** with intuitive input controls
- **Real-time metrics** and progress indicators
- **Color-coded results** based on eco score ranges
- **Helpful tooltips** and recommendations
- **Mobile-responsive** layout

## 📊 Usage Example

1. **Enter Basic Information**:
   - Carbon Footprint: 2.5 kg
   - Water Usage: 150 L
   - Animal-Based: No
   - Imported: Yes

2. **Select Category**: Food

3. **Choose Packaging**: Plastic + Cardboard

4. **Select Transport**: Truck

5. **Get Results**: Eco Score of 65/100 (Good category)

## 🛠️ Technical Details

### Dependencies

- **streamlit**: Web application framework
- **joblib**: Model serialization
- **pandas**: Data manipulation
- **xgboost**: Machine learning model
- **numpy**: Numerical computations
- **scikit-learn**: ML utilities

### Performance

- **Load time**: < 2 seconds
- **Prediction time**: < 100ms
- **Model size**: Typically 1-10 MB
- **Memory usage**: ~50-100 MB

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Setup

```bash
# Clone your fork
git clone https://github.com/yourusername/eco-score-predictor.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install development dependencies
pip install -r requirements.txt

# Run in development mode
streamlit run app.py --server.runOnSave true
```

## 📈 Roadmap

- [ ] **API Endpoint**: FastAPI integration for programmatic access
- [ ] **Batch Processing**: Upload CSV files for bulk predictions
- [ ] **Model Retraining**: Interface for model updates
- [ ] **Historical Tracking**: Save and compare predictions
- [ ] **Advanced Analytics**: Detailed environmental impact breakdown
- [ ] **Integration**: Support for external data sources

## ⚠️ Known Issues

- Model file must be manually added (not included in repository)
- Limited to predefined categories and packaging types
- Requires internet connection for initial Streamlit setup

## 🙏 Acknowledgments

- Built with [Streamlit](https://streamlit.io/) for the web interface
- Powered by [XGBoost](https://xgboost.readthedocs.io/) for machine learning
- Inspired by sustainable development goals

## 📞 Support

- **Issues**: [GitHub Issues](https://github.com/yourusername/eco-score-predictor/issues)
- **Discussions**: [GitHub Discussions](https://github.com/yourusername/eco-score-predictor/discussions)
- **Email**: your.email@example.com

## 🌍 Environmental Impact

This tool is designed to promote environmental awareness and help businesses make more sustainable choices. Every small improvement in eco scores contributes to a healthier planet.

---

**Made with 💚 for a sustainable future**
