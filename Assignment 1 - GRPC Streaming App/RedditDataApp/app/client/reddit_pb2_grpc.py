# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import reddit_pb2 as reddit__pb2


class RedditStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendPost = channel.unary_stream(
                '/app.Reddit/SendPost',
                request_serializer=reddit__pb2.PostRequest.SerializeToString,
                response_deserializer=reddit__pb2.GetPost.FromString,
                )


class RedditServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendPost(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RedditServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendPost': grpc.unary_stream_rpc_method_handler(
                    servicer.SendPost,
                    request_deserializer=reddit__pb2.PostRequest.FromString,
                    response_serializer=reddit__pb2.GetPost.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'app.Reddit', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Reddit(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendPost(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/app.Reddit/SendPost',
            reddit__pb2.PostRequest.SerializeToString,
            reddit__pb2.GetPost.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
