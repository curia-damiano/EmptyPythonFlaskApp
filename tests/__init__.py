import os
import sys

# Get the absolute path of the src directory
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src'))

# Add the src directory to the sys.path
if src_path not in sys.path:
	sys.path.insert(0, src_path)
