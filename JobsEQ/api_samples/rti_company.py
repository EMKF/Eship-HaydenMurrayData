import jobseq

COMPANY_NAME = 'IBM'

def main():
    """Run the JobsEQ RTI analytic with supplied parameters """

    # Retrieve our auth token from JobsEQ using the jobseq module
    token = jobseq.get_token()
    #print("Auth Token Received:\n{0}".format(token))

    # create the analytic parameters for running the 'RTI' analytic
    analytic_id = 'fb9d934a-17db-4a9d-94d2-54a7c93b3a3d' # 'RTI Job Posts' analytic id

    # analytic params that the 'RTI' analytic should be run with
    analytic_params = {
        "region": {
            "code": 39,     # Region code '39' indicates the region of 'Ohio'
            "type": 4       # Region type '4' indicates that the region is a state
        },
        "filters": [{
            "type": "comp",     # Filter based on company
            "filterType": "contains", # Filter comparison type
            "key": COMPANY_NAME   # Company name to filter results for
        }],
        "timeframe": 90     # Last 90 days
    }

    # Run the analytic via an API call and get its response
    analytic_response = jobseq.run_analytic(token, analytic_id, analytic_params)
    # print("Analytic Response Received:\n{0}".format(analytic_response))

    # Transform the analytic response
    table_data = RTITableClass(analytic_response["table"])

    # Print the table data using the overridden __str__ method in the RTITableClass
    job_count = len(table_data.rows)
    rows_to_show = min(10, job_count)
    print(("The company {0} had {1} job postings in Ohio over the last 90 days. "
           "Here are the most recent {2} jobs:").format(COMPANY_NAME, job_count, rows_to_show))
    print("\n")
    print(table_data.get_printable_table(rows_to_show))


class RTITableClass:
    """Table data returned in the What-If analytic response"""
    def __init__(self, table):
        # Set the table's title
        self.title = "RTI Run for {0} in Ohio".format(COMPANY_NAME)

        # Set the table's data_source (contains credits and footnotes)
        self.data_source = "\n".join(table['dataSource'])

        # Populate a list of RTIRowItemClass objects using the row data from the table
        self.rows = []
        for row in table['rows'] if 'rows' in table else []:
            self.rows.append(RTIRowItemClass(row))

    def __str__(self):
        return self.get_printable_table()


    def get_printable_table(self, row_limit=None):
        """Return the table as a formatted string ready to be printed to console view"""
        # Set a format that each printed table entry should follow
        row_format = "{: <40} {: <40} {: <40} {: <22} {: <58}\n"
        max_row_length = len(row_format.format(*(("",) * 10)))    # the max length of the table

        # Initialize the string to be returned starting with the title of the table
        output = "{{0: ^{0}}}\n".format(max_row_length).format(self.title)
        output += ("-" * max_row_length) + "\n"

        # Append a row table header with descriptions for the row columns
        output += row_format.format("Title", "Company",
                                    "Location", "Date", "URL")
        output += ("-" * max_row_length) + "\n"

        # Format and append each row from the table data to the return string
        for row in self.rows[:row_limit] if row_limit is not None else self.rows:
            output += row_format.format(
                row.title[:37] + (row.title[40:] and '...'),
                row.company[:37] + (row.company[40:] and '...'),
                row.location[:37] + (row.location[40:] and '...'),
                row.date,
                row.url)

        # Append the data source/credits to the bottom of the table
        output += "\n{0}".format(self.data_source)

        return output


class RTIRowItemClass:
    """Class to model some of the data from a table row found in the What-If analytic response"""
    def __init__(self, row):
        self.url = "{0}{1}".format(jobseq.JOBSEQ_URL, row[0]['url'])
        self.title = row[0]['displayText']
        self.company = row[1]
        self.location = row[2]
        self.date = row[3]

if __name__ == '__main__':
    main()
