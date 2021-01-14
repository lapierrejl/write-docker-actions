import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument("--output_path", 
                    default="CLUSTERINFO.md", 
                    type=str)
args = parser.parse_args()

OUTPUT_PATH = args.output_path

now = int(time.time())
with open('README.md', 'w') as f:
    f.write(f"# {now} {OUTPUT_PATH}")
