from flask import Flask, request, jsonify
from flask_cors import CORS
from java_lexer import Lexer
import io 
import json 
from keras_preprocessing.text import tokenizer_from_json
import tensorflow as tf
from tensorflow.keras.layers import *
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.sequence import pad_sequences
import tensorflow as tf
import tensorflow_text as text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re 
import numpy as np
from collections import defaultdict

app = Flask(__name__)
CORS(app)

def tokenize(code1):
    lexer1 = Lexer()    
    tokens1 = lexer1.get_token_string(code1)
  
    return tokens1




with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tokenizer_from_json(data)


# Define the maximum sequence length
max_sequence_length = 100

# Define the inputs
input1 = Input(shape=(max_sequence_length,))
input2 = Input(shape=(max_sequence_length,))

# Embedding layer for input1
embedding_layer = Embedding(len(tokenizer.word_index) + 1, 100, input_length=max_sequence_length)
embedded_input1 = embedding_layer(input1)
lstm_output1 = LSTM(128, return_sequences=True)(embedded_input1)
lstm_output1 = GlobalMaxPooling1D()(lstm_output1)

# Embedding layer for input2
embedded_input2 = embedding_layer(input2)
lstm_output2 = LSTM(128, return_sequences=True)(embedded_input2)
lstm_output2 = GlobalMaxPooling1D()(lstm_output2)

# Concatenate the LSTM outputs
merged_output = Concatenate()([lstm_output1, lstm_output2])

# Dense layers
dense_output = Dense(64, activation='relu')(merged_output)
dense_output = Dropout(0.5)(dense_output)

# Output layer
output = Dense(1, activation='sigmoid')(dense_output)

# Define the model
model_lstm = Model(inputs=[input1, input2], outputs=output)

# Compile the model
model_lstm.compile(loss='binary_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])

model_lstm.load_weights('./LSTM_Model/balanced_model')


def compare_tokens_tfidf(tokens1, tokens2, plagium_value):
    print(tokens1,"\n",tokens2)
    # Crear un objeto TfidfVectorizer

    vectorizer = TfidfVectorizer()

    # Aplicar la vectorización TF-IDF a las cadenas de texto
    tfidf_matrix = vectorizer.fit_transform([tokens1, tokens2])

    # Calcular la similitud del coseno entre los vectores TF-IDF
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity[0][0]


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

@app.route("/rougel", methods = ["POST"])
def compare_code_rouge_l():

    text1 = request.json['text1']
    text2 = request.json['text2']
    text1 = tokenize(text1)
    text2 = tokenize(text2)
    
    tokenizer = text.WhitespaceTokenizer()

    # Tokenize code A and code B
    code_A = tokenizer.tokenize([text1])
    code_B = tokenizer.tokenize([text2])

    # Compute Rouge-L
    result = text.metrics.rouge_l(code_A, code_B)
    return jsonify({'value': result.f_measure[0].item()})



@app.route('/lstm', methods=['POST'])
def compare_texts_lstm():
    with open('tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)

    text1 = request.json['text1']
    text2 = request.json['text2']
    text1 = tokenize(text1)
    text2 = tokenize(text2)
    
    X_sequences_firstcode = tokenizer.texts_to_sequences(text1)
    X_sequences_secondcode = tokenizer.texts_to_sequences(text2)


    # Pad sequences to ensure uniform length
    X_padded_firstcode = pad_sequences(X_sequences_firstcode, maxlen=max_sequence_length, padding='post')
    X_padded_secondcode = pad_sequences(X_sequences_secondcode, maxlen=max_sequence_length, padding='post')

    result = model_lstm.predict([X_padded_firstcode, X_padded_secondcode])
    print(result[0][0])

    
    return jsonify({'value': result[0][0].item()})

if __name__ == '__main__':
    app.run()
