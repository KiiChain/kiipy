# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from cosmos.authz.v1beta1 import query_pb2 as cosmos_dot_authz_dot_v1beta1_dot_query__pb2


class QueryStub(object):
    """Query defines the gRPC querier service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Grants = channel.unary_unary(
                '/cosmos.authz.v1beta1.Query/Grants',
                request_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.SerializeToString,
                response_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.FromString,
                )


class QueryServicer(object):
    """Query defines the gRPC querier service.
    """

    def Grants(self, request, context):
        """Returns list of `Authorization`, granted to the grantee by the granter.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_QueryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Grants': grpc.unary_unary_rpc_method_handler(
                    servicer.Grants,
                    request_deserializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.FromString,
                    response_serializer=cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'cosmos.authz.v1beta1.Query', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Query(object):
    """Query defines the gRPC querier service.
    """

    @staticmethod
    def Grants(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/cosmos.authz.v1beta1.Query/Grants',
            cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsRequest.SerializeToString,
            cosmos_dot_authz_dot_v1beta1_dot_query__pb2.QueryGrantsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)