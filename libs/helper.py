def create_locality(request):
    locality = "%s %s %s %s %s" % (
        request.get("address_line_1"),
        request.get("address_line_2"),
        request.get("pin_code"),
        request.get("city"),
        request.get("house_num"),
    )
    return " ".join(sorted(set(locality), key=locality.index))
