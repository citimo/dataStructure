# DFA 图
class DFA:
    def __init__(self):
        self.states = set()  # 存储状态的集合
        self.alphabet = set()  # 存储输入符号的集合
        self.transitions = {}  # 存储状态转移的字典
        self.initial_state = None  # 初始状态
        self.accepting_states = set()  # 接受状态的集合

    def add_state(self, state):
        self.states.add(state)

    def add_alphabet(self, symbol):
        self.alphabet.add(symbol)

    def add_transition(self, from_state, symbol, to_state):
        if from_state not in self.states:
            raise ValueError("Invalid state: {}".format(from_state))
        if symbol not in self.alphabet:
            raise ValueError("Invalid symbol: {}".format(symbol))
        if to_state not in self.states:
            raise ValueError("Invalid state: {}".format(to_state))
        key = (from_state, symbol)
        self.transitions[key] = to_state

    def set_initial_state(self, state):
        if state not in self.states:
            raise ValueError("Invalid initial state: {}".format(state))
        self.initial_state = state

    def add_accepting_state(self, state):
        if state not in self.states:
            raise ValueError("Invalid accepting state: {}".format(state))
        self.accepting_states.add(state)

    def run(self, input_string):
        current_state = self.initial_state
        for symbol in input_string:
            key = (current_state, symbol)
            if key not in self.transitions:
                return False
            current_state = self.transitions[key]
        return current_state in self.accepting_states


# 创建一个 DFA 对象
dfa = DFA()

# 添加状态
dfa.add_state("S0")
dfa.add_state("S1")
dfa.add_state("S2")

# 添加输入符号
dfa.add_alphabet("0")
dfa.add_alphabet("1")

# 设置初始状态
dfa.set_initial_state("S0")

# 添加状态转移
dfa.add_transition("S0", "0", "S1")
dfa.add_transition("S0", "1", "S2")
dfa.add_transition("S1", "0", "S2")
dfa.add_transition("S1", "1", "S0")
dfa.add_transition("S2", "0", "S1")
dfa.add_transition("S2", "1", "S2")

# 添加接受状态
dfa.add_accepting_state("S0")

# 测试输入字符串
input_string = "101010"
result = dfa.run(input_string)
print("输入字符串 '{}' 在 DFA 图中是否被接受: {}".format(input_string, result))
