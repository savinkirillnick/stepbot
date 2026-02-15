

class Strategy:

    def __init__(self, app):
        self.app = app
        self.exchange = ''
        self.pair = ''
        self.buy_at = 'first'
        self.buy_from = 'best'
        self.buy_step_type = 'percents'  # points, percents
        self.buy_step_size = 1.0
        self.buy_step_ratio = 1.0
        self.buy_lot_type = 'percents'  # points, percents
        self.buy_lot_size = 1.0
        self.buy_lot_ratio = 1.0
        self.sell_at = 'average'
        self.sell_from = 'stop'
        self.sell_step_type = 'percents'  # points, percents
        self.sell_step_size = 1.0
        self.sell_step_ratio = 1.0
        self.sell_lot_type = 'percents'  # points, percents
        self.sell_lot_size = 0.0
        self.sell_lot_ratio = 1.0
        self.stop_interval = 0.0
        self.depo = 0.0
        self.depo_ex = 0.0
        self.start_price = 0.0
        self.last_price = 0.0
        self.last_buy_price = 0.0
        self.last_sell_price = 0.0
        self.last_buy_step = 0
        self.last_sell_step = 0
        self.next_buy_lot = 0.0
        self.next_buy_price = 0.0
        self.next_sell_lot = 0.0
        self.next_sell_price = 0.0

    def edit(self, start_price, last_buy_price, last_sell_price, last_buy_step, last_sell_step, depo_ex):
        self.start_price = start_price
        self.last_buy_price = last_buy_price
        self.last_sell_price = last_sell_price
        self.last_buy_step = last_buy_step
        self.last_sell_step = last_sell_step
        self.depo_ex = depo_ex

    def upd(self, data):
        self.exchange = data['exchange'] if 'exchange' in data else self.exchange
        self.pair = data['pair'] if 'pair' in data else self.pair
        self.depo = data['depo'] if 'depo' in data else self.depo
        self.depo_ex = data['depo_ex'] if 'depo_ex' in data else self.depo_ex
        self.start_price = data['start_price'] if 'start_price' in data else self.start_price
        self.last_price = data['last_price'] if 'last_price' in data else self.last_price
        self.buy_at = data['buy_at'] if 'buy_at' in data else self.buy_at
        self.buy_from = data['buy_from'] if 'buy_from' in data else self.buy_from
        self.sell_at = data['sell_at'] if 'sell_at' in data else self.sell_at
        self.sell_from = data['sell_from'] if 'sell_from' in data else self.sell_from
        self.buy_step_type = data['buy_step_type'] if 'buy_step_type' in data else self.buy_step_type
        self.buy_step_size = data['buy_step_size'] if 'buy_step_size' in data else self.buy_step_size
        self.buy_step_ratio = data['buy_step_ratio'] if 'buy_step_ratio' in data else self.buy_step_ratio
        self.buy_lot_type = data['buy_lot_type'] if 'buy_lot_type' in data else self.buy_lot_type
        self.buy_lot_size = data['buy_lot_size'] if 'buy_lot_size' in data else self.buy_lot_size
        self.buy_lot_ratio = data['buy_lot_ratio'] if 'buy_lot_ratio' in data else self.buy_lot_ratio
        self.sell_step_type = data['sell_step_type'] if 'sell_step_type' in data else self.sell_step_type
        self.sell_step_size = data['sell_step_size'] if 'sell_step_size' in data else self.sell_step_size
        self.sell_step_ratio = data['sell_step_ratio'] if 'sell_step_ratio' in data else self.sell_step_ratio
        self.sell_lot_type = data['sell_lot_type'] if 'sell_lot_type' in data else self.sell_lot_type
        self.sell_lot_size = data['sell_lot_size'] if 'sell_lot_size' in data else self.sell_lot_size
        self.sell_lot_ratio = data['sell_lot_ratio'] if 'sell_lot_ratio' in data else self.sell_lot_ratio
        self.last_buy_step = data['last_buy_step'] if 'last_buy_step' in data else self.last_buy_step
        self.last_sell_step = data['last_sell_step'] if 'last_sell_step' in data else self.last_sell_step

    def reset(self):
        self.start_price = 0.0
        self.last_price = 0.0
        self.last_buy_price = 0.0
        self.last_sell_price = 0.0
        self.last_buy_step = 0
        self.last_sell_step = 0
        self.next_buy_lot = 0.0
        self.next_buy_price = 0.0
        self.next_sell_lot = 0.0
        self.next_sell_price = 0.0
        self.depo_ex = 0.0

    def buy(self, price, qty):
        self.last_price = price
        self.last_buy_price = price
        self.last_buy_step += 1
        self.last_sell_step -= 1
        if self.last_sell_step < 0:
            self.last_sell_step = 0
        self.last_sell_price = 0.0
        self.depo_ex += price * qty

    def sell(self, price, qty):
        self.last_price = price
        self.last_sell_price = price
        self.last_sell_step += 1
        self.depo_ex -= price * qty
        self.last_buy_step -= 1
        if self.last_buy_step < 0:
            self.last_buy_step = 0
        self.last_buy_price = 0.0
        if round(self.depo_ex, 8) <= 0:
            self.reset()

    def check(self, last_price, avg_price):

        depo_avail = self.depo - self.depo_ex
        self.last_price = last_price

        next_buy_lot = next_sell_lot = 0.0

        # ~ Вычисляем размеры лота
        if self.buy_lot_type == 'points':
            next_buy_lot = self.buy_lot_size * self.buy_lot_ratio ** float(self.last_buy_step)
        elif self.buy_lot_type == 'percents':
            next_buy_lot = self.depo * self.buy_lot_size / 100.0 * self.buy_lot_ratio ** float(self.last_buy_step)
        if self.sell_lot_type == 'points':
            next_sell_lot = self.sell_lot_size * self.sell_lot_ratio ** float(self.last_sell_step)
        elif self.sell_lot_type == 'percents':
            next_sell_lot = self.depo_ex * self.sell_lot_size / 100.0 * self.sell_lot_ratio ** float(self.last_sell_step)

        self.next_buy_lot = next_buy_lot if next_buy_lot < depo_avail else depo_avail
        self.next_sell_lot = next_sell_lot if next_sell_lot < self.depo_ex else self.depo_ex

        # ~ Построение цен покупки
        if self.last_buy_step == 0:
            # Если стратегия еще не запущена, проверяем цену
            if last_price > self.start_price:
                # Если цена обновила хай, обновляем цену отсчета
                self.start_price = last_price

            # Плюс, строим первый шаг покупки
            if self.buy_step_type == 'points':
                self.next_buy_price = self.start_price - self.buy_step_size
            elif self.buy_step_type == 'percents':
                step_size = self.start_price * self.buy_step_size / 100.0
                self.next_buy_price = self.start_price - step_size

        else:
            # Строим цены следующих шагов покупки
            if self.buy_from == 'first':
                self.next_buy_price = self.start_price

            elif self.buy_from == 'last':
                self.next_buy_price = self.last_buy_price if self.last_sell_price == 0 else self.last_sell_price

            if self.buy_step_type == 'points':
                for i in range(self.last_buy_step + 1):
                    step_size = self.buy_step_size * self.buy_step_ratio ** float(self.last_buy_step)
                    self.next_buy_price -= step_size
            elif self.buy_step_type == 'percents':
                for i in range(self.last_buy_step + 1):
                    step_size = self.next_buy_price * self.buy_step_size / 100.0 * self.buy_step_ratio ** float(self.last_buy_step)
                    self.next_buy_price -= step_size

        if self.last_buy_step == 0:

            # Плюс, строим первый шаг продажи
            if self.sell_step_type == 'points':
                self.next_sell_price = self.start_price + self.buy_step_size
            elif self.sell_step_type == 'percents':
                step_size = self.start_price * self.sell_step_size / 100.0
                self.next_sell_price = self.start_price + step_size
        else:

            # ~ Построение цен продажи
            if self.sell_from == 'first':
                self.next_sell_price = self.start_price
            elif self.sell_from == 'last':
                self.next_sell_price = self.last_sell_price if self.last_buy_price == 0 else self.last_buy_price
            elif self.sell_from == 'average':
                self.next_sell_price = avg_price

        if self.sell_step_type == 'points':
            for i in range(self.last_sell_step + 1):
                step_size = self.sell_step_size * self.sell_step_ratio ** float(self.last_sell_step)
                self.next_sell_price += step_size
        elif self.sell_step_type == 'percents':
            for i in range(self.last_sell_step + 1):
                step_size = self.next_sell_price * self.sell_step_size / 100.0 * self.sell_step_ratio ** float(self.last_sell_step)
                self.next_sell_price += step_size
