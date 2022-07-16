import web3
from web3 import Web3
from web3 import EthereumTesterProvider as ethProvider
import numpy as np
from pprint import pprint

w3 = Web3(ethProvider())
print(w3.isConnected())

latestBlock = w3.eth.get_block('latest')
pprint(vars(latestBlock))
#print(latestBlock)

dtype = np.dtype('B')
try:
    with open("./textfile.txt", "rb") as f:
        numpy_data = np.fromfile(f,dtype)
    print(numpy_data)
except IOError:
    print('Error While Opening the file!')

try:
    with open("./textfileWrite.txt", "wb") as f:
        f.write(numpy_data)
except IOError:
    print('Error While Opening the file!')     