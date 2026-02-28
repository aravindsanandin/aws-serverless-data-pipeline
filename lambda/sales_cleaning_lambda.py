import json
import boto3
import csv
import io

s3 = boto3.client('s3')

def lambda_handler(event, context):

    source_bucket = "jack-raw-sales-2026"
    destination_bucket = "jack-processed-sales-2026"
    file_key = "raw/sale1.csv"

    response = s3.get_object(Bucket=source_bucket, Key=file_key)
    content = response['Body'].read().decode('utf-8')

    reader = csv.DictReader(io.StringIO(content))
    output = io.StringIO()
    writer = None

    for row in reader:

        try:
            units_sold = int(row["Units Sold"])
            revenue = float(row["Total Revenue"])

            # Filter logic
            if units_sold > 0 and revenue > 100000:

                if writer is None:
                    writer = csv.DictWriter(output, fieldnames=row.keys())
                    writer.writeheader()

                row["Units Sold"] = units_sold
                row["Total Revenue"] = revenue

                writer.writerow(row)

        except Exception as e:
            continue

    s3.put_object(
        Bucket=destination_bucket,
        Key="clean/processed_sales.csv",
        Body=output.getvalue()
    )

    return {
        'statusCode': 200,
        'body': json.dumps("Sales file processed successfully!")
    }
