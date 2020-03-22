import numpy as np
import matplotlib.pyplot as plt
import configparser as cgp
from io import StringIO

class ExpandedIni:
    class ExpandedSection:
        def __init__(self, data):
            self.__dict__.update(dict(data))
    
    def __init__(self, data):
        for sect in data.sections():
            self.__dict__[sect] = ExpandedIni.ExpandedSection(data[sect])
            

def load(setup_path, values_path):
    # reading setup values
    setup=cgp.ConfigParser()
    setup.read(setup_path)
    # reading simulation results
    data=np.load(values_path)

    return setup, data

def to_string(setup):
    string_file = StringIO()
    setup.write(string_file)
    res = string_file.getvalue()
    string_file.close()
    return res;
    

if __name__=="__main__":
    
    plt.figure("Mean y")
    
    name = f"Sims\LowT"
    setup, data = load(name + ".ini", name + ".npy")
    print(data.shape)
    y_mean = np.mean(data, axis=1)
    plt.plot(y_mean)
    plt.show()
    
