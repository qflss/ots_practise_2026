# Лабораторная №1: Первичная инициализация
# Курс: Основы теории систем
# Студент: Глотов Всеволод Александрович

def get_system_info():
    system_info = {
        "student_name": "Глотов Всеволод Александрович",
        "academic_group": "ИВТИИбд-11",
        "github_link": "https://github.com/qflss"
    }
  
    return system_info
  
if __name__ == "__main__":
    info = get_system_info()
  
    print("Информация о системе: ")
  
    for key, value in info.items():
        print(f"- {key}: {value}")
