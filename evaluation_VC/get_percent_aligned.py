


import os,sys
import argparse

import pysam


def count_mapped(sam_file):
    SAM_file = pysam.AlignmentFile(sam_file, "r", check_sq=False)

    num_mapped = 0
    for read in SAM_file.fetch(until_eof=True):
        if read.is_mapped:
            num_mapped += 1
    return num_mapped     


def main(args):

    # sam1 = read_sam(args.sam1)
    # sam2 = read_sam(args.sam2)
    # if args.sam3:
    #     alignments_tool = read_sam(args.sam3)
    #     is_paf = False
    # elif args.paf:
    #     alignments_tool, _ = read_paf(args.paf)
    #     is_paf = True
    # alignments_tool = read_sam(args.tool)

    # if args.predicted_sam:
    #     predicted = read_sam(args.predicted_sam)
    # elif args.predicted_paf:
    #     predicted, mapped_to_multiple_pos = read_paf(args.predicted_paf)
    #     # print("Number of reads mapped to several positions (using first pos):", mapped_to_multiple_pos)

    num_mapped = count_mapped(args.sam)
    print(round(num_mapped/8000000,5))

    # for ovl, nr_in_common in overlaps.items():
    #     print("{0} : {1}".format(ovl, nr_in_common))



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Count percent aligned", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('--tool', type=str, default="", help='The tool name')
    parser.add_argument('--outfile', type=str, default=None, help='Path to file.')
    parser.add_argument('--sam', type=str, default=None, help='Path to file')
    # parser.set_defaults(which='main')
    args = parser.parse_args()



    if len(sys.argv)==1:
        parser.print_help()
        sys.exit()

    main(args)
