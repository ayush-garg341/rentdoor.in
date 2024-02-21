from django.conf import settings


def create_locality(request: dict) -> str:
    locality = "%s %s %s %s %s" % (
        request.get("address_line_1"),
        request.get("address_line_2"),
        request.get("pin_code"),
        request.get("city"),
        request.get("house_num"),
    )
    return locality.replace(",", " ")


def validate_file_size(files):
    file_names = []
    for file in files:
        if file.size > settings.MAX_UPLOAD_SIZE:
            file_names.append(file.name)

    return (
        (False, "Please upload files less than 5 MB {}".format(", ".join(file_names)))
        if len(file_names) > 0
        else (True, "")
    )
