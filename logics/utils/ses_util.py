import boto3


class SesUtil:
    @staticmethod
    def send_email(to_email_address, subject, body_text):
        SENDER = 'AWS SCH Notifications <sadasue@alpha-co.com>'
        RECIPIENT = to_email_address
        SUBJECT = subject
        BODY_TEXT = body_text
        CHARSET = "UTF-8"

        client = boto3.client('ses')

        try:
            response = client.send_email(
                Source=SENDER,
                Destination={
                    'ToAddresses': [
                        RECIPIENT,
                    ],
                },
                Message={
                    'Subject': {
                        'Charset': CHARSET,
                        'Data': SUBJECT,
                    },
                    'Body': {
                        'Text': {
                            'Charset': CHARSET,
                            'Data': BODY_TEXT,
                        },
                    },

                },
            )
        except Exception as e:
            print(f"Error sending email: {e}")
            raise e
        else:
            print(f"Email sent! Message ID: {response['MessageId']}")
            return response['MessageId']
