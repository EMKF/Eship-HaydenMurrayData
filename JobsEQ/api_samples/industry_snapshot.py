import jobseq

def main():
    """Run the JobsEQ 'Industry Snapshot' analytic with supplied parameters """

    # Retrieve our auth token from JobsEQ using the jobseq module
    token = jobseq.get_token()
    #print("Auth Token Received:\n{0}".format(token))

    # create the analytic parameters for running the 'Industry Snapshot' analytic
    analytic_id = '9d7913e1-8395-48ec-98b6-a5476cc9c2f3'    # 'Industry Snapshot' analytic id

    # analytic params that the 'Industry Snapshot' analytic should be run with
    analytic_params = {
        "regions": [{       # Primary region:
            "code": 1746,   # Region code '1746' indicates the region of 'Cleveland-Elyria, OH MSA'
            "type": 2       # Region type '2' indicates that the region is an MSA
        }, 
        {                   # Comparison region 1:
            "code": 39,     # Region code '39' indicates the region of 'Ohio'
            "type": 4       # Region type '4' indicates that the region is a state
        }, 
        {                   # Comparison region 2:
            "code": 0,      # Region code '0' indicates the region of 'USA'
            "type": 10      # Region type '10' indicates that the region is the nation
        }],
        "industry": {
            "code": 0,      # Industry code and type '0' indicates all industries
            "type": 0
        },
        "excludePrelim:": "false",  #
        "histYears": 5,     #
        "indLevel": 2,      #
        "model": 0,         #
        "ownLevel": 10,     #
        "projYears": 10     #
    }

    # Run the analytic and retrieve the response using an API call to JobsEQ
    analytic_response = jobseq.run_analytic(token, analytic_id, analytic_params)
    #print("Analytic Response Received:\n{0}".format(analytic_response))

    # Transform the analytic response
    table_data = IndustrySnapshotTableClass(analytic_response["table"])

    # Print the table data using the overridden __str__ method in the IndustrySnapshotTableClass
    print("\n")
    print(table_data)

class IndustrySnapshotTableClass:
    """Table data returned in the Industry Snapshot analytic response"""
    def __init__(self, table):
        # Set the table's title
        self.title = table['titleCaption']

        # Set the table's data_source (contains credits and footnotes)
        self.data_source = "\n".join(table['dataSource'])

        # Populate a list of IndustrySnapshotRowItemClass objects using the row data from the table
        self.rows = []
        for row in table['rows']:
            self.rows.append(IndustrySnapshotRowItemClass(row))

    def __str__(self):
        """Return the table as a formatted string ready to be printed to console view"""
        return self.get_printable_table()

    def get_printable_table(self, row_limit=None):
        """Return the table as a formatted string ready to be printed to console view"""
        # Set a format that each printed table entry should follow
        row_format = ("{: <10} {: <40} {: >15} {: >15} {: >10} {: >15}"
                      "{: >16} {: >16} {: >16} {: >15} {: >15} {: >15}\n")
        # the max length of the table
        max_row_length = len(row_format.format(*(("",) * 12)))

        # Initialize the string to be returned starting with the title of the table
        output = "{{0: ^{0}}}\n".format(max_row_length).format(self.title)
        output += ("-" * max_row_length) + "\n"

        # Append a row table header with descriptions for the row columns
        output += row_format.format("NAICS", "Industry", "Empl", "Avg Wage", "LQ",
                                    "Hist Emp", "Emp Change % 1", "Emp Change % 2",
                                    "Emp Change % 3", "Sep Demand", "Growth Demand",
                                    "Growth Perc")
        output += ("-" * max_row_length) + "\n"

        # Format and append each row from the table data to the return string
        for row in self.rows[:row_limit] if row_limit is not None else self.rows:
            output += row_format.format(
                row.naics,
                row.industry[:37] + (row.industry[40:] and '...'),
                "{0:,.2f}".format(row.empl),
                "{0:,.2f}".format(row.avg_wage),
                "{0:,.2f}".format(row.lq),
                "{0:,.2f}".format(row.hist_emp),
                "{0:,.2f}%".format(row.emp_chg_perc_r1 * 100),
                "{0:,.2f}%".format(row.emp_chg_perc_r2 * 100),
                "{0:,.2f}%".format(row.emp_chg_perc_r3 * 100),
                "{0:,.2f}".format(row.sep_demand),
                "{0:,.2f}".format(row.growth_demand),
                "{0:,.2f}%".format(row.growth_perc * 100))

        # Append the data source/credits to the bottom of the table
        output += "\n{0}".format(self.data_source)

        return output

class IndustrySnapshotRowItemClass:
    """Class to model some of the data from a table row found in the Industry Snapshot analytic response"""
    def __init__(self, row):
        self.naics = row[1]['code'] if row[1] is not None else "N/A"
        self.industry = row[2]['displayText'] if row[2] is not None else "N/A"
        self.empl = row[3]
        self.avg_wage = row[4]
        self.lq = row[5]
        self.hist_emp = row[6]
        # skip the spark chart column
        self.emp_chg_perc_r1 = row[8]   # NOTE: Percentages are represented in decimal form
        self.emp_chg_perc_r2 = row[9]   #       i.e. 0.015 = 1.5%
        self.emp_chg_perc_r3 = row[10]
        self.sep_demand = row[11]
        self.growth_demand = row[12]
        self.growth_perc = row[13]

if __name__ == '__main__':
    main()
