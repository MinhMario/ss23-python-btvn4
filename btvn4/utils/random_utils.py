import random
import string

def generate_assignment_code():
    pool = string.ascii_uppercase + string.digits
    code = ''.join(random.choices(pool, k=4))
    print('--- SINH MÃ BÀI TẬP ---')
    print(f'Mã bài tập của bạn là: PY-{code}')