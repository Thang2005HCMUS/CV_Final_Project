# Nội dung file: tests/test_sample.py

def test_example_pass():
    """Một bài test đơn giản luôn luôn pass"""
    assert 1 == 1

def test_add_function():
    """Ví dụ test một hàm nếu bạn có hàm tính toán"""
    result = 1 + 1
    assert result == 2