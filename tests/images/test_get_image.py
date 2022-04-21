
class TestGetImage:
    def test_user_can_get_one_image_by_id(self, app, image_record):
        id, filename, tags = image_record
        response = app.http_api.get(f"/images/{id}")
        app.checkers.check_json_value_by_name(response, "filename", filename,
                                              "Created image has wrong 'filename'")
        app.checkers.check_json_has_key(response, "size")
        app.checkers.check_json_has_key(response, "tags")
        tags_list = response.json()["tags"][0]
        for tag in tags_list:
            assert (item for item in tags_list if item["name"] == tag), "Created image has wrong tag name"

    def test_cannot_get_image_not_exists(self, app):
        app.http_api.get("/images/0", expected_code=404)

    def test_user_can_get_all_images(self, app):
        response = app.http_api.get(f"/images")
        app.checkers.check_json_has_key(response, "meta")
        app.checkers.check_json_has_key(response, "results")
        results_list = response.json()["results"]
        assert len(results_list) > 0, "Got empty images list"
