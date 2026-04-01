from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# FAQ Data: Keys are the "standard" questions
faq_data = {
    "hi":"Hello! Welcome to RBI Bank Support. How can I help you today?",
    "hello":"Hello! Welcome to RBI Bank Support. How can I help you today?",
    "What is my account balance?": "You can check your balance via our mobile app or by texting 'BAL' to 12345.",
    "How do I open a new account?": "To open an account, you'll need a valid ID and proof of address. You can apply online.",
    "I lost my credit card": "Please call our 24/7 emergency line at 1-800-LOST-CARD immediately.",
    "What are your branch hours?": "Our branches are open Monday-Friday, 9:00 AM to 5:00 PM.",
    "How do I reset my password?": "Click 'Forgot Password' on the login page to receive a reset link via email."
}

questions = list(faq_data.keys())

def get_best_response(user_input):
    # 1. Add user input to the list of known questions
    temp_questions = questions + [user_input]
    
    # 2. Vectorize the text (convert words to numbers)
    vectorizer = TfidfVectorizer().fit_transform(temp_questions)
    
    # 3. Compare the last item (user input) with all previous items (FAQs)
    vectors = vectorizer
    cosine_sim = cosine_similarity(vectors[-1], vectors[:-1])
    
    # 4. Find the index of the highest similarity score
    match_index = cosine_sim.argsort()[0][-1]
    score = cosine_sim[0][match_index]
    
    # 5. Set a threshold (e.g., 0.3) so it doesn't give random answers
    if score > 0.3:
        return faq_data[questions[match_index]]
    else:
        return "I'm not quite sure I understand. Could you rephrase that? Or type 'human' to speak to an agent."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get("message", "")
    response = get_best_response(user_message)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)