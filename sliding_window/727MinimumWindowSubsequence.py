class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        '''
        1. Find a subsequence in S that contains T, and return ending index in S
        2. Improve that subsequence by searching backwards from right-left to find 
        best starting index in S

        e.g.
        i = 0 1 2 3 4 5 6 7 8 9
        s1 = a b a c b c d f e g
        s2 = bcde
        find subsequence - bacbcdfe, end = 8
        improve subsequence - bcdfe, start = 4
        length = 5
        '''
        
        # Find a subsequence in S that contains T, and return ending index in S
        def find_subseq(s):
            t = 0
            while s < len(s1):
                if s1[s] == s2[t]:
                    t += 1
                    if t == len(s2):
                        break
                s += 1
            # Ensure last character of T was found before loop ended
            return s if t == len(s2) else None 

        # Improve - Get best starting point of subsequence ending at S[s1]
        def improve_subsequence(a):
            b = len(s2) - 1
            while b >= 0:
                if s1[a] == s2[b]:
                    b -= 1
                a -= 1
            return a + 1

        s = 0
        min_len = float('inf')
        min_window = ''

        while s < len(s1):
            end = find_subseq(s)

            if end is None:
                break
            
            start = improve_subsequence(end)

            if end - start + 1 < min_len:
                min_len = end - start + 1
                min_window = s1[start:end+1]
            
            s = start + 1
            
        return min_window
            
            
# https://pythontutor.com/visualize.html#code=def%20minWindow%28S,%20T%29%3A%0A%20%20%20%20%0A%20%20%20%20%23%20Find%20-%20Get%20ending%20point%20of%20subsequence%20starting%20after%20S%5Bs%5D%0A%20%20%20%20def%20find_subseq%28s%29%3A%0A%20%20%20%20%20%20%20%20t%20%3D%200%0A%20%20%20%20%20%20%20%20while%20s%20%3C%20len%28S%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20S%5Bs%5D%20%3D%3D%20T%5Bt%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20t%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20if%20t%20%3D%3D%20len%28T%29%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20%20%20%20%20s%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20s%20if%20t%20%3D%3D%20len%28T%29%20else%20None%20%20%20%20%20%20%20%23%20Ensure%20last%20character%20of%20T%20was%20found%20before%20loop%20ended%0A%20%20%20%20%0A%20%20%20%20%23%20Improve%20-%20Get%20best%20starting%20point%20of%20subsequence%20ending%20at%20S%5Bs%5D%0A%20%20%20%20def%20improve_subseq%28s%29%3A%0A%20%20%20%20%20%20%20%20t%20%3D%20len%28T%29%20-%201%0A%20%20%20%20%20%20%20%20while%20t%20%3E%3D%200%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20S%5Bs%5D%20%3D%3D%20T%5Bt%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20t%20-%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20s%20-%3D%201%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20return%20s%2B1%0A%20%20%20%20%0A%20%20%20%20s,%20min_len,%20min_window%20%3D%200,%20float%28'inf'%29,%20''%0A%20%20%20%20%0A%20%20%20%20while%20s%20%3C%20len%28S%29%3A%0A%20%20%20%20%20%20%20%20end%20%3D%20find_subseq%28s%29%20%20%20%20%20%20%20%20%20%20%20%20%23%20Find%20end-point%20of%20subsequence%0A%20%20%20%20%20%20%20%20if%20not%20end%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20break%0A%20%20%20%20%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20start%20%3D%20improve_subseq%28end%29%20%20%20%20%20%23%20Improve%20start-point%20of%20subsequence%0A%0A%20%20%20%20%20%20%20%20if%20end-start%2B1%20%3C%20min_len%3A%20%20%20%20%20%20%20%23%20Track%20min%20length%0A%20%20%20%20%20%20%20%20%20%20%20%20min_len%20%3D%20end-start%2B1%0A%20%20%20%20%20%20%20%20%20%20%20%20min_window%20%3D%20S%5Bstart%3Aend%2B1%5D%0A%20%20%20%20%20%20%20%20%0A%20%20%20%20%20%20%20%20s%20%3D%20start%2B1%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%23%20Start%20next%20subsequence%20search%0A%0A%20%20%20%20return%20min_window%0A%20%20%20%20%0As1%20%3D%20%22abcdebdde%22%0As2%20%3D%20%22bde%22%0A%0AminWindow%28s1,%20s2%29&cumulative=false&curInstr=0&heapPrimitives=nevernest&mode=display&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false


