from writer_agent.ui import try_stream


class FakeGraph:
    def __init__(self):
        self.stream_calls = 0
        self.invoke_calls = 0

    def stream(self, inputs, stream_mode):
        self.stream_calls += 1
        yield {"router": {"mode": "closed_book"}}

    def invoke(self, inputs):
        self.invoke_calls += 1
        return {"final": "should not be called"}


def test_try_stream_does_not_execute_graph_twice() -> None:
    graph = FakeGraph()
    events = list(try_stream(graph, {"topic": "testing"}))

    assert events == [("updates", {"router": {"mode": "closed_book"}})]
    assert graph.stream_calls == 1
    assert graph.invoke_calls == 0