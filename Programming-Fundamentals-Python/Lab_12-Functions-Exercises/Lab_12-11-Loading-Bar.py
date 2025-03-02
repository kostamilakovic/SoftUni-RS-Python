# 11. Loading Bar
# You will receive a single integer number between 0 and 100 (inclusive)
# divisible by 10 without remainder (0, 10, 20, 30...).
# Your task is to create a function that returns a loading bar
# depending on the number you have received in the input.
# Print the result on the console. For more clarification, see the examples below.

def loading_bar (progress):
    bar_list = ['%' if i < progress // 10 else '.' for i in range(10)]
    bar_string = "".join(bar_list)
    if progress < 100:
        print(f"{progress}% [{bar_string}]")
        print("Still loading...")
    else:
        print("100% Complete!")
        print(f"[{bar_string}]")

loading_bar(int(input()))