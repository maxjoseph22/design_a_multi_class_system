from lib.diary_multi_class import *

def test_constructs_with_titles_and_contents():
    diary_entry = DiaryEntry("GREAT DAY!")
    assert diary_entry.entry == "GREAT DAY!"

def test_count_words_no_entries():
    diary_entry = DiaryEntry("")
    result = diary_entry.count_words()
    assert result == 0

def test_count_words_an_entry():
    diary_entry = DiaryEntry("What a boring day!")
    result = diary_entry.count_words()
    assert result == 4

def test_reading_time():
    diary_entry = DiaryEntry("What a wicked day I loved every minute of it")
    result = diary_entry.reading_time(10)
    assert result == "1 minute 0 seconds"

def test_reading_chunk():
    diary_entry = DiaryEntry("What a wicked day I loved every minute of it")
    result = diary_entry.reading_chunk(2,2)
    assert result == "What a wicked day"

def test_reading_chunk_keeps_place():
    diary_entry = DiaryEntry("What a wicked day I loved every minute of it")
    result_1 = diary_entry.reading_chunk(2,2)
    result_2 = diary_entry.reading_chunk(2,2)
    assert result_1 == "What a wicked day"
    assert result_2 == "I loved every minute"

def test_reading_chunk_finishes_when_done():
    diary_entry = DiaryEntry("What a wicked day I loved every minute of it")
    result_1 = diary_entry.reading_chunk(2,2)
    result_2 = diary_entry.reading_chunk(2,2)
    result_3 = diary_entry.reading_chunk(2,10)
    assert result_1 == "What a wicked day"
    assert result_2 == "I loved every minute"
    assert result_3 == "of it"



