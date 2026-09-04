Used GitHub Copilot to complete inline code for initial calculate_flight_time() logic. Corrected the constants BASE_FLIGHT_TIME and WEIGHT_FACTOR - the originals were 20 min base time and .05 grams weight factor. Rewrote the comment for BASE_FLIGHT_TIME - the original mentioned "standard payload" instead of no payload attached.

Used GitHub Copilot to generate the input validation for weight_grams. Prompt in comment in line 15: "Validate input weight, it should not be negative, if negative raise a ValueError with a clear message".

Used GitHub Copilot to auto-complete flight_time_table(). Reviewed and accepted the suggested code as is. 