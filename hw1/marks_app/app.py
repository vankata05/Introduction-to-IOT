from flask import Flask, jsonify, render_template
import pandas as pd
from flask_cors import CORS
from urllib.parse import quote

app = Flask(__name__)
CORS(app)

df = pd.read_csv('marks.csv')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/tests', methods=['GET'])
def average_tests():
    test_columns = ['Test1', 'Test2', 'Test3', 'Test4']
    df['AverageTest'] = df[test_columns].mean(axis=1)
    sorted_df = df.sort_values(by='AverageTest', ascending=False)
    return jsonify(sorted_df.to_dict(orient='records'))

@app.route('/failed', methods=['GET'])
def failed_students():
    test_columns = ['Test1', 'Test2', 'Test3', 'Test4']
    df['AverageGrade'] = df[test_columns].mean(axis=1)
    failed_df = df[df['AverageGrade'] < 50]
    return jsonify(failed_df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
