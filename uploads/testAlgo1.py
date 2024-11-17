import matplotlib.pyplot as plt

def run(data):
    plt.figure()
    plt.plot(data['x'], data['y'], marker='o')
    plt.title('Line Plot of x vs y')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid()
    plt.savefig('uploads/algorithm1_result.png')  # Save the figure
    plt.close()  # Close the figure to avoid display
    return 'uploads/algorithm1_result.png'  # Return the path to the saved figure