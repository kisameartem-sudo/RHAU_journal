from dataclasses import dataclass


@dataclass
class Group:
    id: int
    name: str


@dataclass
class Discipline:
    id: int
    name: str


@dataclass
class Student:
    full_name: str
    group_id: int


class Manager:
    def __init__(self):
        self.disciplines = {}
        self.groups = {}
        self.students = {}

    def _add_named_item(self, name: str, storage: dict, model: object):
        if name in storage:
            return f'[ERROR] "{name}" уже существует'
        else:
            new_id = len(storage)+1
            storage[name] = model(new_id, name)
            return f'[V] "{name}" добавлена'




    def add_discipline(self, name):
        self._add_named_item(
            name,
            self.disciplines,
            Discipline
        )

    def add_group(self, name):
        self._add_named_item(
            name,
            self.groups,
            Group
        )



def main():
    pass


if __name__ == '__main__':
    main()