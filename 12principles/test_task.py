from Task import Task

def test_mark_done():
    task = Task("Протестировать задачу")
    task.mark_done()
    assert task.status == "done"
