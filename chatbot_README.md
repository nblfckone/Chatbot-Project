<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Jackson: Athletic Support ChatBot</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      line-height: 1.6;
      margin: 20px auto;
      max-width: 900px;
      color: #333;
    }
    h1, h2, h3 {
      color: #00509e;
    }
    pre {
      background-color: #f4f4f4;
      padding: 10px;
      border-radius: 4px;
      overflow-x: auto;
    }
    code {
      font-family: 'Courier New', monospace;
      background-color: #eee;
      padding: 2px 5px;
      border-radius: 3px;
    }
    ul {
      margin-bottom: 1em;
    }
  </style>
</head>
<body>

  <h1>Jackson: Athletic Support ChatBot</h1>

  <p><strong>Technology Stack:</strong> Python, Streamlit, TF-IDF, Cosine Similarity, Pandas, Scikit-learn</p>

  <h2>Overview</h2>
  <p>Jackson is a proof-of-concept chatbot designed to provide immediate athletic support information using natural language input. It leverages TF-IDF vectorization and cosine similarity to match user questions with the most relevant pre-defined answers. This lightweight solution requires no machine learning training and is ideal for FAQ-based support systems in athletic departments.</p>

  <h2>Features</h2>
  <ul>
    <li>Natural language input with semantic matching</li>
    <li>Fast response engine using TF-IDF and cosine similarity</li>
    <li>Powered by live data from a Google Sheets document (CSV export)</li>
    <li>Interactive web interface built with Streamlit</li>
    <li>No model training required — works with structured Q&A data</li>
  </ul>

  <h2>How It Works</h2>
  <ol>
    <li><strong>Data Source:</strong> The application loads a dataset of questions and answers from a publicly accessible Google Sheet via direct CSV export.</li>
    <li><strong>Text Vectorization:</strong> A TfidfVectorizer processes all known questions and converts them into numerical vectors.</li>
    <li><strong>Similarity Matching:</strong> When a user submits a query, it is transformed into a vector and compared against known questions using cosine similarity.</li>
    <li><strong>Response Retrieval:</strong> The answer associated with the most similar question is returned as the chatbot's response.</li>
  </ol>

  <h2>Requirements</h2>
  <p>Ensure you have Python 3.8 or higher installed, along with the following packages:</p>
  <ul>
    <li>streamlit</li>
    <li>pandas</li>
    <li>scikit-learn</li>
    <li>numpy</li>
  </ul>

  <h2>Installation</h2>
  <p>Install the required dependencies using pip:</p>
  <pre>pip install streamlit pandas scikit-learn numpy</pre>

  <h2>Running the Application</h2>
  <ol>
    <li>Clone the repository to your local machine:</li>
    <pre>git clone https://github.com/your-username/jackson-athletic-chatbot.git<br>cd jackson-athletic-chatbot</pre>
    
    <li>Launch the Streamlit application:</li>
    <pre>streamlit run app.py</pre>
    
    <li>Open the app in your browser at <a href="http://localhost:8501">http://localhost:8501</a> and begin interacting with the chatbot.</li>
  </ol>

  <h2>Data Format</h2>
  <p>The chatbot reads data from a CSV file generated from a Google Sheet. The sheet must contain two columns:</p>
  <ul>
    <li><code>Question</code></li>
    <li><code>Answer</code></li>
  </ul>
  <p>Both fields must be populated. The current data source is loaded from the following URL:</p>
  <pre>https://docs.google.com/spreadsheets/d/1oSNqY-S3ga7huK4MesZAHRBysFBN_at_JHK5WUE6NOM/export?format=csv&amp;gid=0</pre>
  <p>You can replace this URL with your own Google Sheet if needed, provided it follows the same structure and is publicly accessible.</p>

  <h2>Author</h2>
  <p>Christian Landry</p>
  <p>This project was developed as a proof of concept for improving accessibility to athletic support resources through conversational AI.</p>

</body>
</html>
