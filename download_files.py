import gdown
import os


train_filename = 'mnist_train.csv'
test_filename = 'mnist_test.csv'

if os.path.exists(train_filename) and os.path.exists(test_filename):
    quit()

else:
    train_id = '1UYlB8NsA2K8jZkDVlYo7_S-K5d66fwsZ'
    test_id = '1_t_RPAnMZnLBw3jbV2eTX1Gy3qP8vm6T'
    base_url = 'https://drive.google.com/uc?id='
    gdown.download(base_url + train_id, train_filename, quiet=False)
    gdown.download(base_url + test_id, test_filename, quiet=False)

