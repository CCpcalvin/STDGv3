from .Helper import create_datapack


class Sequence:
    def __init__(
        self,
        id: int,
        cmd_str: str = None,
    ):
        self.id: int = id
        self.cmd_str: str = cmd_str
        self.next: Sequence = None

    def print_content(self):
        return f"\t ID: {self.id}\n\t CommandString: {self.cmd_str}\n"

    def __str__(self):
        return f"Sequence: \n {self.print_content()}"

    def print_tree(self):
        print(self)
        if self.next:
            self.next.print_tree()

    def generate_datapack(
        self,
        datapack_path: str,
        datapack_name: str,
        pack_format: int = 61,
        datapack_description: str = "STDGv3",
    ):
        create_datapack(datapack_path, datapack_name, pack_format, datapack_description)
        print("Not Yet implemented")


class DialogueSequence(Sequence):
    def __init__(self, id: int, dialogue_str: str = None):
        super().__init__(id)
        self.dialogue_str: str = dialogue_str

    def print_content(self):
        return f"{super().print_content()}\t DialogueString: {self.dialogue_str}\n"

    def __str__(self):
        return f"Dialogue Sequence: \n {self.print_content()}\t\n"
