import pytest


class TestDeleteImages:
    @pytest.mark.xfail(reason="delete image is not implemented yet")
    def test_image_delete(self, app, image_record):
        id = image_record
        response = app.http_api.delete(f"/images/{id}", expected_code=204)
        assert response.json() == {}, "Wrong response body"
        app.http_api.get(f"/images/{id}", expected_code=404)
