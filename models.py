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

    def _add_named_item(self, name: str, storage: dict, model):
        if name in storage:
            return f'[ERROR] "{name}" уже существует'

        new_id = len(storage)+1
        storage[name] = model(new_id, name)
        return f'[V] "{name}" добавлена'


    def add_discipline(self, name):
        return self._add_named_item(name, self.disciplines, Discipline)

    def add_group(self, name):
       return  self._add_named_item(name, self.groups, Group)

    def add_student(self, full_name, gr_name):
        if gr_name not in self.groups:
            return f'[ERROR] "{gr_name}" не существует'
        else:
            gr_id = list(self.groups.keys()).index(gr_name)
        if full_name in self.students:
            return f'[ERROR] "{full_name}" уже существует'

        new_id = len(self.students) + 1
        self.students[new_id] = Student(full_name, gr_id)

def main():
    pass


if __name__ == '__main__':
    main()