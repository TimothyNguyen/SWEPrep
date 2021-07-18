from collections import defaultdict 

class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        '''
        emails to name dictionary
        graph = collections.defaultdict(set)
        for each account:
            get name from account
            for each emails by account:
                add email associated to account to graph and vice versa
                emails to name dictionary[email]  = name
        visited = set()
        ans = []
        for email in graph:
            if email not seen in visited:
                add to visited
                stack = [email]
                nodes_list = []
                while stack:
                    node <- pop element of stack
                    nodes_list.append(node)
                    Go through each neighbor of that node in the graph:
                        if neighbor hasn't been seen:
                            Add to stack
                ans.append([em_to_name[email]] + sorted(nodes_list))
        return ans
        # Time complexity (sum of length of accounts * log length of accounts)
        # Space complexity (sum of length of accounts)
        '''
        em_to_name = dict()
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                # add email associated to first account email to graph and vice versa
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name
        visited = set()
        ans = []
        for email in graph:
            if email not in visited:
                visited.add(email)
                stack = [email]
                nodes_list = []
                while stack:
                    node = stack.pop()
                    nodes_list.append(node)
                    #Go through each neighbor of that node in the graph:
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            stack.append(neighbor)
                ans.append([em_to_name[email]] + sorted(nodes_list))
        return ans
        # Time complexity (sum of length of accounts * log length of accounts)
        # Space complexity (sum of length of accounts)