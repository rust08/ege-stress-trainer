# -*- coding: utf-8 -*-
"""Быстрая проверка движка заданий без GUI (запуск из корня репозитория)."""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Словарь_Ударений import (ApplicationData, all_words, correct_words_list,
                              incorrect_words)


def main():
    started = time.perf_counter()
    data = ApplicationData()
    print(f"слов в словаре: {len(correct_words_list)}")
    print(f"вариантов слов: {len(all_words)}")
    print(f"неверных вариантов: {len(incorrect_words)}")

    assert len(correct_words_list) > 100, "словарь подозрительно маленький"
    assert len(incorrect_words) > len(correct_words_list), \
        "неверных вариантов должно быть больше, чем верных"

    for _ in range(50):
        task = data.task_and_response()
        assert len(task) == 5, "в задании должно быть 5 слов"
        assert len({word.lower() for word in task}) == 5, \
            "слова в задании не должны повторяться"
        correct = [word for word, answer in task.items() if answer]
        assert 1 <= len(correct) <= 4, \
            "в задании должно быть от 1 до 4 верных слов"
        for word, answer in task.items():
            if answer:
                assert answer.strip() == word.strip(), \
                    "ответ должен совпадать с верным словом"

    elapsed = time.perf_counter() - started
    print(f"50 заданий собраны за {elapsed:.2f} с")
    print("OK: движок заданий работает")


if __name__ == "__main__":
    sys.exit(main())
