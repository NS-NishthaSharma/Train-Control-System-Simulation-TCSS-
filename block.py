class Block:
    def __init__(self, id):
        self.id = id
        self.occupied_by = None

    def is_free(self):
        return self.occupied_by is None

    def occupy(self, train_id):
        self.occupied_by = train_id

    def release(self):
        self.occupied_by = None
