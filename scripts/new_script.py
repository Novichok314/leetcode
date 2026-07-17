import sys
from pathlib import Path

TEMPLATE = '''"""
LeetCode {number}
Topic: {topic}
Difficulty: {level}
"""


def solution():
    pass


if __name__ == "__main__":
    print(solution())
'''

def main():
    if len(sys.argv) != 4:
        print("Usage: python scripts/new_task.py <topic> <easy|medium|hard> <number>")
        sys.exit(1)

    topic, level, number = sys.argv[1], sys.argv[2], sys.argv[3]

    if level not in ("easy", "medium", "hard"):
        print("Level must be: easy, medium or hard")
        sys.exit(1)

    task_dir = Path("topics") / topic / level
    if not task_dir.exists():
        print(f"Topic '{topic}' doesn't exist. Create the folder first.")
        sys.exit(1)

    task_file = task_dir / f"{number}.py"
    if task_file.exists():
        print(f"{task_file} already exists.")
        sys.exit(1)

    task_file.write_text(TEMPLATE.format(number=number, topic=topic, level=level))
    print(f"Created {task_file}")

if __name__ == "__main__":
    main()