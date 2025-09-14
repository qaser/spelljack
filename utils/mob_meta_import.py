import json
from pathlib import Path
from pymongo import MongoClient
import datetime as dt
import re

def process_mob_folders_detailed(static_path: str, mongo_uri: str, db_name: str = "spelljack_db") -> None:
    try:
        client = MongoClient(mongo_uri)
        db = client[db_name]
        collection = db.mob_meta
    except Exception as e:
        print(f"Ошибка подключения к MongoDB: {e}")
        return

    static_dir = Path(static_path)
    mob_folders = [f for f in static_dir.iterdir() if f.is_dir() and f.name.startswith("mob_")]

    # Получаем список уже обработанных папок из БД
    existing_folders = set()
    try:
        existing_docs = collection.find({}, {"metadata.folder_path": 1})
        existing_folders = {doc.get("metadata", {}).get("folder_path") for doc in existing_docs if doc.get("metadata", {}).get("folder_path")}
    except Exception as e:
        print(f"Ошибка при получении данных из БД: {e}")

    # Регулярные выражения для нужных файлов
    patterns = [
        re.compile(rf"mob_(\d+)_presentation_var(\d+)\.(png|jpg|jpeg|webp)$"),
        re.compile(rf"mob_(\d+)_defeat_var(\d+)\.(png|jpg|jpeg|webp)$"),
        re.compile(rf"mob_(\d+)_victory_var(\d+)\.(png|jpg|jpeg|webp)$"),
        re.compile(rf"mob_(\d+)_demonstration_legs_var(\d+)\.(png|jpg|jpeg|webp)$"),
        re.compile(rf"mob_(\d+)_demonstration_breasts_var(\d+)\.(png|jpg|jpeg|webp)$"),
        re.compile(rf"mob_(\d+)_demonstration_panties_show_var(\d+)\.(png|jpg|jpeg|webp)$")
    ]

    for folder in mob_folders:
        try:
            # Проверяем, не обрабатывалась ли уже эта папка
            folder_path_str = str(folder)
            if folder_path_str in existing_folders:
                print(f"Папка уже обработана, пропускаем: {folder.name}")
                continue

            meta_file = folder / "mob_meta.json"
            if not meta_file.exists():
                print(f"Файл mob_meta.json не найден в папке: {folder.name}")
                continue

            with open(meta_file, 'r', encoding='utf-8') as f:
                meta_data = json.load(f)

            # Собираем только нужные изображения
            valid_images = {
                "presentation": [],
                "defeat": [],
                "victory": [],
                "demonstration_legs": [],
                "demonstration_breasts": [],
                "demonstration_panties_show": []
            }

            # Перебираем все файлы в папке
            for file_path in folder.iterdir():
                if not file_path.is_file():
                    continue

                filename = file_path.name.lower()
                matched = False

                # Проверяем все паттерны
                for pattern in patterns:
                    match = pattern.match(filename)
                    if match:
                        seed_from_file = match.group(1)
                        variant = match.group(2)
                        extension = match.group(3)

                        # Проверяем, что seed совпадает с seed из meta.json
                        if str(meta_data.get('seed')) != seed_from_file:
                            continue

                        # Определяем тип изображения по имени файла
                        if 'presentation' in filename:
                            category = 'presentation'
                        elif 'defeat' in filename:
                            category = 'defeat'
                        elif 'victory' in filename:
                            category = 'victory'
                        elif 'demonstration_legs' in filename:
                            category = 'demonstration_legs'
                        elif 'demonstration_breasts' in filename:
                            category = 'demonstration_breasts'
                        elif 'demonstration_panties_show' in filename:
                            category = 'demonstration_panties_show'
                        else:
                            continue

                        valid_images[category].append({
                            "filename": file_path.name,
                            "variant": int(variant),
                            "path": str(file_path.relative_to(static_dir)),
                            "file_size": file_path.stat().st_size
                        })
                        matched = True
                        break

                if not matched:
                    print(f"Пропускаем файл: {file_path.name}")

            # Сортируем изображения по вариантам
            for category in valid_images:
                valid_images[category].sort(key=lambda x: x["variant"])

            # Дополнительная обработка данных
            processed_data = {
                "_id": f"{meta_data['seed']}_{meta_data['theme']}",
                "seed": meta_data.get("seed"),
                "theme": meta_data.get("theme"),
                "basic_info": {
                    "environment": meta_data.get("environment"),
                    "time_of_day": meta_data.get("time_of_day"),
                    "folder_name": folder.name
                },
                "appearance": {
                    "hair": meta_data.get("hair", {}),
                    "eyes": meta_data.get("eyes", {}),
                    "body": meta_data.get("body", {}),
                    "face": meta_data.get("face", {})
                },
                "clothing": meta_data.get("clothing", {}),
                # "poses": meta_data.get("poses", {}),
                # "view_angles": meta_data.get("view_angles", {}),
                "images": valid_images,  # Только нужные изображения
                "metadata": {
                    "processing_date": dt.datetime.now().isoformat(),
                    "folder_path": folder_path_str,
                    "total_valid_images": sum(len(images) for images in valid_images.values())
                }
            }

            # Сохранение в MongoDB
            collection.replace_one({"_id": processed_data["_id"]}, processed_data, upsert=True)
            print(f"Обработана папка: {folder.name} - найдено {processed_data['metadata']['total_valid_images']} валидных изображений")

        except Exception as e:
            print(f"Ошибка обработки {folder.name}: {e}")
            import traceback
            traceback.print_exc()

if __name__ == "__main__":
    # Настройки
    STATIC_PATH = "static/mobs"
    MONGO_URI = "mongodb://localhost:27017/"
    DB_NAME = "spelljack_db"

    # Запуск обработки
    process_mob_folders_detailed(STATIC_PATH, MONGO_URI, DB_NAME)
