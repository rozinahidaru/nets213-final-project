def main():
    # Read in CVS result file with pandas
    # PLEASE DO NOT CHANGE
    mturk_res = pd.read_csv('hw7_data.csv')

    # Call functions and output required CSV files

    #Part 1 - Majority votes
    votes = majority_vote(mturk_res)
    with open("output1.csv", 'w', newline='') as csvfile:
      csv_writer = csv.writer(csvfile)
      csv_writer.writerow(['attr_id', 'adj', 'label'])
      for row in votes:
        csv_writer.writerow(row)


if __name__ == '__main__':
    main()
