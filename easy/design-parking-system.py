class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.big = big
        self.medium = medium
        self.small = small

    def addCar(self, carType: int) -> bool:
        
        match carType: 
            case 1:
                if self.big > 0:
                    self.big -= 1
                    return True
                return False

            case 2:
                if self.medium > 0:
                    self.medium -= 1
                    return True
                else:
                    return False
            case 3:
                if self.small > 0:
                    self.small -= 1
                    return True
                else:
                    return False