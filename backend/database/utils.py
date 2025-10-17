def remove_none_values(data: dict) -> dict:
    # Remove None values from a dictionary
    return {k: v for k, v in data.items() if v is not None}