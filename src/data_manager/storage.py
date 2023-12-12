from abc import ABC, abstractmethod
from typing import Any, Optional


class DataStorageInterface(ABC):
    """
    Defines an interface for a data storage.
    All data storage types must implement this interface.
    """

    @abstractmethod
    def store_data(self, model_instance) -> None:
        """
        Stores data in the storage system.

        :param data: The data to be stored.
        :param identifier: The unique identifier for the data.
        """
        return

    @abstractmethod
    def retrieve_data(self, model_class, identifier: Any) -> Optional[Any]:
        """
        Retrieves data from the storage system.

        :param identifier: The unique identifier for the data to retrieve.
        :return: The retrieved data or None if not found.
        """
        return


# class DataStorage:
#     """
#     Manages various types of data storages.
#     """

#     def __init__(self) -> None:
#         self.storages: dict[str, DataStorageInterface] = {}

#     def add_storage(self, storage_type: str, **kwargs) -> None:
#         """
#         Adds a new storage type to the manager.

#         :param storage_type: The storage type name.
#         :param storage: The storage instance.
#         """
#         if storage_type in self.storages:
#             raise ValueError(f"Storage type '{storage_type}' already exists.")

#         if storage_type == "sqlite":
#             self.storages[storage_type] = SQLAlchemyDataStorage(db_url=kwargs["db_url"])

#         raise ValueError(f"Storage type '{storage_type}' not found.")

#     def get_storage(self, storage_type: str) -> DataStorageInterface:
#         """
#         Retrieves a storage type from the manager.

#         :param storage_type: The storage type name.
#         :return: The storage instance.
#         """
#         storage = self.storages.get(storage_type)
#         if storage:
#             return storage
#         raise ValueError(f"Storage type '{storage_type}' not found.")

#     def store_data(self, storage_type: str, model_class, data: dict[str, Any]) -> None:
#         """
#         Stores data using the specified storage type.

#         :param storage_type: The storage type name.
#         :param data: The data to be stored.
#         :param identifier: The unique identifier for the data.
#         """
#         storage = self.storages.get(storage_type)
#         if storage:
#             storage.store_data(model_class, data)
#         raise ValueError(f"Storage type '{storage_type}' not found.")

#     def retrieve_data(
#         self, storage_type: str, model_class, identifier: Any
#     ) -> Optional[Any]:
#         """
#         Retrieves data using the specified storage type.

#         :param storage_type: The storage type name.
#         :param identifier: The unique identifier for the data to retrieve.
#         :return: The retrieved data or None if not found.
#         """
#         storage = self.storages.get(storage_type)
#         if storage:
#             return storage.retrieve_data(model_class, identifier)
#         raise ValueError(f"Storage type '{storage_type}' not found.")
