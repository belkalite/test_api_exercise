def check_tags(response, image_body):
    response_tags = response.json()["tags"][0]
    request_tags = image_body["tags"]
    for tag in request_tags:
        assert (item for item in response_tags if item["name"] == tag), "Created image has wrong tags"
