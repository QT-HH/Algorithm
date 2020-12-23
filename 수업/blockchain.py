import hashlib

class Block():
    def __init__(self, data):
        self.data = data
        self.previousHash = ''
        self.nonce = 0
        self.hash = self.calHash()

    def calHash(self):
        return hashlib.sha256(str(self.data).encode()
                            + str(self.previousHash).encode() + str(self.nonce).encode()).hexdigest()


class BlockChain:
    def __init__(self):
        self.chain = []
        self.createGenesis()

    def createGenesis(self):
        self.chain.append(Block('Genesis'))

    def addBlock(self, nBlock):
        nBlock.previousHash = self.chain[len(self.chain)-1].hash
        while 1:
            nBlock.hash = nBlock.calHash()
            if nBlock.hash[:5] == '00000':
                break
            else:
                nBlock.nonce += 1
        self.chain.append(nBlock)

def printBlock(nBlock):
    print("nonce: ", nBlock.nonce)
    print("data: ", nBlock.data)
    print("previousHash: ", nBlock.previousHash)
    print("hash: ", nBlock.hash)
    print()

newChain = BlockChain()
printBlock(newChain.chain[-1])
newChain.addBlock(Block('2nd'))
printBlock(newChain.chain[-1])
newChain.addBlock(Block('3nd'))
printBlock(newChain.chain[-1])
