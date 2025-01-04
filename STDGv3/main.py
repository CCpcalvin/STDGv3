from .Sequence import DialogueSequence, Sequence


def read_script(path: str):
    with open(path, "r", encoding="utf-8") as f:
        head = DialogueSequence(next(f))
        last = head

        for i, line in enumerate(f):
            this = DialogueSequence(line)
            last.next = this
            this.pervious = last

            last = this

    return head


