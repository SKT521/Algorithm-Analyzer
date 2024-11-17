import matplotlib.pyplot as plt

def run(data):
    plt.figure()
    plt.scatter(data['x'], data['y'], color='red')
    plt.title('Scatter Plot of x vs y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.savefig('uploads/algorithm2_result.png')  # Save the figure
    plt.close()  # Close the figure to avoid display
    return 'uploads/algorithm2_result.png'  # Return the path to the saved figure