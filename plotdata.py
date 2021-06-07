import _pickle as pickle
import matplotlib.pyplot as plt

with open("/Users/dhruvgoel/Desktop/CSCC11/A1 2/q2/datasets_1/small_train.pkl", "rb") as f:
    data = pickle.load(f)
    print(data["X"])
    print(data["Y"])
    plt.scatter(data["X"], data["Y"])
    plt.show()

with open("/Users/dhruvgoel/Desktop/CSCC11/A1 2/q2/datasets_1/large_train.pkl", "rb") as f:
    data = pickle.load(f)
    print(data["X"])
    print(data["Y"])
    plt.scatter(data["X"], data["Y"])
    plt.show()

with open("/Users/dhruvgoel/Desktop/CSCC11/A1 2/q2/datasets_2/small_train.pkl", "rb") as f:
    data = pickle.load(f)
    print(data["X"])
    print(data["Y"])
    plt.scatter(data["X"], data["Y"])
    plt.show()

with open("/Users/dhruvgoel/Desktop/CSCC11/A1 2/q2/datasets_2/large_train.pkl", "rb") as f:
    data = pickle.load(f)
    print(data["X"])
    print(data["Y"])
    plt.scatter(data["X"], data["Y"])
    plt.show()

with open("/Users/dhruvgoel/Desktop/CSCC11/A1 2/q2/datasets_3/small_train.pkl", "rb") as f:
    data = pickle.load(f)
    print(data["X"])
    print(data["Y"])
    plt.scatter(data["X"], data["Y"])
    plt.show()

with open("/Users/dhruvgoel/Desktop/CSCC11/A1 2/q2/datasets_3/large_train.pkl", "rb") as f:
    data = pickle.load(f)
    print(data["X"])
    print(data["Y"])
    plt.scatter(data["X"], data["Y"])
    plt.show()

