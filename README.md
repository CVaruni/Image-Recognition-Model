#Football Club Logo Identification Model

I. Overview

Football Club Logo Identifier is a deep learning-based image classification system that recognizes logos of 6 major European football clubs from an uploaded image. Users simply upload a photo and the model predicts which club the logo belongs to along with a confidence score.

II. Supported Clubs

Club                     League
Barcelona                La Liga
Bayern München          Bundesliga
Liverpool              Premier League
Manchester United      Premier League
AC Milan                  Serie A
Real Madrid                La Liga

III. Features

✅ Upload any football club logo image
✅ Instant classification with confidence score
✅ Clean Streamlit web interface
✅ Trained Keras model included (.keras format)
✅ Supports all common image formats (JPG, PNG, WEBP)

IV. How It Works
1. User uploads an image via the Streamlit interface
2. Image is resized to 224x224 pixels
3. Preprocessed image is passed through the trained Keras model
4. Softmax activation outputs probability scores for each club
5. Club with the highest score is returned with confidence %

V. Project Structure
Image-Recognition-Model/
│
├── Images/                          # Training images
├── Sample/                          # Sample test images
├── upload/                          # Uploaded images (runtime)
├── Image_Classification_Model.ipynb # Model training notebook
├── Image_Classify_Model.keras       # Trained model
├── app.py                           # Streamlit web app
├── pd.py                            # Helper script
└── README.md

VI.  Installation & Setup

1. Clone the repository
bashgit clone https://github.com/CVaruni/Image-Recognition-Model.git
cd Image-Recognition-Model

2. Install dependencies
bashpip install tensorflow streamlit numpy keras

3. Run the Streamlit app
bashstreamlit run app.py

4. Open your browser at http://localhost:8501, upload a football club logo and get the prediction!

5. Sample Output
The image belongs to barcelona with a score of 97.43

VII. Tech Stack
ToolPurposeTensorFlow + KerasModel building & trainingStreamlitWeb app interfaceNumPyArray operationsJupyter LabModel development environment
