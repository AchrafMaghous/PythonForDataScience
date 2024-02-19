import time
import sys

def ft_tqdm(lst: range) -> None:
		"""
		@param: lst: range
		@description: Basic progress bar implementation with yield and fixed format.
		"""

		total = len(lst)
		bar_length = 60
		completed = 0
		start_time = time.time()
		last_update = start_time

		def update_progress():
				nonlocal completed, last_update
				current_time = time.time()

				# Update every 0.1 seconds or when completed
				if current_time - last_update >= 0.1 or completed >= total:
						elapsed_seconds = current_time - start_time
						progress = completed / total
						bar = "=" * int(progress * bar_length) + "-" * (bar_length - int(progress * bar_length)) + ">"

						sys.stdout.write("\r100%|[{bar}]{completed}/{total} {elapsed}".format(
								bar=bar, completed=completed, total=total, elapsed=time.strftime("%M:%S", time.gmtime(elapsed_seconds))
						))
						sys.stdout.flush()
						last_update = current_time

		for item in lst:
				yield item
				completed += 1
				update_progress()

		sys.stdout.write("\n")
		sys.stdout.flush()
