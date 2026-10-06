from tasktrack import remove_task_by_number

def test_remove_first_task():
    """Removing task 1 should remove the first task."""
    # Arrange
    tasks = ["Study", "Exercise", "Read"]
    expected_task = "Study"

    # Act
    removed_task = remove_task_by_number(tasks, 1)

    # Assert
    assert removed_task == expected_task
    assert tasks == ["Exercise", "Read"]

def test_remove_middle_task():
    """Removing a task in the middle of the list should remove the middle task"""

    tasks = ["Study", "Exercise", "Read"]
    expected_tasks = ["Study", "Read"]

    removed_task = remove_task_by_number(tasks, 2)

    assert removed_task == "Exercise"
    assert tasks == expected_tasks

def test_remove_last_task():
    """Removing the last task in the list should remove the len(tasks) task"""

    tasks = ["Study", "Exercise", "Read"]
    expected_tasks = ["Study", "Exercise"]

    removed_task = remove_task_by_number(tasks, len(tasks))

    assert removed_task == "Read"
    assert tasks == expected_tasks

def test_remove_task_zero():
    """Attempting to remove task 0 should return None"""

    tasks = ["Study", "Exercise", "Read"]
    expected_tasks = ["Study", "Exercise", "Read"]

    remove_zero = remove_task_by_number(tasks, 0)

    assert remove_zero is None
    assert expected_tasks == tasks

def test_remove_task_number_too_large():
    """Attempting to remove a task out of index should return None"""

    tasks = ["Study", "Exercise", "Read"]
    expected_tasks = ["Study", "Exercise", "Read"]

    remove_too_large = remove_task_by_number(tasks, 9999)

    assert remove_too_large is None
    assert expected_tasks == tasks

def test_remove_task_from_empty_list():
    """Attempting to remove a task from an empty list should return None"""

    tasks = []
    expected_tasks = []

    removed_task = remove_task_by_number(tasks, 1)

    assert removed_task is None
    assert expected_tasks == tasks