import pytest

from main import getOrderRotationSequence, testOrderSequence


def rotate_left(seq, k):
    if not seq:
        return seq
    k = k % len(seq)
    return seq[k:] + seq[:k]


@pytest.mark.parametrize(
    "sequence,expected_index",
    [
        ([1, 2, 3, 4, 5], 0),
        ([5, 1, 2, 3, 4], 1),
        ([3, 4, 5, 1, 2], 3),
        ([2, 3, 4, 5, 1], 4),
        ([2, 1], 1),
        ([42], 0),
        ([-3, -2, -1, 0, 1], 0),
        ([0, 1, -3, -2, -1], 2),
    ],
)
def test_order_sequence_aux_rotation_index(sequence, expected_index):
    idx = getOrderRotationSequence(sequence)
    assert idx == expected_index


@pytest.mark.parametrize(
    "sequence",
    [
        [1, 2, 3, 4, 5],
        [5, 1, 2, 3, 4],
        [3, 4, 5, 1, 2],
        [2, 3, 4, 5, 1],
        [2, 1],
        [42],
        [-3, -2, -1, 0, 1],
        [0, 1, -3, -2, -1],
    ],
)
def test_order_sequence_aux_produces_sorted_when_rotated(sequence):
    idx = getOrderRotationSequence(sequence)
    rotated = rotate_left(sequence, idx)
    assert testOrderSequence(rotated, 0)
