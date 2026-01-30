def approx_real_root(coeffs, interval):
    left = interval[0]
    right = interval[1]
    
    tolerance = 1e-9 
    
    while (right - left) > tolerance:
        mid = (left + right) / 2
        
        f_left = coeffs[0] + coeffs[1]*left + coeffs[2]*(left**2) + coeffs[3]*(left**3)
        f_mid = coeffs[0] + coeffs[1]*mid + coeffs[2]*(mid**2) + coeffs[3]*(mid**3)
        
        if f_left * f_mid < 0:
            right = mid
        else:
            left = mid
            
    return (left + right) / 2
