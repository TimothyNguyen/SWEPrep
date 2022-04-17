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
    def __init__(self, regexp):
        self._regexp = regexp
        self._ops = []
        self._reg_len = len(self._regexp)
        self._graph = defaultdict(list)
        self._graph[self._reg_len] = []
        for i in range(self._reg_len):
            lp = i
            if self._regexp[i] == '(' or self._regexp[i] == '|':
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
            if i < self._reg_len - 1:
                if self._regexp[i + 1] == '*':
                    self._graph[lp].append(i + 1)
                    self._graph[i+1].append(lp)
                elif self._regexp[i+1] == '+':
                   self._graph[i+1].append(lp)
            if self._regexp[i] in ('(', '*', ')', '+') or self._regexp[i].isalpha():
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
                    if self._regexp[node] == text[i] or self._regexp[node] == '.':
                        match.add(node + 1)
        
            visited = set()
            # print(match)
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
print(nfa5.recognizes('dfawefdABCQQQG'))


nfa = NFA('(A|B)(C|D)*')
print(nfa.recognizes("ACCD"))

nfa = NFA('.*AB((C|D|E)F)*G)')
print(nfa.recognizes('RENEABCFDFG'))
print(nfa.recognizes('RENEABDFEFG'))
print(nfa.recognizes('RENEABCFDFEFG'))
print(nfa.recognizes('RENEABCDEFG'))


nfa = NFA('(A|B|C|D|E|F)')
print(nfa.recognizes(''))


nfa = NFA('(RE)+NE')
print(nfa.recognizes('RERERENE'))
print(nfa.recognizes('RENE'))

nfa = NFA('ABCR+PQR')
print(nfa.recognizes('ABCRPQ'))
print(nfa.recognizes('ABCRRRRRRRRRRRRRRPQR'))