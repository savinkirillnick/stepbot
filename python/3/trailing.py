from time import time


class TrailingStop:

    def __init__(self, app):
        self.app = app
        self.kline = list()
        self.max_price = 0.0
        self.stop_interval = 0.0

    def check(self):

        old_time = time() - self.stop_interval

        data = [time(), self.app.user.last_price]
        self.kline.append(data)

        data = list()
        for i in range(len(self.kline)):
            data.append(self.kline[i][1])
        stop_price = min(data)

        if stop_price > self.max_price:
            self.max_price = stop_price

        j = 0
        for i in range(len(self.kline)):
            if self.kline[j][0] < old_time:
                del self.kline[j]
                j -= 1
            j += 1

    def get_price(self):
        return self.max_price

    def upd(self):
        self.stop_interval = self.app.bot.stop_interval

    def reset(self):
        self.max_price = 0.0
        self.kline = list()
