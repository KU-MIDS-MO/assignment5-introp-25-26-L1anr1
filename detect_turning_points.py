import numpy as np
import matplotlib.pyplot as plt

def detect_turning_points(signal, filename="turning_points.pdf"):
    diffs = np.diff(signal)
    signs = np.sign(diffs)
    
    turning_indices = []
    
    for i in range(len(signs) - 1):
        current_sign = signs[i]
        next_sign = signs[i+1]
        
        if current_sign != next_sign:
            turning_indices.append(i + 1)
            
    turning_indices = np.array(turning_indices)

    plt.figure()
    plt.plot(signal, label='Signal')
    if len(turning_indices) > 0:
        plt.plot(turning_indices, signal[turning_indices], 'ro', label='Turning Points')
    
    plt.legend()
    plt.savefig(filename)
    plt.close()
    
    return turning_indices
