# Jackson: Athletic Support ChatBot

## Overview

Jackson is a proof-of-concept chatbot designed to provide immediate athletic support information using natural language input. It leverages TF-IDF vectorization and cosine similarity to match user questions with the most relevant pre-defined answers. This lightweight solution requires no machine learning training and is ideal for FAQ-based support systems in athletic departments.

## Features

- Natural language input with semantic matching
- Fast response engine using TF-IDF and cosine similarity
- Powered by live data from a Google Sheets document (CSV export)
- Interactive web interface built with Streamlit
- No model training required — works with structured Q&A data

## How It Works

1. **Data Source**: The application loads a dataset of questions and answers from a publicly accessible Google Sheet via direct CSV export.
2. **Text Vectorization**: A TfidfVectorizer processes all known questions and converts them into numerical vectors.
3. **Similarity Matching**: When a user submits a query, it is transformed into a vector and compared against known questions using cosine similarity.
4. **Response Retrieval**: The answer associated with the most similar question is returned as the chatbot's response.

## Requirements

Ensure you have Python 3.8 or higher installed, along with the following packages:

- streamlit
- pandas
- scikit-learn
- numpy

## Installation

Install the required dependencies using pip:

pip install streamlit pandas scikit-learn numpy

## Running the Application

1. Clone the repository to your local machine:

   git clone https://github.com/your-username/jackson-athletic-chatbot.git
   cd jackson-athletic-chatbot

2. Launch the Streamlit application:

   streamlit run app.py

3. Open the app in your browser at http://localhost:8501 and begin interacting with the chatbot.

## Data Format

The chatbot reads data from a CSV file generated from a Google Sheet. The sheet must contain two columns:

- Question
- Answer

Both fields must be populated. The current data source is loaded from the following URL:

https://docs.google.com/spreadsheets/d/1oSNqY-S3ga7huK4MesZAHRBysFBN_at_JHK5WUE6NOM/export?format=csv&gid=0

You can replace this URL with your own Google Sheet if needed, provided it follows the same structure and is publicly accessible.

## Author

Christian Landry

This project was developed as a proof of concept for improving accessibility to athletic support resources through conversational AI.

## Future Enhancements

- Implement confidence thresholding with fallback responses for low-match queries
- Support for private Google Sheets using OAuth authentication
- Integration of more advanced semantic models (e.g., Sentence Transformers)
- Add export functionality for chat history
- Improve UI with typing indicators and message alignment

## License

This project is open source and distributed under the MIT License. See the LICENSE file for full details.
