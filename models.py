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

    def _add_named_item(self, name, storage, model):
        pass

    def new_discipline(self, name):
        if name in self.disciplines:
            return f'[ERROR] Дисциплина "{name}" уже существует'
        else:
            self.disciplines[name] = Discipline(len(self.disciplines)+1, name)
            return f'[V] Дисциплина "{name}" добавлена'

    def new_group(self, name):
        if name in self.groups:
            return f'[ERROR] Группа "{name}" уже существует'
        else:
            self.groups[name] = Group(len(self.groups)+1, name)
            return f'[V] Группа "{name}" добавлена'



def main():
    pass


if __name__ == '__main__':
    main()