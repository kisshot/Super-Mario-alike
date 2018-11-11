'''状态类'''
from random import randint

from pygame import Vector2


class Enemy():
    def __init__(self, name):
        self.name = name
    def do_actions(self):
        pass
    def check_conditions(self):
        pass
    def entry_actions(self):
        pass
    def exit_actions(self):
        pass


class StateMachine():
    def __init__(self):
        self.states = {}  # 存储状态
        self.active_state = None  # 当前有效状态

    def add_state(self, state):
        # 增加状态
        self.states[state.name] = state

    def think(self):
        if self.active_state is None:
            return
        # 执行有效状态的动作，并做转移检查
        self.active_state.do_actions()
        new_state_name = self.active_state.check_conditions()
        if new_state_name is not None:
            self.set_state(new_state_name)

    def set_state(self, new_state_name):
        # 更改状态，执行进入/退出动作
        if self.active_state is not None:
            self.active_state.exit_actions()
        self.active_state = self.states[new_state_name]
        self.active_state.entry_actions()



