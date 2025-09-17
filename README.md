# NEWS
This project builds a deep learning model to classify news headlines into predefined categories using an LSTM (Long Short-Term Memory) network. It also includes a Streamlit web app for real-time category prediction.
Clone the Repository
git clone https://github.com/your-username/news-category-classification.git
cd news-category-classification

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Run the Streamlit App
streamlit run app.py

📂 Project Structure
├── app.py                # Streamlit web app
├── lstm_model.keras      # Trained LSTM model
├── tokenizer.pkl         # Saved tokenizer
├── label_encoder.pkl     # Saved label encoder
├── requirements.txt      # Dependencies
├── data/                 # Dataset (if applicable)
└── README.md             # Project documentation

📌 Example Prediction

Input: "Government launches new education policy for schools"
Output: Category: Education
