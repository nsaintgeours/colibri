def run(query: str, platforms: list[str]):
    """Run the whole colibri pipeline

    Wrapper function that will call several sub-functions to execute the whole colibri pipeline, from the scrapping to the characterisation. More details of the pipeline in the README.md file.

    Parameters:
    query (str): universal search query that will be used in each database platform specified in parameters.
    platforms (list[str]): list of platforms that will be scrapped. Be careful of the sythax. Supported: ["WoS"]

    Returns:
    None
    """
    print("\033[1m\U0001F426 Welcome to the pipeline of colibri!\033[0m")

    match platforms:
        case []:
            print("Parameter 'platforms' is empty. At least one platform must be specified.")
            return 0
        case _:

