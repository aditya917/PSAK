from rotate import Rotate
from merge import Merge
import argparse

def rotateFunction(args):
    if args.input_file is None:
        print("Error: --input_file is required when using --rotate")
        exit(1)

    rotator = Rotate(args.input_file)
    rotator.rotate(args.num_pages, args.angle, args.output)

def mergeFunction(args):
    merger = Merge()
    merger.merge(args.files, args.directory, args.output)

def main():
    parser = argparse.ArgumentParser(description="PDF Swiss-Army Knife CLI Tool")
    subparsers = parser.add_subparsers(dest="command")

    merge_parser = subparsers.add_parser("merge", help="merge PDFs sequentially")
    merge_parser.add_argument("--files", nargs="+", default=[], help="pdf files to merge")
    merge_parser.add_argument("--directory", help="merge all pdfs in a directory")
    merge_parser.add_argument("-o", "--output", default="merged_output.pdf", help="output filename")

    rotate_parser = subparsers.add_parser("rotate", help="rotate PDFs sequentially")
    rotate_parser.add_argument("input_file", help="input pdf file to rotate")
    rotate_parser.add_argument("-n", "--num_pages", type=int, required=True, help="number of pages to rotate")
    rotate_parser.add_argument("-a", "--angle", type=int, required=True, help="number of angles to rotate")
    rotate_parser.add_argument("-o", "--output", default="rotated_output.pdf", help="output filename")

    args = parser.parse_args()

    if args.command == "rotate":
        rotateFunction(args)
    if args.command == "merge":
        mergeFunction(args)

if __name__ == "__main__":
    main()





