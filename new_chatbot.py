import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import streamlit as st
from time import sleep

st.title("Jackson : Athletic Support [ChatBot]")
st.caption("This is your Athletic Support bot PoC.")
st.caption("Author: Christian Landry")


@st.cache_data
def data_import():
    csv_url = "https://docs.google.com/spreadsheets/d/1oSNqY-S3ga7huK4MesZAHRBysFBN_at_JHK5WUE6NOM/export?format=csv&gid=0"
    df = pd.read_csv(csv_url, sep=',', engine='python')
    df.dropna(inplace=True)
    return df


@st.cache_data
def train_vectorizer(df):
    vectorizer = TfidfVectorizer()
    vectorizer.fit(np.concatenate(
        (df['Question'].values, df['Answer'].values)))
    question_vectors = vectorizer.transform(df['Question'].values)
    return vectorizer, question_vectors


def find_closest_response(input_question, vectorizer, question_vectors, df):
    input_question_vector = vectorizer.transform(
        [input_question])  # Fixed: () and list input
    similarities = cosine_similarity(input_question_vector, question_vectors)
    closest_index = np.argmax(similarities, axis=1)[0]
    return df['Answer'].iloc[closest_index]  # Fixed: 'Answer', not 'Anser'


def stream_data(response_chat):
    for word in response_chat.split(" "):
        yield word + " "
        sleep(0.02)


# Load data and train vectorizer
df = data_import()
vectorizer, question_vectors = train_vectorizer(
    df)  # Fixed: renamed for clarity

# Initialize conversation history
if "history" not in st.session_state:
    st.session_state["history"] = []

# Input prompt
prompt = st.chat_input("Ask Jackson something (type 'quit' to stop)")
if prompt:
    if prompt.lower() == "quit":
        st.write("**Chatbot session ended. Refresh the page to start a new chat.**")
    else:
        # Append user message
        st.session_state["history"].append({"role": "user", "message": prompt})

        # Get bot response
        bot_response = find_closest_response(
            prompt, vectorizer, question_vectors, df)
        st.session_state["history"].append(
            {"role": "bot", "message": bot_response})

# Display conversation history
for entry in st.session_state["history"]:
    with st.chat_message(entry["role"] if entry["role"] == "user" else "assistant"):
        placeholder = st.empty()
        streamed_text = ""
        for chunk in stream_data(entry["message"]):
            streamed_text += chunk
            placeholder.markdown(
                f"**Bot:** {streamed_text}" if entry["role"] == "bot" else streamed_text)
