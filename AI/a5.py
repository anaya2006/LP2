from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- FAQ Data --------------------

faq_data = {
    "hi": "Hello! Welcome to RBI Bank Support. How can I help you today?",
    "hello": "Hello! Welcome to RBI Bank Support. How can I help you today?",
    "what is my account balance":
        "You can check your balance via our mobile app or by texting 'BAL' to 12345.",
    " balance account":
        "You can check your balance via our mobile app or by texting 'BAL' to 12345.",
     "check my account balance":
        "You can check your balance via our mobile app or by texting 'BAL' to 12345.",

    "how do i open a new account":
        "To open an account, you'll need a valid ID and proof of address. You can apply online.",

    "i lost my credit card":
        "Please call our 24/7 emergency line at 1-800-LOST-CARD immediately.",

    "what are your branch hours":
        "Our branches are open Monday-Friday, 9:00 AM to 5:00 PM.",

    "how do i reset my password":
        "Click 'Forgot Password' on the login page to receive a reset link via email."
}

questions = list(faq_data.keys())


# -------------------- Chatbot Logic --------------------

def get_best_response(user_input):

    # Convert input to lowercase
    user_input = user_input.lower().strip()

    # Add user input to question list
    temp_questions = questions + [user_input]

    # TF-IDF Vectorization
    vectorizer = TfidfVectorizer().fit_transform(temp_questions)

    # Cosine Similarity
    cosine_sim = cosine_similarity(vectorizer[-1], vectorizer[:-1])   # -1 last row for user input and :-1 excludes last row

    # Best match
    match_index = cosine_sim.argsort()[0][-1]  # returns last element of sorted indices (highest value)
    score = cosine_sim[0][match_index]

    # Threshold check
    if score > 0.3:
        return faq_data[questions[match_index]]   #faq_data[str key] -> returns value of the key 
    else:
        return ("I'm not quite sure I understand. "
                "Could you rephrase that? "
                "Or type 'human' to speak to an agent.")


# -------------------- Main Chat Loop --------------------

print("===== RBI BANK SUPPORT CHATBOT =====")
print("Type 'exit' to quit \n Or type human to connect to a customer service agent")
print()

while True:

    user_message = input("You: ").lower().strip()

    # Empty input check
    if not user_message:
        print("Bot: Please type something!")
        continue

    # Exit condition
    if user_message == "exit":
        print("Bot: Thank you for using RBI Bank Support!")
        break

    # Human agent simulation
    if user_message == "human":
        print("Bot: Connecting you to a customer service agent...")
        continue

    # Get chatbot response
    response = get_best_response(user_message)

    print("Bot:", response)