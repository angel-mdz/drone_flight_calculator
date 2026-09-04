def calculate_flight_time(weight_grams):
    """
    Calculate the estimated flight time of a drone based on its payload weight in grams.

    Parameters:
    weight_grams (float): The weight of the payload in grams.

    Returns:
    float: Estimated flight time in minutes.
    """
    # Constants for flight time calculation
    #Copilot suggested 20 minutes and .05 grams here; Edited to assignment's requirements
    BASE_FLIGHT_TIME = 180  # Base flight time in minutes with no payload attached
    WEIGHT_FACTOR = 0.1   # Flight time reduction factor per gram

    # Validate input weight, it should not be negative, if negative raise a ValueError with a clear message
    if weight_grams < 0:
        raise ValueError("Weight cannot be negative. Please provide a non-negative weight in grams.")

    # Calculate the reduction in flight time based on weight
    reduction = weight_grams * WEIGHT_FACTOR

    # Calculate the estimated flight time
    estimated_flight_time = BASE_FLIGHT_TIME - reduction

    # Ensure flight time is not negative
    if estimated_flight_time < 0:
        estimated_flight_time = 0

    return estimated_flight_time

def flight_time_table(max_weight_grams, step_grams):
    """
    Generate a table of estimated flight times for different payload weights.

    Parameters:
    max_weight_grams (float): The maximum weight of the payload in grams.
    step_grams (float): The increment step for the weight in grams.

    Returns:
    list of tuples: Each tuple contains (weight, estimated flight time).
    """
    # Validate input parameters
    if max_weight_grams < 0:
        raise ValueError("Maximum weight cannot be negative. Please provide a non-negative weight in grams.")
    if step_grams <= 0:
        raise ValueError("Step size must be positive. Please provide a positive step size in grams.")

    flight_times = []
    for weight in range(0, int(max_weight_grams) + 1, int(step_grams)):
        flight_time = calculate_flight_time(weight)
        flight_times.append((weight, flight_time))

    return flight_times