from utils.api_utils import get_issues
from utils.json_utils import generate_csv
from dotenv import load_dotenv
import os


def main(repo_config_pass):
    # load .env
    load_dotenv('./.config/.env', override=True)
    os.environ['access_token'] = os.getenv('ACCESS_TOKEN')

    # load repository .env
    load_dotenv(repo_config_pass, override=True)
    os.environ['owner'] = os.getenv('OWNER')
    os.environ['repo'] = os.getenv('REPO')
    os.environ['bug_label'] = os.getenv('BUG_LABEL')

    json_list = get_issues()
    generate_csv(json_list)


if __name__ == "__main__":
    repo_config_pass = './.config/swift.env'
    main(repo_config_pass)
