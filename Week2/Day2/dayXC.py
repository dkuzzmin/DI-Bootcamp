
class Door():
    def __init__(self, isopened):
        self.isopened = isopened
    def open_door(self):
        self.isopened = True
    def close_door(self):
        self.isopened = False
class BlockedDoor(Door):
    def __init__(self, isopened):
        super().__init__(isopened)
    def bark(self):
        pass
    def open_door(self):
        raise Exception("Door is blocked")
    def close_door(self):
        raise Exception("Door is blocked")

door1 = Door(False)
door2 = BlockedDoor(False)

door1.open_door()
door2.close_door()