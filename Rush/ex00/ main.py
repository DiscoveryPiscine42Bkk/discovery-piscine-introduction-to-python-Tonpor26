farm_tasks = []

def show_menu():
    print("\n===== เมนูจัดการงานฟาร์ม =====")
    print("1. เพิ่มงานในฟาร์ม")
    print("2. แสดงรายการงานทั้งหมด")
    print("3. ลบงาน")
    print("4. สรุปจำนวนงานในแต่ละประเภท")
    print("5. ออกจากโปรแกรม")

def add_task():
    name = input("กรอกชื่องาน: ")
    category = input("ประเภทงาน (เช่น crops, livestock): ")
    task = {"name": name, "category": category}
    farm_tasks.append(task)
    print("✅ เพิ่มงานเรียบร้อยแล้ว")

def show_tasks():
    if not farm_tasks:
        print("❗ ยังไม่มีงานในระบบ")
    else:
        print("📋 รายการงาน:")
        for idx, task in enumerate(farm_tasks, 1):
            print(f"{idx}. {task['name']} ({task['category']})")

def delete_task():
    show_tasks()
    if farm_tasks:
        try:
            task_num = int(input("กรุณาใส่หมายเลขงานที่ต้องการลบ: "))
            if 1 <= task_num <= len(farm_tasks):
                removed = farm_tasks.pop(task_num - 1)
                print(f"🗑 ลบงาน '{removed['name']}' เรียบร้อยแล้ว")
            else:
                print("❌ หมายเลขงานไม่ถูกต้อง")
        except ValueError:
            print("❌ กรุณาใส่หมายเลขที่ถูกต้อง")

def summarize_tasks():
    summary = {}
    for task in farm_tasks:
        category = task["category"]
        summary[category] = summary.get(category, 0) + 1
    if not summary:
        print("❗ ยังไม่มีข้อมูลสรุป")
    else:
        print("📊 สรุปจำนวนงานในแต่ละประเภท:")
        for cat, count in summary.items():
            print(f"- {cat}: {count} งาน")

โปรแกรมหลัก
while True:
    show_menu()
    choice = input("เลือกเมนู (1-5): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        show_tasks()
    elif choice == '3':
        delete_task()
    elif choice == '4':
        summarize_tasks()
    elif choice == '5':
        print("👋 ออกจากโปรแกรมแล้ว")
        break
    else:
        print("❌ กรุณาเลือกเมนูให้ถูกต้อง (1-5)")