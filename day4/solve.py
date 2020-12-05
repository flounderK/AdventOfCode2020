#!/usr/bin/python3
import re


class Passport:
    REQUIRED_FIELDS = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    ALL_FIELDS = list(REQUIRED_FIELDS) + ['cid']
    rexp = re.compile(r'(%s):([^ ]+)' % '|'.join(ALL_FIELDS))

    def __init__(self, data):
        self.byr = self.iyr = self.eyr = self.hgt = self.hcl = self.ecl = self.pid = self.cid = ''
        self._raw_data = data
        self._get_valid_fields()

    def _get_valid_fields(self):
        matched_data = {i.groups() for i in re.finditer(self.rexp, self._raw_data)}
        for k, v in matched_data:
            if hasattr(self, k):
                setattr(self, k, v)

    def required_fields_present(self):
        return all((getattr(self, i) != '') for i in self.REQUIRED_FIELDS)

    def __repr__(self):
        return '\n'.join('%s:%s' % (i, getattr(self, i)) for i in self.ALL_FIELDS)

    def check_byr(self):
        check = False
        if re.match(r'^(\d{4})$', self.byr) is not None:
            check = 1920 <= int(self.byr) <= 2002
        return check

    def check_iyr(self):
        check = False
        if re.match(r'^(\d{4})$', self.iyr) is not None:
            check = 2010 <= int(self.iyr) <= 2020
        return check

    def check_eyr(self):
        check = False
        if re.match(r'^(\d{4})$', self.eyr) is not None:
            check = 2020 <= int(self.eyr) <= 2030
        return check

    def check_hgt(self):
        check = False
        if re.match(r'^(\d{2,3}(?:cm|in))$', self.hgt) is not None:
            unit = self.hgt[-2:]
            mn, mx = (150, 193) if unit == 'cm' else (59, 76)
            check = mn <= int(self.hgt[:-2]) <= mx
        return check


    def check_hcl(self):
        return re.match(r'^(#[a-f0-9]{6})$', self.hcl) is not None

    def check_ecl(self):
        return re.match(r'^(amb|blu|brn|gr|grn|hzl|oth)$', self.ecl)

    def check_pid(self):
        return re.match(r'^(\d{,9})$', self.pid) is not None

    def valid_field_format(self):
        required_fields_check_functions = [self.check_byr,
                                           self.check_iyr,
                                           self.check_eyr,
                                           self.check_hgt,
                                           self.check_hcl,
                                           self.check_ecl,
                                           self.check_pid]
        return all(f() for f in required_fields_check_functions)


with open("input.txt", "r") as f:
    data = [i.replace("\n", " ") for i in f.read().strip().split("\n\n")]

passport_objects = [Passport(d) for d in data]

required_fields_present = [p for p in passport_objects if p.required_fields_present()]
print("Part 1: %d" % len(required_fields_present))

correctly_formatted_fields = [p for p in required_fields_present if p.valid_field_format()]

print("Part 2: %d" % len(correctly_formatted_fields))

