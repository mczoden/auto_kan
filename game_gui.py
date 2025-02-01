"""Game GUI"""
from dataclasses import dataclass
from enum import Enum


class Shape(Enum):
    invalid = -1,
    rectangle = 1,
    dot = 2,
    circle = 3


@dataclass
class Area:
    shape: Shape
    x: int
    y: int
    radius_x: int = 0
    radius_y: int = 0
    radius: int = 0

INVALID_SHAPE_AREA = Area(Shape.invalid, 0, 0)


@dataclass
class DotRgbChecker:
    x: int
    y: int
    r_range: tuple[int, int]
    g_range: tuple[int, int]
    b_range: tuple[int, int]

    def ok(self, r: int, g: int, b: int) -> bool:
        return self.r_range[0] < r < self.r_range[1] \
            and self.g_range[0] < g < self.g_range[1] \
            and self.b_range[0] < b < self.b_range[1]

INVALID_DOT_RGB_CHECKER = DotRgbChecker(0, 0, *(((1, -1), ) * 3))


offset_x = 0
offset_y = 75

window_area = Area(Shape.rectangle, 480, 287, 480, 287)
port_area = Area(Shape.rectangle, 55, 55, 45, 45)
port_confirm_areas = (
    DotRgbChecker(940, 536, (-1, 20), (150, 170), (150, 170)),
    DotRgbChecker(926, 543, (240, 256), (240, 256), (240, 256))
)
sortie_in_port_area = Area(Shape.circle, 235, 314, radius=40)
sortie_main_confirm_areas = (
    DotRgbChecker(228, 346, (240, 256), (240, 256), (240, 256)),
)
organize_in_port_area = Area(Shape.rectangle, 0, 0)
supply_in_port_area = Area(Shape.circle, 90, 260, radius=40)
supply_main_confirm_areas = [
    DotRgbChecker(780, 250, (235, 255), (220, 240), (180, 200)),
    DotRgbChecker(900, 250, (235, 235), (180, 190), (165, 175))
]
refit_in_port = INVALID_SHAPE_AREA,
docking_in_port = INVALID_SHAPE_AREA,
factory_in_port = INVALID_SHAPE_AREA,
organize_in_submenu_area = Area(Shape.rectangle, 25, 185, 10, 15)
supply_in_submenu_area = Area(Shape.rectangle, 25, 250, 10, 15)
refit_in_submenu_area = Area(Shape.rectangle, 25, 315, 10, 15)
docking_area = Area(Shape.rectangle, 25, 380, 10, 15)
port_in_submenu_area = Area(Shape.rectangle, 88, 310, 12, 20)
sortie_in_sortie_area = Area(Shape.circle, 270, 270, radius=100)
practice_in_sortie_area = Area(Shape.circle, 540, 270, radius=100)
expedition_in_sortie_area = Area(Shape.circle, 800, 270, radius=100)
expedition_in_sortie_confirm_areas = (
    DotRgbChecker(853, 477, (230, 256), (230, 256), (210, 256)),
)
map_areas_in_expedition = (
    # used to skip index 0
    INVALID_SHAPE_AREA,
    # 1:
    Area(Shape.rectangle, 163, 541, 20, 20),
    # 2:
    Area(Shape.rectangle, 211, 541, 20, 20),
    # 3:
    Area(Shape.rectangle, 259, 541, 20, 20),
    # 4:
    Area(Shape.rectangle, 307, 541, 20, 20),
    # 5: to skip "NEXT" down arrow
    Area(Shape.rectangle, 355, 542, 20, 18),
    # 6:
    Area(Shape.rectangle, 403, 541, 20, 20),
    # 7:
    Area(Shape.rectangle, 451, 541, 20, 20),
)
bottom_map_select_area = Area(Shape.rectangle, 306, 541, 166, 20)
expedition_height = 36
expedition_radius_x = 260
expedition_border = 1,  # not used
expedition_center_x = 397
expedition_left_x = 137
expedition_right_x = 657
# expedition bar in 80% scale is not symmetry in vertical
# use base + height algorithm instead of center + radius
first_expedition_center_y = 207
first_expedition_base_y = 190
human_select_expedition_from_right_center_x = 470
human_select_expedition_from_right_radius_x = 150
human_select_expedition_from_bottom_radius_x = 75
human_select_expedition_from_current_radius_x = 150
human_select_expedition_all_range_probability = 20
confirm_expedition_area = Area(Shape.rectangle, 818, 535, 110, 22)
start_expedition_area = Area(Shape.rectangle, 736, 533, 98, 21)
start_expedition_confirm_areas = (
    DotRgbChecker(689, 238, (40, 60), (40, 60), (40, 60)),
    DotRgbChecker(850, 238, (40, 60), (40, 60), (40, 60)),
    DotRgbChecker(766, 459, (40, 60), (40, 60), (40, 60))
)
no_expedition_is_leaving_confirm_areas = (
    DotRgbChecker(370, 270, (100, 256), (100, 256), (100, 256)),
    DotRgbChecker(370, 280, (100, 256), (100, 256), (100, 256)),
    DotRgbChecker(370, 290, (100, 256), (100, 256), (100, 256)),
    DotRgbChecker(900, 290, (100, 256), (100, 256), (100, 256)),
    DotRgbChecker(130, 290, (100, 256), (100, 256), (100, 256))
)
select_expedition_fleet_areas = (
    # skip the index 0 and 1
    INVALID_SHAPE_AREA,
    INVALID_SHAPE_AREA,
    # 2:
    Area(Shape.rectangle, 468, 137, 13, 11),
    # 3:
    Area(Shape.rectangle, 504, 137, 13, 11),
    # 4:
    Area(Shape.rectangle, 539, 137, 13, 11),
)
supply_all_in_supply_area = Area(Shape.rectangle, 143, 143, 13, 12)
fleet_in_supply_areas = (
    # skip the index 0
    INVALID_SHAPE_AREA,
    # 1
    Area(Shape.rectangle, 176, 143, 10, 11),
    # 2
    Area(Shape.rectangle, 212, 143, 10, 11),
    # 3
    Area(Shape.rectangle, 247, 143, 10, 11),
    # 4
    Area(Shape.rectangle, 283, 144, 10, 10)
)
supply_fleets_is_selected_confirm_areas = (
    # skip the index 0
    (INVALID_DOT_RGB_CHECKER, ),
    # 1
    (DotRgbChecker(184, 141, (60, 70), (175, 185), (172, 182)), ),
    # 2
    (DotRgbChecker(220, 141, (60, 70), (175, 185), (172, 182)), ),
    # 3
    (DotRgbChecker(256, 141, (60, 70), (175, 185), (172, 182)), ),
    # 4
    (DotRgbChecker(292, 141, (60, 70), (175, 185), (172, 182)), )
)
first_ship_need_to_supply_confirm_areas = (
    DotRgbChecker(135, 195, (67, 69), (67, 69), (67, 69)),
)
expedition_flag_confirm_areas = (
    DotRgbChecker(627, 34, (40, 50), (170, 180), (170, 180)),
)
expedition_check_area = Area(Shape.rectangle, 479, 287, 240, 140)
expedition_checked_next_confirm_areas = (
    DotRgbChecker(897, 526, (20, 30), (150, 160), (150, 160)),
)
expedition_fleets_is_selected_confirm_areas = (
    # Skip the index 0 and 1
    (INVALID_DOT_RGB_CHECKER, ),
    (INVALID_DOT_RGB_CHECKER, ),
    # 2
    (DotRgbChecker(477, 135, (60, 70), (175, 185), (172, 182)), ),
    # 3
    (DotRgbChecker(513, 135, (30, 40), (150, 165), (155, 165)), ),
    # 4
    (DotRgbChecker(549, 135, (30, 40), (150, 165), (155, 165)), )
)
expedition_result_confirm_areas = (
    DotRgbChecker(200, 295, (250, 256), (250, 256), (250, 256)),
    DotRgbChecker(320, 295, (250, 256), (250, 256), (250, 256))
)
