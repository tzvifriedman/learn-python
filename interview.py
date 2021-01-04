from datetime import date
import unittest

class LOT(object):
    def __init__(self, treatments):
        self.treatments = treatments

    def start_date(self):
        return self.treatments[0]["start_date"]

    def drug_names(self):
        return [t["name"] for t in self.treatments]


def process_data(treatments):
    lines = []
    tmp_treatments = []
    for t in treatments:
        if not tmp_treatments:
            tmp_treatments = [t]
        else:
            found = False
            for tmp in tmp_treatments:
                if tmp["end_date"] < t["start_date"]:
                    lines.append(LOT(tmp_treatments))
                    tmp_treatments = [t]
                    found = True
                    break
            if not found:
                tmp_treatments.append(t)
    return lines


class TestLoT(unittest.TestCase):
    def test_something(self):
        treatments = [
            {"name": "A", "start_date": date(2020, 1, 1), "end_date": date(2020, 1, 10)},
            {"name": 'B', "start_date": date(2020, 1, 3), "end_date": date(2020, 1, 10)},
            {"name": 'C', "start_date": date(2020, 1, 6), "end_date": date(2020, 1, 15)},
            {"name": 'D', "start_date": date(2020, 1, 12), "end_date": date(2020, 1, 20)}
        ]

        results = process_data(treatments)

        self.assertListEqual(results[0].drug_names(), ['A', 'B', 'C'])
        self.assertEqual(results[0].start_date(), date(2020, 1, 1))
