import sys
import string
from collections import Counter

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

def count_word_frequency(words):
    """Подсчитывает частоту каждого слова."""
    return Counter(words)

def save_sorted_word_frequency_report(filename, word_counts):
    """Сохраняет отсортированный отчет о частоте слов в файл."""
    # Сортируем слова по убыванию частоты
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
    with open(filename, 'w', encoding='utf-8') as file:
        for word, count in sorted_word_counts:
            file.write(f"{word}: {count}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Укажите имя файла для чтения текста.")
        sys.exit(1)

    filename = sys.argv[1]
    text = read_text_from_file(filename)
    words = clean_and_split_text(text)

    # Подсчитаем частоту появления слов
    word_counts = count_word_frequency(words)

    # Сохраняем отсортированный отчет о частоте слов
    report_filename = f"result/{filename.split('.')[0]}_word_frequency_sorted.txt"
    save_sorted_word_frequency_report(report_filename, word_counts)

    print(f"Отчёт о частоте слов (отсортированный) сохранен в {report_filename}")

