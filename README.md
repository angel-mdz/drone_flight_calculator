Used GitHub Copilot to complete inline code for initial calculate_flight_time() logic inside flight_calculator file. Corrected the constants BASE_FLIGHT_TIME and WEIGHT_FACTOR - the originals were 20 min base time and .05 grams weight factor. Rewrote the comment for BASE_FLIGHT_TIME - the original mentioned "standard payload" instead of no payload attached.

Used GitHub Copilot to generate the input validation for weight_grams in calculate_flight_time(). Prompt is at the comment in line 16: "Validate input weight, it should not be negative, if negative raise a ValueError with a clear message". Reviewed and accepted generated if statement with raise ValueError message.

Used GitHub Copilot to auto-complete flight_time_table() function inside flight_calculator file. Reviewed and accepted the suggested code as is. 

Used GiHub Copilot (/test) to generate Pytest test suite for calculate_time_flight(). Checked generated code, and ran the tests in terminal using pytest. All 7 tests passed including: zero payload, avarage payloads, payload to reach 0 timeflight and to exceed the zero-flight-time boundary, and a negative weight input.