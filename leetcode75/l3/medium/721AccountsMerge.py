'''
Given a list of accounts where each element accounts[i] 
is a list of strings, where the first element accounts[i][0] 
is a name, and the rest of the elements are emails 
representing emails of the account.

Now, we would like to merge these accounts. Two 
accounts definitely belong to the same person if there is 
some common email to both accounts. Note that even if two 
accounts have the same name, they may belong to different 
people as people could have the same name. A person can 
have any number of accounts initially, but all of their 
accounts definitely have the same name.

After merging the accounts, return the accounts in the 
following format: the first element of each account is 
the name, and the rest of the elements are emails in 
sorted order. The accounts themselves can be returned 
in any order.

 
Example 1:

Input: accounts = [["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Output: [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]]
Explanation:
The first and second John's are the same person as they have the common email "johnsmith@mail.com".
The third John and Mary are different people as none of their email addresses are used by other accounts.
We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
Example 2:

Input: accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
Output: [["Ethan","Ethan0@m.co","Ethan4@m.co","Ethan5@m.co"],["Gabe","Gabe0@m.co","Gabe1@m.co","Gabe3@m.co"],["Hanzo","Hanzo0@m.co","Hanzo1@m.co","Hanzo3@m.co"],["Kevin","Kevin0@m.co","Kevin3@m.co","Kevin5@m.co"],["Fern","Fern0@m.co","Fern1@m.co","Fern5@m.co"]]
 

Constraints:

1 <= accounts.length <= 1000
2 <= accounts[i].length <= 10
1 <= accounts[i][j].length <= 30
accounts[i][0] consists of English letters.
accounts[i][j] (for j > 0) is a valid email.
'''

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
        # Here N is the number of accounts and KK is the maximum length of an account.
        # Time complexity: O(NKlog(NK))
        # Space: O(NK)