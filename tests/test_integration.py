from lib.diary_multi_class import *
import pytest

def test_add_one_entry_to_diary():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Shawty swing my way.")
    diary.add_to_diary(diary_entry_1)
    result = diary.all_diary_entries()
    assert result == [diary_entry_1]

def test_add_one_todo_to_list():
    diary = Diary()
    to_do_1 = Todo("Water the garden")
    diary.add_to_do(to_do_1)
    result = diary.incomplete()
    assert result == [to_do_1]

def test_todo_list_adds_instance_of_todo_and_returns_incomplete():
    diary = Diary()
    todo = Todo("Brush teeth")
    diary.add_to_do(todo)
    assert diary.incomplete() == [todo]

def test_todo_list_adds_two_of_todo_and_returns_incomplete():
    diary = Diary()
    todo_1 = Todo("Brush teeth")
    todo_2 = Todo("Wash the car")
    diary.add_to_do(todo_1)
    diary.add_to_do(todo_2)
    assert diary.incomplete() == [todo_1, todo_2]

def test_marking_to_do_complete_and_returning_incomplete():
    diary = Diary()
    todo_1 = Todo("Brush teeth")
    todo_2 = Todo("Wash the car")
    diary.add_to_do(todo_1)
    diary.add_to_do(todo_2)
    todo_1.mark_complete()
    assert diary.incomplete() == [todo_2]

def test_marking_to_do_complete_and_returning_complete():
    diary = Diary()
    todo_1 = Todo("Brush teeth")
    todo_2 = Todo("Wash the car")
    diary.add_to_do(todo_1)
    diary.add_to_do(todo_2)
    todo_1.mark_complete()
    assert diary.complete() == [todo_1]

def test_give_up():
    diary = Diary()
    todo_1 = Todo("Brush teeth")
    todo_2 = Todo("Wash the car")
    diary.add_to_do(todo_1)
    diary.add_to_do(todo_2)
    todo_1.mark_complete()
    diary.give_up()
    assert diary.complete() == [todo_1, todo_2]

def test_give_up_again():
    diary = Diary()
    todo_1 = Todo("Brush teeth")
    todo_2 = Todo("Wash the car")
    diary.add_to_do(todo_1)
    diary.add_to_do(todo_2)
    diary.give_up()
    assert diary.complete() == [todo_1, todo_2]

def test_find_best_entry_for_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Shawty swing my way.")
    diary.add_to_diary(diary_entry_1)
    diary_entry_2 = DiaryEntry("Shawty swing my way. Swing it over here.")
    diary.add_to_diary(diary_entry_2)
    result = diary.find_best_entry_for_reading_time(2,4)
    assert result == diary_entry_2

def test_find_best_entry_for_reading_time():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Shawty swing my way.")
    diary.add_to_diary(diary_entry_1)
    diary_entry_2 = DiaryEntry("Shawty swing my way. Swing it over here.")
    diary.add_to_diary(diary_entry_2)
    result = diary.find_best_entry_for_reading_time(1,3)
    assert result == None

def test_find_phone_numbers_in_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Shawty swing my way. 07821120987")
    diary.add_to_diary(diary_entry_1)
    diary_entry_2 = DiaryEntry("Shawty swing my way. Swing it over here.")
    result = diary.phone_numbers()
    assert result == ["07821120987"]

def test_find_phone_numbers_in_multiple_entries():
    diary = Diary()
    diary_entry_1 = DiaryEntry("Shawty swing my way. 07821120987")
    diary.add_to_diary(diary_entry_1)
    diary_entry_2 = DiaryEntry("Shawty swing my way. Swing it over here. 07818088799")
    diary.add_to_diary(diary_entry_2)
    result = diary.phone_numbers()
    assert result == ["07821120987", "07818088799"]