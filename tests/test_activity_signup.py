def test_signup_for_activity_adds_new_student(client):
    # Arrange
    activity_name = "Chess Club"
    student_email = "new.student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": student_email},
    )

    # Assert
    assert response.status_code == 200
    assert response.json() == {
        "message": f"Signed up {student_email} for {activity_name}"
    }

    activities_response = client.get("/activities")
    participants = activities_response.json()[activity_name]["participants"]
    assert student_email in participants


def test_signup_for_activity_rejects_duplicate_student(client):
    # Arrange
    activity_name = "Chess Club"
    existing_student = "michael@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": existing_student},
    )

    # Assert
    assert response.status_code == 400
    assert response.json() == {
        "detail": "Student already signed up for this activity"
    }


def test_signup_for_activity_returns_not_found_for_missing_activity(client):
    # Arrange
    activity_name = "Nonexistent Club"
    student_email = "student@mergington.edu"

    # Act
    response = client.post(
        f"/activities/{activity_name}/signup",
        params={"email": student_email},
    )

    # Assert
    assert response.status_code == 404
    assert response.json() == {"detail": "Activity not found"}
