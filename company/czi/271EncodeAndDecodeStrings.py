'''
Design an algorithm to encode a list of strings to a string. 
The encoded string is then sent over the network and is 
decoded back to the original list of strings.
'''
class Codec:
    def encode(self, strs: List[str]) -> str:
        msg = ''
        for s in strs:
            msg += s + chr(257)
        msg = msg[0:len(msg) - 1]
        return msg

    def decode(self, s: str) -> List[str]:
        lst = s.split(chr(257))
        return lst