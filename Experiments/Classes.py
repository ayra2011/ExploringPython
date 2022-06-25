import sys
import collections

from collections import OrderedDict, Counter

most_common_count = 2
c = Counter("Sumit")
print("Cx: {}".format(c))
print(list(c.elements()))
print(c.most_common(most_common_count))
c = Counter(['a', 'a', 'b', 'c', 'c', 'c'])
print("Cx: {}".format(c))
print(list(c.elements()))
print(c.most_common(most_common_count))
d = Counter({'a': 1, 'b': 2, 'c': 2, 'd': 0})
print("Cx: {}".format(d))
print(list(d.elements()))
print(d.most_common(most_common_count))
d.subtract(c)
print("subtracted: {}".format(d))
# add
d.update(c)
print("added-back: {}".format(d))
# d.clear()
# print("cleared: {}".format(d))
print(list(d - c))
c = Counter(cats=3, dogs=5, goats=4)
print("Cx: {}".format(c))
print(list(c.elements()))
print(c.most_common(most_common_count))


class Person:
    person_counter: int = 0

    def __init__(self, name: str) -> None:
        self.name: str = name
        Person.person_counter += 1

    def __call__(self):
        self.print()

    def print(self) -> None:
        print(self.name)

    @classmethod
    def print_cls(cls):
        print(str(cls.__name__))
        if issubclass(cls, Person):
            print("subclass of Person")
        else:
            print("not subclass of person")

    @property
    def email(self) -> str:
        return self.name + "@domain.com"

    @email.setter
    def email(self, email: str) -> None:
        self.name, company = email.split("@")

    @email.deleter
    def email(self) -> None:
        self.name = None

    # def __str__(self) -> str:
    #     return "Counter: {}".format(Person.person_counter)

    # absence of dunder str implies fallback automatically to dunder repr - if only one is to be implemented, it's: repr
    # that said : rule of thumb for dunder repr : return string that shows how to create this instance of object
    # we clearly are not following above advice for now - but that's intentional (for now)
    def __repr__(self) -> str:
        return "Counter: {}".format(Person.person_counter)

    @classmethod
    def decrement_person_counter(cls, count) -> None:
        cls.person_counter -= count


class MalePerson(Person):
    def __init__(self, name, age) -> None:
        Person.__init__(self, name)
        self.age = age

    def print_age(self) -> None:
        print(self.age)


class FemalePerson(Person):
    def print(self) -> None:
        print(f"female: {self.name}")


yuvi: Person = Person("Yuvi")
sumit: MalePerson = MalePerson("Sumit Kumar", 40)
ayra: Person = FemalePerson("Ayra Singh")
ishi: FemalePerson = FemalePerson("Ishika Singh")
sumit.print()
ayra()
ishi()
sumit.print_cls()
yuvi.print_cls()
ayra.print_cls()
ishi.print_cls()

#
# Person.decrement_person_counter(1)
# print(sumit)
# print(ayra)
# print(sumit.email)
# sumit.email = "sumit@test.com"
# print(sumit.email, sumit)
# sumit.print()
#
# sumit.print_age()
# print(sys.version)
#
# # if ("Sumit" or "Amit") is "None":
# if False and True and True:
#     print("Y")
# else:
#     print("N")

# print(help(MalePerson))
