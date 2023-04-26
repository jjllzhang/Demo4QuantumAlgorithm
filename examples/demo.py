import subprocess
import time
import argparse

parser = argparse.ArgumentParser(description='运行Python可执行文件并测量时间')
parser.add_argument('executable_file', type=str, help='要运行的可执行文件名称')
parser.add_argument('--arguments', nargs='+', type=str, help='传递给可执行文件的参数')
parser.add_argument('--runs', type=int, default=1, help='每个参数运行的次数')

args = parser.parse_args()

if not args.arguments:
    print('请提供参数列表')
else:
    # 循环运行可执行文件，并测量时间
    total_time = 0
    for arg in args.arguments:
        arg_time = 0
        for i in range(args.runs):
            start_time = time.time()
            # 使用subprocess运行可执行文件并传递参数
            subprocess.run(['python', args.executable_file] + arg.split())
            end_time = time.time()

            # 计算运行时间并累加到arg_time
            run_time = end_time - start_time
            arg_time += run_time

        # 计算平均运行时间并展示
        avg_time = arg_time / args.runs
        total_time += avg_time
        print(f"运行参数 {arg} 的平均时间为: {avg_time:.4f} 秒")

    # 计算所有参数的平均运行时间并展示
    avg_time_all = total_time / len(args.arguments)
    print(f"\n所有参数的平均运行时间为: {avg_time_all:.4f} 秒")
