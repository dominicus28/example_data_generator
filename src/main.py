import src.config_validator as validator
import src.start as start
import os
# import src.references as ref


if __name__ == "__main__":

	if os.path.exists("script.sql"):
		os.remove("script.sql")
	start.read_config_and_run()

	# print(ref.reference_dict)