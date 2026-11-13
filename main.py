from app.retrieval import retrieve_relevant_chunks
from app.generation import generate_answer


def main():

    print("\n===================================")
    print("       PSYCHOLOGY RAG SYSTEM")
    print("===================================")

    print("\nAsk questions about your psychology document.")
    print("Type 'exit' to close the application.\n")

    while True:

        question = input("You: ")

        if question.lower() == "exit":
            print("\nThank you for using the RAG System!")
            break

        if not question.strip():
            print("Please enter a question.\n")
            continue

        try:

            # Retrieve relevant information
            retrieved_chunks = retrieve_relevant_chunks(question)

            # Generate an answer using retrieved information
            answer = generate_answer(question, retrieved_chunks)

            print("\nAnswer:", answer)
            print("\n-----------------------------------\n")

        except Exception as error:
            print("\nSomething went wrong:", error)


if __name__ == "__main__":
    main()