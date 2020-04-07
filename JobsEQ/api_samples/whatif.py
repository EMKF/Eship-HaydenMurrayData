import jobseq

def main():
    """Run the JobsEQ What-If analytic with supplied parameters """

    # Retrieve our auth token from JobsEQ using the jobseq module
    token = jobseq.get_token()
    #print("Auth Token Received:\n{0}".format(token))

    # create the analytic parameters for running the 'What-If' analytic
    analytic_id = '8d554e48-8940-4d0f-958b-067c462340ca'    # 'What-If' analytic id

    # analytic params that the 'What-If' analytic should be run with
    analytic_params = {
        "regions": [
            {
                "code": 1746,   # Region code '1746' indicates the region of 'Cleveland-Elyria, OH MSA'
                "type": 2       # Region type '2' indicates that the region is an MSA
            }
        ],
        "industry": {
            "code": 312112,     # Industry code '312112' indicates the industry of 'NAICS 312112 - Bottled Water Manufacturing'
            "type": 6           # Industry type '6' indicates a 6 digit industry type
        },
        "firmSize": 100,        # 
        "showCount": -1,        # 
        "type" : "Expansion"    # 
    }

    # Run the analytic and retrieve the response using an API call to JobsEQ
    analytic_response = jobseq.run_analytic(token, analytic_id, analytic_params)
    #print("Analytic Response Received:\n{0}".format(analytic_response))

    # Transform the analytic response
    table_data = WhatIfTableClass(analytic_response["table"])

    # Print the table data using the overridden __str__ method in the WhatIfTableClass
    print("\n")
    print(table_data)

class WhatIfTableClass:
    """Table data returned in the What-If analytic response"""
    def __init__(self, table):
        # Set the table's title
        self.title = table['titleCaption']

        # Set the table's data_source (contains credits and footnotes)
        self.data_source = "\n".join(table['dataSource'])

        # Populate a list of WhatIfRowItemClass objects using the row data from the table
        self.rows = []
        for row in table['rows']:
            self.rows.append(WhatIfRowItemClass(row))

    def __str__(self):
        """Return the table as a formatted string ready to be printed to console view"""
        return self.get_printable_table()

    def get_printable_table(self, row_limit=None):
        """Return the table as a formatted string ready to be printed to console view"""
        # Set a format that each printed table entry should follow
        row_format = ("{: <10} {: <40} {: >10} {: >10} {: >10} "
                      "{: >10} {: >10} {: >10} {: >10} {: >10}\n")
        # the max length of the table
        max_row_length = len(row_format.format(*(("",) * 10)))

        # Initialize the string to be returned starting with the title of the table
        output = "{{0: ^{0}}}\n".format(max_row_length).format(self.title)
        output += ("-" * max_row_length) + "\n"

        # Append a row table header with descriptions for the row columns
        output += row_format.format("Soc", "Title", "Empl New", "Empl Res", "Unempl",
                                    "Avg Wage", "Nat Wage", "Empl Ext", "Unempl Ext", "Ratio")
        output += ("-" * max_row_length) + "\n"

        # Format and append each row from the table data to the return string
        for row in self.rows[:row_limit] if row_limit is not None else self.rows:
            output += row_format.format(
                row.soc,
                # Print the full title if it fits or the partial title and an ellipsis
                row.title[:37] + (row.title[40:] and '...'),
                "{0:,.2f}".format(row.empl_new),
                "{0:,.2f}".format(row.empl_res),
                "{0:,.2f}".format(row.unempl),
                "{0:,.2f}".format(row.avg_wage),
                "{0:,.2f}".format(row.nat_wage),
                "{0:,.2f}".format(row.empl_ext) if isinstance(
                    row.empl_ext, float) else "N/A",
                "{0:,.2f}".format(row.unempl_ext) if isinstance(
                    row.unempl_ext, float) else "N/A",
                "{0:,.2f}".format(row.ratio))

        # Append the data source/credits to the bottom of the table
        output += "\n{0}".format(self.data_source)

        return output

class WhatIfRowItemClass:
    """Class to model some of the data from a table row found in the What-If analytic response"""
    def __init__(self, row):
        self.soc = row[1]['code']
        self.title = row[2]['displayText']
        self.empl_new = row[3]
        self.empl_res = row[4]
        self.unempl = row[5]
        self.avg_wage = row[6]
        self.nat_wage = row[7]
        self.empl_ext = row[8]['displayText'] if row[8] is not None else "N/A"
        self.unempl_ext = row[9] if row[9] is not None else "N/A"
        self.ratio = row[10]

if __name__ == '__main__':
    main()
