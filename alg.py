from huffman import HuffmanCoding
import time


def algorithm(path):
    h = HuffmanCoding(path)
    first1 = time.time()
    output_path = h.compress()
    second1 = time.time()
    delta_time1 = second1 - first1
    first2 = time.time()
    decom_path = h.decompress(output_path)
    second3 = time.time()
    delta_time2 = second3 - first2
    return output_path, delta_time1, delta_time2, decom_path

