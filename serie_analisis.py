import numpy as np
import matplotlib.pyplot as plt
import configparser as cgp
from io import StringIO


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
    
    for i in range(20):
        name = f"Sims\Serie\Serie{i}.ini"
        with open(name) as out:
            setup, data = load(name, name + ".npy")
        i= list(range(0,data.shape[0],(data.shape[0])//1000))
        y_mean = np.mean(data[i], axis=1)
        plt.plot(i, y_mean)
    plt.show()
    
