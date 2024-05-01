#!/usr/bin/env python3
""" 1-simple_pagination """
import csv
import math
from typing import List


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the page of the dataset"""
        csv_data = self.dataset()
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = index_range(page, page_size)
        return csv_data[start:end]


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of size two containing a start index and an end index."""
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
    """Get the page of the dataset"""
    csv_data = self.dataset()
    assert isinstance(page, int) and page > 0
    assert isinstance(page_size, int) and page_size > 0
    start, end = index_range(page, page_size)
    return {
        "page_size": page_size,
        "page": page,
        "data": csv_data[start:end],
        "next_page": page + 1 if end < len(csv_data) else None,
        "prev_page": page - 1 if start > 0 else None,
        "total_pages": math.ceil(len(csv_data) / page_size),
    }
