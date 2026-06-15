def normalize_student_names(records):
    if not records:
        print('Hệ thống chưa có dữ liệu sinh viên.')
        return

    print('--- CHUẨN HÓA TÊN SINH VIÊN ---')
    for sv in records:
        sv['name'] = ' '.join(sv['name'].split()).title()
        print(f"{sv['student_id']}: {sv['name']}")
    print('>> Đã chuẩn hóa toàn bộ tên sinh viên.')