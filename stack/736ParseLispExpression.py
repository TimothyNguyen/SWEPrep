class Solution:
    # the conciseness of this solution comes from the great separation of reponsibilities.
    # all layer transitions and string tokenization are handled by the plain expresion iteration "for c in experssion:"
    # all simple calculations are handled by the self-defined evaluate() function
    # these two responsibilities are all you need for this Lisp Parser.
    def evaluate(self, expression):
        # token and stack to separate different layers of expressions
        # dictionary to memorize let
        st, d, tokens = list(), dict(), ['']

        def getval(x):
            return d.get(x, x)
        
        # process the current layer of expression        
        def evaluate(tokens):
            if tokens[0] in ('add', 'mult'):
                n1, n2 = int(getval(tokens[1])), int(getval(tokens[2]))
                return str(n1 + n2) if tokens[0] == 'add' else str(n1*n2)
            else: # let, update dictionary
                # skip the last one because it's not updating the dictionary
                for i in range(1, len(tokens)-2, 2):
                    d[tokens[i]] = getval(tokens[i + 1])
                    # the last token cannot be a nested expression which is intercepted before entering this
                    # so it can only be a variable, an integer or ''
                return getval(tokens[-1])
        
        for c in expression:
            # 4 situations: 
            # transit layers: 1. enter the deeper layer, 2. get back from the deeper layer, 
            # current layer: 3. start a new token, 4. continue reading the current token
            # the magic is, by using stack, recursions for the deeper layers are avoided
            if c == '(':
                # update the dictionary before entering the deeper layer
                if tokens[0] == 'let': evaluate(tokens)
                # tokens is reserved because the "tokens" in the next line is entirely overwritten as a new variable. (for example, tokens[-1] = 'a' won't reserve it)
                # d is reserved because of dict()
                st.append((tokens, dict(d)))
                tokens = ['']
            elif c == ')': 
                # get the current layer value
                val = evaluate(tokens)
                tokens, d = st.pop()
                # update the outside layer
                tokens[-1] += val
            elif c == ' ': tokens.append('')
            else: tokens[-1] += c
        # make sure to have the return outside the for loop
        return int(tokens[0])