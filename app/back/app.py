from flask import Flask, request, jsonify
from flask_cors import CORS
from java_lexer import Lexer

app = Flask(__name__)
CORS(app)

def tokenize(code1):
    lexer1 = Lexer()
    
    tokens1 = lexer1.get_token_string(code1)
  
    return tokens1


import tensorflow as tf
import tensorflow_text as text

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compare_tokens_tfidf(tokens1, tokens2, plagium_value):
    print(tokens1,"\n",tokens2)
    # Crear un objeto TfidfVectorizer

    vectorizer = TfidfVectorizer()

    # Aplicar la vectorización TF-IDF a las cadenas de texto
    tfidf_matrix = vectorizer.fit_transform([tokens1, tokens2])

    # Calcular la similitud del coseno entre los vectores TF-IDF
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity[0][0]

import re 
import numpy as np
from collections import defaultdict
def calculate_transition_matrix(text):
    # Eliminar caracteres no alfanuméricos y convertir a minúsculas
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())

    words = text.split()  # Dividir el texto en palabras
    unique_words = sorted(list(set(words)))  # Obtener las palabras únicas en el texto
    word_indices = {word: i for i, word in enumerate(unique_words)}  # Asignar un índice numérico a cada palabra

    matrix = np.zeros((len(unique_words), len(unique_words)))  # Crear una matriz de ceros para la matriz de transición

    # Calcular las frecuencias de transición entre palabras consecutivas en el texto
    transitions = defaultdict(int)
    for i in range(len(words)-1):
        current_word = words[i]
        next_word = words[i+1]
        transitions[(current_word, next_word)] += 1

    # Llenar la matriz de transición con las frecuencias de transición
    for (current_word, next_word), count in transitions.items():
        current_index = word_indices[current_word]
        next_index = word_indices[next_word]
        matrix[current_index, next_index] = count

    # Normalizar las filas de la matriz para obtener probabilidades de transición
    row_sums = np.sum(matrix, axis=1)
    row_sums[row_sums == 0] = 1  # Reemplazar los valores de suma cero por 1 para evitar divisiones entre cero
    matrix = matrix / row_sums[:, np.newaxis]

    return matrix, unique_words



def cosine_ang(a, b):
    # Obtener las dimensiones de las matrices
    rows1, cols1 = a.shape
    rows2, cols2 = b.shape

    # Ajustar las dimensiones de las matrices si son diferentes
    if rows1 < rows2:
        a = np.vstack((a, np.zeros((rows2 - rows1, cols1))))
    elif rows1 > rows2:
        b = np.vstack((b, np.zeros((rows1 - rows2, cols2))))

    if cols1 < cols2:
        a = np.hstack((a, np.zeros((a.shape[0], cols2 - cols1))))
    elif cols1 > cols2:
        b = np.hstack((b, np.zeros((b.shape[0], cols1 - cols2))))

    aT = a.transpose()
    bT = b.transpose()
    C = np.dot(bT, a)
    prod_int = C.trace()

    normA = np.sqrt(np.dot(aT, a).trace())
    normB = np.sqrt(np.dot(bT, b).trace())

    cos_ang = prod_int / (normA * normB)

    return cos_ang


def compare_tokens_transition_matrix(a,b,plagium_value):
    a_matrix, words = calculate_transition_matrix(a)
    b_matrix, words = calculate_transition_matrix(b)
    cos_ang = cosine_ang(a_matrix,b_matrix)
    return cos_ang
    if cos_ang > plagium_value:
        return 1
    else:
        return 0


@app.route('/tfidf', methods=['POST'])
def compare_texts_tfidf():
    
    text1 = request.json['text1']
    text2 = request.json['text2']

    text1 = tokenize(text1)
    text2 = tokenize(text2)
    result = compare_tokens_tfidf(text1,text2,0.999)  

    return jsonify({'value': result})



@app.route('/transition', methods=['POST'])
def compare_texts_transition():
    lexer = Lexer()
    text1 = request.json['text1']
    text2 = request.json['text2']
    text1 = tokenize(text1)
    text2 = tokenize(text2)

    result = compare_tokens_transition_matrix(text1,text2,0.999) 
    
    return jsonify({'value': result})
if __name__ == '__main__':
    app.run()
