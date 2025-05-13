import simpy
from block import Block
from train import Train
from controller import SignalController

def main():
    NUM_BLOCKS = 10
    env = simpy.Environment()
    blocks = [Block(i) for i in range(NUM_BLOCKS)]

    controller = SignalController(blocks)

    # Initialize trains on different blocks
    blocks[0].occupy(1)
    blocks[3].occupy(2)

    Train(env, 1, blocks, 0, controller)
    Train(env, 2, blocks, 3, controller)

    env.run(until=20)

if __name__ == "__main__":
    main()
