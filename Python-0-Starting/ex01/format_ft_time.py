import time

current_time = time.time()

sci_notation = "{:.2e}".format(current_time)

readable_date = time.strftime("%b %d %Y", time.localtime(current_time))

print(f"Seconds since January 1, 1970: {current_time:.4f} or {sci_notation} in scientific notation")
print(readable_date)