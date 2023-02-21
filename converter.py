import csv
import json
from abc import ABC, abstractmethod
from typing import List, Dict


class DataPreparationBase(ABC):
    def __init__(self, file_cvs_path: str, file_json_path: str):
        self.file_cvs_path = file_cvs_path
        self.file_json_path = file_json_path

    def reading_csv(self) -> list[Dict: type[str]]:
        with open(self.file_cvs_path, newline='', encoding="utf-8") as csvfile:
            data: List = list(csv.DictReader(csvfile))
        return data

    def _write_json(self, data):
        with open(self.file_json_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)

    @abstractmethod
    def converter_csv_to_json(self, model):
        pass


class ConverterForHomework(DataPreparationBase):

    def converter_csv_to_json(self, model):
        result = []
        try:
            for item in self.reading_csv():
                data = {}
                if "is_published" in item:
                    if item["is_published"] == 'TRUE':
                        item["is_published"] = True
                    else:
                        item["is_published"] = False
                if "price" in item:
                    item["price"] = int(item['price'])
                if "author_id" in item:
                    item["author"] = int(item["author_id"])
                    del item["author_id"]
                if "category_id" in item:
                    item["category"] = int(item["category_id"])
                    del item["category_id"]
                if "lat" in item:
                    item["lat"] = float(item["lat"])
                if "lng" in item:
                    item["lng"] = float(item["lng"])
                if "age" in item:
                    item["age"] = int(item["age"])
                if "location_id" in item:
                    location: int = int(item["location_id"])
                    item["location"] = []
                    item["location"].append(location)
                    del item["location_id"]

                data["model"] = model
                data["pk"] = int(item['Id'] if 'Id' in item else item['id'])
                data["fields"] = item

                if "Id" in data["fields"]:
                    del data["fields"]["Id"]
                else:
                    del data["fields"]["id"]

                result.append(data)

            self._write_json(result)
            return {"status": "ок"}
        except Exception as e:
            return {"error": e,
                    "status": "Аn error occurred while opening the file or the file is corrupted"
                    }


print(ConverterForHomework("data_csv/ad.csv", "data_json/ads.json").converter_csv_to_json("ads.ad"))
print(ConverterForHomework("data_csv/category.csv", "data_json/categories.json").converter_csv_to_json("ads.category"))
print(ConverterForHomework("data_csv/location.csv", "data_json/locations.json").converter_csv_to_json("ads.location"))
print(ConverterForHomework("data_csv/user.csv", "data_json/users.json").converter_csv_to_json("ads.user"))




