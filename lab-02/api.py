from cipher.transposition import TranspositionCipher
from flask import Flask, request, jsonify

app = Flask(__name__)

transposition_cipher = TranspositionCipher()


@app.route("/api/transposition/encrypt", methods=["POST"])
def transposition_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/transposition/decrypt", methods=["POST"])
def transposition_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})

# Main function 
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
