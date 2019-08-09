def main():
    d = {"red": 4, "blue": 1, "green": 14, "yellow": 2}
    print(d["red"])
    print(list(d.keys()))
    print(list(d.values()))
    print(d.items())
    print("blue" in d)
    print("cyan" in d)
    d["blue"] += 10
    print(d["blue"])

if __name__ == "__main__":
    main()