import cv2


class Crop:
    def __init__(self, frame, layout):
        b, g, r = cv2.split(frame)
        self.frame = cv2.merge((r, g, b))

        self.height, self.width, self.channels = self.frame.shape
        self.layout = layout
        self.locations = []
        self.opponent_cards = []
        self.player_cards = []

        self.crop_locations()
        self.crop_opponent_cards()
        self.crop_player_cards()

    def crop_locations(self):
        for location in self.layout["locations"]:
            row_start = int(float(location["row_start"])*self.height)
            row_end = int(float(location["row_end"])*self.height)
            col_start = int(float(location["col_start"])*self.width)
            col_end = int(float(location["col_end"])*self.width)

            self.locations.append(self.frame[row_start:row_end, col_start:col_end])

    def crop_opponent_cards(self):
        for location in self.layout["opponent_cards"]:
            row_start = int(float(location["row_start"])*self.height)
            row_end = int(float(location["row_end"])*self.height)
            col_start = int(float(location["col_start"])*self.width)
            col_end = int(float(location["col_end"])*self.width)

            self.opponent_cards.append(self.frame[row_start:row_end, col_start:col_end])

    def crop_player_cards(self):
        for location in self.layout["player_cards"]:
            row_start = int(float(location["row_start"])*self.height)
            row_end = int(float(location["row_end"])*self.height)
            col_start = int(float(location["col_start"])*self.width)
            col_end = int(float(location["col_end"])*self.width)

            self.player_cards.append(self.frame[row_start:row_end, col_start:col_end])

    def get_all(self):
        return self.locations + self.opponent_cards + self.player_cards
