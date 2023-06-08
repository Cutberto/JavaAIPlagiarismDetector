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

def compare_code_rouge_l(code_A, code_B, plagium_value):

    tokenizer = text.WhitespaceTokenizer()

    # Tokenize code A and code B
    code_A = tokenizer.tokenize([code_A])
    code_B = tokenizer.tokenize([code_B])

    # Compute Rouge-L
    result = text.metrics.rouge_l(code_A, code_B)
    return int(result.f_measure)
    if result.f_measure >= plagium_value:
        return 1
    else:
        return 0

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def compare_tokens_tfidf(tokens1, tokens2, plagium_value):

    # Crear un objeto TfidfVectorizer
    vectorizer = TfidfVectorizer()

    # Aplicar la vectorización TF-IDF a las cadenas de texto
    tfidf_matrix = vectorizer.fit_transform([tokens1, tokens2])

    # Calcular la similitud del coseno entre los vectores TF-IDF
    similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
    return similarity[0][0]
    if similarity[0][0] >= plagium_value:
        return 1
    else:
        return 0



@app.route('/compare', methods=['POST'])
def compare_texts():
    
    text1 = request.json['text1']
    text2 = request.json['text2']

    # Perform the text comparison logic here and get the result as a value between 0 and 1
    #result = compare_code_rouge_l(text1,text2,0.999)  # Replace with your actual comparison logic
    result = compare_tokens_tfidf(text1,text2,0.999)  # Replace with your actual comparison logic

    return jsonify({'value': result})

if __name__ == '__main__':
    app.run()
