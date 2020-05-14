import minst_loader
import nn

def main():
    training_data, validation_data, test_data = minst_loader.load_data_wrapper()
    net = nn.Network([784, 30, 10])
    net.SGD(training_data, 10, 10, 3.0, test_data = test_data)

if __name__ == '__main__':
    main()