import argparse

if __name__=='__main__':
#Creating a parser
    args_parser = argparse.ArgumentParser(description="process args")
# Adding arguments
    args_parser.add_argument('--agrg_1=',
                             required=True,
                             help="this is the first argument...",
                             default=None,
                             type=str,
                             )
# Parsing arguments
    args = args_parser.parse_args()

    print(args)