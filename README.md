# AWS Textract implementation

Amazon Textract is a machine learning (ML) service that automatically extracts text, handwriting, layout elements, and data from scanned documents. It goes beyond simple optical character recognition (OCR) to identify, understand, and extract specific data from documents. Today, many companies manually extract data from scanned documents such as PDFs, images, tables, and forms, or through simple OCR software that requires manual configuration (which often must be updated when the form changes). To overcome these manual and expensive processes, Textract uses ML to read and process any type of document, accurately extracting text, handwriting, tables, and other data with no manual effort. You can use one of our pretrained or custom features to quickly automate document processing, whether you’re automating loans processing or extracting information from invoices and receipts. Textract provides you the ability to customize our pretrained features to meet the document processing needs specific to your business. Textract can extract the data in minutes instead of hours or days. "[AWS Official documentation](https://aws.amazon.com/textract/?nc1=h_ls "AWS Official documentation")"

![AWS Textract](./Diagram.png)

## Prerequisites:

- [AWS SAM CLI installed](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/install-sam-cli.html "AWS SAM CLI installed").

# How deploy the AWS elements

```
sam deploy --stack-name aws-textract \
--template-file template.yaml \
--capabilities CAPABILITY_NAMED_IAM \
--resolve-s3 \
--profile <your_aws_local_profile>
```
