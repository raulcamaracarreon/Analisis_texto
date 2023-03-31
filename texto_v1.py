import streamlit as st
import nltk
from nltk import word_tokenize
from collections import Counter
import pandas as pd

nltk.download('punkt')

def analyze_text(text):
    # Tokenize the text into words
    words = word_tokenize(text, language="spanish")

    # Get the number of words
    num_words = len(words)

    # Get the number of letters
    num_letters = sum(len(word) for word in words)

    return num_words, num_letters

st.title("Análisis de Texto")
st.write("Qué transa Sargento, hice esta App a ver qué te parece; creo que puede ser útil para lingüistas, o ¿cómo ves?")
text = st.text_area("Ingrese el texto que desea analizar:")

if st.button("Analizar"):
    num_words, num_letters = analyze_text(text)

    st.write(f"Número de palabras: {num_words}")
    st.write(f"Número de letras: {num_letters}")

    # Calculate letter counts
    letter_counts = Counter(c.lower() for c in text if c.isalpha())

    # Create dataframe for letter counts and percentages
    df_letter_counts = pd.DataFrame.from_dict(letter_counts, orient='index', columns=['Frecuencia'])
    df_letter_counts.index.name = 'Letra'
    df_letter_counts.sort_index(inplace=True)

    total_letters = sum(df_letter_counts['Frecuencia'])
    df_letter_counts['Porcentaje'] = df_letter_counts['Frecuencia'] / total_letters * 100

    # Create table with letter counts and percentages
    st.write("Tabla de frecuencia y porcentaje de cada letra del abecedario:")
    st.dataframe(df_letter_counts)

    # Create horizontal bar plot of letter frequencies
    st.write("Frecuencia de cada letra del abecedario:")
    st.bar_chart(df_letter_counts['Frecuencia'])






