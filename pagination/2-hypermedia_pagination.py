#!/usr/bin/env python3
""" 1-simple_pagination """
import csv
from typing import List
import math


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

    def index_range(self, page: int, page_size: int) -> tuple:
        """
        Return a tuple of size two containing a start
        index and an end index.
        """
        start = (page - 1) * page_size
        end = page * page_size
        return (start, end)

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get the page of the dataset"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        start, end = self.index_range(page, page_size)
        return self.dataset()[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary containing the following key-value pairs"""
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": (
                page + 1 if len(data) ==
                page_size and page < total_pages else None
            ),
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages,
        }
