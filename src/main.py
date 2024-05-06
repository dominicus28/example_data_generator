import src.config_validator as validator
import src.start as start
import os

if __name__ == "__main__":

	if os.path.exists("script.sql"):
		os.remove("script.sql")

	validator.check_dependencies()
	start.read_config_and_run()