import sys
import string

def read_text_from_file(filename):
    """Читает текст из указанного файла."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        sys.exit(1)

def clean_and_split_text(text):
    """Удаляет знаки препинания, переводит текст в нижний регистр и разделяет его на слова."""
    # Переводим текст в нижний регистр
    text = text.lower()
    # Удаляем знаки препинания
    text = text.translate(str.maketrans("", "", string.punctuation))
    # Разделяем текст на слова
    words = text.split()
    return words

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Укажите имя файла для чтения текста.")
        sys.exit(1)

    filename = sys.argv[1]
    text = read_text_from_file(filename)
    words = clean_and_split_text(text)

    # Печатаем первые 20 слов для проверки
    print("Обработанные слова:")
    print(words[:20])

    # Сохраняем обработанные слова в файл отчета
    report_filename = f"result/{filename.split('.')[0]}_words.txt"
    with open(report_filename, 'w', encoding='utf-8') as report_file:
        for word in words:
            report_file.write(f"{word}\n")
