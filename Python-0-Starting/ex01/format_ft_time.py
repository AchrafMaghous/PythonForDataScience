import time

current_time = time.time()

curr_time_with_comas = "{:,.4f}".format(current_time)

sci_notation = "{:.2e}".format(current_time)

readable_date = time.strftime("%b %d %Y", time.localtime(current_time))

print(f"Seconds since January 1, 1970: {curr_time_with_comas} or {sci_notation} in scientific notation")
print(readable_date)