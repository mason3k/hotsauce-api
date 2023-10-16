from pathlib import Path
import csv
from contextlib import suppress
from dataclasses import dataclass, field
from .model import HotSauce


@dataclass
class MockDb:
    items: list[HotSauce] = field(init=False)
    items_by_id: dict[int, HotSauce] = field(init=False)

    def __post_init__(self):
        self.items = self._load_data()
        self.items_by_id = {entry.id: entry for entry in self.items}

    def _load_data(self) -> list[HotSauce]:
        sauces = []
        with Path("data.csv").open() as f:
            reader = csv.reader(f)
            next(reader, None)  # skip header
            for row in reader:
                with suppress(Exception):
                    sauces.append(HotSauce(**dict(zip(HotSauce.model_fields, row))))
        return sauces

    def add(self, sauce: HotSauce):
        if self.items_by_id.get(sauce.id):
            raise ValueError(f"Error: id {sauce.id} is already in use")
        self.items.append(sauce)
        self.items_by_id[sauce.id] = sauce
