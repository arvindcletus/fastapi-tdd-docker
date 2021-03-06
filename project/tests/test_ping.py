"""# project/tests/test_ping.py"""


def test_ping(test_app):
    """Test that ping works"""
    # Given
    # test_app

    # When
    response = test_app.get("/ping")

    # Then
    assert response.status_code == 200
    assert response.json() == {"environment": "dev", "ping": "hello!", "testing": True}
