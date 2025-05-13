import simpy

class Train:
    def __init__(self, env, id, blocks, start_block, controller):
        self.env = env
        self.id = id
        self.blocks = blocks
        self.current_block = start_block
        self.controller = controller
        self.action = env.process(self.run())

    def run(self):
        while self.current_block < len(self.blocks) - 1:
            can_move = self.controller.can_train_move(self.id, self.current_block)

            if can_move:
                self.controller.move_train(self.id, self.current_block)
                self.current_block += 1
                print(f"[{self.env.now}] Train {self.id} moved to Block {self.current_block}")
            else:
                print(f"[{self.env.now}] Train {self.id} waiting at Block {self.current_block}")
            yield self.env.timeout(1)
