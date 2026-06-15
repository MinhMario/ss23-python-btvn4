from core.students import student_records
from utils.string_utils import normalize_student_names
from utils.random_utils import generate_assignment_code
from core.report_generator import display_student_scores, export_learning_report


while True:
        print('\n===== HỆ THỐNG TIỆN ÍCH HỌC TẬP RIKKEI ACADEMY =====')
        print('1. Xem danh sách sinh viên và điểm trung bình')
        print('2. Chuẩn hóa tên sinh viên')
        print('3. Sinh mã bài tập ngẫu nhiên')
        print('4. Xuất báo cáo học tập')
        print('5. Thoát chương trình')
        print('====================================================')

        choice = input('Chọn chức năng (1-5): ').strip()

        match choice:
            case '1': display_student_scores(student_records)
            case '2': normalize_student_names(student_records)
            case '3': generate_assignment_code()
            case '4': export_learning_report(student_records)
            case '5':
                print('Cảm ơn bạn đã sử dụng hệ thống!')
                break
            case _:
                print('Chức năng không hợp lệ. Vui lòng chọn từ 1 đến 5.')