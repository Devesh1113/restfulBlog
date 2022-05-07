class WashingMachine:
    def __init__(self, cloth_washer, cloth_dryer):
        self.rinse = cloth_washer
        self.dryer = cloth_dryer

    def wash_clothes(self, on):
        self.rinse = on

    def dry_clothes(self, on):
        self.dryer = on

washing_machine = WashingMachine("clothes_in", "clothes_out")

print(washing_machine.rinse)
washing_machine.wash_clothes("on")

import builtins

absolute_value = help(abs)
print(absolute_value)











