# # algorithm1.py
# import matplotlib.pyplot as plt
# matplotlib.use('Agg')

# def run(data):
#     plt.figure()
#     data.plot()  # Example plot
#     plt.savefig('uploads/algorithm1_result.png')  # Save the figure
#     return 'uploads/algorithm1_result.png'

import matplotlib.pyplot as plt

def run(df):
    # Example: Create a simple plot
    plt.plot(df['Column1'], df['Column2'])
    graph_filename = 'graph.png'  # Just the filename, not the full path
    graph_path = os.path.join('uploads', graph_filename)  # Save the file in the uploads directory
    plt.savefig(graph_path)
    plt.close()  # Close the plot to free up memory
    
    # Return just the filename to be used in the URL
    return graph_filename