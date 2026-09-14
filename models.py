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
    id: int
    full_name: str
    group_id: int


class Manager:
    def __init__(self):
        self.disciplines_dct = {}
        self.groups_dct = {}
        self.students_lst = {}

    def get_num_disc(self):
        return len(self.disciplines_dct)

    def check_unique_disc(self):
        return self.disciplines_dct.keys()

    def new_discipline(self, name):
        num_disc = self.get_num_disc()
        if not num_disc:
            self.disciplines_dct[name] = Discipline(1, name)
        else:
            if name in self.check_unique_disc():
                return f'[ERROR] Дисциплина "{name}" уже существует'
            else:
                self.disciplines_dct[name] = Discipline(num_disc+1, name)
                return f'[V] Дисциплина "{name}" добавлена'

    def get_num_group(self):
        return len(self.groups_dct)

    def check_unique_group(self):
        return self.groups_dct.keys()

    def new_group(self, name):
        num_gr = self.get_num_group()
        if not num_gr:
            self.groups_dct[name] = Group(1, name)
        else:
            if name in self.check_unique_group():
                return f'[ERROR] Группа "{name}" уже существует'
            else:
                self.groups_dct[name] = Group(num_gr+1, name)
                return f'[V] Группа "{name}" добавлена'



def main():
    pass


if __name__ == '__main__':
    main()