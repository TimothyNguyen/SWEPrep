from collections import defaultdict
import collections
class DirectedDFS:
    def __init__(self, graph, sources):
        self.marked = defaultdict(bool)
        def dfs(graph, node):
            self.marked[node] = True
            for nei in graph[node]:
                if not self.marked[nei]:
                    dfs(graph, nei)
        for node in sources:
            if not self.marked[node]:
                dfs(graph, node)      
    def marked(self, node):
        return self.marked[node]
class NFA:
    def __init__(self, regexp):
        self._regexp = regexp
        self._ops = []
        self._reg_len = len(self._regexp)
        self._graph = defaultdict(list)
        self._graph[self._reg_len] = []
        self.sets_match = defaultdict(int)
        for i in range(self._reg_len):
            lp = i
            if self._regexp[i] == '(' or self._regexp[i] == '|' or self._regexp[i] == '[':
                self._ops.append(i)
            elif self._regexp[i] == ')':
                or_op_set = set()
                while len(self._ops) > 0 and self._regexp[self._ops[-1]] == '|':
                    ops = self._ops.pop()
                    or_op_set.add(ops)
                if len(self._ops) > 0:
                    lp = self._ops.pop()
                for or_op in or_op_set:                    
                    self._graph[lp].append(or_op + 1)
                    self._graph[or_op].append(i)
            elif self._regexp[i] == ']':
                lp = self._ops.pop()
                for idx_inside_brackets in range(lp + 1, i):
                    self._graph[lp].append(idx_inside_brackets)
                    self.sets_match[idx_inside_brackets] = i  # If a match occurs while checking the character in this set, the DFA will go to the right square bracket state.
                    if self._regexp[idx_inside_brackets + 1] == '-': # if it's a range there's no need to process the next two chars
                        idx_inside_brackets += 2
            if i < self._reg_len - 1:
                if self._regexp[i + 1] == '*':
                    self._graph[lp].append(i + 1)
                    self._graph[i+1].append(lp)
                elif self._regexp[i+1] == '+':
                   self._graph[i+1].append(lp)
            if self._regexp[i] in ('(', '*', ')', '+', '[', ']'):
                self._graph[i].append(i + 1)
    def recognizes(self, text):
        visited = set()
        dfs = DirectedDFS(self._graph, (0, ))
        for node in self._graph:
            if dfs.marked[node]:
                visited.add(node)
        for i in range(len(text)):
            match = set()
            for node in visited:
                if node < self._reg_len:
                    if node in self.sets_match:
                        if self._regexp[node + 1] == '-':
                            l = self._regexp[node]
                            r = self._regexp[node + 2]
                            if l <= text[i] <= r:
                                r_sq_bracket = self.sets_match[node]
                                match.add(r_sq_bracket)
                        elif self._regexp[node] == text[i] or self._regexp[node] == '.':
                            if node in self.sets_match:
                                idx_right_bracket = self.sets_match[node]
                                match.add(idx_right_bracket)
                    elif self._regexp[node] == text[i] or self._regexp[node] == '.':
                        match.add(node + 1)
            visited = set()
            dfs = DirectedDFS(self._graph, match)
            for node in self._graph:
                if dfs.marked[node]:
                    visited.add(node)
            if len(visited) == 0:
               return False
        for node in visited:
            if node == self._reg_len:
                return True
        return False


'''
nfa4 = NFA('(a|(bc)*d)*')
ops = [(, ]
'''
nfa = NFA('(A*B|AC)D')
print(nfa.recognizes('AAAABD'))

nfa2 = NFA('(A*B|AC)D')
print(nfa2.recognizes('ACD'))

nfa3 = NFA('(a|(bc)*d)*')
print(nfa3.recognizes('abcbcd'))

nfa4 = NFA('(a|(bc)*d)*')
print(nfa4.recognizes('abcbcbcdaaaabcbcdaaaddd'))

nfa5 = NFA('(.*AB((C|D|E)F)*G)')
print(nfa5.recognizes('dfawefdABCQQQG')) # False


nfa = NFA('(A|B)(C|D)*')
print(nfa.recognizes("ACCD"))

nfa = NFA('.*AB((C|D|E)F)*G)')
print(nfa.recognizes('RENEABCFDFG'))
print(nfa.recognizes('RENEABDFEFG'))
print(nfa.recognizes('RENEABCFDFEFG'))
print(nfa.recognizes('RENEABCDEFG')) # False


nfa = NFA('(A|B|C|D|E|F)')
print(nfa.recognizes('A'))


nfa = NFA('(RE)+NE')
print(nfa.recognizes('RERERENE'))
print(nfa.recognizes('RENE'))

nfa = NFA('ABCR+PQR')
print(nfa.recognizes('ABCRPQ')) # False
print(nfa.recognizes('ABCRPQR')) # True
print(nfa.recognizes('ABCRRRRRRRRRRRRRRPQR')) # True

nfa = NFA(".*[ABC]Z")
print(nfa.recognizes("This is a text AZ"))
print(nfa.recognizes("This is a text BZ"))
print(nfa.recognizes("This is a text CZ"))
print(nfa.recognizes("D")) # False

'''
NFA(nondeterministic finite state automaton) algorithm for regular expression.
Regular expression is a effective string searching method, it will identify specific
string with a given regular expression. First this algorithm construct a NFA with a
given regular expression, that will be a directed graph of epsilon transitions. Then
input a text and go through every character. For each character, first reach all the
possible states  and then execute a epsilon transition which output a set with all possible
states. When all character is checked, if we reach the end state, that means the input
text match the regular expression. The worst case of running time is proportional to
O(MN), M is the length of regular expression, N is the length of the input text.
nfa = NFA('(A*B|AC)D')
nfa.recognizes('AAAABD')
True
nfa2 = NFA('(A*B|AC)D')
nfa2.recognizes('AAAAC')
False
    nfa3 = NFA('(a|(bc)*d)*')
    nfa3.recognizes('abcbcd')
True
    nfa4 = NFA('(a|(bc)*d)*')
    nfa4.recognizes('abcbcbcdaaaabcbcdaaaddd')
True
    nfa5 = NFA('(.*AB((C|D|E)F)*G)')
    nfa5.recognizes('dfawefdABCQQQG')
True
'''