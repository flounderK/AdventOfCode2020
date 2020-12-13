#!/usr/bin/python3
import re
from collections import defaultdict, deque


class BagContainmentMapping:

    def __init__(self, data):
        self._raw_data = data
        # key bag contains value bags, values contain dict representations of
        # amount and bagtype
        self.bag_contains_data = dict()
        # key bag contains value bags
        self.bag_contains = dict()
        # direct inverse mapping of bag containment
        # key is directly contained by values
        self.bag_contained_by = defaultdict(set)
        self.all_bag_types = set()
        self._parse_data()
        self._find_inverse_containment()
        self.forward_endpoints = self.get_forward_endpoints()
        self.back_endpoints = self.get_backward_endpoints()

    def _parse_data(self):
        # split into rhs and lhs
        basic_rexp = re.compile(r'(.+) bags contain(.+)')
        # split rhs into different bags. Also ignores 'no other bags'
        rhs_rexp = re.compile(r'( (?P<AMOUNT>\d+) (?P<BAGTYPE>[^.,]+) bags*[,.])')
        for line in self._raw_data:
            containing_bag, rhs = re.search(basic_rexp, line).groups()
            contained_bags = [i.groupdict() for i in re.finditer(rhs_rexp, rhs)]
            self.bag_contains_data[containing_bag] = contained_bags
            self.bag_contains[containing_bag] = [i['BAGTYPE'] for i in contained_bags]
            self.all_bag_types.add(containing_bag)
            for i in contained_bags:
                self.all_bag_types.add(i.get('BAGTYPE'))

    def _find_inverse_containment(self):
        for containing_bag, contained_bags in self.bag_contains.items():
            for bag in contained_bags:
                self.bag_contained_by[bag].add(containing_bag)

    def get_forward_endpoints(self):
        return [k for k, v in self.bag_contains.items() if len(v) == 0]

    def get_backward_endpoints(self):
        containing_bags = set(self.bag_contains.keys())
        contained_bags = set(self.bag_contained_by.keys())
        back_endpoints = list(containing_bags - contained_bags)
        return back_endpoints

    def get_parents_of(self, bag_type):
        return self.bag_contained_by.get(bag_type)

    def get_children_of(self, bag_type):
        return self.bag_contains.get(bag_type)

    def get_ancestors_of(self, bag_type):
        """get all possible ancestors"""
        stack = deque([bag_type])
        ancestors = []
        while stack:
            current_node = stack.pop()
            if current_node in ancestors:
                continue
            ancestors.append(current_node)
            parents = self.bag_contained_by.get(current_node)
            if parents is None:
                continue
            for parent in parents:
                stack.append(parent)

        ancestors.remove(bag_type)
        return ancestors

    def get_decendants_of(self, bag_type):
        """get all possible decendants of"""
        stack = deque([bag_type])
        decendants = []
        while stack:
            current_node = stack.pop()
            if current_node in decendants:
                continue
            decendants.append(current_node)
            children = self.bag_contains.get(current_node)
            if children is None:
                continue
            for child in children:
                stack.append(child)

        decendants.remove(bag_type)
        return decendants



with open("input.txt", "r") as f:
    data = f.read().splitlines()

containment_mapping = BagContainmentMapping(data)

ancestors_of_shiny_gold = containment_mapping.get_ancestors_of('shiny gold')
print("Part 1: %s" % len(ancestors_of_shiny_gold))
