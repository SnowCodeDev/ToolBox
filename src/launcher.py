import os
import sys

def clear_screen():
    """清屏函数 - Windows用cls，其他用clear"""
    os.system('cls' if os.name == 'nt' else 'clear')

def read_config():
    """读取配置文件并解析"""
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'config.txt')
    
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        clear_screen()
        print("~ 哎呀，找不到config.txt文件呢 ~")
        print("~ 请确保config.txt和我在同一个文件夹里 ~")
        sys.exit(1)
    
    # 解析配置
    lines = content.split('\n')
    
    # 获取max和min
    max_val = 0
    min_val = 0
    for line in lines:
        if line.startswith('max ='):
            max_val = int(line.split('=')[1].strip())
        elif line.startswith('min ='):
            min_val = int(line.split('=')[1].strip())
    
    # 解析代码块
    code_blocks = {}
    current_code = None
    current_lines = []
    in_code_block = False
    
    for line in lines:
        if line.startswith('code ='):
            if current_code is not None and current_lines:
                code_blocks[current_code] = '\n'.join(current_lines)
            current_code = int(line.split('=')[1].strip())
            current_lines = []
            in_code_block = True
        elif in_code_block and line == '---':
            if current_code is not None and current_lines:
                code_blocks[current_code] = '\n'.join(current_lines)
            in_code_block = False
        elif in_code_block:
            current_lines.append(line)
    
    # 获取菜单选项
    menu_items = {}
    in_menu = False
    current_menu_num = None
    menu_lines = []
    
    for line in lines:
        if line == 'code :':
            in_menu = True
        elif in_menu and line.startswith('---'):
            if current_menu_num is not None and menu_lines:
                menu_items[current_menu_num] = ' '.join(menu_lines)
            in_menu = False
        elif in_menu and line and not line.startswith('code ='):
            if '. ' in line:
                if current_menu_num is not None and menu_lines:
                    menu_items[current_menu_num] = ' '.join(menu_lines)
                parts = line.split('. ', 1)
                current_menu_num = int(parts[0])
                menu_lines = [parts[1]]
            else:
                menu_lines.append(line.strip())
    
    return max_val, min_val, code_blocks, menu_items

def show_menu(menu_items):
    """清屏并显示菜单"""
    clear_screen()
    print("=" * 40)
    print("  欢迎使用系统小工具")
    print("=" * 40)
    for num, desc in sorted(menu_items.items()):
        print(f"  {num}. {desc}")
    print("  q. 退出程序")
    print("=" * 40)

def execute_code(code_num, code_blocks, current_file):
    """执行对应的代码块"""
    if code_num not in code_blocks:
        print(f"~ 哎呀，没有找到选项 {code_num} 的代码呢 ~")
        input("\n按回车键继续...")
        return
    
    code = code_blocks[code_num]
    print(f"\n~ 正在执行选项 {code_num} ~")
    print("-" * 30)
    
    try:
        # 把需要用到的模块都传进去
        exec_globals = {
            '__name__': '__main__',
            '__file__': current_file,  # 关键！把当前文件路径传进去
            'os': os,
            'sys': sys,
            'shutil': __import__('shutil'),
            'platform': __import__('platform'),
            'time': __import__('time')
        }
        exec(code, exec_globals)
    except Exception as e:
        print(f"~ 哎呀，执行出错了: {e} ~")
        import traceback
        traceback.print_exc()  # 打印详细错误信息，方便调试
    
    print("-" * 30)
    print(f"~ 选项 {code_num} 执行完成 ~")
    input("\n按回车键返回菜单...")

def main():
    """主程序"""
    max_val, min_val, code_blocks, menu_items = read_config()
    
    while True:
        show_menu(menu_items)
        choice = input("  请输入选项: ").strip()
        
        if choice.lower() == 'q':
            clear_screen()
            print("\n~ 感谢使用，下次再见啦 ~")
            break
        
        try:
            choice_num = int(choice)
            if choice_num < min_val or choice_num > max_val:
                print(f"~ 哎呀，请输入 {min_val}~{max_val} 之间的数字哦 ~")
                input("\n按回车键继续...")
                continue
            
            # 传入 __file__
            execute_code(choice_num, code_blocks, __file__)
            
        except ValueError:
            print("~ 哎呀，请输入数字或者 q 啦 ~")
            input("\n按回车键继续...")

if __name__ == '__main__':
    main()