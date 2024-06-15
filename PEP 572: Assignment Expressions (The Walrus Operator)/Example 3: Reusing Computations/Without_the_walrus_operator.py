def process_data(data, threshold):
    result = complex_computation(data)
    if result > threshold:
        return result
    return None
