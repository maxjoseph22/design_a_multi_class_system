from lib.diary_multi_class import *
import pytest

def test_diary_instantiates_with_empty_diary_and_to_do_lists():
    diary = Diary()
    result_1 = diary.diary_entries
    result_2 = diary.to_do_list
    assert result_1 == []
    assert result_2 == []

    


# def pick_best_diary_entry_with_emtpy_list_error():
#     diary = Diary()
#     with pytest.raises(Exception) as error: 
#         diary.find_best_entry_for_reading_time(2,2)
#     error_message = str(error.value) 
#     assert error_message == "N/A - No diary entries"