import sys
from pathlib import Path

SOLUTION_TEMPLATE = '''"""
LeetCode {number}
Topic: {topic}
Difficulty: {level}
"""


class Solution:
    def {func_name}(self):
        pass


if __name__ == "__main__":
    solution = Solution()
    print(solution.{func_name}())
'''

TEST_TEMPLATE = '''from topics.{topic}.{level}.problem_{number} import Solution


def test():
    solution = Solution()
    assert solution.{func_name}() is None
'''

def main():
    if len(sys.argv) != 5:
        print("Usage: python scripts/new_task.py <topic> <easy|medium|hard> <number> <function_name>")
        sys.exit(1)

    topic, level, number, func_name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    if level not in ("easy", "medium", "hard"):
        print("Level must be: easy, medium or hard")
        sys.exit(1)

    task_dir = Path("topics") / topic / level
    if not task_dir.exists():
        print(f"Topic '{topic}' doesn't exist. Create the folder first.")
        sys.exit(1)

    solution_file = task_dir / f"problem_{number}.py"
    test_file = task_dir / f"test_{number}.py"
    init_file = task_dir / "__init__.py"

    if solution_file.exists():
        print(f"{solution_file} already exists.")
        sys.exit(1)

    solution_file.write_text(
        SOLUTION_TEMPLATE.format(number=number, topic=topic, level=level, func_name=func_name)
    )
    test_file.write_text(
        TEST_TEMPLATE.format(number=number, topic=topic, level=level, func_name=func_name)
    )
    init_file.touch(exist_ok=True)
    print(f"Created {solution_file}")
    print(f"Created {test_file}")
    print(f"Created {init_file}")

if __name__ == "__main__":
    main()