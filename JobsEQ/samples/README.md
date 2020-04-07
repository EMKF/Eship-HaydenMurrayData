# JobsEQ Samples for Python 3

These samples were built and tested using `Python 3.6.3`

If you receive a `UnicodeEncodeError` when trying to run these samples, there is a chance that the encoding your terminal is using does not support a character included in the sample program outputs.

If you are using Windows, you can try running the command `chcp 65001` in your terminal or command prompt before running the sample programs to switch the code page in use.

See [this post](https://stackoverflow.com/questions/14284269/why-doesnt-python-recognize-my-utf-8-encoded-source-file/14284404#14284404) on Stack Overflow for more information.

## jobseq.py

This is a sample module that demonstrates how to request an auth token and call an analytic using JobsEQ API calls.

This module is used by the following samples to simplify retrieving an auth token and running the analytic.

## whatif.py

This sample demonstrates how to request an auth token and call the **What-If** analytic using the provided `jobseq` (see `jobseq.py`) module.

The analytic response returned is transformed using a class that pulls select fields from the response for this specific analytic. This data is then used to print a formatted text table to the console.

## industry_snapshot.py

This sample demonstrates how to request an auth token and call the **Industry Snapshot** analytic using the provided `jobseq` (see `jobseq.py`) module.

The analytic response returned is transformed using a class that pulls select fields from the response for this specific analytic. This data is then used to print a formatted text table to the console.

## rti_job_post_feed.py

This sample demonstrates how to use the provided `jobseq` module (see `jobseq.py`) to request an auth token and call the **RTI Job Posts** analytic with custom parameters filtering for a specific occupation.

The analytic response returned is transformed using a class that pulls select fields from the response for this specific analytic. This data is then used to print a formatted text table to the console.

## rti_company.py

This sample demonstrates how to use the provided `jobseq` module (see `jobseq.py`) to request an auth token and call the **RTI Job Posts** analytic with custom parameters filtering for a specific company.

The analytic response returned is transformed using a class that pulls select fields from the response for this specific analytic. This data is then used to print a formatted text table to the console.

## rti_company_chart.py

Note: This script requires the `matplotlib` library!

This sample demonstrates how to use the provided `jobseq` module (see `jobseq.py`) to request an auth token and call the **RTI Job Posts** analytic with parameters to filter results based on a specific company, as well as use `pyplot` to output a bar chart using some of the **RTI Job Posts** data.

The analytic response returned is transformed using a class that pulls select fields from the response for this specific analytic. The data is then transformed again to be used in a barchart. The bar chart is then saved to file the file `rti_company_chart_image.png`.