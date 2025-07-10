import argparse
import logging
from paper_finder.pubmed import fetch_papers
from paper_finder.filters import filter_non_academic_authors
from paper_finder.utils import save_to_csv, print_to_console

def main():
    parser = argparse.ArgumentParser(
        description=" PubMed Paper Filter: Fetch and filter papers with non-academic pharma/biotech authors."
    )
    parser.add_argument(
        "query",
        nargs="?",
        help="PubMed search query (e.g., 'cancer immunotherapy')"
    )
    parser.add_argument(
        "-d", "--debug",
        action="store_true",
        help="Enable debug logging during execution"
    )
    parser.add_argument(
        "-f", "--file",
        help="Filename to save results (e.g., results.csv). If not provided, results are printed to console."
    )

    args = parser.parse_args()

    # Prompt user if no query is passed
    if not args.query:
        args.query = input(" Enter a PubMed search query: ").strip()
        if not args.query:
            print(" No query provided. Exiting.")
            return

    # Enable debug logging
    logging.basicConfig(level=logging.DEBUG if args.debug else logging.INFO)

    logging.info(f" Searching PubMed for: {args.query}")
    papers = fetch_papers(args.query)
    filtered = filter_non_academic_authors(papers)

    if not filtered:
        print("No papers with non-academic authors found.")
        return

    # Save to file or print to console
    if args.file:
        filename = args.file
        if not filename.endswith(".csv"):
            filename += ".csv"
        save_to_csv(filtered, filename)
        logging.info(f" Results saved to {filename}")
    else:
        print_to_console(filtered)

if __name__ == "__main__":
    main()
