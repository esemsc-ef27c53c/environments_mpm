import numpy as np
import pandas as pd
from scipy.ndimage import gaussian_filter
from scipy import misc


__all__ = ['rand_array', 'smooth_image', 'my_mat_solve', 'create_dataframe']


def rand_array(shape):
    return np.random.rand(*shape)

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

def my_mat_solve(A, b):
    return A.inv()*b

def create_dataframe():
    # Create a dictionary with some sample data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [24, 27, 22, 32],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
    
    # Convert the dictionary into a pandas DataFrame
    df = pd.DataFrame(data)
    
    # Print the DataFrame
    print("DataFrame:")
    print(df)
    
    # Return basic information about the DataFrame
    return df.describe()