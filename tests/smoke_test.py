# -*- coding: utf-8 -*-
"""Проверка движка заданий без GUI (запуск из корня репозитория)."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ApplicationData import (ApplicationData, correct_words_list, hash_key,
                             incorrect_words)


def main():
    started = time.perf_counter()
    data = ApplicationData()
    print(f"слов в словаре: {len(correct_words_list)}")
    print(f"неверных вариантов: {len(incorrect_words)}")

    assert len(correct_words_list) > 100, "словарь подозрительно маленький"
    assert len(incorrect_words) > len(correct_words_list), \
        "неверных вариантов должно быть больше, чем верных"

    for _ in range(50):
        task, answer, false_word = data.task_and_response()
        assert len(task) == 5, "в задании должно быть 5 слов"
        assert len({word.lower() for word in task}) == 5, \
            "слова в задании не должны повторяться"
        assert isinstance(answer, int) and 1 <= answer <= 5, \
            "номер ответа должен быть от 1 до 5"
        assert task[answer - 1] == false_word, \
            "номер ответа должен указывать на неверное слово"
        assert hash_key(false_word) in incorrect_words, \
            "ответ должен быть из неверных вариантов"

    elapsed = time.perf_counter() - started
    print(f"50 заданий собраны за {elapsed:.2f} с")
    print("OK: движок заданий работает")


if __name__ == "__main__":
    sys.exit(main())
