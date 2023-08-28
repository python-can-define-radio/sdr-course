import deal
from queue import SimpleQueue, Empty
from typing import List, TypeVar, Union, Optional



T = TypeVar('T')



class SimpleQueueTypeWrapped(SimpleQueue):
    """Created this as an alternative to SimpleQueue because Python 3.8 (which we're stuck with currently)
    doesn't support the type annotation SimpleQueue[something].

    This is specifically for queues of numpy arrays of fixed length and type.
    
    The `dtype` parameter is the dtype of the numpy array contents.
    The `chunk_size` parameter is the length of each queue element.
    """
    def __init__(self, qtype, dtype, chunk_size: int):
        self.qtype = qtype
        self.dtype = dtype
        self.chunk_size = chunk_size
        super().__init__()
    
    @deal.pre(lambda _: isinstance(_.item, _.self.qtype))
    @deal.pre(lambda _: _.item.dtype == _.self.dtype)
    @deal.pre(lambda _: len(_.item) == _.self.chunk_size)
    def put(self, item):
        return super().put(item)


@deal.has()
def make_queue_with_one_item(item: T) -> SimpleQueue:
    q = SimpleQueue()
    q.put(item)
    return q


@deal.has()
@deal.example(lambda: queue_to_list(SimpleQueue()) == [])
@deal.example(lambda: queue_to_list(make_queue_with_one_item(3)) == [3])
def queue_to_list(q: SimpleQueue) -> list:
    ## Unfortunately I have to remove the "better"
    ## type annotations for now, such as SimpleQueue[T]
    retval = []
    while True:
        try:
            retval.append(q.get_nowait())
        except Empty:
            return retval


@deal.example(lambda: bytes_to_bin_list(b"C") == [0, 1, 0, 0, 0, 0, 1, 1])
@deal.example(lambda: bytes_to_bin_list([67]) == bytes_to_bin_list(b"C"))
@deal.example(lambda: bytes_to_bin_list([192]) == [1, 1, 0, 0, 0, 0, 0, 0])
@deal.example(lambda: bytes_to_bin_list(b"CB") == [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0])

@deal.pre(lambda b: all(0 <= item < 256 for item in b))
@deal.ensure(lambda _: len(_.result) == len(_.b) * 8)
@deal.post(lambda result: all(x in [0, 1] for x in result))
@deal.has()
def bytes_to_bin_list(b: Union[bytes, List[int]]) -> List[int]:
    bitstrs = [f"{c:08b}" for c in b]
    joined = "".join(bitstrs)
    return list(map(int, joined))


NON_ASCII_ERR = "Currently, this only works for characters whose `ord` value is less than 256. For now, use `bytes_to_bin_list` if you wish to use non-ASCII characters. However, this may cause unexpected results for certain characters such as '«' that have multiple possible encodings."
@deal.pre(lambda _: all(ord(c) < 256 for c in _.message), message=NON_ASCII_ERR)
@deal.ensure(lambda _: _.result == bytes_to_bin_list(_.message.encode("ASCII")) if all(ord(c) < 128 for c in _.message) else True)
@deal.example(lambda: str_to_bin_list("«") == [1, 0, 1, 0, 1, 0, 1, 1])
@deal.example(lambda: str_to_bin_list("CB") == [0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0])
@deal.has()
def str_to_bin_list(message: str) -> List[int]:
    return bytes_to_bin_list([ord(c) for c in message])
