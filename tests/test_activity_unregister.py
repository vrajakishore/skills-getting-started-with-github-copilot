def test_unregister_from_activity_removes_student(client):
    # Arrange
    activity_name = "Chess Club"
    existing_student = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": existing_student},
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Unregistered {existing_student} from {activity_name}"
    }

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert existing_student not in participants


def test_unregister_from_activity_returns_not_found_for_missing_student(client):
    # Arrange
    activity_name = "Chess Club"
    unknown_student = "not.enrolled@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": unknown_student},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {
        "detail": "Student not signed up for this activity"
    }


def test_unregister_from_activity_returns_not_found_for_missing_activity(client):
    # Arrange
    activity_name = "Nonexistent Club"
    student_email = "student@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/signup",
        params={"email": student_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
