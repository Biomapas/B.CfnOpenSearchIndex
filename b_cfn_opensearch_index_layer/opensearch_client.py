import boto3
from opensearchpy import OpenSearch, RequestsHttpConnection
from requests_aws4auth import AWS4Auth


class OpensearchClient(OpenSearch):
    def __init__(
        self,
        boto3_session: boto3.Session,
        opensearch_endpoint: str
    ) -> None:

        credentials = boto3_session.get_credentials()
        aws_auth = AWS4Auth(
            credentials.access_key,
            credentials.secret_key,
            boto3_session.region_name,
            'es',
            session_token=credentials.token
        )
        super().__init__(
            hosts=[{'host': opensearch_endpoint, 'port': 443}],
            http_auth=aws_auth,
            use_ssl=True,
            verify_certs=True,
            connection_class=RequestsHttpConnection
        )
