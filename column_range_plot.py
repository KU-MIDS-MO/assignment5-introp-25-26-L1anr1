import numpy as np
import matplotlib.pyplot as plt

def column_range_plot(A, filename="column_ranges.pdf"):

    max_values = np.max(A, axis=0)
    min_values = np.min(A, axis=0)
    
    ranges = max_values - min_values
    
    num_columns = A.shape[1]
    x_positions = np.arange(num_columns)
    

    plt.figure()
    plt.bar(x_positions, ranges)
    plt.xlabel("Column Index")
    plt.ylabel("Range")
    
    plt.savefig(filename)
    plt.close()
    
    return ranges
