import numpy as np
import os

# NOTE Python has a built-in os module with methods for interacting with the operating system, like creating files and directories, management of files and directories, input, output, environment variables, process management, etc

# NOTE - np.loadtxt, np.genfromtxt
print(os.path.exists("Topic2-Numpy/spambase.csv"))  # to check file path

data = np.loadtxt("Topic2-Numpy/spambase.csv", delimiter=",", dtype=np.float32)
print(data.shape)
print(data)
