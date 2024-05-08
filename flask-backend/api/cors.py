def corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response