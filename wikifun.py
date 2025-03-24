import sys

def format_line(line):
    if line.lower().startswith("primary"):
        return f"== {line} =="
    else:
        words = line.split()
        if not words:
            return ""
        formatted = ' '.join([words[0].capitalize()] + [w.lower() for w in words[1:]])
        return f"* [[{formatted}]]"

def main():
    if len(sys.argv) < 2:
        print("Usage: python wikifun.py list.txt")
        return

    input_file = sys.argv[1]
    output_file = "result.txt"

    with open(input_file, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f if line.strip()]

    formatted_lines = [format_line(line) for line in lines]

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(formatted_lines))

    print(f"Done! Output written to {output_file}")

if __name__ == "__main__":
    main()
