from copy import deepcopy

class TextEditor:
    
    def __init__(self):
        self.text = []
        self.history = []
        self.clipboard = []
    
    def __repr__(self):
        return ''.join(self.text)
        
    def insert(self, text):
        if text:
            self.history.append(deepcopy(self.text))
            self.text += list(text)
            
    def delete(self):
        if self.text:
            self.history.append(deepcopy(self.text))
            self.text.pop()
            
    def copy(self, index):
        if index < len(self.text):
            self.clipboard = deepcopy(self.text[index:])
            
    def paste(self):
        if self.clipboard:
            self.history.append(deepcopy(self.text))
            self.text += deepcopy(self.clipboard)
            
    def undo(self):
        if self.history:
            self.text = self.history.pop()
            
editor = TextEditor()
print(editor)
editor.insert('Da')
print(editor)
editor.copy(0)
print(editor)
editor.undo()
print(editor)
editor.paste()
print(editor)
editor.paste()
print(editor)
editor.copy(2)
print(editor)
editor.paste()
print(editor)
editor.paste()
print(editor)
editor.delete()
print(editor)
editor.insert('aaam')
print(editor)
