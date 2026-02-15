

class Bot:

    def __init__(self):
        self.error = ''
        self.api_key = ''
        self.api_secret = ''
        self.opt_key = ''
        self.exchange = ''
        self.depo = 0.0
        self.pair = ''
        self.order_life = 0.0
        self.pause = 0.0
        self.upd_time = 1.0
        self.num_set = ''
        self.buy_at = ''
        self.buy_from = ''
        self.buy_step_type = ''  # points, percents
        self.buy_step_size = 0.0
        self.buy_step_ratio = 0.0
        self.buy_lot_type = ''  # points, percents
        self.buy_lot_size = 0.0
        self.buy_lot_ratio = 0.0
        self.sell_at = ''
        self.sell_from = ''
        self.sell_step_type = ''  # points, percents
        self.sell_step_size = 0.0
        self.sell_step_ratio = 0.0
        self.sell_lot_type = ''  # points, percents
        self.sell_lot_size = 0.0
        self.sell_lot_ratio = 0.0
        self.stop_interval = 0.0

    def upd(self, data):
        self.api_key = data['api_key'] if 'api_key' in data else self.api_key
        self.api_secret = data['api_secret'] if 'api_secret' in data else self.api_secret
        self.opt_key = data['opt_key'] if 'opt_key' in data else self.opt_key
        self.exchange = data['exchange'] if 'exchange' in data else self.exchange
        self.depo = data['depo'] if 'depo' in data else self.depo
        self.pair = data['pair'] if 'pair' in data else self.pair
        self.num_set = data['num_set'] if 'num_set' in data else self.num_set
        self.order_life = data['order_life'] if 'order_life' in data else self.order_life
        self.pause = data['pause'] if 'pause' in data else self.pause
        self.upd_time = data['upd_time'] if 'upd_time' in data else self.upd_time
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
        self.stop_interval = data['stop_interval'] if 'stop_interval' in data else self.stop_interval

    def get_set_data(self):
        data = dict()
        data['api_key'] = self.api_key
        data['api_secret'] = self.api_secret
        data['opt_key'] = self.opt_key
        data['num_set'] = self.num_set
        data['exchange'] = self.exchange
        data['depo'] = self.depo
        data['pair'] = self.pair
        data['order_life'] = self.order_life
        data['pause'] = self.pause
        data['upd_time'] = self.upd_time
        data['buy_at'] = self.buy_at
        data['buy_from'] = self.buy_from
        data['buy_step_type'] = self.buy_step_type
        data['buy_step_size'] = self.buy_step_size
        data['buy_step_ratio'] = self.buy_step_ratio
        data['buy_lot_type'] = self.buy_lot_type
        data['buy_lot_size'] = self.buy_lot_size
        data['buy_lot_ratio'] = self.buy_lot_ratio
        data['sell_at'] = self.sell_at
        data['sell_from'] = self.sell_from
        data['sell_step_type'] = self.sell_step_type
        data['sell_step_size'] = self.sell_step_size
        data['sell_step_ratio'] = self.sell_step_ratio
        data['sell_lot_type'] = self.sell_lot_type
        data['sell_lot_size'] = self.sell_lot_size
        data['sell_lot_ratio'] = self.sell_lot_ratio
        data['stop_interval'] = self.stop_interval
        return data

    def clear(self):
        self.error = ''
        self.api_key = ''
        self.api_secret = ''
        self.opt_key = ''
        self.exchange = ''
