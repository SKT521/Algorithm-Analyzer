
# @app.route('/upload', methods=['POST'])
# def upload_files():
#     print("Upload route reached")
#     csv_file = request.files['csv_file']
#     algorithm_files = request.files.getlist('algorithm_files')

#     if not csv_file or not algorithm_files:
#         return "No files uploaded.", 400

#     # Save the CSV file
#     csv_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
#     csv_file.save(csv_path)

#     results = []
#     for algorithm_file in algorithm_files:
#         algorithm_path = os.path.join(app.config['UPLOAD_FOLDER'], algorithm_file.filename)
#         algorithm_file.save(algorithm_path)

#         # Import the algorithm file as a module
#         spec = importlib.util.spec_from_file_location("algorithm_module", algorithm_path)
#         algorithm_module = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(algorithm_module)

#         df = pd.read_csv(csv_path)
#         result = algorithm_module.run(df)
#         results.append(result)

#     return render_template('results.html', results=results)

# from flask import Flask, render_template, request, send_from_directory
# import pandas as pd
# import os
# import importlib.util

# app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = 'uploads/'

# # Ensure the uploads directory exists
# if not os.path.exists(app.config['UPLOAD_FOLDER']):
#     os.makedirs(app.config['UPLOAD_FOLDER'])

# @app.route('/')
# def index():
#     return render_template('index.html')



# @app.route('/upload', methods=['POST'])
# def upload_files():
#     print("Upload route reached")
#     csv_file = request.files['csv_file']
#     algorithm_files = request.files.getlist('algorithm_files')

#     if not csv_file or not algorithm_files:
#         return "No files uploaded.", 400

#     # Save the CSV file
#     csv_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
#     csv_file.save(csv_path)

#     results = []
#     for algorithm_file in algorithm_files:
#         algorithm_path = os.path.join(app.config['UPLOAD_FOLDER'], algorithm_file.filename)
#         algorithm_file.save(algorithm_path)

#         # Import the algorithm file as a module
#         spec = importlib.util.spec_from_file_location("algorithm_module", algorithm_path)
#         algorithm_module = importlib.util.module_from_spec(spec)
#         spec.loader.exec_module(algorithm_module)

#         # Load the CSV data and run the algorithm
#         df = pd.read_csv(csv_path)
#         graph_path = algorithm_module.run(df)  # Get the path to the generated graph
#         results.append(graph_path)  # Store the path to the graph in the results list

#     # Pass the list of graph paths to the template
#     return render_template('results.html', results=results)

# @app.route('/uploads/<filename>')
# def uploaded_file(filename):
#     return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)


from flask import Flask, render_template, request, send_from_directory
import pandas as pd
import os
import importlib.util

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

# Ensure the uploads directory exists
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_files():
    print("Upload route reached")
    csv_file = request.files['csv_file']
    algorithm_files = request.files.getlist('algorithm_files')

    if not csv_file or not algorithm_files:
        return "No files uploaded.", 400

    # Save the CSV file
    csv_path = os.path.join(app.config['UPLOAD_FOLDER'], csv_file.filename)
    csv_file.save(csv_path)

    results = []
    for algorithm_file in algorithm_files:
        algorithm_path = os.path.join(app.config['UPLOAD_FOLDER'], algorithm_file.filename)
        algorithm_file.save(algorithm_path)

        # Import the algorithm file as a module
        spec = importlib.util.spec_from_file_location("algorithm_module", algorithm_path)
        algorithm_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(algorithm_module)

        # Load the CSV data and run the algorithm
        df = pd.read_csv(csv_path)
        graph_path = os.path.join(app.config['UPLOAD_FOLDER'], algorithm_module.run(df).replace(app.config['UPLOAD_FOLDER'], '').strip(os.path.sep))
        print(f"Generated graph path: {graph_path}")
        results.append(graph_path)  # Store the path to the graph in the results list

    # Pass the list of graph paths to the template
    return render_template('results.html', results=results)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
