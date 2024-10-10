from lib.diary_multi_class import *

def test_to_do_initialises_with_task():
    todo = Todo("Brush teeth")
    result = todo.task
    assert result == "Brush teeth"
    assert todo.complete == False


def test_mark_complete():
    todo = Todo("Brush teeth")
    todo.mark_complete()
    complete_status = todo.complete
    assert complete_status == True


