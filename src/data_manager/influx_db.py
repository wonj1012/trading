from typing import Any, Optional

from influxdb_client_3 import InfluxDBClient3 as InfluxDBClient

from data_manager.storage import DataStorageInterface


class InfluxDBStorage(DataStorageInterface):
    """
    Data storage implementation using InfluxDB.
    """

    def __init__(self, url: str, token: str, org: str, bucket: str) -> None:
        """
        Initializes the InfluxDB client.

        :param url: URL of the InfluxDB server.
        :param token: Authentication token for InfluxDB.
        :param org: Organization name in InfluxDB.
        :param bucket: Bucket name in InfluxDB.
        """
        self.client = InfluxDBClient(url=url, token=token, org=org, bucket=bucket)
        self.bucket = bucket

    def store_data(self, data: dict[str, Any], identifier: str) -> None:
        """
        Stores data in InfluxDB.

        :param data: The data to be stored.
        :param identifier: The unique identifier for the data.
        """
        point = {"measurement": identifier, "fields": data}
        self.client.write(point)

    def retrieve_data(self, identifier: str) -> Optional[Any]:
        """
        Retrieves data from InfluxDB.

        :param identifier: The unique identifier for the data to retrieve.
        :return: The retrieved data or None if not found.
        """
        query = f'from(bucket: "{self.bucket}") |> range(start: -1h) |> filter(fn: (r) => r["_measurement"] == "{identifier}")'
        result = self.client.query(query)
        points = list(result)
        return points[0] if points else None
