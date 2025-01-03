from .Sequence import *

def read_script(path: str):
    with open(path, "r") as f:
        head = DialogueSequence(0, next(f))
        last = head

        for (i, line) in enumerate(f):
            this = DialogueSequence(i + 1, line)
            last.next = this
            last = this
    
    return head
