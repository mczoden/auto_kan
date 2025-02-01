"""Auto expedition core algorithm"""
import time
import random
from utils import KanError


CHECK_RESERVE_TIME = 2 * 1
FORGET_RATE = 0


class Expedition:
    def __init__(self, expedition_id: str, expedition_time: int, expedition_fleet: int):
        self.expedition_id = expedition_id
        self.expedition_time = expedition_time
        self.expedition_fleet = expedition_fleet
        self.end_time = 0
        self.update_end_time()

    def update_end_time(self):
        self.end_time = int(time.time() + self.expedition_time)

    def __str__(self):
        return '[id {}] [time {}] [fleet {}] [end {}]'.format(
            self.expedition_id,
            self.expedition_time,
            self.expedition_fleet,
            self.end_time
        )


INIT_MISSION_LIST = [
    Expedition('2', 18, 1),
    Expedition('5', 54, 2),
    Expedition('21', 84, 3)
]
MAX_EXPEDITION = 3


class ExpeditionPool:
    def __init__(self, check_reserve_time: int = CHECK_RESERVE_TIME):
        self.running_pool: list[Expedition] = []
        self.complete_pool: list[Expedition] = []
        self.ready_pool: list[Expedition] = []
        self.check_reserve_time = check_reserve_time

    def new_running_expedition(self, expedition: Expedition):
        if len(self.running_pool) >= MAX_EXPEDITION:
            debug('new expedition to add:\n{}'.format(expedition))
            debug(self.str_all_pool())
            raise KanError('Running pool full')

        # self.__insert_new_expedition_by_end_time(expedition)
        expedition.update_end_time()
        self.running_pool.append(expedition)
        self.running_pool.sort(key=lambda x: x.end_time)
        debug('{} start running'.format(str(expedition)))

    # def __insert_new_expedition_by_end_time(self, expedition):
    #     index = 0
    #     for i in self.running_pool:
    #         if i.end_time < expedition.end_time:
    #             index += 1
    #     self.running_pool.insert(index, expedition)

    def new_ready_expedition(self, expedition: Expedition):
        if len(self.ready_pool) >= MAX_EXPEDITION:
            debug('new expedition to add:\n{}'.format(expedition))
            debug(self.str_all_pool())
            raise KanError('Ready pool full')

        self.ready_pool.append(expedition)

    def get_next_expedition_remaining_time(self):
        margin_time = float('inf')
        next_expedition_end_time = None

        if self.running_pool:
            next_expedition_end_time = self.running_pool[0].end_time
        if next_expedition_end_time is not None:
            margin_time = next_expedition_end_time - int(time.time())
        return margin_time

    def is_expedition_almost_complete(self):
        return self.get_next_expedition_remaining_time() \
               <= self.check_reserve_time

    def get_coming_expeditions_wait_time_and_number(self):
        if not self.is_expedition_almost_complete():
            raise KanError('You call this function too early')

        if not self.running_pool:
            raise KanError('Running pool empty')

        wait_time, wait_number = 0, 0
        current_time = int(time.time())
        end_time_list = [x.end_time for x in self.running_pool]

        for end_time in end_time_list:
            if current_time >= end_time:
                wait_number += 1

        end_time_list = [current_time] + end_time_list[wait_number:]
        interval_list = \
            [y - x for x, y in zip(end_time_list[:-1], end_time_list[1:])]

        for interval in interval_list:
            if interval > self.check_reserve_time:
                break
            wait_time += interval
            wait_number += 1

        debug('wait time: {}, expeditions: {}'.format(wait_time, wait_number))
        debug('Almost complete:\n\t{}'.format(
            '\n\t'.join([str(m) for m in self.running_pool[:wait_number]])))
        return wait_time, wait_number

    def wait_to_check_expedition(self):
        wait_time, number = self.get_coming_expeditions_wait_time_and_number()
        debug('Wait: {}s'.format(wait_time))
        time.sleep(wait_time)
        for expedition in self.running_pool[:number]:
            debug('{} wait to check'.format(str(expedition)))
        self.complete_pool += self.running_pool[:number]
        self.complete_pool.sort(key=lambda x: x.expedition_fleet)
        self.running_pool = self.running_pool[number:]

    def is_complete_expedition_empty(self):
        return True if not self.complete_pool else False

    def check_expedition(self):
        for expedition in self.complete_pool:
            debug('{} checked'.format(str(expedition)))
            self.ready_pool += self.complete_pool
            self.complete_pool = []

        self.ready_pool.sort(key=lambda x: x.expedition_fleet)

    def is_ready_expedition_empty(self):
        return True if not self.ready_pool else False

    def do_expedition(self):
        for expedition in self.ready_pool:
            self.new_running_expedition(expedition)
        self.ready_pool = []

    def get_complete_pool(self):
        return [x for x in self.complete_pool]

    def str_all_pool(self):
        output = '[running]\n{}\n[complete]\n{}\n[ready]\n{}'.format(
            [str(expedition) for expedition in self.running_pool],
            [str(expedition) for expedition in self.complete_pool],
            [str(expedition) for expedition in self.ready_pool]
        )
        return output

    def __str__(self):
        output = self.str_all_pool()
        return output


def debug(message: str):
    print('[{} Expedition] {}'.format(
        time.strftime("%m-%d %H:%M:%S", time.localtime()),
        message))


def forget():
    if random.randint(0, 100) < FORGET_RATE:
        debug('Forget !')
        return True
    return False


def main_control():
    """Main process"""
    expedition_pool = ExpeditionPool()

    for expedition in INIT_MISSION_LIST:
        expedition_pool.new_running_expedition(expedition)

    first_time = True
    while True:
        if expedition_pool.is_expedition_almost_complete():
            debug('\nExpedition complete coming')
            expedition_pool.wait_to_check_expedition()
            if first_time:
                time.sleep(55)
                first_time = False
                continue

        if not expedition_pool.is_complete_expedition_empty() and not forget():
            expedition_pool.check_expedition()

        if not expedition_pool.is_ready_expedition_empty() and not forget():
            expedition_pool.do_expedition()

        # print('.', end='', flush=True)
        # print(expedition_pool)
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            print(expedition_pool)
            break


if __name__ == '__main__':
    main_control()
