
# from flask import Flask, request, jsonify, render_template
# import pandas as pd
# import webbrowser
# import threading
# import os

# app = Flask(__name__, template_folder='templates')

# def extract_csv_data(csv_path):
#     if not os.path.exists(csv_path):
#         print( "C:\Users\hp1\OneDrive\Desktop\Copy of DATASET.xlsx")
#         return {}

#     try:
#         df = pd.read_csv(csv_path)
#         if 'QUESTION' not in df.columns or 'ANSWER' not in df.columns:
#             print("❌ CSV must contain 'QUESTION' and 'ANSWER' columns.")
#             return {}

#         data = {}
#         for _, row in df.iterrows():
#             question = str(row["QUESTION"]).strip()
#             answer = str(row["ANSWER"]).strip()
#             data[question.lower()] = answer

#         print("✅ Q&A pairs loaded successfully.")
#         return data

#     except Exception as e:
#         print("❌ Error loading CSV data:", e)
#         return {}

# csv_path = 'DATASET1.csv'
# qa_data = extract_csv_data(csv_path)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/chat', methods=['POST'])
# def chat():
#     user_message = request.json.get('message', '').lower().strip()
#     response = qa_data.get(user_message, "Sorry, I don't have an answer for that.")
#     return jsonify({'reply': response})

# def open_browser():
#     webbrowser.open_new('http://127.0.0.1:5000/')

# if __name__ == '__main__':
#     threading.Timer(1.5, open_browser).start()
#     app.run(debug=True)


from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__, template_folder='templates')  # ✅ Fixed __name__

# Function to read Q&A from CSV
def extract_csv_data(csv_path):
    try:
        df = pd.read_csv(csv_path)
        data = {}

        for _, row in df.iterrows():
            question = str(row["QUESTION"]).strip()
            answer = str(row["ANSWER"]).strip()
            data[question.lower()] = answer

        print("✅ Q&A pairs loaded successfully.")
        return data

    except Exception as e:
        print("❌ Error loading CSV data:", e)
        return {}

# Load Q&A from your dataset
csv_path = 'DATASET1.csv'
qa_data = extract_csv_data(csv_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message'].lower().strip()
    response = qa_data.get(user_message, "Sorry, I don't have an answer for that.")
    return jsonify({'reply': response})

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
