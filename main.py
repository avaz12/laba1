
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
    # Удаляем знаки препинания, кроме многоточия
    text = text.replace("...", "DOTDOTDOT")  # временно заменяем многоточие
    text = text.translate(str.maketrans("", "", string.punctuation))
    text = text.replace("DOTDOTDOT", "...")  # восстанавливаем многоточие
    # Разделяем текст на слова
    words = text.split()
    return words

def count_word_frequency(words):
    """Подсчитывает частоту каждого слова."""
    return Counter(words)

def count_punctuation(text):
    """Подсчитывает количество знаков препинания в тексте, включая многоточие как один знак."""
    punctuation_count = 0
    i = 0
    while i < len(text):
        if text[i:i+3] == "...":  # проверяем многоточие
            punctuation_count += 1
            i += 3  # пропускаем три символа
        elif text[i] in string.punctuation:
            punctuation_count += 1
            i += 1
        else:
            i += 1
    return punctuation_count

def save_statistics_report(filename, word_counts, punctuation_count, unique_word_count):
    """Сохраняет статистику в файл."""
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(f"Количество уникальных слов: {unique_word_count}\n")
        file.write(f"Количество знаков препинания: {punctuation_count}\n")
        file.write(f"\nЧастота слов:\n")
        for word, count in word_counts.items():
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

    # Подсчитаем статистику
    punctuation_count = count_punctuation(text)
    unique_word_count = len(word_counts)

    # Сохраняем статистику в файл
    stat_filename = f"result/{filename.split('.')[0]}_stat.txt"
    save_statistics_report(stat_filename, word_counts, punctuation_count, unique_word_count)

    print(f"Статистика сохранена в {stat_filename}")
