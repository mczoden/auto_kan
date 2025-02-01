"""Human auto expedition"""
# import human_play
import time
import random

from fleet_expedition_data import fleet_expedition_data
from expedition_data import expedition_data
import human_expedition
from human_expedition import HumanExpedition, HumanExpeditionPool, CHECK_RESERVE_TIME
import human_play


class AutoExpeditionPool(HumanExpeditionPool):
    def __init__(self, check_reserve_time: int = CHECK_RESERVE_TIME):
        super().__init__(check_reserve_time)

    def check_expedition(self):
        debug('check all expedition')
        human_play.check_all_expedition()
        debug('go to supply from port')
        human_play.goto_supply_from_port()
        time.sleep(random.random() * 3 + 2)
        for complete_expedition in self.complete_pool:
            fleet = complete_expedition.expedition_fleet
            debug('supply fleet {}'.format(fleet))
            human_play.supply(fleet)
            time.sleep(random.random() * 3 + 1)
        super().check_expedition()

    def do_expedition(self):
        debug('do_expedition')
        if not human_play.is_at_port():
            human_play.back_to_port_from_upper_left()
            time.sleep(random.random() * 0.5 + 1)
        human_play.sortie_from_port()
        time.sleep(random.random() * 0.5 + 1)
        human_play.expedition_from_sortie()
        time.sleep(random.random() * 0.5 + 1)
        e_f: list[tuple[str, int]] = []
        for expedition in self.ready_pool:
            e_f.append((expedition.expedition_id, expedition.expedition_fleet))
        human_play.select_and_do_expeditions(e_f)
        super().do_expedition()


def debug(message: str):
    print('[{} Auto Expedition] {}'.format(
        time.strftime("%m-%d %H:%M:%S", time.localtime()),
        message))


def init() -> list[HumanExpedition]:
    init_human_expedition_table: list[HumanExpedition] = []
    for fleet in fleet_expedition_data:
        expedition_no = fleet_expedition_data[fleet]
        expedition_time = expedition_data[expedition_no]['time']
        init_human_expedition_table.append(
            HumanExpedition(
                expedition_no, expedition_time, fleet))

    return init_human_expedition_table


def run():
    init_human_expedition_table = init()
    auto_expedition_pool = AutoExpeditionPool()

    for init_human_expedition in init_human_expedition_table:
        auto_expedition_pool.new_ready_expedition(init_human_expedition)

    human_play.goto_supply_from_port()
    time.sleep(random.random() * 3 + 2)
    for i in range(2, 5):
        fleet = i
        debug('supply fleet {}'.format(fleet))
        human_play.supply(fleet)
        time.sleep(random.random() * 0.5 + 0.5)
    auto_expedition_pool.do_expedition()

    while True:
        if auto_expedition_pool.is_expedition_almost_complete():
            debug('Expedition complete coming')
            auto_expedition_pool.wait_to_check_expedition()

        if not auto_expedition_pool.is_complete_expedition_empty():
            if human_expedition.forget_to_check(auto_expedition_pool):
                human_expedition.random_sleep_forget_to_check(
                    auto_expedition_pool)
                continue
            # pyautogui.alert('Wait to check')
            human_expedition.random_sleep_between_complete_and_check(
                auto_expedition_pool)
            auto_expedition_pool.check_expedition()

        if not auto_expedition_pool.is_ready_expedition_empty():
            auto_expedition_pool.do_expedition()

        # print(auto_expedition_pool)
        try:
            time.sleep(1)
        except KeyboardInterrupt:
            # print(auto_expedition_pool)
            break
    """
    time.sleep(3)
    human_play.goto_supply_from_port()
    time.sleep(2)
    human_play.supply(2)
    time.sleep(1)
    human_play.supply(3)
    time.sleep(3)
    human_play.back_to_port_from_upper_left()
    time.sleep(random.random() * 0.5 + 1)
    human_play.sortie_from_port()
    time.sleep(random.random() * 0.5 + 1)
    human_play.expedition_from_sortie()
    time.sleep(random.random() * 0.5 + 1)
    for expedition in expedition_fleet_table:
        human_play.select_and_go_expedition(
            expedition, expedition_fleet_table[expedition])
        time.sleep(3)
    """


if __name__ == '__main__':
    run()
