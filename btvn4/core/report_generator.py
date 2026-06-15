from datetime import datetime
from colorama import init, Fore, Style

from utils.score_utils import calculate_average, classify_student

init(autoreset=True)


def display_student_scores(records):
    if not records:
        print('Hệ thống chưa có dữ liệu sinh viên.')
        return

    print('--- DANH SÁCH ĐIỂM SINH VIÊN ---')
    for i, sv in enumerate(records, 1):
        avg  = calculate_average(sv['scores'])
        rank = classify_student(avg)
        print(f"{i}. [{sv['student_id']}] {sv['name']} | "
              f"Điểm: {sv['scores']} | ĐTB: {avg:.2f} - {rank}")
    print('---------------------------------')


def export_learning_report(records):
    if not records:
        print('Hệ thống chưa có dữ liệu sinh viên.')
        return

    total   = len(records)
    passed  = sum(1 for sv in records if calculate_average(sv['scores']) >= 5.0)
    failed  = total - passed
    created = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    print('--- XUẤT BÁO CÁO HỌC TẬP ---')
    print(f'Tổng số sinh viên: {total}')
    print(f'Số sinh viên đạt yêu cầu: {passed}')
    print(f'Số sinh viên cần cải thiện: {failed}')

    with open('learning_report.txt', 'w', encoding='utf-8') as f:
        f.write(f'BÁO CÁO HỌC TẬP\n')
        f.write(f'Thời gian tạo: {created}\n')
        f.write(f'{"="*30}\n')
        f.write(f'Tổng số sinh viên: {total}\n')
        f.write(f'Số sinh viên đạt yêu cầu (ĐTB >= 5.0): {passed}\n')
        f.write(f'Số sinh viên cần cải thiện (ĐTB < 5.0): {failed}\n')

    print(Fore.GREEN + '>> Đã xuất báo cáo ra file learning_report.txt')