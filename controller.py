class SignalController:
    def __init__(self, blocks):
        self.blocks = blocks

    def can_train_move(self, train_id, current_block_index):
        next_index = current_block_index + 1
        if next_index >= len(self.blocks):
            return False
        return self.blocks[next_index].is_free()

    def move_train(self, train_id, current_block_index):
        current_block = self.blocks[current_block_index]
        next_block = self.blocks[current_block_index + 1]

        # Release current, occupy next
        current_block.release()
        next_block.occupy(train_id)
