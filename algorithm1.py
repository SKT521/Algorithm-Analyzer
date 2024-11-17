# algorithm1.py
import matplotlib.pyplot as plt

def run(data):
    plt.figure()
    data.plot()  # Example plot
    plt.savefig('uploads/algorithm1_result.png')  # Save the figure
    return 'uploads/algorithm1_result.png'