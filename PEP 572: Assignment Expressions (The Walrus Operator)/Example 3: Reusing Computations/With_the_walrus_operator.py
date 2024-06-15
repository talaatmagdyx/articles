def process_data(data, threshold):
    if (result := complex_computation(data)) > threshold:
        return result
    return None
