import argparse
# simple arg parse
parser = argparse.ArgumentParser()
parser.add_argument("echo",  help="echo the string here")
args = parser.parse_args()
print args.echo
