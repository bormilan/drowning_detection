class Region:
    
    def __init__(self, start, end):
        self.top_left = start
        self.bottom_right = end
        self.state: int = 0

    def get_coordinates(self):
        return {
                "start": self.top_left,
                "end": self.bottom_right
                }

