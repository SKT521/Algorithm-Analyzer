from flask import Flask, request, render_template, redirect, url_for, send_file
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/uploads'

# Ensure the upload directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the files were uploaded
        if 'file1' not in request.files or 'file2' not in request.files:
            return "Please upload both CSV files."
        
        file1 = request.files['file1']
        file2 = request.files['file2']

        if file1.filename == '' or file2.filename == '':
            return "No selected file."

        # Save files to the upload folder
        file1_path = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
        file2_path = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)
        file1.save(file1_path)
        file2.save(file2_path)

        # Process the CSVs with a custom algorithm
        output_path = process_csvs(file1_path, file2_path)

        # Send the output CSV file as a response
        return send_file(output_path, as_attachment=True)

    return render_template('index.html')

def process_csvs(file1_path, file2_path):
    # Read the CSVs into DataFrames
    df1 = pd.read_csv(file1_path)
    df2 = pd.read_csv(file2_path)

    # Example algorithm: Merge the two CSVs on a common column (e.g., 'id')
    result = pd.merge(df1, df2, on='id', how='outer')

    # Save the result to a new CSV
    output_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.csv')
    result.to_csv(output_path, index=False)

    return output_path

if __name__ == '__main__':
    app.run(debug=True)

    