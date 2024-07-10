from utils.api_utils import get_issues
from utils.json_utils import generate_csv

def main():
    json_list = get_issues()
    generate_csv(json_list)

if __name__ == "__main__":
    main()