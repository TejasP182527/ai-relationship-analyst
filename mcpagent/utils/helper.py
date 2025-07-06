def extract_client(query: str) -> str:
    """
    Extract client name from query using a basic match.
    """
    known_clients = ["anil", "sridhar", "bala"]
    query = query.lower()
    print(f"Extracting client from query: {query}\n\n")
    for name in known_clients:
        if name in query:
            print(f"Matched client: {name}\n\n")
            return name
    return "anil" 
