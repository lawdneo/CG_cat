

    
        

from question1 import question1
from question2 import question2
import argparse

def main():
    parser = argparse.ArgumentParser(description="Answer Generator")
    parser.add_argument('--dataset_directory', type=str, help='Directory path of the massive dataset')
    parser.add_argument('--destination_directory', type=str, help='Destination Directory Path of Processed files')
    parser.add_argument('--partitioned_directory', type=str, help='Destination Directory of the Partitioned_datasets')
    parser.add_argument('--question',type=int,help="Question to answer")
    
    args = parser.parse_args()
    if args.question==1:
        question1(dataset_directory_path=args.dataset_directory,destination_directory_path=args.destination_directory)
    else:

        question2()





if __name__ == '__main__':
    main()
    
    

